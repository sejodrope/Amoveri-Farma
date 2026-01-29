# Ata de Reunião - Integração Bionexo x NetSuite

**Data:** [PREENCHER] - Segunda-feira, ___/___/2026, 14h
**Local:** [PREENCHER] - [ ] Presencial [ ] Teams [ ] Zoom [ ] Google Meet
**Duração:** [PREENCHER] - Início: ___:___ | Término: ___:___
**Redator:** Pedro (Inteligência Comercial - Amoveri Pontual)

---

## Participantes

### Presentes

**Bionexo:**
- [ ] Gisele - Gestora de Contas - gisele@bionexo.com
- [ ] _______________ - Especialista Integração - _______________
- [ ] _______________ - Especialista Integração - _______________
- [ ] _______________ (outros) - _______________ - _______________

**Amoveri Pontual:**
- [ ] Bruna - Comercial - bruna@amoverifarma.com.br
- [ ] Kamila - TI NetSuite - kamila@amoverifarma.com.br
- [ ] Pedro - Inteligência Comercial - pedro@amoverifarma.com.br
- [ ] _______________ (outros) - _______________ - _______________

### Ausentes Justificados
- _______

---

## Pauta

1. [ ] Alinhamento de objetivos e expectativas
2. [ ] Mapeamento de processos de negócio
3. [ ] Arquitetura técnica e descoberta da API
4. [ ] Segurança e compliance
5. [ ] Cronograma e próximos passos

---

## 1. ALINHAMENTO DE OBJETIVOS

### 1.1 Contexto Amoveri Pontual

**Objetivo do projeto:**
[PREENCHER]
```
Exemplo:
Automatizar fluxo completo de cotações entre NetSuite e Bionexo,
eliminando entrada manual de dados e reduzindo tempo de resposta
de cotações de 2h para 15 minutos.
```

**Escopo da integração:**
- [ ] Cotações (RFQ) - NetSuite → Bionexo
- [ ] Propostas - Bionexo → NetSuite
- [ ] Pedidos de Compra (PO) - NetSuite ↔ Bionexo
- [ ] Sincronização de fornecedores
- [ ] Sincronização de produtos
- [ ] Outros: _______________

**Volumes estimados:**
- Cotações/mês: _______________
- Pedidos/mês: _______________
- Fornecedores ativos: _______________
- Produtos no catálogo: _______________

### 1.2 Expectativas Bionexo

**Posicionamento da Bionexo:**
[PREENCHER - anotar pontos levantados pela Gisele]

**Cases de sucesso mencionados:**
[PREENCHER]

---

## 2. MAPEAMENTO DE PROCESSOS

### 2.1 Fluxo de Cotações (As-Is)

**Processo atual (manual):**
[PREENCHER - descrever com Bruna]
```
Exemplo:
1. Comprador cria RFQ no NetSuite
2. Exporta planilha Excel
3. Faz upload manual na Bionexo
4. Aguarda propostas dos fornecedores
5. Baixa propostas em Excel
6. Importa manualmente no NetSuite
7. Analisa e aprova
```

**Pain points identificados:**
- [PREENCHER]
- [PREENCHER]
- [PREENCHER]

**Tempo médio por cotação (atual):**
- _______ horas/minutos

### 2.2 Fluxo de Cotações (To-Be)

**Processo automatizado (desejado):**
[PREENCHER]
```
Exemplo:
1. Comprador cria RFQ no NetSuite
2. [AUTOMÁTICO] NetSuite envia para Bionexo via API
3. Fornecedores enviam propostas na Bionexo
4. [AUTOMÁTICO] Propostas retornam para NetSuite
5. Comprador analisa e aprova no NetSuite
6. [AUTOMÁTICO] Pedido é criado e enviado à Bionexo
```

**Tempo esperado por cotação (automatizado):**
- _______ minutos

**Meta de redução de tempo:**
- _______ % de redução

### 2.3 Regras de Negócio Identificadas

**Aprovações:**
- [PREENCHER]
```
Exemplo:
- Cotações acima de R$ 10.000 precisam aprovação de gerente
- Fornecedores novos precisam homologação antes de pedido
```

**Exceções:**
- [PREENCHER]

**Priorização:**
- [PREENCHER]
```
Exemplo:
- Fase 1: Cotações simples (sem urgência)
- Fase 2: Cotações urgentes
- Fase 3: Cotações com importação
```

---

## 3. ARQUITETURA TÉCNICA

