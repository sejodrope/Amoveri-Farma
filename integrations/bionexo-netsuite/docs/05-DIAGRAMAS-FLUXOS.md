# Diagramas e Fluxogramas - Integração Bionexo x NetSuite

**Data:** 2026-01-30
**Responsável:** Pedro (Inteligência Comercial)
**Atualizado após conversa com Bruna (Comercial)**

---

## ESCOPO DA INTEGRAÇÃO (Atualizado)

```
A integração Bionexo ↔ NetSuite é para que a BIONEXO ENXERGUE
os PREÇOS que estão no NetSuite.

Direção principal: NetSuite → Bionexo (preços)

PROBLEMA ATUAL: Não temos tabela de preços no NetSuite.
AÇÃO NECESSÁRIA: Criar tabela de preços por ESTADO (UF) e por
LABORATÓRIO/FORNECEDOR (4-5 principais) antes de integrar.
```

---

## 1. FLUXO ATUAL (AS-IS) - Sem Tabela de Preços

```mermaid
flowchart TD
    Start([Hospital/Clínica abre cotação<br/>na Bionexo]) --> A[Bionexo recebe cotação]

    A --> B{Amoveri tem preço<br/>cadastrado na Bionexo?}

    B -->|Não existe tabela<br/>de preços integrada| C[Analista Amoveri recebe<br/>alerta de cotação na Bionexo]

    C --> D[Acessa Bionexo manualmente]
    D --> E[Vê itens da cotação]

    E --> F[Consulta custo do produto<br/>Excel/Planilha/NetSuite manual]
    F --> G[Verifica qual laboratório<br/>fornece o produto]
    G --> H[Busca regras especiais<br/>do laboratório]
    H --> I[Verifica OL do laboratório<br/>Desconto pode variar por cliente]

    I --> J[Consulta UF do hospital/clínica]
    J --> K[Calcula ICMS da UF destino<br/>Thiago / Planilha manual]
    K --> L[Consulta PMC CMED<br/>Planilha manual]

    L --> M[Calcula preço manualmente<br/>Excel]
    M --> N{Preço <= PMC?}

    N -->|Não| O[Reajusta manualmente]
    O --> M

    N -->|Sim| P[Digita preço na Bionexo<br/>Item por item manualmente]
    P --> Q[Envia proposta na Bionexo]

    Q --> End([Proposta enviada])

    style B fill:#ff6b6b
    style C fill:#ffd93d
    style F fill:#ffd93d
    style M fill:#ffd93d
    style P fill:#ff6b6b
    style Start fill:#95e1d3
    style End fill:#95e1d3
```

### Pontos de Dor - Processo Atual

| Etapa | Problema | Impacto |
|-------|----------|---------|
| Sem tabela de preços | Não existe precificação estruturada | Impossível automatizar |
| Consulta manual de custos | Informação dispersa | Lento, erro |
| Cálculo manual por UF | ICMS varia por estado | Risco de erro tributário |
| Verificação PMC manual | Planilha CMED | Risco de ultrapassar PMC |
| Digitação na Bionexo | Item por item | Lento, propenso a erros |
| OL por laboratório | Cada lab tem desconto diferente | Complexidade manual |

---

## 2. O QUE PRECISA SER CONSTRUÍDO ANTES DA INTEGRAÇÃO

```mermaid
flowchart TD
    subgraph "FASE 0: Criar Estrutura de Preços no NetSuite"
        A[Definir estrutura de<br/>tabela de preços]
        B[Criar tabela BASE<br/>por ESTADO - 27 UFs]
        C[Criar tabela por<br/>LABORATÓRIO - 4 a 5 principais]
        D[Criar tabela por<br/>CLIENTE específico - se necessário]
        E[Popular com dados<br/>Custo + Margem + ICMS + PMC]

        A --> B
        A --> C
        A --> D
        B --> E
        C --> E
        D --> E
    end

    subgraph "FASE 1: Integração NetSuite → Bionexo"
        F[API expõe preços<br/>do NetSuite]
        G[Bionexo consulta<br/>preços via API]
        H[Preços aparecem<br/>automaticamente nas cotações]
    end

    E --> F
    F --> G
    G --> H

    style A fill:#ff6b6b
    style B fill:#ffd93d
    style C fill:#ffd93d
    style D fill:#ffd93d
    style F fill:#6c5ce7
    style G fill:#0984e3
    style H fill:#00b894
```

