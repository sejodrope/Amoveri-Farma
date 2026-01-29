# Diagramas e Fluxogramas - Integração Bionexo x NetSuite

**Data:** 2026-01-29
**Responsável:** Pedro (Inteligência Comercial)

---

## 1. FLUXO ATUAL (AS-IS) - Processo Manual

```mermaid
flowchart TD
    Start([Cliente solicita cotação]) --> A[Analista recebe solicitação<br/>Email/WhatsApp/Telefone]
    A --> B[Analista registra no NetSuite<br/>Purchase Order ou RFQ]

    B --> C{Precisa consultar<br/>laboratórios?}
    C -->|Sim| D[Verifica regras especiais<br/>do laboratório]
    C -->|Não| E[Consulta custos no NetSuite]

    D --> E
    E --> F[Consulta tabela CMED<br/>Verifica PMC máximo]
    F --> G[Aplica regras de tributação<br/>Thiago - ICMS-ST, PIS/COFINS]
    G --> H[Aplica descontos OL<br/>Operadora Logística]

    H --> I[Calcula preço de venda<br/>Manual no Excel]
    I --> J{Preço <= PMC?}

    J -->|Não| K[ERRO: Reajusta preço<br/>Não pode passar PMC]
    K --> I

    J -->|Sim| L[Exporta Excel do NetSuite]
    L --> M[Acessa Bionexo manualmente]
    M --> N[Faz upload da cotação<br/>Excel → Bionexo]

    N --> O[Aguarda propostas<br/>Fornecedores respondem]
    O --> P[Baixa propostas em Excel<br/>Bionexo → Download]

    P --> Q[Importa manualmente no NetSuite<br/>Excel → NetSuite]
    Q --> R{Aprova cotação?}

    R -->|Não| S[Rejeita e arquiva]
    R -->|Sim| T[Gera Pedido no NetSuite]

    T --> U[Envia PO manualmente<br/>Email ou Portal fornecedor]
    U --> End([Pedido enviado])

    S --> End

    style K fill:#ff6b6b
    style J fill:#ffd93d
    style R fill:#ffd93d
    style Start fill:#95e1d3
    style End fill:#95e1d3
```

### Pontos de Dor Identificados

| Etapa | Tempo | Problema |
|-------|-------|----------|
| Registro manual (A→B) | 10 min | Risco de erro de digitação |
| Consulta regras (D→H) | 30 min | Informação dispersa, pode estar desatualizada |
| Cálculo manual (I) | 20 min | Erros de fórmula, validação PMC manual |
| Upload/Download (L→Q) | 40 min | Trabalho repetitivo, propenso a erros |
| Envio PO (U) | 10 min | Manual por fornecedor |
| **TOTAL** | **~2h** | **Alto risco de erro + não escalável** |

---

## 2. FLUXO AUTOMATIZADO (TO-BE) - Com Integração API

```mermaid
flowchart TD
    Start([Cliente solicita cotação]) --> A[Analista cria RFQ no NetSuite]

    A --> B{Trigger automático<br/>Webhook ou botão}
    B --> C[API Middleware<br/>Valida dados]

    C --> D[Busca custos no NetSuite<br/>Saved Search]
    D --> E[Busca tabela CMED<br/>Database]
    E --> F[Aplica regras tributárias<br/>Thiago - Matriz fiscal]
    F --> G[Aplica descontos OL<br/>Tabela atualizada]

    G --> H[Motor de Precificação<br/>Calcula preço automático]
    H --> I{Validação PMC<br/>Preço <= PMC?}

    I -->|Não| J[ALERTA: Requer ajuste manual<br/>Notifica analista]
    J --> K[Analista ajusta no NetSuite]
    K --> H

    I -->|Sim| L{Regras especiais<br/>laboratório?}
    L -->|Sim| M[Aplica regras do laboratório<br/>Database de regras]
    L -->|Não| N[Envia para Bionexo API<br/>POST /rfq]
    M --> N

    N --> O[Bionexo recebe cotação<br/>Retorna ID]
    O --> P[Atualiza NetSuite<br/>Campo custbody_bionexo_id]

    P --> Q[Webhook Bionexo<br/>Nova proposta recebida]
    Q --> R[API busca propostas<br/>GET /rfq/:id/proposals]

    R --> S[Insere propostas no NetSuite<br/>Automaticamente]
    S --> T{Analista aprova?}

    T -->|Não| U[Status: Rejeitado]
    T -->|Sim| V[Gera PO no NetSuite]

    V --> W[Envia PO para Bionexo API<br/>POST /purchase-orders]
    W --> X[Bionexo notifica fornecedor<br/>Automaticamente]

    X --> End([Pedido enviado])
    U --> End

    style J fill:#ffd93d
    style I fill:#6bcf7f
    style L fill:#ffd93d
    style Start fill:#95e1d3
    style End fill:#95e1d3
    style C fill:#6c5ce7
    style H fill:#6c5ce7
    style N fill:#0984e3
    style R fill:#0984e3
```

