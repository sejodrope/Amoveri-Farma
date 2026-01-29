# Guia Visual - Diagramas da Integração

**Referência rápida dos fluxogramas Mermaid criados**

---

## 📊 Diagramas Disponíveis

### 1. Fluxo Atual (AS-IS) - Processo Manual
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#1-fluxo-atual-as-is---processo-manual)

**O que mostra:**
- Processo manual completo (passo a passo)
- Pontos de dor identificados (em vermelho/amarelo)
- Tempo gasto em cada etapa
- Total: ~2 horas por cotação

**Use para:**
- Explicar para Bionexo como funciona hoje
- Identificar gargalos
- Justificar necessidade de automação

---

### 2. Fluxo Automatizado (TO-BE) - Com Integração API
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#2-fluxo-automatizado-to-be---com-integração-api)

**O que mostra:**
- Processo automatizado ideal
- Onde a API entra
- Validações automáticas (PMC, tributação)
- Tempo esperado: 15 minutos

**Use para:**
- Apresentar visão futura
- Alinhar expectativas com Bionexo
- Definir requisitos técnicos

---

### 3. Arquitetura de Integração
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#3-arquitetura-de-integração)

**O que mostra:**
- Componentes técnicos (NetSuite, Middleware, Bionexo)
- Bases de dados auxiliares (CMED, OL, Laboratórios, Tributação)
- Fluxo de dados numerado (1→12)
- Tecnologias propostas

**Use para:**
- Discussão técnica com especialistas Bionexo
- Decisão: Middleware vs Integração Direta
- Entender dependências

---

### 4. Fluxo de Precificação (Detalhado)
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#4-fluxo-de-precificação-detalhado)

**O que mostra:**
- Motor de precificação completo
- Validação PMC CMED (crítico!)
- Aplicação de regras de laboratórios
- Aplicação de descontos OL
- Tratamento de erros

**Use para:**
- Explicar complexidade de precificação farmacêutica
- Validar lógica de cálculo
- Identificar dados necessários

---

### 5. Fluxo de Atualizações de Tabelas
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#5-fluxo-de-atualizações-de-tabelas)

**O que mostra:**
- Cronograma de atualizações (Gantt)
- CMED: 1º abril (anual)
- OL: Frequente, sem padrão
- Regras Labs: Sob demanda
- Matriz Tributária: Trimestral

**Use para:**
- Entender dinâmica de mudanças
- Planejar manutenção do sistema

---

### 6. Diagrama de Estados - Ciclo de Vida da Cotação
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#6-diagrama-de-estados---ciclo-de-vida-da-cotação)

**O que mostra:**
- Estados possíveis de uma cotação
- Transições entre estados
- Pontos de validação crítica

**Use para:**
- Alinhar status entre NetSuite e Bionexo
- Definir webhooks necessários

---

### 7. Fluxo de Exceções e Erros
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#7-fluxo-de-exceções-e-erros)

**O que mostra:**
- Tipos de erro (PMC, API, Validação, Tributário)
- Estratégias de retry
- Notificações e responsáveis

**Use para:**
- Planejar tratamento de erros
- Definir SLA de resposta

---

### 8. Integrações e Dependências
**Arquivo:** [05-DIAGRAMAS-FLUXOS.md](05-DIAGRAMAS-FLUXOS.md#8-integrações-e-dependências)

**O que mostra:**
- Todos os sistemas envolvidos
- Stakeholders (Analistas, Thiago, Gerente)
- Direção do fluxo de dados

**Use para:**
- Visão holística do projeto
- Identificar pontos de contato

---

## 📋 Dicionário de Dados

### Arquivo: [06-DICIONARIO-DADOS.md](06-DICIONARIO-DADOS.md)

**O que contém:**
- Mapeamento de IDs (RFQ, PO, Vendor, Item)
- Chaves de relacionamento
- Campos obrigatórios vs opcionais
- Transformações necessárias (datas, CNPJ, valores)
- Tabelas auxiliares do middleware

**Seções importantes:**

#### 1. Identificadores Únicos
- Como relacionar NetSuite ↔ Bionexo
- Campos customizados necessários no NetSuite

#### 2-4. Mapeamento de Campos
- Cotação (RFQ): Cabeçalho + Linhas
- Proposta: Cabeçalho + Linhas
- Pedido (PO): Cabeçalho + Linhas

#### 5. Campos Customizados NetSuite
- Lista completa de custom fields a criar
- Script IDs sugeridos

#### 6. Formatos e Transformações
- Código para converter datas, CNPJ, valores
- Validação de EAN

#### 7. Tabelas Auxiliares
- `tbl_cmed_pmc` - PMC da CMED
- `tbl_operadora_logistica_descontos` - Descontos OL
- `tbl_regras_laboratorios` - Regras especiais
- `tbl_matriz_tributaria` - ICMS-ST, PIS, COFINS
- `tbl_integration_log` - Logs

#### 8. Perguntas Críticas para Bionexo
- ⚠️ Checklist de perguntas sobre IDs, formatos, campos obrigatórios

---

## 🎯 Como Usar na Reunião

### Início (10 min)
Mostrar: **Fluxo Atual (AS-IS)**
- Explicar dores do processo manual
- Tempo gasto: 2h por cotação

### Alinhamento (15 min)
Mostrar: **Fluxo Automatizado (TO-BE)**
- Visão de como deveria funcionar
- Ganhos esperados: 87.5% redução de tempo

### Discussão Técnica (30 min)
Mostrar: **Arquitetura de Integração**
- Decidir: Middleware ou Direto?
- Identificar endpoints necessários

Mostrar: **Fluxo de Precificação**
- Explicar complexidade farmacêutica
- PMC CMED é crítico!

### Mapeamento de Dados (20 min)
Usar: **[Dicionário de Dados](06-DICIONARIO-DADOS.md)**
- Seção 8: Fazer perguntas críticas
- Preencher campos "A DEFINIR"
- Confirmar formatos

### Cronograma (10 min)
Mostrar: **Fluxo de Atualizações**
- Explicar dinâmica de mudanças (CMED, OL, Labs)
- Sistema precisa ser flexível

---

## 📝 Anotações Durante Reunião

**Preencher conforme respostas da Bionexo:**

### IDs e Formatos
- [ ] `rfq_id` formato: _______________
- [ ] `po_id` formato: _______________
- [ ] CNPJ formato: [ ] Com formatação [ ] Sem formatação
- [ ] Data formato: [ ] ISO 8601 [ ] DD/MM/YYYY [ ] Timestamp
- [ ] Moeda: [ ] Sempre BRL [ ] Informar no payload

### Endpoints
- [ ] Criar RFQ: `POST _______________`
- [ ] Buscar propostas: `GET _______________`
- [ ] Criar PO: `POST _______________`

### Webhooks
- [ ] Disponível: [ ] Sim [ ] Não
- [ ] Eventos: _______________
- [ ] URL callback: _______________

### Limitações
- [ ] Rate limit: _______ req/min
- [ ] Max itens por RFQ: _______
- [ ] Timeout: _______ segundos

---

## 🔄 Próximos Passos Após Preencher

1. **Completar Dicionário de Dados**
   - Substituir todos "A DEFINIR" com valores reais
   - Validar mapeamentos

2. **Criar Especificação Técnica**
   - Baseado em diagramas + dicionário preenchido
   - Detalhamento de APIs

3. **Implementar PoC**
   - Autenticação
   - Primeira chamada de API
   - Validar fluxo básico

---

**Documento complementar:** [RESUMO-EXECUTIVO.md](RESUMO-EXECUTIVO.md) - Apresentação de 5 minutos
