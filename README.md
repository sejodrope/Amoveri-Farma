# Projeto de Automação e Análise de Dados - Amoveri Farma

## Sobre o Projeto

Projeto de automação de processos, extração, tratamento e análise de dados para a área comercial da **Amoveri Farma** (antiga Pontual Farmacêutica).

**Responsável:** José Silva
**Área:** Comercial - Dados e Automação
**Início:** Janeiro/2026

---

## Objetivo

Automatizar rotinas da área comercial através de:
- Extração de dados de múltiplas fontes (NetSuite, SharePoint, Excel)
- Tratamento e transformação de dados (ETL)
- Análise e correlação de bases de dados
- Criação de dashboards e indicadores
- Automação de relatórios e processos manuais

---

## Sistemas Envolvidos

### Sistemas Principais
- **NetSuite (Oracle)** - ERP principal, fonte de dados de vendas
- **Microsoft 365** - Excel, Power BI, SharePoint, Teams
- **Bases de Dados Complementares** - Metas, comissões, tabelas auxiliares

### Acesso e Integrações
- [ ] Reunião com TI para levantamento de acessos
- [ ] APIs e credenciais NetSuite (SuiteTalk, SuiteAnalytics Connect)
- [ ] Permissões SharePoint/OneDrive
- [ ] Definição de infraestrutura de dados

---

## Escopo Inicial

### Fase 1: Levantamento (Em andamento)
- [x] Estrutura de planejamento criada
- [ ] Reunião com coordenadora comercial
- [ ] Reunião com responsável TI
- [ ] Mapeamento completo de processos
- [ ] Identificação de fontes de dados

### Fase 2: Tratamento de Dados NetSuite
**Primeira entrega:** Tratamento do relatório de vendas de janeiro/2026

**Transformações necessárias:**
1. Remover arredondamento da coluna Q
   - Fórmula atual: `=ARRED(N2;2) + ARRED(P2;2)`
   - Ajustar para: `= N2 + P2`

2. Ajustar referência na coluna R
   - Trocar referência de "P" para "Q"
   - Aplicar fórmula corrigida

**Campos identificados:**
- Coluna N: Desconto
- Coluna P: [A definir na reunião]
- Coluna Q: ADO TOTAL
- Coluna R: Pagamento Líquido
- Coluna S: Pedido

### Fase 3: Pipeline de Dados (Planejado)
- [ ] Arquitetura de ETL definida
- [ ] Conexão automatizada com NetSuite
- [ ] Data Warehouse estruturado
- [ ] Validação e qualidade de dados

### Fase 4: Dashboards e Análises (Planejado)
- [ ] Power BI - Dashboard executivo
- [ ] Análise de vendas por regional
- [ ] KPIs de performance
- [ ] Relatórios automatizados

---

## Estrutura do Repositório

```
Amoveri-Farma/
├── README.md                    # Este arquivo
├── Plano Inicial/              # Documentação de planejamento
│   ├── 00-INDICE.md            # Índice geral
│   ├── 01-CHECKLIST-LEVANTAMENTO.md
│   ├── 02-TEMPLATE-REUNIAO.md
│   ├── 03-MAPA-PROCESSOS.md
│   ├── 04-REQUISITOS-TECNICOS.md
│   └── 05-KPIS-METRICAS.md
├── Base de Dados/              # Dados brutos (não versionados)
├── scripts/                    # Scripts de automação (futuro)
├── etl/                        # Pipeline de dados (futuro)
└── dashboards/                 # Arquivos Power BI (futuro)
```

---

## Tecnologias Previstas

**Extração e Tratamento:**
- Python (pandas, requests, sqlalchemy)
- NetSuite APIs (SuiteTalk REST/SOAP)
- Microsoft Graph API

**Armazenamento:**
- SQL Server / PostgreSQL / Azure SQL (a definir)
- Azure Data Lake / Blob Storage (a definir)

**Visualização:**
- Power BI
- Excel (relatórios complementares)

**Automação:**
- Azure Data Factory / Apache Airflow (a definir)
- Python scripts + agendamento

---

## Status Atual

**Última atualização:** 2026-01-27

### Pendências Críticas
- [ ] Reunião com coordenadora comercial
- [ ] Reunião com responsável TI
- [ ] Definição de acessos e credenciais
- [ ] Validação de escopo e prioridades

### Próximos Passos
1. Realizar reuniões de levantamento
2. Documentar requisitos técnicos completos
3. Validar tratamento do relatório NetSuite
4. Definir arquitetura de dados
5. Criar primeiro pipeline (MVP)

---

## Documentação Detalhada

Toda a documentação detalhada está na pasta [Plano Inicial](./Plano%20Inicial/):

- **[00-INDICE](./Plano%20Inicial/00-INDICE.md)** - Índice e visão geral
- **[01-CHECKLIST-LEVANTAMENTO](./Plano%20Inicial/01-CHECKLIST-LEVANTAMENTO.md)** - Perguntas estruturadas para reuniões
- **[02-TEMPLATE-REUNIAO](./Plano%20Inicial/02-TEMPLATE-REUNIAO.md)** - Template para documentar reuniões
- **[03-MAPA-PROCESSOS](./Plano%20Inicial/03-MAPA-PROCESSOS.md)** - Processos identificados
- **[04-REQUISITOS-TECNICOS](./Plano%20Inicial/04-REQUISITOS-TECNICOS.md)** - Arquitetura e infraestrutura
- **[05-KPIS-METRICAS](./Plano%20Inicial/05-KPIS-METRICAS.md)** - Indicadores e dashboards

---

## Contato

**José Silva**
Área Comercial - Amoveri Farma
Foco: Dados, Análise e Automação

---

## Notas

- Este é um projeto em fase inicial de levantamento
- A arquitetura final será definida após reuniões com TI
- Prioridades serão ajustadas conforme necessidades do negócio
- Documentação será atualizada continuamente

---

*Projeto iniciado em janeiro/2026*