---

## 3. ESTRUTURA DE TABELAS DE PREÇO

```mermaid
graph TD
    subgraph "Tabela de Preço MASTER"
        MASTER[Preço Base do Produto<br/>Custo + Margem Padrão]
    end

    subgraph "Variação por ESTADO - UF"
        UF_SP[SP - ICMS 18%<br/>PMC 18%]
        UF_RJ[RJ - ICMS 20%<br/>PMC 20%]
        UF_MG[MG - ICMS 18%<br/>PMC 18%]
        UF_XX[... demais UFs]
    end

    subgraph "Variação por LABORATÓRIO/FORNECEDOR"
        LAB_A[Laboratório A<br/>OL: 5% desconto]
        LAB_B[Laboratório B<br/>OL: 8% desconto]
        LAB_C[Laboratório C<br/>OL: 3% desconto]
        LAB_D[Laboratório D<br/>OL: 6% desconto]
        LAB_E[Laboratório E<br/>OL: 4% desconto]
    end

    subgraph "Preço Final por Combinação"
        PRECO["PREÇO FINAL =<br/>f(Produto, UF, Laboratório, OL)<br/><br/>Validação: <= PMC da UF"]
    end

    MASTER --> UF_SP
    MASTER --> UF_RJ
    MASTER --> UF_MG
    MASTER --> UF_XX

    UF_SP --> PRECO
    UF_RJ --> PRECO
    UF_MG --> PRECO
    UF_XX --> PRECO

    LAB_A --> PRECO
    LAB_B --> PRECO
    LAB_C --> PRECO
    LAB_D --> PRECO
    LAB_E --> PRECO

    style MASTER fill:#74b9ff
    style PRECO fill:#00b894
    style LAB_A fill:#fdcb6e
    style LAB_B fill:#fdcb6e
    style LAB_C fill:#fdcb6e
    style LAB_D fill:#fdcb6e
    style LAB_E fill:#fdcb6e
```

### Lógica de Precificação

```
PREÇO FINAL = Custo Base
              + Margem de Lucro
              + Tributação da UF (ICMS-ST, PIS, COFINS)
              - Desconto OL do Laboratório

VALIDAÇÃO: SE Preço Final > PMC da UF → BLOQUEAR
```

### Dimensões da Tabela de Preço

| Dimensão | Quantidade | Exemplo |
|----------|------------|---------|
| Produtos (SKU/EAN) | [PREENCHER] | Paracetamol 500mg, Amoxicilina 875mg |
| Estados (UF) | Até 27 | SP, RJ, MG, BA, PR, RS, ... |
| Laboratórios/Fornecedores | 4-5 principais | [PREENCHER nomes] |
| OL por Laboratório | Variável | Cada lab pode ter OL diferente |

**Total de combinações possíveis:**
```
N_produtos × N_estados × N_laboratórios

Exemplo: 500 produtos × 27 UFs × 5 labs = 67.500 preços
```

---

## 4. FLUXO AUTOMATIZADO (TO-BE) - Com Tabela de Preços