### Ganhos Esperados

| Métrica | Antes | Depois | Melhoria |
|---------|-------|--------|----------|
| Tempo por cotação | 2h | 15 min | **87.5% ⬇️** |
| Taxa de erro | ~5% | <0.1% | **98% ⬇️** |
| Validação PMC | Manual | Automática | **100% cobertura** |
| Capacidade | ~10 cotações/dia | ~40 cotações/dia | **4x ⬆️** |
| Rastreabilidade | Baixa | Alta (logs) | **100% auditável** |

---

## 3. ARQUITETURA DE INTEGRAÇÃO

```mermaid
graph TB
    subgraph "NetSuite ERP"
        NS1[Purchase Order / RFQ]
        NS2[Saved Searches<br/>Custos, Estoque, Fiscal]
        NS3[Custom Fields<br/>custbody_bionexo_id]
        NS4[SuiteScript<br/>RESTlet ou User Event]
    end

    subgraph "Middleware - Azure/Python"
        MW1[API Gateway<br/>FastAPI]
        MW2[Motor de Precificação<br/>Regras tributárias]
        MW3[Validador PMC<br/>CMED]
        MW4[Database Config<br/>Regras OL, Labs]
        MW5[Fila de Tarefas<br/>Celery/Redis]
        MW6[Logs & Monitoring<br/>Application Insights]
    end

    subgraph "Bionexo API"
        BX1[POST /rfq<br/>Criar cotação]
        BX2[GET /rfq/:id/proposals<br/>Buscar propostas]
        BX3[POST /purchase-orders<br/>Criar pedido]
        BX4[Webhooks<br/>Eventos em tempo real]
    end

    subgraph "Bases de Dados Auxiliares"
        DB1[(Tabela CMED<br/>PMC atualizado)]
        DB2[(OL Descontos<br/>Atualização frequente)]
        DB3[(Regras Laboratórios<br/>Mantido por analistas)]
        DB4[(Matriz Tributária<br/>Thiago)]
    end

    NS4 -->|1. Trigger| MW1
    MW1 -->|2. Busca dados| NS2
    MW1 -->|3. Consulta| DB1
    MW1 -->|4. Consulta| DB2
    MW1 -->|5. Consulta| DB3
    MW1 -->|6. Consulta| DB4

    MW1 --> MW2
    MW2 --> MW3
    MW3 -->|7. Envia RFQ| BX1

    BX4 -->|8. Webhook: Nova proposta| MW5
    MW5 -->|9. Busca propostas| BX2
    MW5 -->|10. Insere no NetSuite| NS3

    NS1 -->|11. Aprovação| MW1
    MW1 -->|12. Cria PO| BX3

    MW1 --> MW6

    style MW1 fill:#6c5ce7
    style MW2 fill:#6c5ce7
    style MW3 fill:#e17055
    style BX1 fill:#0984e3
    style BX2 fill:#0984e3
    style BX3 fill:#0984e3
    style BX4 fill:#00b894
```

