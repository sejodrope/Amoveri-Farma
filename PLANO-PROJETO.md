# Plano de Projeto - Amoveri Farma

**Data:** 2026-01-30
**Responsável:** Pedro
**Status:** Em andamento

---

## Visao Geral

```
O que precisamos:

1. TABELA DE PRECOS  -> Produto x UF x Laboratorio (nao existe hoje)
2. INTEGRACAO        -> Bionexo ve nossos precos
3. MIDDLEWARE        -> Motor que calcula precos e orquestra tudo
4. DADOS             -> Relatorios de GT Plan, Apoio, Bionexo para analise
```

### Modelo de Negocio (atualizado 30/01)

```
IMPORTANTE - Descobertas da conversa com Bruna e Kamilla:

1. NAO TEMOS PRECO FIXO. Trabalhamos com FAIXAS DE PRECO:
   - Preco piso:  custo + impostos + margem minima (nao dar prejuizo)
   - Preco alvo:  custo + impostos + margem ideal
   - Preco teto:  PMC CMED (nunca ultrapassar, risco de multa)
   - Analistas negociam dentro da faixa conforme o cliente

2. AMOVERI ATUA EM DOIS PAPEIS:
   - DISTRIBUIDORA: compra dos labs e revende (margem propria)
   - OPERADORA LOGISTICA (OL): presta servico logistico para labs
     (desconto OL e diferente nesse caso)
   - Temos sedes/CDs em multiplos locais para guardar estoque

3. SOBRE ONDE FICAM OS PRECOS (resposta Kamilla):
   - No NetSuite: precisaria criar varios campos de precos (complexo)
   - Alternativa anterior: pasta no servidor com planilha de precos
   - DECISAO: Middleware local gera e mantem a tabela de precos
     O middleware e o dono da tabela, NAO o NetSuite
     NetSuite fornece custos, middleware calcula precos

4. PRECOS SAO RELATIVAMENTE ESTAVEIS:
   - Mudam quando: CMED atualiza (abril), tributacao muda, OL muda
   - Nao mudam a cada cotacao individual
   - Podem ficar fixados por meses
```

---

## Fases do Projeto (em ordem de prioridade)

### FASE 0: Reunião Bionexo + Coleta de Insumos
**Prazo:** Esta semana + próxima
**Responsável:** Pedro

**Segunda (14h):**
- [ ] Reunião com Bionexo (Gisele + Especialistas)
- [ ] Entender como Bionexo recebe preços (push/pull/CSV/API)
- [ ] Entender mapeamento de IDs (EAN, CNPJ, etc)
- [ ] Obter documentação da API e sandbox

**Após reunião:**
- [ ] Pedir para Bruna: lista dos 4-5 labs principais + tabelas OL
- [ ] Pedir para Kamila: credenciais API NetSuite (TBA)
- [ ] Pedir para Thiago: matriz tributária completa (NCM x UF)
- [ ] Fazer download da lista CMED atual (Anvisa)

**Entregável:** Ter todos os insumos para começar a construir

---

### FASE 1: Tabela de Preços (Pré-requisito de tudo)
**Responsável:** Pedro + Kamila + Thiago

**Sem tabela de preços = impossível integrar com Bionexo ou qualquer portal.**

**O que precisa ser construido:**

```
Para CADA produto, CADA estado, CADA laboratorio:

Custo Tributado = Custo (NetSuite)
               + ICMS-ST (Thiago: NCM x UF)
               + PIS/COFINS (0 se monofasico)

PRECO PISO  = Custo Tributado x (1 + Margem Minima) x (1 - Desconto OL)
PRECO ALVO  = Custo Tributado x (1 + Margem Ideal)  x (1 - Desconto OL)
PRECO TETO  = min(Custo Tributado x (1 + Margem Maxima) x (1 - OL), PMC)

VALIDACAO: SE Preco Alvo > PMC da UF -> Ajustar para PMC
           SE Preco Piso > PMC -> BLOQUEAR (produto inviavel nessa UF)

PARA BIONEXO: Publicar PRECO ALVO como referencia
              Analistas negociam dentro da faixa [PISO, TETO]

OBS: Quando Amoveri atua como OL (nao distribuidora),
     o calculo de margem/desconto e diferente
```

**Tarefas:**

1. **Onde fica a tabela** (decidido apos conversa com Kamilla 30/01):
   - [x] **DECISAO: Middleware local e o dono da tabela de precos**
   - Kamilla confirmou que no NetSuite precisaria criar muitos campos
   - A alternativa anterior era planilha no servidor (manual)
   - Middleware calcula e mantem a tabela automaticamente
   - NetSuite fornece apenas os CUSTOS dos produtos