```mermaid
flowchart TD
    Start([Hospital/Clínica abre cotação<br/>na Bionexo]) --> A[Bionexo recebe cotação<br/>com lista de produtos]

    A --> B[Bionexo consulta API<br/>NetSuite / Middleware]
    B --> C[Identifica UF do hospital]
    C --> D[Identifica laboratório<br/>de cada produto]

    D --> E[Busca preço na tabela<br/>Produto × UF × Laboratório]

    E --> F{Preço encontrado?}

    F -->|Sim| G[Retorna preço calculado<br/>Já com ICMS e desconto OL]
    F -->|Não| H[Marca como sem preço<br/>Notifica analista]

    G --> I{Preço <= PMC?}
    I -->|Sim| J[Preço válido<br/>Envia para Bionexo]
    I -->|Não| K[Ajusta para PMC<br/>ou bloqueia]

    K --> L{Margem ainda<br/>viável?}
    L -->|Sim| J
    L -->|Não| H

    J --> M[Bionexo exibe preço<br/>automaticamente na cotação]
    M --> N[Hospital vê preço<br/>da Amoveri]

    N --> O{Hospital aceita?}
    O -->|Sim| P[Pedido gerado<br/>na Bionexo]
    O -->|Não| End2([Cotação perdida])

    P --> Q[Webhook notifica<br/>NetSuite / Middleware]
    Q --> R[Cria Purchase Order<br/>no NetSuite automaticamente]

    R --> End([Pedido registrado no NetSuite])
    H --> End3([Cotação pendente<br/>análise manual])

    style F fill:#ffd93d
    style I fill:#ffd93d
    style J fill:#00b894
    style H fill:#ff6b6b
    style Start fill:#95e1d3
    style End fill:#95e1d3
    style B fill:#6c5ce7
    style E fill:#6c5ce7
```

### Ganhos Esperados

| Métrica | Antes (Manual) | Depois (Automatizado) |
|---------|----------------|----------------------|
| Tempo de resposta | Horas/Dias | Segundos (automático) |
| Erros de preço | Frequentes | Zero (validação PMC) |
| Cotações perdidas por demora | Muitas | Mínimas |
| Capacidade | Limitada pela equipe | Ilimitada (API) |
| Consistência de preços | Variável | 100% padronizado |

---

## 5. FLUXO DE CÁLCULO DE PREÇO (Motor de Precificação)

```mermaid
flowchart TD
    Start([Produto + UF + Laboratório]) --> A[Busca Custo do Produto<br/>NetSuite: Item Master]

    A --> B[Busca NCM do Produto<br/>Classificação Fiscal]
    B --> C[Identifica UF Destino<br/>Estado do hospital/clínica]

    C --> D[Busca Matriz Tributária<br/>NCM + UF → Thiago]

    D --> E[Calcula ICMS-ST]
    E --> F{Produto monofásico?}

    F -->|Sim| G[PIS/COFINS = 0<br/>Já pago na origem]
    F -->|Não| H[Calcula PIS/COFINS<br/>Alíquotas normais]

    G --> I[Custo Tributado =<br/>Custo + ICMS-ST]
    H --> I2[Custo Tributado =<br/>Custo + ICMS-ST + PIS + COFINS]

    I --> J[Aplica Margem de Lucro<br/>Configurável por categoria]
    I2 --> J

    J --> K[Identifica Laboratório<br/>Fornecedor do produto]
    K --> L{Laboratório tem OL<br/>com desconto?}

    L -->|Sim| M[Aplica Desconto OL<br/>Pode variar por cliente]
    L -->|Não| N[Sem desconto OL]

    M --> O[Preço Calculado]
    N --> O

    O --> P[Busca PMC da UF<br/>Tabela CMED]
    P --> Q{Preço <= PMC?}

    Q -->|Sim| R[PREÇO VÁLIDO<br/>Grava na tabela]
    Q -->|Não| S[Tenta reduzir margem]

    S --> T{Margem >= Mínima?}
    T -->|Sim| U[Ajusta preço = PMC<br/>Flag: margem reduzida]
    T -->|Não| V[BLOQUEADO<br/>Requer análise manual]

    U --> R
    V --> W[Notifica Analista + Gerente]

    R --> End([Preço Final Calculado])
    W --> End

    style Q fill:#ffd93d
    style R fill:#00b894
    style V fill:#ff6b6b
    style P fill:#e17055
```

### Fórmula Resumida

```
PREÇO_FINAL(produto, uf, laboratório) =

    Custo_Base(produto)
    + ICMS_ST(ncm, uf_origem, uf_destino)
    + PIS_COFINS(ncm)                         // 0 se monofásico
    × (1 + Margem_Lucro)
    × (1 - Desconto_OL(laboratório))

    VALIDAÇÃO: MIN(Preço_Calculado, PMC(ean, uf))
```

