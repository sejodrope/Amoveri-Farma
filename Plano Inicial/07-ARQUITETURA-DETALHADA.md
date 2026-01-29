Vou analisar seu plano de arquitetura e adaptá-lo à realidade da Amoveri Farma. Primeiro, deixe-me examinar a imagem para entender melhor sua infraestrutura atual.

Excelente! Vejo que você já está usando a funcionalidade de **Consulta Web Salva** do NetSuite, o que simplifica significativamente a arquitetura. Vou analisar o plano e propor melhorias contextualizadas.

## 📊 Análise Crítica do Plano Atual

### ✅ **Pontos Fortes do Plano**
1. **Arquitetura sólida e bem fundamentada** - O documento demonstra profundo conhecimento técnico
2. **Foco em custos** - Evita licenças Premium desnecessárias
3. **Uso inteligente de DuckDB** - Excelente escolha para OLAP local
4. **Considerações de segurança** - OAuth, gestão de credenciais, auditoria

### ⚠️ **Desafios para a Amoveri Farma**

1. **Complexidade vs. Maturidade Atual**
   - O plano propõe uma arquitetura de Data Lakehouse completa, mas vocês ainda não têm datalake
   - Risco de "over-engineering" para o estágio atual da empresa

2. **Recursos Humanos**
   - Requer desenvolvedor Python experiente em tempo integral
   - Manutenção de infraestrutura local complexa

3. **Três Portais Diferentes**
   - Bionexo, Apoio Cotações e GT Plan têm arquiteturas distintas
   - O esforço de web scraping será triplicado

## 🎯 **Plano de Arquitetura Otimizado para Amoveri Farma**

Vou propor uma abordagem **evolutiva e pragmática** em 3 fases:

---

## **FASE 1: Quick Wins (1-2 meses) - Foundation**
*Objetivo: Criar valor imediato sem infraestrutura complexa*

### Arquitetura Simplificada 

```
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA DE INGESTÃO                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Bionexo    │  │    Apoio     │  │   GT Plan    │      │
│  │   Portal     │  │  Cotações    │  │    Portal    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │               │
│         └──────────────────┼──────────────────┘               │
│                            │                                   │
│                   ┌────────▼────────┐                         │
│                   │  Python Script   │                         │
│                   │   (Playwright)   │                         │
│                   │  - Login         │                         │
│                   │  - Download      │                         │
│                   │  - Parse HTML    │                         │
│                   └────────┬────────┘                         │
└─────────────────────────────┼───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│              CAMADA DE DADOS SIMPLIFICADA                    │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │         OneDrive / SharePoint (Existente)            │   │
│  │                                                       │   │
│  │  📁 Cotacoes/                                        │   │
│  │     ├── Bronze/ (CSV/Excel dos portais)             │   │
│  │     ├── Silver/ (Excel consolidado)                 │   │
│  │     └── Logs/                                        │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              NetSuite (Via Consulta Web)             │   │
│  │  - Custos                                            │   │
│  │  - Estoque                                           │   │
│  │  - Regras Fiscais                                    │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────┬───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│           CAMADA DE PROCESSAMENTO (Python Local)            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌────────────────────────────────────────┐                 │
│  │  Script de Precificação (Pandas)       │                 │
│  │  - Lê dados do OneDrive                │                 │
│  │  - Consulta NetSuite via Web Query     │                 │
│  │  - Calcula ICMS-ST, PIS/COFINS         │                 │
│  │  - Gera preço sugerido                 │                 │
│  │  - Salva Excel no OneDrive             │                 │
│  └────────────────────────────────────────┘                 │
└─────────────────────────────┬───────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────┐
│                CAMADA DE VISUALIZAÇÃO                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Power BI Desktop/Service                │   │
│  │                                                       │   │
│  │  Conectores:                                         │   │
│  │  • Excel/CSV do OneDrive (via Web.Contents)         │   │
│  │  • NetSuite (via Consulta Web Salva)                │   │
│  │                                                       │   │
│  │  Dashboards:                                         │   │
│  │  • KPIs Comerciais                                   │   │
│  │  • Win/Loss Analysis                                 │   │
│  │  • Histórico de Preços                               │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Implementação Prática - Fase 1

#### **1.1. Estrutura de Pastas no OneDrive**

```
📁 Amoveri_DataHub/
├── 📁 01_Bronze/
│   ├── 📁 Bionexo/
│   │   └── cotacao_2026-01-28_143022.html
│   ├── 📁 Apoio/
│   │   └── relatorio_2026-01-28.xlsx
│   └── 📁 GTPlan/
│       └── espelho_pedido_20260128.csv
├── 📁 02_Silver/
│   └── cotacoes_consolidadas.xlsx
├── 📁 03_Gold/
│   └── precos_calculados.xlsx
├── 📁 04_Logs/
│   └── execucao_2026-01-28.log
└── 📁 05_Config/
    └── credenciais.env