2. **Coletar dados base:**
   - [ ] Exportar custos de todos os produtos do NetSuite (Saved Search)
   - [ ] Importar lista CMED com PMC por UF
   - [ ] Receber matriz tributária do Thiago
   - [ ] Receber tabelas OL da Bruna (por laboratório)

3. **Construir motor de cálculo (Python):**
   - [ ] Script que lê custo + tributos + margem + OL = preço final
   - [ ] Validação PMC automática
   - [ ] Gera tabela completa: Produto x UF x Lab

4. **Validar com equipe:**
   - [ ] Bruna valida preços de 10-20 produtos amostra
   - [ ] Thiago valida cálculos tributários
   - [ ] Kamila valida dados do NetSuite

**Entregável:** Tabela de preços funcional (mesmo que em SQLite/Excel)

---

### FASE 2: Middleware Local
**Responsável:** Pedro

**Stack tecnológico:**
```
Linguagem:  Python 3.11+
Database:   SQLite (início) → PostgreSQL (se precisar escalar)
Analytics:  DuckDB + Pandas
Scheduler:  Windows Task Scheduler (agendamento)
Interface:  CLI (linha de comando) → Web simples (futuro, FastAPI)
Storage:    OneDrive/SharePoint (já usamos)
BI:         Power BI
```

**Por que NÃO Azure/Cloud:**
- Não temos assinatura cloud
- Para o volume atual, PC local é suficiente
- Quando/se precisar escalar: migrar para VPS barata (R$50-100/mês)

**Componentes do middleware:**

```
middleware/
|-- main.py                    ← Orquestrador principal
|-- config.py                  ← Configurações e .env
|
|-- pricing/                   ← Motor de precificação
|   |-- calculator.py          ← Calcula preço (custo+icms+margem-ol)
|   |-- cmed_validator.py      ← Valida contra PMC
|   +-- tax_engine.py          ← Calcula ICMS-ST, PIS/COFINS
|
|-- extractors/                ← Extratores de dados
|   |-- netsuite.py            ← API NetSuite (custos, estoque)
|   |-- bionexo.py             ← API ou scraping Bionexo
|   |-- gtplan.py              ← Download relatórios GT Plan
|   +-- apoio_cotacoes.py      ← Download relatórios Apoio
|
|-- database/                  ← Camada de dados
|   |-- models.py              ← Definição das tabelas
|   |-- migrations.py          ← Criação/atualização de schema
|   +-- queries.py             ← Queries prontas
|
|-- exporters/                 ← Exportação de dados
|   |-- to_bionexo.py          ← Envia preços para Bionexo
|   |-- to_excel.py            ← Exporta para Excel/CSV
|   +-- to_powerbi.py          ← Alimenta Power BI
|
+-- utils/                     ← Utilitários
    |-- logger.py
    +-- validators.py          ← Validação EAN, CNPJ, etc
```

**Tarefas:**
- [ ] Criar estrutura de pastas do middleware
- [ ] Implementar database SQLite com tabelas (ver dicionário de dados)
- [ ] Implementar motor de precificação
- [ ] Implementar extrator NetSuite (custos)
- [ ] Implementar importador CMED
- [ ] Implementar interface de atualização OL

**Entregável:** Middleware rodando localmente, calculando preços

---

### FASE 3: Integração Bionexo
**Responsável:** Pedro + Bionexo
**Depende:** Fase 1 (tabela de preços) + Fase 2 (middleware)

**Baseado no que descobrirmos na reunião de segunda:**

- [ ] Implementar autenticação na API Bionexo
- [ ] Implementar envio de preços (push) ou exposição (pull)
- [ ] Mapear IDs: EAN (produto), CNPJ (fornecedor)
- [ ] Testar em sandbox
- [ ] Piloto com 10-20 produtos
- [ ] Go-live

**Entregável:** Bionexo enxerga nossos preços automaticamente

---

### FASE 4: Dados e Relatórios (GT Plan, Apoio, etc)
**Responsável:** Pedro

Mesmo sem integração API com GT Plan e Apoio Cotações, podemos:
- Fazer download de relatórios/CSVs dessas plataformas
- Importar para o middleware/database
- Consolidar dados para análise

**Tarefas:**
- [ ] Entender formato dos relatórios de cada plataforma
- [ ] Criar extratores/importadores (CSV → SQLite)
- [ ] Consolidar dados de todas as plataformas
- [ ] Criar visões analíticas (DuckDB + Pandas)
- [ ] Alimentar Power BI

**Entregável:** Base consolidada com dados de todos os portais

---

### FASE 5: Dashboards e Analytics
**Responsável:** Pedro