---

## 6. ESTRUTURA DE TABELA DE PREÇOS NO NETSUITE

### Opções de Implementação no NetSuite

```mermaid
graph TD
    subgraph "Opção A: Price Level por UF (Recomendado)"
        A1[Price Level: SP - ICMS 18%]
        A2[Price Level: RJ - ICMS 20%]
        A3[Price Level: MG - ICMS 18%]
        A4[... 27 UFs]
        A5[Cada Item tem preço<br/>em cada Price Level]
    end

    subgraph "Opção B: Custom Record"
        B1[Custom Record:<br/>Tabela de Preços]
        B2[Campos: EAN, UF,<br/>Lab, Preço, PMC,<br/>Vigência]
        B3[Mais flexível<br/>Mais complexo]
    end

    subgraph "Opção C: Item Pricing por Customer Group"
        C1[Customer Group: Lab A - SP]
        C2[Customer Group: Lab B - SP]
        C3[Customer Group: Lab A - RJ]
        C4[Item Pricing dentro<br/>de cada grupo]
    end

    A1 --> DISCUSS{Discutir com Kamila<br/>na reunião}
    B1 --> DISCUSS
    C1 --> DISCUSS

    style DISCUSS fill:#ffd93d
```

### Opção A: Price Level (Nativo NetSuite)

**Vantagens:**
- Funcionalidade nativa do NetSuite
- Kamila provavelmente já conhece
- Fácil de consultar via SuiteScript/API

**Estrutura:**
```
Price Levels:
├── PRECO_SP (ICMS 18%)
├── PRECO_RJ (ICMS 20%)
├── PRECO_MG (ICMS 18%)
├── PRECO_BA (ICMS 18%)
├── PRECO_PR (ICMS 18%)
├── PRECO_RS (ICMS 17%)
└── ... (27 UFs)

Cada Item:
├── Base Price: R$ 50,00
├── PRECO_SP: R$ 58,50
├── PRECO_RJ: R$ 60,00
├── PRECO_MG: R$ 58,50
└── ...
```

**Limitação:** Não diferencia por laboratório diretamente

### Opção B: Custom Record (Mais Flexível)

**Estrutura:**
```
Custom Record: "Tabela de Preços Bionexo"
├── Item (EAN)
├── UF Destino
├── Laboratório/Fornecedor
├── Preço Calculado
├── PMC da UF
├── Desconto OL aplicado
├── Margem aplicada
├── Data vigência
└── Status (ativo/inativo)
```

**Vantagens:**
- Pode ter preço por Produto × UF × Laboratório
- Flexível para regras complexas
- Pode incluir histórico de preços

### Opção C: Middleware com Database Própria

**Estrutura:**
```
Database Middleware (Python/Azure):
├── Tabela: precos_por_uf
├── Tabela: descontos_ol_por_laboratorio
├── Tabela: pmc_cmed
├── Motor de cálculo
└── API para Bionexo consultar
```

**Vantagens:**
- Total controle
- Performance (cache)
- Independente do NetSuite

**Discussão para reunião com Kamila:** Qual opção se encaixa melhor?

---

## 7. FLUXO DE ATUALIZAÇÃO DE PREÇOS

```mermaid
flowchart TD
    subgraph "Triggers de Atualização"
        T1[1 de abril<br/>CMED atualiza PMC]
        T2[OL muda desconto<br/>Qualquer momento]
        T3[Laboratório muda regra<br/>Analista informa]
        T4[Custo muda no NetSuite<br/>Nova compra]
        T5[Legislação fiscal muda<br/>Thiago atualiza]
    end

    subgraph "Processo de Atualização"
        A[Recalcula preços afetados]
        B[Valida contra PMC]
        C{Algum preço > PMC?}
        D[Atualiza tabela de preços]
        E[Gera relatório de alertas]
    end

    subgraph "Sincronização"
        F[Envia preços atualizados<br/>para Bionexo via API]
        G[Confirma atualização]
        H[Log de auditoria]
    end

    T1 --> A
    T2 --> A
    T3 --> A
    T4 --> A
    T5 --> A

    A --> B
    B --> C

    C -->|Não| D
    C -->|Sim| E
    E --> D

    D --> F
    F --> G
    G --> H

    style T1 fill:#e17055
    style T2 fill:#ffd93d
    style C fill:#ffd93d
    style F fill:#6c5ce7
```

