# 🚀 Guia de Implementação Completo - Automação Amoveri Farma

**Última atualização:** 2026-01-29
**Status:** 🟢 Pronto para implementação
**Responsável:** José Silva

---

## 📋 Índice Rápido

1. [Visão Geral](#visão-geral)
2. [Pré-requisitos](#pré-requisitos)
3. [FASE 1: Quick Wins (Esta Semana)](#fase-1-quick-wins)
4. [FASE 2: Escala (Próximos 2 meses)](#fase-2-escala)
5. [FASE 3: Machine Learning (4-6 meses)](#fase-3-machine-learning)
6. [Troubleshooting](#troubleshooting)

---

## 🎯 Visão Geral

### O Que Vamos Fazer

Automatizar o processo de cotações e precificação da Amoveri Farma através de:

**Sistemas envolvidos:**
- **Bionexo** - Portal de cotações (principal)
- **Apoio Cotações** - Portal de cotações (secundário)
- **GT Plan** - Portal de cotações (secundário)
- **NetSuite** - ERP (custos, estoque, regras fiscais)

**Resultado final:**
- Extração automática de cotações dos 3 portais
- Cálculo automático de preços com ICMS-ST, PIS/COFINS
- Dashboards em Power BI com análises
- Economia de 15-20 horas/semana de trabalho manual

### Arquitetura Simplificada - Fase 1

```
┌─────────────────────────────────────────────────────┐
│  Bionexo / Apoio / GT Plan                          │
│  (Portais de Cotação)                               │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼ Python Scripts (Playwright)
┌─────────────────────────────────────────────────────┐
│  OneDrive/SharePoint                                │
│  ├── Bronze/ (dados brutos)                         │
│  ├── Silver/ (dados tratados)                       │
│  └── Gold/ (preços calculados)                      │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼ Pandas + DuckDB
┌─────────────────────────────────────────────────────┐
│  NetSuite (API/Consultas Web)                       │
│  - Custos, Estoque, Matriz Tributária               │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼ Power BI
┌─────────────────────────────────────────────────────┐
│  Dashboards e Análises                              │
└─────────────────────────────────────────────────────┘
```

---

## ✅ Pré-requisitos

### 1. Softwares Necessários

#### Python 3.11+ (OBRIGATÓRIO)
```bash
# Baixar de: https://www.python.org/downloads/
# Durante instalação: MARCAR "Add Python to PATH"

# Verificar instalação:
python --version
# Deve mostrar: Python 3.11.x ou superior
```

#### Git (OBRIGATÓRIO)
```bash
# Baixar de: https://git-scm.com/download/win
# Usar configurações padrão

# Verificar instalação:
git --version
```

#### Visual Studio Code (RECOMENDADO)
```bash
# Baixar de: https://code.visualstudio.com/
# Extensões recomendadas:
# - Python (Microsoft)
# - Pylance (Microsoft)
# - Jupyter (Microsoft)
```

#### Power BI Desktop (OBRIGATÓRIO)
```bash
# Baixar de: https://powerbi.microsoft.com/pt-br/downloads/
# Já está instalado? Verificar versão
```

### 2. Credenciais Necessárias

**Coletar com TI antes de começar:**

- [ ] **Bionexo**
  - Email de acesso: `__________________`
  - Senha: (guardar em cofre de senhas)
  - URL do portal: `https://bionexonew.bionexo.com`

- [ ] **Apoio Cotações**
  - Email de acesso: `__________________`
  - Senha: (guardar em cofre de senhas)
  - URL do portal: `__________________`

- [ ] **GT Plan**
  - Email de acesso: `__________________`
  - Senha: (guardar em cofre de senhas)
  - URL do portal: `__________________`

- [ ] **NetSuite**
  - URL da conta: `https://6245503.app.netsuite.com` (exemplo)
  - Token de acesso (TBA - Token Based Authentication)
  - ID da Saved Search de custos: `__________________`
  - ID da Saved Search de estoque: `__________________`

- [ ] **OneDrive/SharePoint**
  - Caminho local do OneDrive: `C:\Users\jose.silva\OneDrive - Amoveri`
  - URL do SharePoint: `__________________`

### 3. Acessos e Permissões

**Validar com TI:**

- [ ] Acesso de leitura ao NetSuite (consultas web salvas)
- [ ] Permissão de escrita no SharePoint
- [ ] Acesso aos portais de cotação (Bionexo, Apoio, GT Plan)
- [ ] Permissão para instalar software no computador
- [ ] VPN corporativa configurada (se aplicável)

---

## 🚀 FASE 1: Quick Wins (Esta Semana)

**Objetivo:** Ter o primeiro pipeline funcionando em 5-7 dias

### Dia 1: Configuração do Ambiente

#### 1.1. Criar Estrutura de Pastas

**Local:** OneDrive corporativo

```powershell
# Abrir PowerShell como Administrador
# Ajustar o caminho para seu OneDrive

$BASE = "C:\Users\jose.silva\OneDrive - Amoveri\Amoveri_DataHub"

# Criar pastas
New-Item -ItemType Directory -Path "$BASE\01_Bronze\Bionexo" -Force
New-Item -ItemType Directory -Path "$BASE\01_Bronze\Apoio" -Force
New-Item -ItemType Directory -Path "$BASE\01_Bronze\GTPlan" -Force
New-Item -ItemType Directory -Path "$BASE\02_Silver" -Force
New-Item -ItemType Directory -Path "$BASE\03_Gold" -Force
New-Item -ItemType Directory -Path "$BASE\04_Logs" -Force
New-Item -ItemType Directory -Path "$BASE\05_Config" -Force

Write-Host "✅ Estrutura de pastas criada em: $BASE"
```

**Resultado esperado:**
```
Amoveri_DataHub/
├── 01_Bronze/
│   ├── Bionexo/
│   ├── Apoio/
│   └── GTPlan/
├── 02_Silver/
├── 03_Gold/
├── 04_Logs/
└── 05_Config/
```

#### 1.2. Configurar Ambiente Python

```powershell
# Navegar para pasta do projeto
cd C:\Users\jose.silva\Documents\Amoveri-Farma

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate

# Verificar ativação (deve mostrar (venv) no prompt)
# Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# Instalar browsers do Playwright
playwright install chromium
```

#### 1.3. Criar Arquivo de Configuração

**Arquivo:** `05_Config/.env`

```bash
# Caminho do OneDrive
ONEDRIVE_PATH=C:\Users\jose.silva\OneDrive - Amoveri\Amoveri_DataHub

# Credenciais Bionexo
BIONEXO_EMAIL=seu_email@amoverifarma.com.br
BIONEXO_PASSWORD=sua_senha_aqui

# Credenciais Apoio Cotações
APOIO_EMAIL=seu_email@amoverifarma.com.br
APOIO_PASSWORD=sua_senha_aqui

# Credenciais GT Plan
GTPLAN_EMAIL=seu_email@amoverifarma.com.br
GTPLAN_PASSWORD=sua_senha_aqui

# NetSuite
NETSUITE_ACCOUNT_ID=6245503
NETSUITE_TOKEN_ID=seu_token_id
NETSUITE_TOKEN_SECRET=seu_token_secret
NETSUITE_CONSUMER_KEY=sua_consumer_key
NETSUITE_CONSUMER_SECRET=sua_consumer_secret
NETSUITE_SAVED_SEARCH_CUSTOS=123
NETSUITE_SAVED_SEARCH_ESTOQUE=456

# Configurações gerais
LOG_LEVEL=INFO
HEADLESS_MODE=false  # true para rodar sem abrir navegador
```

**⚠️ SEGURANÇA:**
```powershell
# Adicionar .env ao .gitignore (se ainda não estiver)
echo ".env" >> .gitignore
echo "05_Config/.env" >> .gitignore
```

---

### Dia 2-3: Implementar Extrator Bionexo

**Objetivo:** Conseguir extrair a primeira cotação automaticamente

#### 2.1. Entender a Estrutura da Bionexo

**AÇÃO MANUAL (10 minutos):**

1. Abrir navegador e logar na Bionexo manualmente
2. Navegar para lista de cotações
3. Abrir DevTools (F12) → aba Network
4. Recarregar a página
5. Procurar por chamadas de API (filtrar por XHR/Fetch)
6. Anotar:
   - URLs das APIs (`/api/cotacoes`, `/api/itens`, etc.)
   - Estrutura JSON de resposta
   - Seletores CSS dos elementos (se não houver API)

**Exemplo de anotações:**
```
URL Login: https://bionexonew.bionexo.com/login
API Cotações: https://bionexonew.bionexo.com/api/v1/cotacoes?status=ativa
Seletor lista: .cotacao-card
Seletor botão download: button[data-action="download"]
```

#### 2.2. Testar Script de Extração

**Arquivo:** `scripts/extraction_bionexo.py` (já criado)

```powershell
# Ativar ambiente virtual
.\venv\Scripts\Activate

# Executar script de teste
python scripts/extraction_bionexo.py

# O que deve acontecer:
# 1. Navegador abre (visível se HEADLESS_MODE=false)
# 2. Faz login automaticamente
# 3. Navega para cotações
# 4. Extrai dados
# 5. Salva JSON em 01_Bronze/Bionexo/
```

**Possíveis problemas e soluções:**

| Problema | Solução |
|----------|---------|
| Erro de login | Verificar credenciais no .env |
| Timeout | Aumentar `page.wait_for_timeout(5000)` |
| Seletor não encontrado | Atualizar seletores CSS (site mudou) |
| JSON vazio | Bionexo pode estar usando GraphQL - verificar aba Network |

#### 2.3. Validar Dados Extraídos

```powershell
# Verificar arquivos gerados
ls "C:\Users\jose.silva\OneDrive - Amoveri\Amoveri_DataHub\01_Bronze\Bionexo"

# Deve mostrar arquivos .json com timestamp
# Exemplo: cotacao_12345_20260129_143022.json
```

**Abrir JSON e validar campos:**
- ✅ `cotacao_id`
- ✅ `cliente`
- ✅ `data_entrega`
- ✅ `itens[]` (array de produtos)
  - ✅ `sku`
  - ✅ `descricao`
  - ✅ `quantidade`
  - ✅ `unidade`

---

### Dia 4-5: Implementar Motor de Precificação

**Objetivo:** Calcular preço de venda com impostos

#### 4.1. Preparar Matriz Tributária

**AÇÃO MANUAL (30 minutos):**

1. **Exportar matriz tributária do NetSuite** (ou criar planilha inicial)
   - Ir para: Configurações → Impostos → ICMS-ST
   - Exportar para Excel

2. **Estrutura da planilha:**

| NCM | UF_Destino | MVA_Ajustada | Aliq_Interna | Observacao |
|-----|------------|--------------|--------------|------------|
| 30049099 | SP | 53.76 | 0.18 | Medicamentos |
| 30049099 | RJ | 41.50 | 0.20 | Medicamentos |
| 30021099 | SP | 36.00 | 0.18 | Imunológicos |

3. **Salvar como:** `05_Config/matriz_tributaria.xlsx`

#### 4.2. Configurar Conexão com NetSuite

**Arquivo:** `scripts/netsuite_client.py`

Testar conexão:
```powershell
python scripts/test_netsuite_connection.py

# Deve retornar:
# ✅ Conexão com NetSuite OK
# ✅ Saved Search de custos: 50 registros encontrados
# ✅ Saved Search de estoque: 50 registros encontrados
```

Se der erro:
1. Verificar credenciais no `.env`
2. Verificar se Token Based Authentication está habilitado no NetSuite
3. Validar IDs das Saved Searches

#### 4.3. Executar Precificação

```powershell
# Processar cotação extraída
python scripts/pricing_engine.py \
  --input "01_Bronze/Bionexo/cotacao_12345_20260129_143022.json" \
  --output "03_Gold/precos_calculados_12345.xlsx"

# Tempo estimado: 30-60 segundos (dependendo da quantidade de itens)
```

**Verificar resultado:**
1. Abrir `03_Gold/precos_calculados_12345.xlsx`
2. Validar colunas:
   - ✅ `sku`
   - ✅ `descricao`
   - ✅ `quantidade`
   - ✅ `custo_medio` (do NetSuite)
   - ✅ `estoque_disponivel` (do NetSuite)
   - ✅ `icms_st_calculado`
   - ✅ `pis_calculado`
   - ✅ `cofins_calculado`
   - ✅ `custo_total`
   - ✅ `preco_sugerido`
   - ✅ `margem_percentual`

3. **Validação manual (importante!):**
   - Escolher 3-5 produtos aleatórios
   - Calcular manualmente o ICMS-ST
   - Comparar com resultado do script
   - Diferença aceitável: < R$ 0,10

---

### Dia 6-7: Dashboard Power BI

**Objetivo:** Visualizar dados em dashboard executivo

#### 6.1. Conectar Power BI ao Excel do OneDrive

**Passo a passo:**

1. Abrir Power BI Desktop
2. **Obter Dados → Excel**
3. Navegar até: `C:\Users\jose.silva\OneDrive - Amoveri\Amoveri_DataHub\03_Gold\precos_calculados_12345.xlsx`
4. Selecionar planilha → **Carregar**

5. **Obter Dados → Web** (para NetSuite)
   - URL: `https://6245503.app.netsuite.com/app/common/search/searchresults.nl?searchid=123&...`
   - Autenticação: Web API
   - Usar credenciais do NetSuite

#### 6.2. Criar Medidas DAX

```dax
// Valor Total Cotação
Valor_Total = SUMX(Cotacoes, [quantidade] * [preco_sugerido])

// Margem Média
Margem_Media = AVERAGE(Cotacoes[margem_percentual])

// Taxa de Conversão (se houver histórico)
Taxa_Conversao =
    DIVIDE(
        CALCULATE(COUNT(Cotacoes[cotacao_id]), Cotacoes[status] = "Ganha"),
        COUNT(Cotacoes[cotacao_id]),
        0
    )

// Economia de Tempo (meta: 20h/semana)
Horas_Economizadas =
    COUNTROWS(Cotacoes) * 0.5  // 30 min por cotação
```

#### 6.3. Montar Dashboard Executivo

**Layout sugerido:**

```
┌────────────────────────────────────────────────────────┐
│  DASHBOARD COMERCIAL - AMOVERI FARMA                   │
├────────────────────────────────────────────────────────┤
│                                                         │
│  📊 KPIs Principais                                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ Total    │ │ Margem   │ │ Taxa     │ │ Horas    │ │
│  │ Cotações │ │ Média    │ │ Conversão│ │ Economiz.│ │
│  │   125    │ │  15.2%   │ │  42.5%   │ │   62h    │ │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ │
│                                                         │
│  📈 Evolução Mensal                                    │
│  [Gráfico de linha: Cotações por dia]                 │
│                                                         │
│  🏆 Top 10 Produtos                                    │
│  [Gráfico de barras: Produtos mais cotados]           │
│                                                         │
│  🎯 Win/Loss Analysis                                  │
│  [Gráfico de pizza: Cotações ganhas vs perdidas]      │
│                                                         │
└────────────────────────────────────────────────────────┘
```

**Salvar como:** `dashboards/Dashboard_Comercial_v1.pbix`

---

## 📅 Cronograma Detalhado - Fase 1

### Semana 1

| Dia | Tarefa | Tempo Est. | Responsável | Status |
|-----|--------|------------|-------------|--------|
| Seg | Instalar software + criar pastas | 2h | José | ⬜ |
| Ter | Configurar Python + .env | 2h | José | ⬜ |
| Qua | Implementar extrator Bionexo | 4h | José | ⬜ |
| Qui | Testar extração + ajustes | 3h | José | ⬜ |
| Sex | Implementar motor precificação | 4h | José | ⬜ |
| Sáb/Dom | (Opcional) Testar precificação | 2h | José | ⬜ |

### Semana 2

| Dia | Tarefa | Tempo Est. | Responsável | Status |
|-----|--------|------------|-------------|--------|
| Seg | Conectar NetSuite | 3h | José + TI | ⬜ |
| Ter | Validar cálculos tributários | 4h | José + Fiscal | ⬜ |
| Qua | Criar dashboard Power BI | 3h | José | ⬜ |
| Qui | Testes end-to-end | 4h | José | ⬜ |
| Sex | Apresentação para gestão | 2h | José + Coord. | ⬜ |

---

## 🔄 FASE 2: Escala (Meses 2-4)

**Objetivo:** Automatizar os 3 portais e implementar DuckDB

### 2.1. Adicionar Apoio Cotações e GT Plan

**Tempo estimado:** 1-2 semanas por portal

Repetir processo da Bionexo:
1. Análise do portal (seletores CSS, APIs)
2. Implementação do extrator
3. Testes
4. Integração com motor de precificação

**Arquivo:** `scripts/extraction_apoio.py` (similar ao Bionexo)
**Arquivo:** `scripts/extraction_gtplan.py` (similar ao Bionexo)

### 2.2. Implementar DuckDB para Performance

**Por quê DuckDB?**
- Consultas SQL em arquivos Parquet
- 10x mais rápido que Pandas para grandes volumes
- Sem necessidade de servidor de banco de dados

**Instalação:**
```powershell
pip install duckdb pyarrow
```

**Migração de Excel para Parquet:**
```python
# Converter Excel para Parquet (mais rápido)
import pandas as pd

df = pd.read_excel('03_Gold/precos_calculados.xlsx')
df.to_parquet('03_Gold/precos_calculados.parquet', compression='zstd')

# Tamanho: Excel ~5MB → Parquet ~500KB (10x menor!)
```

**Consultas com DuckDB:**
```python
import duckdb

# Conectar
conn = duckdb.connect('amoveri.duckdb')

# Query SQL diretamente em Parquet
result = conn.execute("""
    SELECT
        portal,
        COUNT(*) as total_cotacoes,
        AVG(margem_percentual) as margem_media
    FROM read_parquet('03_Gold/*.parquet')
    WHERE data_captura >= '2026-01-01'
    GROUP BY portal
""").fetchdf()

print(result)
```

### 2.3. Automação com Task Scheduler

**Criar arquivo batch:** `scripts/run_daily_pipeline.bat`

```batch
@echo off
cd C:\Users\jose.silva\Documents\Amoveri-Farma
call venv\Scripts\activate

echo [%date% %time%] === INICIANDO PIPELINE DIARIO ===

REM Bionexo
echo [%date% %time%] Extraindo Bionexo...
python scripts/extraction_bionexo.py >> logs/daily.log 2>&1

REM Apoio
echo [%date% %time%] Extraindo Apoio...
python scripts/extraction_apoio.py >> logs/daily.log 2>&1

REM GT Plan
echo [%date% %time%] Extraindo GT Plan...
python scripts/extraction_gtplan.py >> logs/daily.log 2>&1

REM Precificação
echo [%date% %time%] Calculando precos...
python scripts/pricing_engine.py --all >> logs/daily.log 2>&1

echo [%date% %time%] === PIPELINE CONCLUIDO ===
deactivate
```

**Agendar no Windows:**
1. Abrir **Task Scheduler** (`taskschd.msc`)
2. **Criar Tarefa Básica**
3. Nome: `Amoveri - Pipeline Diario`
4. Gatilho: **Diariamente às 8:00 e 14:00**
5. Ação: **Iniciar programa**
   - Programa: `C:\Users\jose.silva\Documents\Amoveri-Farma\scripts\run_daily_pipeline.bat`
6. **Executar mesmo sem usuário logado** (usar conta de serviço)

---

## 🤖 FASE 3: Machine Learning (Meses 4-6)

**Objetivo:** Otimizar preços usando histórico de ganho/perda

### 3.1. Coletar Dados Históricos

**Requisito:** Mínimo 6 meses de histórico (ideal: 1 ano)

**Estrutura necessária:**
```csv
cotacao_id,cliente,uf,produto,quantidade,preco_ofertado,preco_concorrente,ganhou,margem
12345,Cliente A,SP,Produto X,100,50.00,52.00,1,0.15
12346,Cliente B,RJ,Produto Y,200,75.00,73.00,0,0.18
```

### 3.2. Treinar Modelo de Win/Loss

```python
# scripts/ml_train_model.py
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Carregar histórico
df = pd.read_parquet('03_Gold/historico_cotacoes.parquet')

# Features
X = df[['preco_ofertado', 'margem', 'quantidade', 'uf', 'dia_semana']]
y = df['ganhou']  # 1 = ganhou, 0 = perdeu

# Treinar
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Avaliar
from sklearn.metrics import classification_report
print(classification_report(y_test, model.predict(X_test)))

# Salvar modelo
import joblib
joblib.dump(model, 'models/win_loss_model.pkl')
```

### 3.3. Usar Modelo para Sugerir Preços

```python
# Integrar no pricing_engine.py
def suggest_optimized_price(item, model):
    """Sugere preço otimizado usando ML"""

    # Simular diferentes preços
    prices = np.linspace(item['custo_total'] * 1.10, item['preco_mercado'], 50)

    # Prever probabilidade de ganhar para cada preço
    features = prepare_features(item, prices)
    win_prob = model.predict_proba(features)[:, 1]

    # Calcular valor esperado
    expected_value = (prices - item['custo_total']) * win_prob

    # Retornar preço que maximiza valor esperado
    return prices[expected_value.argmax()]
```

---

## 🔧 Troubleshooting

### Problema 1: Extração Bionexo Falhando

**Sintomas:**
- Script trava no login
- Timeout errors
- Captcha aparece

**Soluções:**
```python
# 1. Aumentar timeout
page.wait_for_timeout(10000)  # 10 segundos

# 2. Usar user-agent real
context = browser.new_context(
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
)

# 3. Salvar cookies da sessão
context.storage_state(path='cookies.json')
# Na próxima execução:
context = browser.new_context(storage_state='cookies.json')

# 4. Se captcha persistir, usar 2Captcha API
```

### Problema 2: Cálculo de ICMS-ST Incorreto

**Validação:**
```python
# Teste unitário
def test_icms_st():
    item = {
        'preco_produto': 100.00,
        'ncm': '30049099',
        'uf_origem': 'SP',
        'uf_destino': 'RJ'
    }

    result = calcular_icms_st(item)

    # Cálculo manual:
    # Base ST = 100 * (1 + 0.4150) = 141.50
    # ICMS Próprio = 100 * 0.12 = 12.00
    # ICMS ST = (141.50 * 0.20) - 12.00 = 16.30

    assert abs(result - 16.30) < 0.01, f"Esperado 16.30, obtido {result}"
```

### Problema 3: Power BI Não Atualiza Dados

**Soluções:**
1. **Refresh manual:** Abrir .pbix → Atualizar
2. **Agendamento automático:** Publicar no Power BI Service → Configurar refresh
3. **Gateway:** Instalar Power BI Gateway para dados on-premise

---

## 📊 Métricas de Sucesso

### KPIs do Projeto

| Métrica | Meta Fase 1 | Meta Fase 2 | Meta Fase 3 |
|---------|-------------|-------------|-------------|
| % Cotações automatizadas | 30% | 80% | 95% |
| Tempo médio por cotação | 15 min | 5 min | 2 min |
| Horas economizadas/semana | 10h | 20h | 30h |
| Precisão cálculo impostos | 95% | 98% | 99% |
| Taxa de adoção (usuários) | 50% | 80% | 100% |
| ROI (R$ economizado / R$ investido) | 2x | 5x | 10x |

### Como Medir

**Arquivo:** `scripts/metrics_tracker.py`

```python
import pandas as pd
from datetime import datetime

class MetricsTracker:
    def log_execution(self, portal, cotacoes_processadas, tempo_total):
        """Registra execução do pipeline"""
        log = {
            'timestamp': datetime.now(),
            'portal': portal,
            'cotacoes_processadas': cotacoes_processadas,
            'tempo_total_segundos': tempo_total,
            'tempo_medio_por_cotacao': tempo_total / cotacoes_processadas
        }

        # Salvar em CSV
        df = pd.DataFrame([log])
        df.to_csv('04_Logs/metrics.csv', mode='a', header=False, index=False)

    def generate_report(self):
        """Gera relatório mensal de métricas"""
        df = pd.read_csv('04_Logs/metrics.csv')

        report = {
            'total_cotacoes': df['cotacoes_processadas'].sum(),
            'tempo_total_horas': df['tempo_total_segundos'].sum() / 3600,
            'tempo_medio_minutos': df['tempo_medio_por_cotacao'].mean() / 60
        }

        return report
```

---

## 📞 Contatos e Suporte

**Dúvidas Técnicas:**
- José Silva (você) - Implementação

**Validações de Negócio:**
- Coordenadora Comercial - Regras de precificação
- Responsável TI - Acessos e infraestrutura
- Fiscal/Contábil - Validação cálculos tributários

**Suporte Externo:**
- NetSuite Support: https://www.netsuite.com/portal/resource/support.shtml
- Playwright Docs: https://playwright.dev/python/
- Power BI Community: https://community.powerbi.com/

---

## ✅ Checklist Final - Antes de Ir para Produção

### Técnico
- [ ] Scripts funcionando sem erros
- [ ] Logs sendo gravados corretamente
- [ ] Backup automático configurado
- [ ] Tratamento de erros implementado
- [ ] Variáveis de ambiente seguras (.env não versionado)
- [ ] Documentação atualizada
- [ ] Task Scheduler configurado
- [ ] Testes de carga realizados (100+ cotações)

### Negócio
- [ ] Cálculos validados pelo fiscal
- [ ] Aprovação da coordenadora comercial
- [ ] Treinamento dos usuários realizado
- [ ] Processo de fallback definido (se sistema cair)
- [ ] SLA acordado (tempo de resposta)
- [ ] Plano de contingência documentado

### Compliance
- [ ] Dados sensíveis protegidos
- [ ] LGPD: Consentimento para uso de dados
- [ ] Auditoria: Logs rastreáveis
- [ ] Credenciais rotacionadas regularmente
- [ ] Backup testado (recovery point objetivo < 24h)

---

## 🎯 Próximos Passos Imediatos

**HOJE:**
1. ✅ Ler este guia completamente
2. ✅ Validar pré-requisitos (softwares, credenciais)
3. ✅ Agendar reunião com TI (obter credenciais NetSuite)

**ESTA SEMANA:**
1. ✅ Configurar ambiente (Dia 1)
2. ✅ Implementar extrator Bionexo (Dias 2-3)
3. ✅ Implementar precificação (Dias 4-5)
4. ✅ Dashboard Power BI (Dias 6-7)

**PRÓXIMO MÊS:**
1. ✅ Adicionar Apoio Cotações e GT Plan
2. ✅ Migrar para DuckDB
3. ✅ Automatizar com Task Scheduler
4. ✅ Treinar equipe

---

**Lembre-se:**
> "Done is better than perfect"
> Comece simples, valide rápido, itere constantemente.

Boa implementação! 🚀