### Decisões de Arquitetura

**Middleware (Recomendado):**
- **Onde:** Azure App Service ou Azure Functions
- **Linguagem:** Python (FastAPI)
- **Vantagens:**
  - Desacopla NetSuite da Bionexo
  - Facilita manutenção de regras complexas (CMED, OL, tributação)
  - Permite retry e fila de tarefas
  - Logs centralizados

**Alternativa - Direto no NetSuite:**
- **SuiteScript RESTlet** chama Bionexo diretamente
- **Vantagens:** Menos infraestrutura
- **Desvantagens:** Regras de precificação complexas ficam no SuiteScript (difícil manter)

---

## 4. FLUXO DE PRECIFICAÇÃO (Detalhado)

```mermaid
flowchart TD
    Start([Item da cotação]) --> A[Busca custo médio<br/>NetSuite: Saved Search]

    A --> B[Busca NCM do produto<br/>NetSuite: Item Master]
    B --> C[Consulta UF destino<br/>NetSuite: Customer]

    C --> D[Busca Matriz Tributária<br/>Database Thiago<br/>NCM + UF]
    D --> E[Calcula ICMS-ST<br/>MVA ajustado]
    E --> F[Calcula PIS/COFINS<br/>Monofásico ou normal]

    F --> G{Produto tem<br/>regra especial<br/>laboratório?}

    G -->|Sim| H[Busca regra do laboratório<br/>Database analistas]
    G -->|Não| I[Aplica margem padrão<br/>Configurável]

    H --> J[Aplica regra especial<br/>Desconto ou markup]
    J --> K[Consulta descontos OL<br/>Database OL atualizada]
    I --> K

    K --> L[Calcula preço base<br/>Custo + Tributos + Margem]
    L --> M[Aplica desconto OL]

    M --> N[Consulta PMC<br/>Tabela CMED<br/>EAN + Data vigência]

    N --> O{Preço calculado<br/><= PMC?}

    O -->|Sim| P[Preço VÁLIDO<br/>Retorna valor]
    O -->|Não| Q[ALERTA PMC<br/>Reduz margem automaticamente]

    Q --> R{Margem mínima<br/>ainda viável?}
    R -->|Sim| S[Ajusta para PMC<br/>Marca como "margem reduzida"]
    R -->|Não| T[ERRO CRÍTICO<br/>Requer intervenção manual]

    S --> P
    T --> U[Notifica analista<br/>Email + Dashboard]

    P --> End([Preço final calculado])
    U --> End

    style O fill:#ffd93d
    style T fill:#ff6b6b
    style P fill:#00b894
    style N fill:#fdcb6e
    style D fill:#74b9ff
```

### Fórmulas de Precificação

**1. Cálculo ICMS-ST:**
```
Base_ST = Custo × (1 + MVA_Ajustada)
ICMS_Proprio = Custo × Aliq_Origem
ICMS_ST = (Base_ST × Aliq_Destino) - ICMS_Proprio
```

**2. Cálculo PIS/COFINS:**
```
Se monofásico:
    PIS_COFINS = 0 (já pago na origem)
Senão:
    PIS = Preço × 0.0165
    COFINS = Preço × 0.076
```

**3. Preço Final:**
```
Custo_Total = Custo + ICMS_ST + PIS + COFINS
Preço_Base = Custo_Total × (1 + Margem)
Preço_Com_Desconto_OL = Preço_Base × (1 - Desconto_OL)

SE Preço_Com_Desconto_OL > PMC:
    Preço_Final = PMC (ajusta na margem)
SENÃO:
    Preço_Final = Preço_Com_Desconto_OL
```

---

## 5. FLUXO DE ATUALIZAÇÕES DE TABELAS