### Frequência de Atualização

| Evento | Frequência | Impacto | Ação |
|--------|------------|---------|------|
| CMED (PMC) | Anual (1º abril) | Todos os preços | Recalcular TUDO |
| OL Desconto | Sem padrão (frequente) | Preços do laboratório | Recalcular lab afetado |
| Regra Laboratório | Sob demanda | Preços do laboratório | Recalcular lab afetado |
| Custo produto | A cada compra | Produto específico | Recalcular produto |
| Legislação fiscal | Quando muda | UF afetada | Recalcular UF |

---

## 8. ARQUITETURA DE INTEGRAÇÃO (Atualizada)

```mermaid
graph TB
    subgraph "NetSuite ERP"
        NS1[Item Master<br/>Custos, EAN, NCM]
        NS2[Tabela de Preços<br/>Price Level ou Custom Record]
        NS3[Purchase Orders<br/>Pedidos recebidos]
    end

    subgraph "Middleware LOCAL - Python no PC"
        MW1[Orquestrador<br/>Python CLI / FastAPI]
        MW2[Motor de Precificação<br/>Calcula preço por UF×Lab]
        MW3[Validador PMC]
        MW4[Windows Task Scheduler<br/>Atualização de preços]
    end

    subgraph "Outros Portais"
        GT[GT Plan<br/>Download CSV/Relatórios]
        AP[Apoio Cotações<br/>Download CSV/Relatórios]
    end

    subgraph "Database LOCAL - SQLite/DuckDB"
        DB1[(CMED / PMC<br/>Atualiza 1º abril)]
        DB2[(OL Descontos<br/>Por laboratório)]
        DB3[(Regras Labs<br/>4-5 principais)]
        DB4[(Matriz Tributária<br/>NCM × UF - Thiago)]
        DB5[(Tabela de Preços<br/>Produto × UF × Lab)]
        DB6[(Cotações Importadas<br/>GT Plan + Apoio)]
    end

    subgraph "Bionexo"
        BX1[Consulta Preços<br/>GET /prices]
        BX2[Envia Pedidos<br/>Webhook novo pedido]
    end

    subgraph "Stakeholders"
        ANA[Analistas<br/>Mantêm regras labs]
        THI[Thiago<br/>Mantém tributação]
    end

    NS1 -->|Custos| MW2
    MW2 -->|Preços calculados| NS2
    MW2 -->|Preços calculados| DB5

    MW1 <-->|API| BX1
    BX2 -->|Novo pedido| MW1
    MW1 -->|Cria PO| NS3

    MW2 --> MW3
    MW3 --> DB1

    MW2 --> DB2
    MW2 --> DB3
    MW2 --> DB4

    ANA -->|Atualiza| DB3
    THI -->|Atualiza| DB4

    GT -->|CSV/Relatórios| MW1
    AP -->|CSV/Relatórios| MW1
    MW1 -->|Importa cotações| DB6

    MW4 -->|Recalcula| MW2

    style MW1 fill:#6c5ce7
    style MW2 fill:#6c5ce7
    style MW3 fill:#e17055
    style BX1 fill:#0984e3
    style DB5 fill:#00b894
    style NS2 fill:#00b894
    style GT fill:#fdcb6e
    style AP fill:#fdcb6e
    style DB6 fill:#74b9ff
```

### Fluxo Resumido

```
1. Motor de Precificação calcula preços
   INPUT: Custo (NetSuite) + ICMS (Thiago) + OL (Labs) + PMC (CMED)
   OUTPUT: Tabela de Preços (Produto × UF × Laboratório)

2. Tabela fica disponível via API

3. Bionexo consulta preços via API
   REQUEST: GET /prices?ean=789123&uf=SP&lab=ABC
   RESPONSE: { preco: 58.50, pmc: 62.00, valido: true }

4. Hospital vê preço automaticamente na cotação

5. Se hospital aceita → Pedido volta para NetSuite via webhook
```

