"""
Extrator de Cotações - Bionexo
Amoveri Farma

Descrição:
    Script para extrair cotações automaticamente do portal Bionexo.
    Usa Playwright para automação do navegador.

Uso:
    python extraction_bionexo.py

Autor: José Silva
Data: 2026-01-29
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

from playwright.sync_api import sync_playwright, Page, Browser
from dotenv import load_dotenv
from loguru import logger

# Configurar logger
logger.remove()
logger.add(sys.stdout, level=os.getenv('LOG_LEVEL', 'INFO'))
logger.add("logs/extraction_{time:YYYY-MM-DD}.log", rotation="1 day", retention="30 days")


class BionexoExtractor:
    """Extrator de cotações da Bionexo"""

    def __init__(self, onedrive_path: str):
        """
        Inicializa o extrator

        Args:
            onedrive_path: Caminho do OneDrive onde os dados serão salvos
        """
        self.onedrive_path = Path(onedrive_path)
        self.bronze_path = self.onedrive_path / "01_Bronze" / "Bionexo"
        self.bronze_path.mkdir(parents=True, exist_ok=True)

        # Configurações da Bionexo
        self.base_url = os.getenv('BIONEXO_URL', 'https://bionexonew.bionexo.com')
        self.email = os.getenv('BIONEXO_EMAIL')
        self.password = os.getenv('BIONEXO_PASSWORD')

        # Validações
        if not self.email or not self.password:
            raise ValueError("BIONEXO_EMAIL e BIONEXO_PASSWORD devem estar definidos no .env")

        logger.info(f"Extrator inicializado. Dados serão salvos em: {self.bronze_path}")

    def login(self, page: Page) -> bool:
        """
        Realiza login na Bionexo

        Args:
            page: Página do Playwright

        Returns:
            True se login bem-sucedido, False caso contrário
        """
        try:
            logger.info("Acessando página de login...")
            page.goto(f"{self.base_url}/login", timeout=30000)

            # Preencher formulário de login
            logger.debug("Preenchendo credenciais...")
            page.fill('input[name="email"]', self.email)
            page.fill('input[name="password"]', self.password)

            # Clicar em entrar
            logger.debug("Clicando em entrar...")
            page.click('button[type="submit"]')

            # Aguardar navegação
            page.wait_for_load_state('networkidle', timeout=30000)

            # Verificar se login foi bem-sucedido
            # Ajustar seletor conforme a página real
            if page.is_visible('text=Sair') or page.is_visible('[data-testid="user-menu"]'):
                logger.success("✅ Login realizado com sucesso!")
                return True
            else:
                logger.error("❌ Login falhou - credenciais inválidas ou página mudou")
                return False

        except Exception as e:
            logger.error(f"❌ Erro durante login: {str(e)}")
            return False

    def extract_cotacoes(self, page: Page) -> List[Dict]:
        """
        Extrai lista de cotações ativas

        Args:
            page: Página do Playwright

        Returns:
            Lista de dicionários com dados das cotações
        """
        try:
            logger.info("Navegando para lista de cotações...")
            page.goto(f"{self.base_url}/cotacoes", timeout=30000)
            page.wait_for_load_state('networkidle')

            cotacoes = []

            # ESTRATÉGIA 1: Interceptar chamadas de API
            # A Bionexo provavelmente faz chamadas AJAX/Fetch para carregar cotações
            def handle_response(response):
                """Captura respostas da API"""
                if 'api/cotacoes' in response.url or 'api/v1/cotacoes' in response.url:
                    try:
                        data = response.json()
                        logger.debug(f"API response capturada: {response.url}")
                        if isinstance(data, list):
                            cotacoes.extend(data)
                        elif isinstance(data, dict) and 'items' in data:
                            cotacoes.extend(data['items'])
                        elif isinstance(data, dict):
                            cotacoes.append(data)
                    except Exception as e:
                        logger.warning(f"Erro ao parsear resposta da API: {str(e)}")

            page.on('response', handle_response)

            # Recarregar para capturar API calls
            logger.debug("Recarregando página para capturar API calls...")
            page.reload()
            page.wait_for_timeout(5000)  # Aguardar carregamento completo

            # ESTRATÉGIA 2: Se API não funcionar, fazer scraping HTML
            if not cotacoes:
                logger.warning("API não capturada, tentando scraping HTML...")
                cotacoes = self._scrape_cotacoes_html(page)

            logger.success(f"✅ {len(cotacoes)} cotações extraídas")
            return cotacoes

        except Exception as e:
            logger.error(f"❌ Erro ao extrair cotações: {str(e)}")
            return []

    def _scrape_cotacoes_html(self, page: Page) -> List[Dict]:
        """
        Extrai cotações via scraping HTML (fallback)

        Args:
            page: Página do Playwright

        Returns:
            Lista de cotações
        """
        cotacoes = []

        try:
            # Ajustar seletores conforme a estrutura real da Bionexo
            cards = page.query_selector_all('.cotacao-card, .quote-card, [data-testid="cotacao-item"]')

            for card in cards:
                try:
                    cotacao = {
                        'id': card.get_attribute('data-id') or card.get_attribute('id'),
                        'cliente': card.text_content('.cliente, .customer-name'),
                        'data_entrega': card.text_content('.data-entrega, .delivery-date'),
                        'status': card.text_content('.status'),
                        'valor_estimado': card.text_content('.valor, .amount'),
                    }
                    cotacoes.append(cotacao)

                except Exception as e:
                    logger.warning(f"Erro ao extrair dados de um card: {str(e)}")
                    continue

        except Exception as e:
            logger.error(f"Erro no scraping HTML: {str(e)}")

        return cotacoes

    def extract_detalhes_cotacao(self, page: Page, cotacao_id: str) -> Dict:
        """
        Extrai detalhes completos de uma cotação específica

        Args:
            page: Página do Playwright
            cotacao_id: ID da cotação

        Returns:
            Dicionário com detalhes da cotação
        """
        try:
            logger.info(f"Extraindo detalhes da cotação {cotacao_id}...")
            page.goto(f"{self.base_url}/cotacoes/{cotacao_id}", timeout=30000)
            page.wait_for_load_state('networkidle')

            # Aguardar carregamento dos itens
            page.wait_for_selector('.item-list, .product-list', timeout=10000)

            # Extrair dados
            detalhes = {
                'cotacao_id': cotacao_id,
                'data_captura': datetime.now().isoformat(),
                'itens': []
            }

            # Extrair itens (ajustar seletores conforme necessário)
            itens = page.query_selector_all('.item-row, .product-row')

            for item in itens:
                try:
                    item_data = {
                        'sku': item.text_content('.sku, .code'),
                        'descricao': item.text_content('.descricao, .description'),
                        'quantidade': item.text_content('.quantidade, .quantity'),
                        'unidade': item.text_content('.unidade, .unit'),
                    }
                    detalhes['itens'].append(item_data)
                except Exception as e:
                    logger.warning(f"Erro ao extrair item: {str(e)}")

            logger.success(f"✅ {len(detalhes['itens'])} itens extraídos da cotação {cotacao_id}")
            return detalhes

        except Exception as e:
            logger.error(f"❌ Erro ao extrair detalhes da cotação {cotacao_id}: {str(e)}")
            return {}

    def save_raw_data(self, data: Dict, cotacao_id: str) -> Path:
        """
        Salva dados brutos em JSON

        Args:
            data: Dados a serem salvos
            cotacao_id: ID da cotação

        Returns:
            Caminho do arquivo salvo
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cotacao_{cotacao_id}_{timestamp}.json"
        filepath = self.bronze_path / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"📁 Dados salvos em: {filepath}")
        return filepath

    def run(self) -> List[Path]:
        """
        Executa extração completa

        Returns:
            Lista de arquivos salvos
        """
        headless = os.getenv('HEADLESS_MODE', 'false').lower() == 'true'

        logger.info("🚀 Iniciando extração Bionexo...")
        logger.debug(f"Modo headless: {headless}")

        saved_files = []

        with sync_playwright() as p:
            browser: Browser = p.chromium.launch(headless=headless)
            context = browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page = context.new_page()

            try:
                # Login
                if not self.login(page):
                    logger.error("❌ Falha no login. Abortando.")
                    return []

                # Extrair lista de cotações
                cotacoes = self.extract_cotacoes(page)

                if not cotacoes:
                    logger.warning("⚠️ Nenhuma cotação encontrada")
                    return []

                # Extrair detalhes de cada cotação
                for cotacao in cotacoes[:10]:  # Limitar a 10 para teste
                    cotacao_id = cotacao.get('id', 'unknown')

                    detalhes = self.extract_detalhes_cotacao(page, cotacao_id)

                    if detalhes:
                        filepath = self.save_raw_data(detalhes, cotacao_id)
                        saved_files.append(filepath)

                logger.success(f"✅ Extração concluída! {len(saved_files)} arquivos salvos")

            except Exception as e:
                logger.error(f"❌ Erro durante extração: {str(e)}")

            finally:
                browser.close()

        return saved_files


def main():
    """Função principal"""
    # Carregar variáveis de ambiente
    load_dotenv()

    # Validar configurações
    onedrive_path = os.getenv('ONEDRIVE_PATH')

    if not onedrive_path:
        logger.error("❌ ONEDRIVE_PATH não definido no arquivo .env")
        sys.exit(1)

    # Executar extração
    try:
        extractor = BionexoExtractor(onedrive_path=onedrive_path)
        saved_files = extractor.run()

        if saved_files:
            logger.success(f"✅ Sucesso! {len(saved_files)} cotações extraídas:")
            for file in saved_files:
                logger.info(f"  📄 {file.name}")
        else:
            logger.warning("⚠️ Nenhuma cotação foi extraída")

    except Exception as e:
        logger.error(f"❌ Erro fatal: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