```

#### **1.2. Script Python - Extração Bionexo (Simplificado)**

Vou criar um script inicial focado apenas na Bionexo como MVP:

```python
# extraction_bionexo.py
import os
from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import json
from pathlib import Path

class BionexoExtractor:
    """Extrator de cotações da Bionexo"""
    
    def __init__(self, onedrive_path: str):
        self.onedrive_path = Path(onedrive_path)
        self.bronze_path = self.onedrive_path / "01_Bronze" / "Bionexo"
        self.bronze_path.mkdir(parents=True, exist_ok=True)
        
    def login(self, page, email: str, password: str):
        """Realiza login na Bionexo"""
        page.goto("https://bionexonew.bionexo.com/login")
        page.fill('input[name="email"]', email)
        page.fill('input[name="password"]', password)
        page.click('button[type="submit"]')
        page.wait_for_load_state('networkidle')
        
    def extract_cotacoes(self, page):
        """Extrai lista de cotações ativas"""
        page.goto("https://bionexonew.bionexo.com/cotacoes")
        page.wait_for_selector('.cotacao-item')  # Ajustar seletor
        
        # Estratégia: interceptar API calls
        cotacoes = []
        
        def handle_response(response):
            if 'api/cotacoes' in response.url:
                try:
                    data = response.json()
                    cotacoes.append(data)
                except:
                    pass
        
        page.on('response', handle_response)
        page.reload()
        page.wait_for_timeout(3000)
        
        return cotacoes
    
    def save_raw_data(self, data: dict, cotacao_id: str):
        """Salva dados brutos em JSON"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cotacao_{cotacao_id}_{timestamp}.json"
        filepath = self.bronze_path / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def run(self, email: str, password: str):
        """Executa extração completa"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)  # headless=True em produção
            context = browser.new_context()
            page = context.new_page()
            
            try:
                self.login(page, email, password)
                cotacoes = self.extract_cotacoes(page)
                
                saved_files = []
                for cotacao in cotacoes:
                    cotacao_id = cotacao.get('id', 'unknown')
                    filepath = self.save_raw_data(cotacao, cotacao_id)
                    saved_files.append(filepath)
                
                print(f"✅ Extraídas {len(saved_files)} cotações")
                return saved_files
                
            finally:
                browser.close()

# Uso
if __name__ == "__main__":
    # Carregar credenciais do arquivo .env
    from dotenv import load_dotenv
    load_dotenv()
    
    extractor = BionexoExtractor(
        onedrive_path=os.getenv('ONEDRIVE_PATH', 'C:/Users/User/OneDrive/Amoveri_DataHub')
    )
    
    extractor.run(
        email=os.getenv('BIONEXO_EMAIL'),
        password=os.getenv('BIONEXO_PASSWORD')
    )
```

#### **1.3. Script Python - Motor de Precificação Básico**

```python
# pricing_engine.py
import pandas as pd
import numpy as np
from pathlib import Path
import requests
from typing import Dict, List