```mermaid
gantt
    title Cronograma de Atualizações de Dados
    dateFormat YYYY-MM-DD

    section CMED (Anual)
    Atualização CMED          :crit, 2026-04-01, 1d
    Validação preços          :     2026-04-02, 3d

    section OL Descontos (Variável)
    Atualização OL - Jan      :active, 2026-01-15, 1d
    Atualização OL - Fev      :       2026-02-20, 1d
    Atualização OL - Mar      :       2026-03-10, 1d

    section Regras Laboratórios (Sob demanda)
    Lab A - Nova regra        :       2026-01-25, 1d
    Lab B - Ajuste regra      :       2026-02-15, 1d
    Lab C - Nova regra        :       2026-03-05, 1d

    section Matriz Tributária (Trimestral)
    Revisão Thiago - Q1       :       2026-03-25, 2d
```

### Processo de Atualização

```mermaid
flowchart LR
    subgraph "1º Abril - CMED"
        A1[Anvisa publica nova CMED]
        A2[Download arquivo oficial]
        A3[Importa para Database]
        A4[Valida PMC produtos]
        A5[Notifica discrepâncias]
    end

    subgraph "OL Descontos - Qualquer momento"
        B1[OL envia nova tabela]
        B2[Analista valida]
        B3[Upload no sistema]
        B4[Integração aplica automaticamente]
    end

    subgraph "Regras Laboratórios - Sob demanda"
        C1[Laboratório comunica mudança]
        C2[Analista comercial documenta]
        C3[Cadastra regra no sistema]
        C4[Integração aplica em novas cotações]
    end

    subgraph "Matriz Tributária - Thiago"
        D1[Mudança legislação fiscal]
        D2[Thiago atualiza matriz]
        D3[Importa para sistema]
        D4[Motor precificação usa nova regra]
    end

    A1 --> A2 --> A3 --> A4 --> A5
    B1 --> B2 --> B3 --> B4
    C1 --> C2 --> C3 --> C4
    D1 --> D2 --> D3 --> D4

    style A3 fill:#ff6b6b
    style B3 fill:#ffd93d
    style C3 fill:#6bcf7f
    style D3 fill:#74b9ff
```

---

## 6. DIAGRAMA DE ESTADOS - Ciclo de Vida da Cotação

```mermaid
stateDiagram-v2
    [*] --> Criada: Analista cria RFQ no NetSuite

    Criada --> Precificando: Trigger integração
    Precificando --> Validando_PMC: Motor calcula preços

    Validando_PMC --> Erro_PMC: Preço > PMC
    Validando_PMC --> Aguardando_Envio: Preço OK

    Erro_PMC --> Ajuste_Manual: Notifica analista
    Ajuste_Manual --> Precificando: Analista ajusta

    Aguardando_Envio --> Enviada_Bionexo: API POST /rfq
    Enviada_Bionexo --> Aguardando_Propostas: Fornecedores recebem

    Aguardando_Propostas --> Propostas_Recebidas: Webhook/Polling
    Propostas_Recebidas --> Em_Analise: Importa para NetSuite

    Em_Analise --> Rejeitada: Analista rejeita
    Em_Analise --> Aprovada: Analista aprova

    Aprovada --> Gerando_PO: Cria Purchase Order
    Gerando_PO --> PO_Enviada: API POST /purchase-orders

    PO_Enviada --> Confirmada: Fornecedor confirma
    PO_Enviada --> Cancelada: Fornecedor cancela

    Confirmada --> [*]
    Rejeitada --> [*]
    Cancelada --> [*]

    note right of Validando_PMC
        Validação crítica
        PMC CMED obrigatório
    end note

    note right of Aguardando_Propostas
        Prazo típico: 24-48h
    end note
```

---

## 7. FLUXO DE EXCEÇÕES E ERROS