---

## 9. DIAGRAMA DE ESTADOS - Tabela de Preços

```mermaid
stateDiagram-v2
    [*] --> Sem_Tabela: Estado atual

    Sem_Tabela --> Estrutura_Criada: Criar tabela no NetSuite
    Estrutura_Criada --> Populando: Importar custos + calcular

    Populando --> Precos_Calculados: Motor de precificação
    Precos_Calculados --> Validando_PMC: Validar contra CMED

    Validando_PMC --> Precos_Validos: Todos <= PMC
    Validando_PMC --> Ajuste_Necessario: Alguns > PMC

    Ajuste_Necessario --> Precos_Validos: Ajustar margens

    Precos_Validos --> Integrado_Bionexo: Sincronizar via API
    Integrado_Bionexo --> Operacional: Bionexo consulta preços

    Operacional --> Atualizando: Trigger de atualização
    Atualizando --> Precos_Calculados: Recalcular

    note right of Sem_Tabela
        ESTADO ATUAL
        Não temos tabela
        de preços no NetSuite
    end note

    note right of Operacional
        ESTADO DESEJADO
        Bionexo consulta
        preços automaticamente
    end note
```

---

## 10. FLUXO DE EXCEÇÕES

```mermaid
flowchart TD
    Start([Exceção detectada]) --> A{Tipo?}

    A -->|Preço > PMC| B[Produto acima do PMC]
    A -->|Sem custo| C[Produto sem custo no NetSuite]
    A -->|Sem NCM| D[Produto sem classificação fiscal]
    A -->|OL desatualizada| E[Desconto OL expirado ou mudou]
    A -->|Lab sem regra| F[Laboratório novo sem regra cadastrada]

    B --> B1{Pode reduzir margem?}
    B1 -->|Sim| B2[Ajusta para PMC<br/>Flag: margem reduzida]
    B1 -->|Não| B3[BLOQUEIA preço<br/>Notifica gerente]

    C --> C1[Produto sem preço na Bionexo<br/>Notifica compras]

    D --> D1[Não calcula tributo<br/>Notifica Thiago]

    E --> E1[Usa último desconto válido<br/>Notifica analista para atualizar]

    F --> F1[Usa margem padrão<br/>Notifica analista para cadastrar regra]

    B2 --> Log[Registra no log]
    B3 --> Log
    C1 --> Log
    D1 --> Log
    E1 --> Log
    F1 --> Log

    Log --> End([Fim])

    style B3 fill:#ff6b6b
    style C1 fill:#ff6b6b
    style D1 fill:#ffd93d
    style E1 fill:#ffd93d
    style F1 fill:#ffd93d
```

---

## 11. EXEMPLO PRÁTICO - Cálculo de Preço

```mermaid
flowchart LR
    subgraph "INPUT"
        P[Paracetamol 500mg<br/>EAN: 7891234567890<br/>NCM: 30049099]
        UF[Hospital em SP<br/>ICMS: 18%]
        LAB[Laboratório EMS<br/>OL: 5% desconto]
    end

    subgraph "CÁLCULO"
        C1["Custo: R$ 10,00"]
        C2["+ ICMS-ST: R$ 3,50<br/>(MVA 35%)"]
        C3["+ PIS/COFINS: R$ 0,00<br/>(monofásico)"]
        C4["= Custo tributado: R$ 13,50"]
        C5["× Margem 20%: R$ 16,20"]
        C6["- OL EMS 5%: R$ 15,39"]
    end

    subgraph "VALIDAÇÃO"
        V1["PMC SP: R$ 18,50"]
        V2["R$ 15,39 <= R$ 18,50"]
        V3["VÁLIDO"]
    end

    P --> C1
    UF --> C2
    LAB --> C6
    C1 --> C2 --> C3 --> C4 --> C5 --> C6
    C6 --> V1 --> V2 --> V3

    style V3 fill:#00b894
```

---