class PricingEngine:
    """Motor de precificação farmacêutica"""
    
    def __init__(self, netsuite_config: Dict):
        self.ns_config = netsuite_config
        self.matrix_tributaria = self.load_tax_matrix()
        
    def load_tax_matrix(self) -> pd.DataFrame:
        """Carrega matriz tributária do NetSuite ou arquivo local"""
        # TODO: Implementar consulta via NetSuite Saved Search
        # Por enquanto, carregar de Excel
        return pd.read_excel("matriz_tributaria.xlsx")
    
    def get_custo_from_netsuite(self, skus: List[str]) -> pd.DataFrame:
        """Busca custo e estoque do NetSuite via Consulta Web Salva"""
        # Você já tem a Consulta Web configurada!
        # Aqui adaptamos para fazer via script
        
        url = self.ns_config['saved_search_url']
        headers = {
            'Authorization': f'Bearer {self.ns_config["token"]}',
            'Content-Type': 'application/json'
        }
        
        # NetSuite permite passar parâmetros na URL da saved search
        params = {'sku': ','.join(skus)}
        
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        # Converter para DataFrame
        df = pd.DataFrame(data['items'])
        return df[['sku', 'custo_medio', 'estoque_disponivel']]
    
    def calcular_icms_st(self, row: pd.Series) -> float:
        """Calcula ICMS-ST conforme legislação"""
        # Simplificado - na prática, considerar MVA, convênios, etc.
        
        if row['uf_origem'] == row['uf_destino']:
            # Operação interna - sem ST
            return 0.0
        
        # Buscar MVA da matriz tributária
        regra = self.matrix_tributaria[
            (self.matrix_tributaria['ncm'] == row['ncm']) &
            (self.matrix_tributaria['uf_destino'] == row['uf_destino'])
        ]
        
        if regra.empty:
            print(f"⚠️ Regra não encontrada para NCM {row['ncm']}")
            return 0.0
        
        mva = regra.iloc[0]['mva_ajustada']
        aliq_interna = regra.iloc[0]['aliq_interna']
        aliq_interestadual = 0.12  # Padrão para a maioria dos estados
        
        # Fórmula ICMS-ST
        base_st = row['preco_produto'] * (1 + mva)
        icms_proprio = row['preco_produto'] * aliq_interestadual
        icms_st = (base_st * aliq_interna) - icms_proprio
        
        return max(icms_st, 0)
    
    def calcular_pis_cofins(self, row: pd.Series) -> Dict[str, float]:
        """Calcula PIS/COFINS conforme lista do produto"""
        
        # Verificar lista (Positiva/Negativa/Neutra)
        if row['lista'] == 'POSITIVA':
            return {'pis': 0.0, 'cofins': 0.0}
        elif row['lista'] == 'NEGATIVA':
            return {'pis': 0.0, 'cofins': 0.0}
        else:  # NEUTRA
            return {
                'pis': row['preco_produto'] * 0.0165,
                'cofins': row['preco_produto'] * 0.076
            }
    
    def calcular_preco_venda(self, df_cotacao: pd.DataFrame) -> pd.DataFrame:
        """Pipeline completo de precificação"""
        
        # 1. Buscar custos do NetSuite
        skus = df_cotacao['sku'].unique().tolist()
        df_custos = self.get_custo_from_netsuite(skus)
        
        # 2. Merge com cotação
        df = df_cotacao.merge(df_custos, on='sku', how='left')
        
        # 3. Calcular impostos
        df['icms_st'] = df.apply(self.calcular_icms_st, axis=1)
        
        pis_cofins = df.apply(self.calcular_pis_cofins, axis=1)
        df['pis'] = pis_cofins.apply(lambda x: x['pis'])
        df['cofins'] = pis_cofins.apply(lambda x: x['cofins'])
        
        # 4. Calcular preço final
        df['custo_total'] = (
            df['custo_medio'] + 
            df['icms_st'] + 
            df['pis'] + 
            df['cofins']
        )
        
        # 5. Aplicar margem comercial (exemplo: 15%)
        df['margem_percentual'] = 0.15
        df['preco_sugerido'] = df['custo_total'] * (1 + df['margem_percentual'])
        
        # 6. Arredondar
        df['preco_sugerido'] = df['preco_sugerido'].round(2)
        
        return df
    
    def process_cotacao_file(self, filepath: Path, output_path: Path):
        """Processa arquivo de cotação e gera preços"""
        
        # Ler dados brutos
        if filepath.suffix == '.json':
            import json
            with open(filepath, 'r') as f:
                data = json.load(f)
            df = pd.DataFrame(data['items'])
        else:
            df = pd.read_excel(filepath)
        
        # Calcular preços
        df_precificado = self.calcular_preco_venda(df)
        
        # Salvar resultado
        df_precificado.to_excel(output_path, index=False)
        print(f"✅ Preços calculados salvos em: {output_path}")
        
        return df_precificado