```mermaid
flowchart TD
    Start([Erro detectado]) --> A{Tipo de erro?}

    A -->|Erro PMC| B[Preço > PMC CMED]
    A -->|Erro API| C[Falha comunicação Bionexo]
    A -->|Erro Validação| D[Dados incompletos NetSuite]
    A -->|Erro Tributário| E[Falta regra fiscal]

    B --> B1[Tenta reduzir margem automaticamente]
    B1 --> B2{Margem mínima<br/>viável?}
    B2 -->|Sim| B3[Ajusta para PMC<br/>Marca como exceção]
    B2 -->|Não| B4[Bloqueia cotação<br/>Notifica analista + gerente]

    C --> C1[Retry exponential backoff<br/>3 tentativas]
    C1 --> C2{Sucesso?}
    C2 -->|Sim| C3[Continua fluxo]
    C2 -->|Não| C4[Move para fila de erro<br/>Notifica TI + Pedro]

    D --> D1[Valida campos obrigatórios]
    D1 --> D2[Lista campos faltantes]
    D2 --> D3[Notifica analista<br/>Email com campos necessários]

    E --> E1[Verifica se NCM existe<br/>na matriz tributária]
    E1 --> E2{NCM cadastrado?}
    E2 -->|Não| E3[Notifica Thiago<br/>Cadastrar NCM urgente]
    E2 -->|Sim| E4[Erro na query<br/>Notifica TI]

    B3 --> Log[Registra no log]
    B4 --> Log
    C3 --> Log
    C4 --> Log
    D3 --> Log
    E3 --> Log
    E4 --> Log

    Log --> End([Fim do tratamento])

    style B4 fill:#ff6b6b
    style C4 fill:#ff6b6b
    style E3 fill:#ffd93d
    style Log fill:#a29bfe
```

---

## 8. INTEGRAÇÕES E DEPENDÊNCIAS

```mermaid
graph LR
    subgraph "NetSuite"
        NS[NetSuite ERP]
    end

    subgraph "Sistemas Externos"
        BX[Bionexo API]
        CMED[Base CMED<br/>Anvisa]
    end

    subgraph "Bases Internas"
        DB_OL[(Descontos OL)]
        DB_LAB[(Regras Labs)]
        DB_FISC[(Matriz Fiscal<br/>Thiago)]
    end

    subgraph "Stakeholders"
        ANA[Analistas Comerciais]
        THI[Thiago Tributário]
        GER[Gerente Comercial]
    end

    NS <-->|SuiteScript/API| MW[Middleware<br/>Python/Azure]
    MW <-->|REST API| BX
    MW -->|Consulta PMC| CMED

    MW -->|Aplica descontos| DB_OL
    MW -->|Aplica regras| DB_LAB
    MW -->|Calcula impostos| DB_FISC

    ANA -->|Mantém| DB_LAB
    THI -->|Mantém| DB_FISC

    MW -->|Notifica exceções| ANA
    MW -->|Alerta PMC crítico| GER
    MW -->|Alerta erro fiscal| THI

    style MW fill:#6c5ce7
    style CMED fill:#e17055
    style BX fill:#0984e3
```

---

## NOTAS IMPORTANTES

### Regras de Negócio Críticas

1. **PMC CMED (Preço Máximo ao Consumidor)**
   - Atualizado todo **1º de abril**
   - Limite regulatório - **não pode ser ultrapassado**
   - Denúncia à CMED se violado
   - Sistema deve **bloquear automaticamente** preços acima do PMC

2. **Operadoras Logísticas (OL)**
   - Descontos **mudam frequentemente** (sem padrão)
   - Analistas recebem tabelas atualizadas
   - Sistema precisa permitir **atualização fácil** sem deploy

3. **Regras Especiais de Laboratórios**
   - Cada laboratório pode ter regras únicas
   - Mantido pelas **analistas comerciais**
   - Exemplos: desconto progressivo, margem mínima, prazo diferenciado
   - Sistema precisa ser **flexível** para cadastrar novas regras

4. **Matriz Tributária**
   - Mantida por **Thiago**
   - ICMS-ST varia por NCM + UF
   - Mudanças na legislação fiscal devem ser refletidas rapidamente

### Informações que a Bionexo JÁ POSSUI

- ✅ Média de cotações por dia
- ✅ % de conversão (cotações → pedidos)
- ❓ Perguntar se há relatórios/dashboards disponíveis via API

---

**Próximo:** [Dicionário de Dados](06-DICIONARIO-DADOS.md)