- [ ] Dashboard de cotações (volume, conversão, tempo de resposta)
- [ ] Dashboard de precificação (margem por produto, UF, lab)
- [ ] Alertas de PMC (produtos próximos do limite)
- [ ] Análise de competitividade
- [ ] KPIs de performance comercial

**Entregável:** Power BI com dashboards operacionais

---

## Tabelas do Database

| Tabela | Dados | Quem mantém | Frequência |
|--------|-------|-------------|------------|
| `produtos` | EAN, SKU, NCM, Nome | NetSuite (automático) | Diário |
| `precos` | Produto x UF x Lab = Faixa (piso/alvo/teto) | Motor de calculo | Sob trigger |
| `cmed_pmc` | PMC por EAN por UF | Import Anvisa | Anual (1 abril) |
| `ol_descontos` | Descontos por OL/Lab | Analistas (upload) | Frequente |
| `regras_labs` | Regras especiais | Analistas | Sob demanda |
| `matriz_tributaria` | ICMS-ST por NCM x UF | Thiago | Quando muda |
| `laboratorios` | 4-5 labs principais | Bruna | Raramente |
| `uf_icms` | Alíquota ICMS por UF | Thiago | Quando muda |
| `logs` | Auditoria de operações | Sistema | Contínuo |
| `cotacoes_importadas` | Dados de GT Plan, Apoio | Import CSV | Semanal |

Ver detalhes completos: [Dicionário de Dados](integrations/bionexo-netsuite/docs/06-DICIONARIO-DADOS.md)

---

## Cronograma Resumido

```
SEMANA 1 (atual):
  [x] Preparação reunião Bionexo
  [ ] Reunião segunda 14h
  [ ] Coletar insumos (Bruna, Kamila, Thiago)

SEMANA 2-3:
  [ ] Importar CMED
  [ ] Receber matriz tributária
  [ ] Criar database SQLite
  [ ] MVP motor de precificação (10-20 produtos)

SEMANA 4-5:
  [ ] Validar preços com equipe
  [ ] Expandir para todos os produtos
  [ ] Primeira chamada API Bionexo

SEMANA 6-8:
  [ ] Integração Bionexo funcional
  [ ] Importar dados GT Plan e Apoio
  [ ] Primeiro dashboard Power BI

MES 3+:
  [ ] Otimização e expansão
  [ ] Mais análises e automações
  [ ] Avaliar necessidade de servidor/cloud
```

---

## Decisoes Tomadas

| Decisao | Escolha | Justificativa |
|---------|---------|---------------|
| Hospedagem | PC local | Sem assinatura cloud. Suficiente para volume atual |
| Database | SQLite -> PostgreSQL | Comeca simples, migra se precisar |
| Linguagem | Python | Ja conhecemos, bom para dados |
| Analytics | DuckDB + Pandas | Leve, sem servidor |
| BI | Power BI | Ja usamos na empresa |
| Scheduler | Windows Task Scheduler | Ja disponivel no PC |
| Dono da tabela de precos | Middleware (nao NetSuite) | NetSuite fornece custos, middleware calcula e mantem precos. Evita criar campos complexos no NetSuite (feedback Kamilla) |
| Modelo de preco | Faixa (piso/alvo/teto) | Nao temos preco fixo. Analistas negociam dentro da faixa (feedback Bruna) |
| Papel Amoveri | Distribuidora + OL | Calculo de preco muda conforme o papel em cada operacao |

---

## Riscos

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| API Bionexo limitada/indisponível | Média | Alto | Alternativa: upload CSV |
| Thiago demora com matriz | Média | Alto | Começar com UFs principais |
| Kamila sem tempo para NetSuite | Média | Médio | Começar com exports manuais |
| PC pessoal = sem redundância | Alta | Médio | Backup OneDrive + Git |
| Volume cresce e PC não aguenta | Baixa | Médio | Migrar para VPS |

---

## O Que NÃO Faz Parte do Escopo (Por Enquanto)

- Automação de WhatsApp/Email (muito complexo, pouco ROI agora)
- Machine Learning / Previsão de demanda (futuro)
- App mobile
- Portal web próprio para clientes
- Integração com sistemas de faturamento

---

## Documentos Relacionados

- [README.md](README.md) - Visão geral do projeto
- [Diagramas e Fluxos](integrations/bionexo-netsuite/docs/05-DIAGRAMAS-FLUXOS.md) - Fluxogramas Mermaid
- [Dicionário de Dados](integrations/bionexo-netsuite/docs/06-DICIONARIO-DADOS.md) - Tabelas e mapeamento
- [Preparação Reunião](integrations/bionexo-netsuite/docs/01-PREPARACAO-REUNIAO.md) - Guia para segunda
- [Checklist Técnico](integrations/bionexo-netsuite/docs/02-CHECKLIST-TECNICO-API.md) - Perguntas API