# Uso
if __name__ == "__main__":
    engine = PricingEngine(netsuite_config={
        'saved_search_url': 'https://6245503.app.netsuite.com/...',  # Sua URL
        'token': os.getenv('NETSUITE_TOKEN')
    })
    
    engine.process_cotacao_file(
        filepath=Path("01_Bronze/Bionexo/cotacao_123.json"),
        output_path=Path("03_Gold/precos_calculados.xlsx")
    )
```

#### **1.4. Orquestração com Windows Task Scheduler**

Crie um arquivo `.bat` para automatizar:

```batch
REM run_daily_pricing.bat
@echo off
cd C:\Amoveri\Scripts
call venv\Scripts\activate

echo [%date% %time%] Iniciando extração Bionexo...
python extraction_bionexo.py >> logs\daily.log 2>&1

echo [%date% %time%] Processando precificação...
python pricing_engine.py >> logs\daily.log 2>&1

echo [%date% %time%] Concluído!
deactivate
```

Configure no **Task Scheduler**:
- Executar diariamente às 8h e 14h
- Rodar mesmo sem usuário logado
- Usar conta de serviço com acesso ao OneDrive

---

## **FASE 2: Escala e Robustez (2-4 meses)**

Nesta fase, implementamos o DuckDB e evoluímos para Parquet:

### Arquitetura com DuckDB

```python
# duckdb_pipeline.py
import duckdb
from pathlib import Path

class DataLakehousePipeline:
    """Pipeline ETL com DuckDB"""
    
    def __init__(self, data_path: Path):
        self.data_path = data_path
        self.db_path = data_path / "amoveri.duckdb"
        self.conn = duckdb.connect(str(self.db_path))
        self._setup_schema()
    
    def _setup_schema(self):
        """Cria esquema do banco"""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS cotacoes_raw (
                cotacao_id VARCHAR,
                portal VARCHAR,
                data_captura TIMESTAMP,
                dados JSON
            )
        """)
        
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS itens_cotacao (
                item_id VARCHAR PRIMARY KEY,
                cotacao_id VARCHAR,
                sku VARCHAR,
                descricao VARCHAR,
                quantidade INTEGER,
                unidade VARCHAR,
                data_entrega DATE
            )
        """)
    
    def ingest_json_to_duckdb(self, json_files: List[Path]):
        """Carrega JSONs para DuckDB"""
        for file in json_files:
            self.conn.execute(f"""
                INSERT INTO cotacoes_raw 
                SELECT * FROM read_json_auto('{file}')
            """)
    
    def export_to_parquet(self, table: str, output_path: Path):
        """Exporta tabela para Parquet"""
        self.conn.execute(f"""
            COPY {table} TO '{output_path}' 
            (FORMAT PARQUET, COMPRESSION ZSTD)
        """)
    
    def run_aggregation_gold(self):
        """Cria views agregadas para Power BI"""
        self.conn.execute("""
            CREATE OR REPLACE VIEW vw_kpis_comerciais AS
            SELECT 
                DATE_TRUNC('month', data_captura) as mes,
                portal,
                COUNT(DISTINCT cotacao_id) as total_cotacoes,
                SUM(quantidade * preco_sugerido) as valor_total,
                AVG(margem_percentual) as margem_media
            FROM itens_cotacao
            JOIN cotacoes_raw USING (cotacao_id)
            GROUP BY 1, 2
        """)
        
        # Exportar para Parquet
        self.export_to_parquet(
            'vw_kpis_comerciais',
            self.data_path / '03_Gold' / 'kpis_comerciais.parquet'
        )