### 3.1 Decisões de Arquitetura

**Modelo escolhido:**
- [ ] Integração direta (NetSuite ↔ Bionexo)
- [ ] Middleware (NetSuite ↔ Middleware ↔ Bionexo)
- [ ] Outro: _______________

**Justificativa:**
[PREENCHER]

**Diagrama:**
[ANEXAR ou DESCREVER]
```
Exemplo:
NetSuite (SuiteScript) → RESTlet → Python Middleware → Bionexo API
                                         ↓
                                   Logs + Monitoring
```

### 3.2 API Bionexo - Descobertas

#### Documentação
- **URL:** _______________
- **Formato:** [ ] Swagger [ ] Postman [ ] PDF [ ] Outro: ___
- **Acesso obtido?** [ ] Sim [ ] Aguardando [ ] Não disponível

#### Tipo de API
- **Arquitetura:** [ ] REST [ ] GraphQL [ ] SOAP [ ] Outro: ___
- **Versão atual:** _______________
- **Base URL:** _______________

#### Autenticação
- **Método:** [ ] OAuth2 [ ] API Key [ ] JWT [ ] Outro: ___
- **Credenciais fornecidas?** [ ] Sim [ ] Aguardando [ ] Solicitar separadamente
- **Validade:** _______________

#### Rate Limits
- **Requisições/minuto:** _______________
- **Requisições/hora:** _______________
- **Requisições/dia:** _______________
- **Comportamento ao atingir limite:** _______________

#### Webhooks
- **Disponível?** [ ] Sim [ ] Não [ ] Roadmap futuro
- **Eventos disponíveis:**
  - [ ] Nova cotação
  - [ ] Proposta recebida
  - [ ] Status de pedido atualizado
  - [ ] Outros: _______________
- **Se não disponível, polling recomendado a cada:** _______ minutos

#### Endpoints Principais

**Criar Cotação:**
- Método: _____ | URL: `_______________`
- Campos obrigatórios: _______________

**Listar Propostas:**
- Método: _____ | URL: `_______________`
- Filtros disponíveis: _______________

**Criar Pedido:**
- Método: _____ | URL: `_______________`
- Campos obrigatórios: _______________

**Consultar Status:**
- Método: _____ | URL: `_______________`

### 3.3 NetSuite - Decisões Técnicas

**Kamila - Capacidades do NetSuite:**

**Método de integração escolhido:**
- [ ] SuiteScript RESTlet (código interno)
- [ ] SuiteTalk (Web Services)
- [ ] Middleware externo (Python/Node)
- [ ] Outro: _______________

**Justificativa:**
[PREENCHER]

**Saved Searches necessárias:**
- [PREENCHER]
```
Exemplo:
- Saved Search: Produtos para cotação (ID: 123)
- Saved Search: Fornecedores homologados (ID: 456)
```

**Custom Fields mapeados:**
- [PREENCHER]
```
Exemplo:
- custbody_bionexo_rfq_id (armazena ID da cotação na Bionexo)
- custbody_proposta_link (link para proposta na Bionexo)
```

**Workflows impactados:**
- [PREENCHER]

### 3.4 Mapeamento de Dados

**Formatos padronizados:**
- Data/Hora: [ ] ISO 8601 [ ] Unix timestamp [ ] Outro: ___
- Timezone: [ ] UTC [ ] America/Sao_Paulo [ ] Outro: ___
- Moeda: [ ] BRL [ ] USD [ ] Outro: ___
- Decimal: Separador = [ ] `.` [ ] `,` | Casas decimais = ___

**Mapeamento de campos críticos:**
| Campo NetSuite | Campo Bionexo | Transformação Necessária |
|----------------|---------------|--------------------------|
| [PREENCHER] | [PREENCHER] | [PREENCHER] |
| Exemplo: `entity` (Vendor) | `fornecedor_id` | CNPJ → ID Bionexo |
| | | |

**Unidades de medida:**
- Como será feita conversão? _______________
- Tabela de DE→PARA necessária? [ ] Sim [ ] Não

---

## 4. AMBIENTE E TESTES

### 4.1 Sandbox/Homologação

**Bionexo:**
- **URL Sandbox:** _______________
- **Credenciais fornecidas:** [ ] Sim [ ] Aguardando
- **Dados de teste disponíveis:** [ ] Sim [ ] Não
  - Fornecedores fictícios: _______________
  - Produtos fictícios: _______________