## 12. VISÃO GERAL DO PROJETO (Fases)

```mermaid
flowchart LR
    subgraph "FASE 0 - Reunião"
        F0A[Kickoff Bionexo]
        F0B[Coletar inputs<br/>Bruna/Kamila/Thiago]
    end

    subgraph "FASE 1 - Tabela Preços"
        F1A[Criar tabela no NetSuite]
        F1B[Montar matriz tributária]
        F1C[Popular e validar PMC]
    end

    subgraph "FASE 2 - Middleware Local"
        F2A[Python + SQLite no PC]
        F2B[Motor de precificação]
        F2C[Task Scheduler]
    end

    subgraph "FASE 3 - Bionexo"
        F3A[Integrar API Bionexo]
        F3B[Piloto 10-20 produtos]
        F3C[Produção]
    end

    subgraph "FASE 4 - Multi-plataforma"
        F4A[Importar GT Plan]
        F4B[Importar Apoio Cotações]
        F4C[Base consolidada]
    end

    subgraph "FASE 5 - Analytics"
        F5A[Dashboards Power BI]
        F5B[Relatórios automáticos]
    end

    F0A --> F0B --> F1A --> F1B --> F1C --> F2A --> F2B --> F2C --> F3A --> F3B --> F3C
    F2C --> F4A --> F4B --> F4C
    F4C --> F5A --> F5B

    style F0A fill:#74b9ff
    style F1A fill:#ff6b6b
    style F1B fill:#ff6b6b
    style F1C fill:#ff6b6b
    style F2A fill:#6c5ce7
    style F3A fill:#0984e3
    style F4A fill:#fdcb6e
    style F5A fill:#00b894
```

### Resumo das Fases

| Fase | O que | Dependência | Responsável |
|------|-------|-------------|-------------|
| **FASE 0** | Reunião kickoff + coletar inputs | Nenhuma | Pedro + Bruna + Kamila |
| **FASE 1** | Criar tabela de preços no NetSuite | Inputs de Thiago (tributação) | Kamila + Pedro + Thiago |
| **FASE 2** | Middleware local (Python + SQLite) | Fase 1 completa | Pedro |
| **FASE 3** | Integração API Bionexo | Fase 2 completa | Pedro + Bionexo |
| **FASE 4** | Importar dados GT Plan + Apoio | Fase 2 completa | Pedro |
| **FASE 5** | Dashboards e analytics | Fase 4 completa | Pedro |

---

## NOTAS IMPORTANTES

### Mudança de Escopo (30/01/2026)

**Escopo ANTERIOR (incorreto):**
- Integração bidirecional de cotações
- NetSuite ↔ Bionexo (enviar e receber cotações)

**Escopo CORRETO (após conversa com Bruna):**
- Bionexo precisa ENXERGAR os PREÇOS do NetSuite
- Direção principal: **NetSuite → Bionexo (preços)**
- Direção secundária: **Bionexo → NetSuite (pedidos aceitos)**

### Pré-requisito Crítico

```
⚠️ NÃO TEMOS TABELA DE PREÇOS NO NETSUITE HOJE!
⚠️ Precisamos CRIAR essa estrutura ANTES de integrar
⚠️ A tabela precisa ter dimensão: Produto × UF × Laboratório
⚠️ Cada combinação tem preço diferente por causa de ICMS e OL
```

### Informações que a Bionexo JÁ POSSUI

- ✅ Média de cotações por dia
- ✅ % de conversão (cotações → pedidos)

### Regras de Negócio

1. **PMC CMED:** Preço NUNCA pode ultrapassar. Atualiza todo 1º abril.
2. **OL Descontos:** Muda frequentemente. Cada laboratório tem seu desconto.
3. **4-5 Laboratórios principais:** Cada um pode ter OL e regras diferentes.
4. **ICMS por UF:** Determina PMC aplicável e impacta preço final.
5. **Thiago:** Responsável pela matriz tributária.

---

**Próximo:** [06-DICIONARIO-DADOS.md](06-DICIONARIO-DADOS.md) (Atualizado)
**Última atualização:** 2026-01-30