```

### Conectar Power BI ao Parquet

```powerquery
// Power Query M
let
    Source = Parquet.Document(
        Web.Contents(
            "https://yourdomain.sharepoint.com/sites/AmoveriDataHub/Shared%20Documents/03_Gold/kpis_comerciais.parquet"
        )
    )
in
    Source
```

---

## **FASE 3: Machine Learning e Otimização (4-6 meses)**

Implementação dos modelos preditivos descritos no documento original:

```python
# ml_bidding_strategy.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

class BiddingOptimizer:
    """Otimiza lances usando ML"""
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
    
    def prepare_features(self, df_historico: pd.DataFrame) -> pd.DataFrame:
        """Engenharia de features"""
        df = df_historico.copy()
        
        # Features temporais
        df['mes'] = df['data_cotacao'].dt.month
        df['dia_semana'] = df['data_cotacao'].dt.dayofweek
        
        # Features de comportamento
        df['preco_vs_media_historica'] = df['preco_ofertado'] / df.groupby('cliente')['preco_ofertado'].transform('mean')
        
        # Features de concorrência
        df['num_concorrentes'] = df.groupby('cotacao_id')['fornecedor'].transform('count')
        
        return df
    
    def train(self, df_historico: pd.DataFrame):
        """Treina modelo de Win/Loss"""
        df = self.prepare_features(df_historico)
        
        X = df[['preco_ofertado', 'mes', 'dia_semana', 'preco_vs_media_historica', 'num_concorrentes']]
        y = df['ganhou']  # 1 = ganhou, 0 = perdeu
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        print(f"Acurácia do modelo: {score:.2%}")
        
        joblib.dump(self.model, 'modelo_bidding.pkl')
    
    def suggest_price(self, item: Dict, margem_minima: float = 0.10) -> float:
        """Sugere preço otimizado"""
        # Simular diferentes preços
        precos_teste = np.linspace(
            item['custo_total'] * (1 + margem_minima),
            item['preco_mercado'],
            num=50
        )
        
        # Prever probabilidade de vitória para cada preço
        features = self.prepare_features_single(item, precos_teste)
        prob_vitoria = self.model.predict_proba(features)[:, 1]
        
        # Calcular margem esperada
        margens = precos_teste - item['custo_total']
        valor_esperado = margens * prob_vitoria
        
        # Retornar preço que maximiza valor esperado
        idx_otimo = valor_esperado.argmax()
        return precos_teste[idx_otimo]
```

---

## 📋 **Recomendações Estratégicas para Amoveri Farma**

### 🎯 Comece AGORA (Esta Semana)

1. **Configure a estrutura de pastas no OneDrive** (15 min)
2. **Instale Python e dependências** (30 min)
   ```bash
   pip install playwright pandas openpyxl python-dotenv requests
   playwright install
   ```
3. **Crie o extrator simplificado da Bionexo** (2-3 dias)
4. **Teste a integração NetSuite → Power BI** que você já tem

### 🚀 Próximos 30 Dias

1. Automatize extração de **1 portal por vez** (Bionexo primeiro)
2. Implemente motor de precificação básico
3. Crie dashboard Power BI com 3 KPIs essenciais:
   - Taxa de conversão (cotações ganhas/total)
   - Margem média
   - Tempo de resposta

### 📊 Métrica de Sucesso

- **Semana 1**: Primeiro dashboard funcionando
- **Mês 1**: 50% das cotações sendo precificadas automaticamente
- **Mês 3**: 3 portais integrados + ML básico
- **Mês 6**: ROI positivo (horas economizadas vs. custo de desenvolvimento)

---

## ⚡ Código Completo Pronto para Usar

Quer que eu crie os arquivos Python completos e funcionais para você começar hoje? Posso gerar:

1. ✅ `extraction_bionexo.py` completo
2. ✅ `pricing_engine.py` adaptado para seu NetSuite
3. ✅ `config.yaml` com todas as configurações
4. ✅ `requirements.txt` com dependências
5. ✅ Scripts de Power Query para Power BI

**Pergunta**: Você quer que eu crie esses arquivos agora para você baixar e começar a implementar?