**NetSuite:**
- **Ambiente Sandbox:** [ ] Disponível [ ] Não temos [ ] Usar Production com flag de teste
- **URL:** _______________

### 4.2 Estratégia de Testes

**Fases de teste:**
1. [ ] **Teste Unitário** - Endpoints isolados
2. [ ] **Teste de Integração** - Fluxo completo (RFQ → Proposta → PO)
3. [ ] **Teste de Carga** - Simular _______ cotações simultâneas
4. [ ] **UAT (User Acceptance)** - _______ usuários piloto

**Casos de teste prioritários:**
1. [PREENCHER]
2. [PREENCHER]
3. [PREENCHER]

**Critérios de aceite para go-live:**
- [ ] _______ cotações processadas com sucesso no piloto
- [ ] Tempo de resposta < _______ segundos
- [ ] Taxa de erro < _______ %
- [ ] Aprovação dos usuários piloto
- [ ] Outro: _______________

---

## 5. SEGURANÇA E COMPLIANCE

### 5.1 Segurança

**Autenticação e criptografia:**
- TLS/SSL: [ ] 1.2+ [ ] Versão: ___
- Rotação de credenciais: [ ] Manual [ ] Automática - a cada: ___
- IP Whitelist: [ ] Necessário [ ] Não necessário
  - IPs da Amoveri: _______________

**Armazenamento de credenciais:**
- Onde serão armazenadas? [ ] NetSuite (cofre) [ ] Azure Key Vault [ ] AWS Secrets [ ] .env [ ] Outro: ___
- Responsável: _______________

### 5.2 LGPD e Compliance

**Dados pessoais tratados:**
- [PREENCHER]

**Base legal:**
- [PREENCHER]

**DPO (Data Protection Officer):**
- Bionexo: _______________
- Amoveri: _______________

**Logs de auditoria:**
- Retenção: _______ meses
- Como acessar: _______________

---

## 6. TRATAMENTO DE ERROS E MONITORAMENTO

### 6.1 Estratégia de Erro

**Retry policy:**
- [ ] Exponential backoff
- [ ] Tentativas: _______
- [ ] Delay entre tentativas: _______

**Erros críticos vs não-críticos:**
- Crítico (bloqueia operação): _______________
- Não-crítico (registra log, continua): _______________

**Notificações:**
- [ ] Email para: _______________
- [ ] Slack/Teams webhook: _______________
- [ ] Dashboard de monitoramento: _______________

### 6.2 Logs e Troubleshooting

**Request ID:**
- Gerado por: [ ] Cliente [ ] Servidor
- Header: `_______________`

**Logs centralizados:**
- Ferramenta: [ ] OneDrive [ ] Azure Monitor [ ] Datadog [ ] Outro: ___
- Retenção: _______ dias

**Acesso a logs da Bionexo:**
- [ ] Via portal [ ] Via API [ ] Solicitar ao suporte

---

## 7. CRONOGRAMA E MILESTONES

### 7.1 Fases do Projeto

**Fase 1: Proof of Concept (PoC)**
- **Duração:** _______ semanas
- **Início:** ___/___/2026
- **Término:** ___/___/2026
- **Entregável:**
  - [ ] Autenticação funcionando
  - [ ] 1 cotação criada via API
  - [ ] 1 proposta lida via API
  - [ ] Outro: _______________

**Fase 2: Piloto**
- **Duração:** _______ semanas
- **Início:** ___/___/2026
- **Término:** ___/___/2026
- **Entregável:**
  - [ ] 10-20 cotações reais processadas
  - [ ] Tratamento de erros implementado
  - [ ] Logs e monitoramento funcionando
  - [ ] Aprovação de _______ usuários piloto

**Fase 3: Rollout Produção**
- **Duração:** _______ semanas
- **Início:** ___/___/2026
- **Término (Go-Live):** ___/___/2026
- **Estratégia:**
  - Semana 1: 20% das cotações
  - Semana 2: 50% das cotações
  - Semana 3: 100% das cotações

### 7.2 Responsabilidades

| Tarefa | Responsável | Prazo | Status |
|--------|-------------|-------|--------|
| [PREENCHER] | [PREENCHER] | ___/___/___ | [ ] Pendente |
| Exemplo: Enviar doc API | Bionexo (Especialista) | ___/___ | [ ] Pendente |
| Exemplo: Criar Saved Search | Kamila (NetSuite) | ___/___ | [ ] Pendente |
| Exemplo: Desenvolver PoC | Pedro (Dev) | ___/___ | [ ] Pendente |
| | | | |

