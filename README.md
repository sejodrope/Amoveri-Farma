# Amoveri Farma - Inteligência Comercial

**Responsável:** Pedro (José Silva)
**Área:** Inteligência Comercial - Dados e Automação
**Início:** Janeiro/2026
**Última atualização:** 2026-01-30

---

## O Que É Este Projeto

Automação de cotações, precificação e análise de dados da Amoveri Farma (distribuidora farmacêutica).

### Problema Atual
- Cotações respondidas manualmente em múltiplos portais (Bionexo, GT Plan, Apoio Cotações)
- Sem tabela de preços estruturada no NetSuite
- Cálculos de ICMS, PMC e descontos OL feitos em planilha/Excel
- Comunicação com clientes via WhatsApp/email/chat portal sem rastreamento
- Cada laboratório tem regras e OLs diferentes

### Objetivo
Criar um middleware local (Python) que:
1. **Centraliza preços** - Tabela de precificação por Produto x UF x Laboratório
2. **Integra com portais** - Bionexo, GT Plan, Apoio Cotações
3. **Automatiza cálculos** - ICMS-ST, PIS/COFINS, PMC CMED, descontos OL
4. **Alimenta dashboards** - Power BI para tomada de decisão

---

## Plataformas de Cotação

| Plataforma | Tipo | Status Acesso | Integração |
|------------|------|---------------|------------|
| **Bionexo** | Portal principal | Credenciais obtidas | API (reunião segunda) |
| **GT Plan** | Portal | Credenciais obtidas | Download relatórios |
| **Apoio Cotações** | Portal | Credenciais obtidas | Download relatórios |
| **NetSuite** | ERP (custos, estoque) | Credenciais API pendentes | SuiteScript/REST |
| **WhatsApp/Email** | Comunicação clientes | Funcionando | Manual |

---

## Regras de Negócio

1. **PMC CMED** - Preço Maximo ao Consumidor. Atualiza todo 1 de abril. Nunca ultrapassar.
2. **ICMS por UF** - Varia por NCM + estado destino. Impacta preco final.
3. **OL Descontos** - Mudam frequentemente. Cada laboratorio tem desconto diferente.
4. **4-5 Labs principais** - Cada um com regras comerciais especificas.
5. **Thiago** - Responsavel pela matriz tributaria (NCM x UF).

---

## Arquitetura

```
PORTAIS DE COTACAO
  Bionexo | GT Plan | Apoio Cotacoes | WhatsApp/Email
          |
          v  API / Scraping / Download CSV
MIDDLEWARE LOCAL (Python no PC)
  +--------------------------------------+
  | Motor de Precificacao                |
  | Custo + ICMS + Margem - OL <= PMC    |
  +--------------------------------------+
  | Database Local (SQLite/DuckDB)       |
  | - Tabela de Precos (Prod x UF x Lab) |
  | - CMED/PMC                           |
  | - Descontos OL                       |
  | - Regras Labs                        |
  | - Matriz Tributaria                  |
  +--------------------------------------+
          |
          v
NETSUITE ERP
  Custos | Estoque | Pedidos | Fiscal
          |
          v
DASHBOARDS (Power BI)
  Analises | KPIs | Relatorios
```

---

## Estrutura do Projeto

```
Amoveri-Farma/
|-- README.md                      <-- VOCE ESTA AQUI
|-- PLANO-PROJETO.md               <-- Plano com fases e prioridades
|
|-- integrations/                  <-- Integracoes com plataformas
|   +-- bionexo-netsuite/
|       |-- INICIO-RAPIDO.md       <-- Guia rapido
|       +-- docs/                  <-- Documentacao reuniao segunda
|
|-- scripts/                       <-- Scripts Python (a desenvolver)
|-- tests/                         <-- Testes
|-- logs/                          <-- Logs de execucao
|
|-- _archive/                      <-- Docs antigos (referencia)
|
|-- .env.example
|-- requirements.txt
+-- .gitignore
```

---

## Status (30/01/2026)

### Feito
- [x] Estrutura inicial do projeto
- [x] Credenciais Bionexo, GT Plan, Apoio obtidas
- [x] Documentacao para reuniao de segunda preparada
- [x] Diagramas de fluxo e dicionario de dados criados

### Proxima Acao
- [ ] **Segunda 14h: Reuniao com Bionexo** (Gisele + Especialistas)
- [ ] Criar tabela de precos (nao existe no NetSuite hoje)
- [ ] Obter credenciais API NetSuite (Kamila)
- [ ] Obter matriz tributaria (Thiago)
- [ ] Listar 4-5 labs principais e OLs (Bruna)

---

## Equipe

| Nome | Papel | Responsabilidade |
|------|-------|-----------------|
| Pedro | Inteligencia Comercial | Dev, dados, automacao, middleware |
| Bruna | Comercial | Processos, regras, labs |
| Kamila | TI NetSuite | Config NetSuite, API, campos |
| Thiago | Tributacao | Matriz fiscal, ICMS-ST |
| Analistas | Comercial | Regras labs, OL, cotacoes |

---

## Documentacao Reuniao (Segunda)

Ver [integrations/bionexo-netsuite/docs/](integrations/bionexo-netsuite/docs/)
