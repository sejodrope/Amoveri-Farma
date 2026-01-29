"""
Teste de Conexão - NetSuite
Amoveri Farma

Descrição:
    Script para testar conexão com NetSuite e validar Saved Searches

Uso:
    python test_netsuite_connection.py

Autor: José Silva
Data: 2026-01-29
"""

import os
import sys
from dotenv import load_dotenv
from loguru import logger
import requests
from requests_oauthlib import OAuth1

# Configurar logger
logger.remove()
logger.add(sys.stdout, level='INFO')


class NetSuiteConnectionTest:
    """Testa conexão com NetSuite"""

    def __init__(self):
        """Inicializa cliente NetSuite"""
        # Carregar credenciais
        self.account_id = os.getenv('NETSUITE_ACCOUNT_ID')
        self.token_id = os.getenv('NETSUITE_TOKEN_ID')
        self.token_secret = os.getenv('NETSUITE_TOKEN_SECRET')
        self.consumer_key = os.getenv('NETSUITE_CONSUMER_KEY')
        self.consumer_secret = os.getenv('NETSUITE_CONSUMER_SECRET')

        # Validar credenciais
        missing = []
        if not self.account_id:
            missing.append('NETSUITE_ACCOUNT_ID')
        if not self.token_id:
            missing.append('NETSUITE_TOKEN_ID')
        if not self.token_secret:
            missing.append('NETSUITE_TOKEN_SECRET')
        if not self.consumer_key:
            missing.append('NETSUITE_CONSUMER_KEY')
        if not self.consumer_secret:
            missing.append('NETSUITE_CONSUMER_SECRET')

        if missing:
            logger.error(f"❌ Variáveis faltando no .env: {', '.join(missing)}")
            sys.exit(1)

        # Configurar OAuth
        self.auth = OAuth1(
            client_key=self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.token_id,
            resource_owner_secret=self.token_secret,
            realm=self.account_id,
            signature_method='HMAC-SHA256'
        )

        self.base_url = f"https://{self.account_id}.suitetalk.api.netsuite.com"

        logger.info(f"Cliente NetSuite inicializado para conta: {self.account_id}")

    def test_connection(self) -> bool:
        """
        Testa conexão básica com NetSuite

        Returns:
            True se conexão OK, False caso contrário
        """
        try:
            logger.info("Testando conexão com NetSuite...")

            # Endpoint de teste (listar subsidiárias)
            url = f"{self.base_url}/services/rest/record/v1/subsidiary"

            response = requests.get(url, auth=self.auth, timeout=30)

            if response.status_code == 200:
                logger.success("✅ Conexão com NetSuite OK!")
                return True
            else:
                logger.error(f"❌ Erro na conexão: {response.status_code} - {response.text}")
                return False

        except Exception as e:
            logger.error(f"❌ Erro ao conectar: {str(e)}")
            return False

    def test_saved_search(self, search_id: int, search_name: str) -> bool:
        """
        Testa uma Saved Search específica

        Args:
            search_id: ID da Saved Search
            search_name: Nome descritivo da search

        Returns:
            True se funcionar, False caso contrário
        """
        try:
            logger.info(f"Testando Saved Search: {search_name} (ID: {search_id})...")

            # Endpoint de Saved Search
            url = f"{self.base_url}/services/rest/query/v1/suiteql"

            # Query usando Saved Search
            query = f"SELECT * FROM (SELECT * FROM transaction WHERE id IN (SELECT id FROM saved_search WHERE id = {search_id})) LIMIT 10"

            payload = {"q": query}

            response = requests.post(url, json=payload, auth=self.auth, timeout=30)

            if response.status_code == 200:
                data = response.json()
                count = len(data.get('items', []))
                logger.success(f"✅ Saved Search '{search_name}' OK! {count} registros retornados")
                return True
            else:
                logger.warning(f"⚠️ Saved Search '{search_name}' retornou erro: {response.status_code}")
                logger.debug(f"Resposta: {response.text}")
                return False

        except Exception as e:
            logger.error(f"❌ Erro ao testar Saved Search '{search_name}': {str(e)}")
            return False

    def run_all_tests(self):
        """Executa todos os testes"""
        logger.info("🧪 Iniciando testes de conexão NetSuite...\n")

        results = []

        # Teste 1: Conexão básica
        logger.info("=" * 60)
        logger.info("TESTE 1: Conexão Básica")
        logger.info("=" * 60)
        results.append(('Conexão Básica', self.test_connection()))

        # Teste 2: Saved Search de Custos
        logger.info("\n" + "=" * 60)
        logger.info("TESTE 2: Saved Search de Custos")
        logger.info("=" * 60)
        custos_id = os.getenv('NETSUITE_SAVED_SEARCH_CUSTOS')
        if custos_id:
            results.append(('Saved Search Custos', self.test_saved_search(int(custos_id), 'Custos')))
        else:
            logger.warning("⚠️ NETSUITE_SAVED_SEARCH_CUSTOS não definido no .env")
            results.append(('Saved Search Custos', False))

        # Teste 3: Saved Search de Estoque
        logger.info("\n" + "=" * 60)
        logger.info("TESTE 3: Saved Search de Estoque")
        logger.info("=" * 60)
        estoque_id = os.getenv('NETSUITE_SAVED_SEARCH_ESTOQUE')
        if estoque_id:
            results.append(('Saved Search Estoque', self.test_saved_search(int(estoque_id), 'Estoque')))
        else:
            logger.warning("⚠️ NETSUITE_SAVED_SEARCH_ESTOQUE não definido no .env")
            results.append(('Saved Search Estoque', False))

        # Resumo
        logger.info("\n" + "=" * 60)
        logger.info("RESUMO DOS TESTES")
        logger.info("=" * 60)

        passed = sum(1 for _, result in results if result)
        total = len(results)

        for test_name, result in results:
            status = "✅ PASSOU" if result else "❌ FALHOU"
            logger.info(f"{test_name:30s} {status}")

        logger.info("\n" + "=" * 60)
        logger.info(f"RESULTADO FINAL: {passed}/{total} testes passaram")
        logger.info("=" * 60)

        if passed == total:
            logger.success("\n🎉 Todos os testes passaram! NetSuite configurado corretamente.")
            return True
        else:
            logger.error(f"\n⚠️ {total - passed} teste(s) falharam. Verifique as configurações.")
            return False


def main():
    """Função principal"""
    load_dotenv()

    tester = NetSuiteConnectionTest()
    success = tester.run_all_tests()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