### 7.3 Reuniões de Checkpoint

**Próxima reunião:**
- Data: ___/___/2026, ___:___
- Objetivo: [PREENCHER]

**Frequência:**
- [ ] Semanal (___-feira, ___:___)
- [ ] Quinzenal (___-feira, ___:___)
- [ ] Sob demanda

---

## 8. RISCOS IDENTIFICADOS

| Risco | Probabilidade | Impacto | Mitigação | Responsável |
|-------|---------------|---------|-----------|-------------|
| [PREENCHER] | Alta/Média/Baixa | Alto/Médio/Baixo | [PREENCHER] | [PREENCHER] |
| Exemplo: Rate limit muito baixo | Média | Médio | Implementar fila e processamento assíncrono | Pedro |
| | | | | |

---

## 9. DECISÕES TOMADAS

### Decisões Técnicas
1. [PREENCHER]
2. [PREENCHER]
3. [PREENCHER]

**Exemplo:**
```
1. Arquitetura escolhida: Middleware em Python hospedado em Azure
2. Autenticação: OAuth2 com Client Credentials
3. Sincronização: Webhooks da Bionexo + Polling de fallback a cada 5 min
```

### Decisões de Negócio
1. [PREENCHER]
2. [PREENCHER]

**Exemplo:**
```
1. Piloto com 3 compradores do time de Bruna
2. Go-live previsto para [data], alinhado com fechamento mensal
```

---

## 10. ITENS EM ABERTO (ACTION ITEMS)

| # | Item | Responsável | Prazo | Status |
|---|------|-------------|-------|--------|
| 1 | [PREENCHER] | [PREENCHER] | ___/___/___ | Aberto |
| 2 | Exemplo: Enviar link da documentação da API | Bionexo | ___/___ | Aberto |
| 3 | Exemplo: Fornecer credenciais de sandbox | Bionexo | ___/___ | Aberto |
| 4 | Exemplo: Mapear custom fields do NetSuite | Kamila | ___/___ | Aberto |
| 5 | Exemplo: Criar ambiente de desenvolvimento | Pedro | ___/___ | Aberto |
| | | | | |

---

## 11. DOCUMENTOS E LINKS COMPARTILHADOS

**Recebidos durante a reunião:**
- [ ] Documentação da API: _______________
- [ ] Postman Collection: _______________
- [ ] Diagrama de arquitetura: _______________
- [ ] Contrato/SLA: _______________
- [ ] Outro: _______________

**A serem compartilhados pela Amoveri:**
- [ ] Diagrama de processo NetSuite: _______________
- [ ] Planilha de mapeamento de campos: _______________
- [ ] Outro: _______________

---

## 12. OBSERVAÇÕES E NOTAS ADICIONAIS

[PREENCHER - qualquer informação relevante que não se encaixe nas seções anteriores]

```
Exemplo:
- Gisele mencionou que há um case de sucesso com empresa similar
  (farmacêutica) que pode ser compartilhado
- Especialista da Bionexo recomendou usar biblioteca X para facilitar
- Kamila alertou sobre limitação Y do NetSuite que precisa workaround
```

---

## 13. ANEXOS

- [ ] Anexo A: Screenshots de telas
- [ ] Anexo B: Diagramas desenhados durante reunião
- [ ] Anexo C: Planilha de mapeamento de dados
- [ ] Outro: _______________

---

## ENCERRAMENTO

**Resumo executivo:**
[PREENCHER - 2-3 parágrafos resumindo o que foi decidido]

**Próximos passos imediatos:**
1. [PREENCHER]
2. [PREENCHER]
3. [PREENCHER]

**Assinaturas/Aprovações:**

_______________________________________________
Pedro - Inteligência Comercial (Amoveri Pontual)
Redator da ata

_______________________________________________
[Nome] - [Cargo] (Bionexo)
Validação

_______________________________________________
Kamila - TI NetSuite (Amoveri Pontual)
Validação técnica

---

**Distribuição da ata:**
- [ ] Todos os participantes da reunião
- [ ] Gestão Amoveri: _______________
- [ ] Gestão Bionexo: _______________
- [ ] Compartilhar no SharePoint: [LINK]

**Prazo para revisões/comentários:** ___/___/2026

---

**Documento criado em:** [DATA/HORA]
**Versão:** 1.0
**Status:** [ ] Rascunho [ ] Aguardando aprovação [ ] Aprovado
