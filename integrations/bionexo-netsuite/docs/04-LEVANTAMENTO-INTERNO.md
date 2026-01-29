# Levantamento Interno - Amoveri Pontual

**Objetivo:** Documentar informações internas antes da reunião com Bionexo
**Responsável:** Pedro (Inteligência Comercial)
**Prazo:** Concluir até Domingo (antes da reunião de Segunda)
**Status:** [ ] Em andamento [ ] Concluído

---

## Como Usar Este Documento

Este levantamento deve ser feito **ANTES** da reunião com a Bionexo. As informações aqui coletadas vão:
1. Ajudar a entender o cenário atual
2. Definir requisitos técnicos e de negócio
3. Facilitar discussões durante a reunião
4. Servir de base para documentação do projeto

**Instruções:**
- Preencher cada seção com ajuda dos stakeholders internos
- Marcar [ ] como [x] quando completar cada item
- Se alguma informação não estiver disponível, anotar: "A LEVANTAR"

---

## SEÇÃO 1: PROCESSO ATUAL DE COTAÇÕES

### 1.1 Visão Geral
**Responsável por preencher:** Bruna (Comercial) + Pedro

**Descrição do processo atual:**
```
[PREENCHER - descrever passo a passo como funciona hoje]

Exemplo:
1. Cliente envia solicitação de cotação por email/WhatsApp
2. Comprador registra no NetSuite (Purchase Order ou RFQ)
3. Comprador exporta Excel com itens
4. Comprador faz upload na Bionexo
5. Fornecedores enviam propostas via Bionexo
6. Comprador baixa propostas (Excel)
7. Comprador importa no NetSuite manualmente
8. Análise e aprovação no NetSuite
9. Gera pedido no NetSuite
10. Envia pedido ao fornecedor (email/portal)
```

**Frequência:**
- Cotações/dia: _______
- Cotações/semana: _______
- Cotações/mês: _______

**Sazonalidade:**
- Há picos em determinados períodos? [ ] Sim [ ] Não
  - Se sim, quando? _______

### 1.2 Dores e Problemas Atuais

**Tempo gasto:**
- Tempo médio por cotação: _______ minutos/horas
- Etapa mais demorada: _______
- Total de horas/semana gastas em cotações: _______

**Erros comuns:**
- [ ] Erro de digitação em preços/quantidades
- [ ] Itens faltando na cotação
- [ ] Divergência entre NetSuite e Bionexo
- [ ] Atraso na resposta a clientes
- [ ] Outros: _______

**Impacto negativo:**
- Perda de vendas? [ ] Sim [ ] Não - Estimativa: R$ _______ /mês
- Retrabalho? [ ] Sim [ ] Não - Frequência: _______
- Insatisfação do cliente? [ ] Sim [ ] Não

### 1.3 Expectativas com Automação

**O que esperamos melhorar:**
- [ ] Reduzir tempo de resposta de _______ para _______
- [ ] Eliminar erros de digitação
- [ ] Aumentar capacidade de processar _______ cotações adicionais/mês
- [ ] Liberar equipe para atividades estratégicas
- [ ] Outros: _______

**Meta de ROI:**
- Horas economizadas/semana: _______
- Valor estimado (R$/hora × horas economizadas): R$ _______/mês
- Investimento esperado: R$ _______
- Payback esperado: _______ meses

---

## SEÇÃO 2: VOLUMES E ESTATÍSTICAS

### 2.1 Volumes de Transações
**Responsável por preencher:** Pedro + Bruna

**Cotações (RFQ):**
- Último mês: _______
- Últimos 3 meses (média/mês): _______
- Últimos 12 meses (média/mês): _______
- Projeção para próximos 12 meses: _______

**Pedidos de Compra (PO):**
- Último mês: _______
- Taxa de conversão (RFQ → PO): _______ %

**Itens por cotação:**
- Mínimo: _______
- Média: _______
- Máximo: _______
- Cotações com mais de 100 itens: _______ % do total

**Valor médio:**
- Cotação média: R$ _______
- Pedido médio: R$ _______
- Ticket mínimo: R$ _______
- Ticket máximo: R$ _______

### 2.2 Fornecedores
**Responsável por preencher:** Bruna + Compras

**Cadastro:**
- Total de fornecedores cadastrados no NetSuite: _______
- Fornecedores ativos (últimos 6 meses): _______
- Fornecedores cadastrados na Bionexo: _______

**Distribuição:**
- Fornecedores que concentram 80% das compras: _______
- Novos fornecedores cadastrados/mês: _______

**Observações:**
```
[PREENCHER - há fornecedores problemáticos? Há preferências?]
```

### 2.3 Produtos
**Responsável por preencher:** Pedro + Compras

**Catálogo:**
- Total de SKUs no NetSuite: _______
- SKUs ativos (movimentação nos últimos 6 meses): _______
- SKUs no catálogo Bionexo: _______

**Categorias principais:**
1. _______ (_______ % do volume)
2. _______ (_______ % do volume)
3. _______ (_______ % do volume)

**Complexidade:**
- Produtos com múltiplas unidades de medida: [ ] Sim [ ] Não
- Produtos com lotes/validade: [ ] Sim [ ] Não
- Produtos controlados (Anvisa): [ ] Sim [ ] Não
- Produtos importados: [ ] Sim [ ] Não

---

## SEÇÃO 3: NETSUÍTE - CONFIGURAÇÃO ATUAL

### 3.1 Informações Gerais
**Responsável por preencher:** Kamila (TI NetSuite)

**Conta NetSuite:**
- Account ID: _______
- URL: _______ (ex: https://1234567.app.netsuite.com)
- Versão/Bundle: _______

**Usuários:**
- Total de usuários: _______
- Usuários de compras (que usarão integração): _______

**Ambientes:**
- [ ] Produção
- [ ] Sandbox/Homologação
  - URL Sandbox: _______

### 3.2 Módulos e Funcionalidades Utilizadas

**Módulos ativos:**
- [ ] Purchase Orders
- [ ] Purchase Requisitions
- [ ] RFQ (Request for Quote)
- [ ] Vendor Management
- [ ] Inventory Management
- [ ] Aprovações (Approval Routing)
- [ ] Outros: _______

**Custom Records ou objetos customizados:**
- [ ] Sim [ ] Não
- Se sim, quais são relevantes para cotações/compras? _______

### 3.3 Campos Customizados Relevantes
**Responsável por preencher:** Kamila

**Transaction (Purchase Order / RFQ):**
| Script ID | Label | Tipo | Obrigatório? | Descrição |
|-----------|-------|------|--------------|-----------|
| [PREENCHER] | [PREENCHER] | Text/Number/Date/etc | Sim/Não | [PREENCHER] |
| Exemplo: custbody_prazo_entrega | Prazo de Entrega | Integer | Sim | Dias para entrega |
| | | | | |

**Vendor:**
| Script ID | Label | Tipo | Obrigatório? | Descrição |
|-----------|-------|------|--------------|-----------|
| [PREENCHER] | [PREENCHER] | Text/Number/Date/etc | Sim/Não | [PREENCHER] |
| | | | | |

**Item:**
| Script ID | Label | Tipo | Obrigatório? | Descrição |
|-----------|-------|------|--------------|-----------|
| [PREENCHER] | [PREENCHER] | Text/Number/Date/etc | Sim/Não | [PREENCHER] |
| | | | | |

### 3.4 Workflows e Automações Existentes

**Workflows ativos que podem impactar:**
| Nome do Workflow | Tipo de Record | Ações | Pode conflitar? |
|------------------|----------------|-------|-----------------|
| [PREENCHER] | Purchase Order | [PREENCHER] | Sim/Não |
| Exemplo: Aprovação de PO > R$10k | Purchase Order | Envia email para gerente | Não |
| | | | |

**Scripts existentes (SuiteScripts):**
- [ ] User Event Scripts
- [ ] Scheduled Scripts
- [ ] RESTlets
- [ ] Outros: _______

**Detalhes dos scripts relevantes:**
```
[PREENCHER - listar scripts que manipulam PO, RFQ, Vendor]

Exemplo:
- UE_ValidateVendor.js - Valida se fornecedor está homologado antes de criar PO
- SS_SyncInventory.js - Scheduled script que atualiza estoque diariamente
```

### 3.5 Integrações Existentes

**Outras integrações ativas no NetSuite:**
| Sistema Integrado | Método | Frequência | Pode conflitar? |
|-------------------|--------|------------|-----------------|
| [PREENCHER] | API/CSV/Outro | Real-time/Diário | Sim/Não |
| Exemplo: Power BI | Saved Search export | Diário (6h) | Não |
| | | | |

### 3.6 Saved Searches Existentes

**Saved Searches úteis para integração:**
| Nome | ID | Tipo | Campos principais | URL |
|------|----|----- |-------------------|-----|
| [PREENCHER] | [PREENCHER] | Transaction/Item/Vendor | [PREENCHER] | [PREENCHER] |
| Exemplo: Produtos Ativos | 123 | Item | SKU, Descricao, Custo | https://... |
| | | | | |

**Precisamos criar novas Saved Searches?**
- [ ] Sim [ ] Não
- Se sim, quais? _______

### 3.7 Permissões e Roles

**Roles que precisam acesso:**
| Role | Tipo de acesso | Usuários |
|------|----------------|----------|
| [PREENCHER] | Leitura/Escrita/Admin | [PREENCHER] |
| Exemplo: Comprador | Escrita (criar RFQ/PO) | 5 usuários |
| Exemplo: Gerente de Compras | Admin (aprovar) | 2 usuários |
| | | |

**Role para integração (API):**
- Será criado role específico? [ ] Sim [ ] Não
- Nome sugerido: _______
- Permissões necessárias:
  - [ ] Purchase Order (Leitura/Escrita)
  - [ ] RFQ (Leitura/Escrita)
  - [ ] Vendor (Leitura)
  - [ ] Item (Leitura)

### 3.8 Token Based Authentication (TBA)

**TBA já configurado?**
- [ ] Sim [ ] Não [ ] Não sei

**Se sim:**
- Integration Record Name: _______
- Token ID: _______
- Token Secret: _______ (guardar em local seguro)
- Consumer Key: _______
- Consumer Secret: _______ (guardar em local seguro)

**Se não:**
- Responsável por criar: _______
- Prazo: ___/___/___

---

## SEÇÃO 4: BIONEXO - ACESSO E CREDENCIAIS

### 4.1 Acessos Existentes
**Responsável por preencher:** Pedro

**Credenciais atuais:**
- [x] Bionexo Apoio Cotações
  - Email: _______
  - Senha: _______ (guardar em cofre)
  - URL: _______
  - Último acesso: ___/___/___

- [x] Bionexo GT Plan
  - Email: _______
  - Senha: _______ (guardar em cofre)
  - URL: _______
  - Último acesso: ___/___/___

**Teste de credenciais:**
- [ ] Testei login manual no Bionexo Apoio - Status: _______
- [ ] Testei login manual no Bionexo GT Plan - Status: _______

### 4.2 Portais e Funcionalidades

**Funcionalidades utilizadas atualmente:**
- [ ] Criação de cotações
- [ ] Recebimento de propostas
- [ ] Comparação de propostas
- [ ] Criação de pedidos
- [ ] Acompanhamento de entregas
- [ ] Relatórios/Analytics
- [ ] Outras: _______

**Usuários:**
- Total de usuários Amoveri com acesso à Bionexo: _______
- Nomes: _______

**Contato Bionexo:**
- Gestora de Contas (Gisele): _______
- Email: _______
- Telefone: _______

---

## SEÇÃO 5: INFRAESTRUTURA E TECNOLOGIA

### 5.1 Ambiente de Desenvolvimento
**Responsável por preencher:** Pedro + TI

**Onde a integração será hospedada:**
- [ ] Azure (recomendado)
- [ ] AWS
- [ ] Google Cloud
- [ ] On-premise (servidor local)
- [ ] Outro: _______

**Por quê escolhemos isso?**
```
[PREENCHER - justificar escolha]

Exemplo:
Azure, pois já temos assinatura corporativa e integração nativa com Power BI
```

**Recursos já disponíveis:**
- [ ] Virtual Machine / App Service
- [ ] Banco de dados (SQL/NoSQL)
- [ ] Storage (para logs e arquivos)
- [ ] Monitoramento (Application Insights, etc)
- [ ] Outro: _______

### 5.2 Stack Tecnológico Proposto
**Responsável por preencher:** Pedro

**Linguagem de programação:**
- [ ] Python (recomendado para Data/Automation)
- [ ] Node.js / TypeScript
- [ ] Java
- [ ] .NET/C#
- [ ] Outro: _______

**Justificativa:**
```
[PREENCHER]

Exemplo:
Python, pois já utilizamos no projeto de automação de cotações e
temos familiaridade com bibliotecas de integração (requests, pandas).
```

**Frameworks/Bibliotecas:**
- [ ] Flask/FastAPI (API web)
- [ ] Celery (fila de tarefas assíncronas)
- [ ] Pandas (manipulação de dados)
- [ ] Requests (chamadas HTTP)
- [ ] SQLAlchemy (ORM)
- [ ] Outros: _______

### 5.3 Segurança

**Cofre de senhas/secrets:**
- [ ] Azure Key Vault
- [ ] AWS Secrets Manager
- [ ] HashiCorp Vault
- [ ] .env (apenas desenvolvimento)
- [ ] Outro: _______

**VPN/Rede:**
- Integração precisa estar dentro da VPN corporativa? [ ] Sim [ ] Não
- IP fixo necessário? [ ] Sim [ ] Não
  - Se sim, qual IP? _______

**Certificados SSL:**
- Algum certificado específico necessário? [ ] Sim [ ] Não
- Se sim, detalhes: _______

### 5.4 Backup e Disaster Recovery

**Estratégia de backup:**
- [ ] Backup diário de logs
- [ ] Backup de configurações
- [ ] Backup de banco de dados (se aplicável)
- [ ] Versionamento de código (Git)

**Retenção:**
- Logs: _______ dias
- Backups: _______ dias

**Plano de contingência:**
```
[PREENCHER - o que fazer se integração cair?]

Exemplo:
1. Alertar equipe via email/Slack
2. Equipe volta a processar manualmente por até 24h
3. Suporte técnico da Bionexo acionado se necessário
```

---

## SEÇÃO 6: REGRAS DE NEGÓCIO

### 6.1 Aprovações e Workflow
**Responsável por preencher:** Bruna + Kamila

**Regras de aprovação de cotações:**
| Condição | Aprovador | Tempo SLA |
|----------|-----------|-----------|
| [PREENCHER] | [PREENCHER] | [PREENCHER] |
| Exemplo: Valor > R$ 10.000 | Gerente de Compras | 4 horas |
| Exemplo: Fornecedor novo | Compras + Fiscal | 24 horas |
| | | |

**Exceções:**
- Casos que não precisam seguir workflow padrão: _______
- Quem pode aprovar exceções: _______

### 6.2 Validações Necessárias

**Validações de fornecedor:**
- [ ] Fornecedor deve estar ativo no NetSuite
- [ ] Fornecedor deve estar homologado
- [ ] Fornecedor não pode ter pendências fiscais
- [ ] CNPJ válido
- [ ] Outras: _______

**Validações de produto:**
- [ ] Produto deve existir no cadastro NetSuite
- [ ] Produto deve ter estoque disponível (para revenda)
- [ ] Produto não pode estar inativo
- [ ] Preço dentro da faixa aceitável (variação máxima: _______ %)
- [ ] Outras: _______

**Validações de cotação:**
- [ ] Data de entrega mínima: _______ dias
- [ ] Valor mínimo de pedido: R$ _______
- [ ] Prazo de resposta: _______ horas
- [ ] Outras: _______

### 6.3 Priorização

**Critérios de prioridade:**
| Tipo de Cotação | Prioridade | SLA de Resposta |
|-----------------|------------|-----------------|
| [PREENCHER] | Alta/Média/Baixa | [PREENCHER] |
| Exemplo: Urgente (cliente aguardando) | Alta | 2 horas |
| Exemplo: Reposição estoque | Média | 24 horas |
| Exemplo: Cotação exploratória | Baixa | 48 horas |

**Como identificar prioridade:**
```
[PREENCHER - há campo no NetSuite? Tag? Status?]

Exemplo:
Campo customizado "custbody_prioridade" com valores: Alta, Média, Baixa
```

### 6.4 Exceções e Casos Especiais

**Situações que NÃO devem ser automatizadas (pelo menos inicialmente):**
- [ ] Cotações de importação
- [ ] Cotações com produtos controlados
- [ ] Cotações acima de R$ _______
- [ ] Fornecedores internacionais
- [ ] Outras: _______

**Justificativa:**
```
[PREENCHER - por que essas exceções?]
```

---

## SEÇÃO 7: COMPLIANCE E REGULAMENTAÇÃO

### 7.1 LGPD
**Responsável por preencher:** TI + Jurídico/Compliance

**Dados pessoais tratados:**
- [ ] Nome de compradores
- [ ] Email de compradores
- [ ] Dados de fornecedores (razão social, CNPJ, contatos)
- [ ] Outros: _______

**Base legal:**
- [ ] Execução de contrato
- [ ] Legítimo interesse
- [ ] Consentimento
- [ ] Outra: _______

**DPO (Data Protection Officer) da Amoveri:**
- Nome: _______
- Email: _______
- Telefone: _______

**Medidas de proteção:**
- [ ] Criptografia de dados sensíveis
- [ ] Anonimização de logs (remover CPF/email)
- [ ] Controle de acesso (RBAC)
- [ ] Auditoria de acessos
- [ ] Outras: _______

### 7.2 Regulamentação Setorial

**Anvisa (se aplicável):**
- Lidamos com produtos controlados? [ ] Sim [ ] Não
- Se sim, há implicações para integração? _______

**Fiscal/Tributário:**
- Informações fiscais devem trafegar na integração? [ ] Sim [ ] Não
- Se sim, quais? _______

---

## SEÇÃO 8: TREINAMENTO E CHANGE MANAGEMENT

### 8.1 Usuários Finais
**Responsável por preencher:** Bruna + RH/Treinamento

**Perfis de usuários:**
| Perfil | Quantidade | Familiaridade com tecnologia | Necessita treinamento? |
|--------|------------|------------------------------|------------------------|
| [PREENCHER] | [PREENCHER] | Alta/Média/Baixa | Sim/Não |
| Exemplo: Comprador | 5 | Média | Sim (2h) |
| Exemplo: Gerente de Compras | 2 | Alta | Não |

**Resistência à mudança:**
- Esperamos resistência? [ ] Sim [ ] Não
- Se sim, de quem? _______
- Como mitigar? _______

### 8.2 Plano de Treinamento

**Materiais necessários:**
- [ ] Manual do usuário
- [ ] Vídeo tutorial (step-by-step)
- [ ] FAQ (perguntas frequentes)
- [ ] Quick reference guide (1 página)
- [ ] Outros: _______

**Formato de treinamento:**
- [ ] Presencial
- [ ] Online (Teams/Zoom)
- [ ] Gravado (assíncrono)
- [ ] Combinação

**Responsável pelo treinamento:**
- Nome: _______
- Data prevista: ___/___/___

### 8.3 Suporte Pós Go-Live

**Quem vai dar suporte aos usuários após implementação?**
- Nível 1 (dúvidas simples): _______
- Nível 2 (troubleshooting técnico): _______
- Nível 3 (desenvolvimento/ajustes): _______

**Canal de suporte:**
- [ ] Email: _______
- [ ] Slack/Teams channel: _______
- [ ] Sistema de tickets (Jira, ServiceDesk): _______
- [ ] Telefone: _______

---

## SEÇÃO 9: BUDGET E RECURSOS

### 9.1 Orçamento
**Responsável por preencher:** Gestão/Financeiro

**Orçamento disponível para projeto:**
- Total aprovado: R$ _______
- Distribuição:
  - Desenvolvimento: R$ _______ (______ %)
  - Infraestrutura (hosting): R$ _______ /mês
  - Licenças/Ferramentas: R$ _______
  - Treinamento: R$ _______
  - Contingência (15%): R$ _______

**Justificativa/ROI esperado:**
```
[PREENCHER]

Exemplo:
Investimento de R$ 50.000 será pago em 6 meses através da economia
de 20h/semana (R$ 80/h × 20h × 4 semanas = R$ 6.400/mês).

Adicional: Redução de erros (estimado R$ 2.000/mês em retrabalho)
```

### 9.2 Recursos Humanos

**Equipe do projeto:**
| Nome | Papel | % Dedicação | Período |
|------|-------|-------------|---------|
| [PREENCHER] | [PREENCHER] | [PREENCHER] | [PREENCHER] |
| Exemplo: Pedro | Tech Lead / Dev | 60% | 3 meses |
| Exemplo: Kamila | Consultor NetSuite | 20% | 3 meses |
| Exemplo: Bruna | Product Owner | 10% | 3 meses |

**Necessidade de contratação externa:**
- [ ] Não, equipe interna é suficiente
- [ ] Sim, consultor NetSuite especializado
- [ ] Sim, desenvolvedor freelancer
- [ ] Sim, outro: _______

**Budget para contratação:**
- R$ _______ (total ou /mês)

---

## SEÇÃO 10: CRONOGRAMA INTERNO

### 10.1 Pré-Requisitos
**Tarefas que precisam ser concluídas ANTES da integração:**

| Tarefa | Responsável | Prazo | Status |
|--------|-------------|-------|--------|
| [PREENCHER] | [PREENCHER] | ___/___/___ | Pendente/Andamento/Concluído |
| Exemplo: Criar role de integração no NetSuite | Kamila | ___/___ | Pendente |
| Exemplo: Mapear custom fields necessários | Kamila | ___/___ | Pendente |
| Exemplo: Obter aprovação de budget | Gestão | ___/___ | Concluído |
| | | | |

### 10.2 Disponibilidade de Stakeholders

**Disponibilidade para reuniões e validações:**
- Bruna (Comercial): _______ horas/semana
- Kamila (NetSuite): _______ horas/semana
- Pedro (Dev): _______ horas/semana

**Períodos de indisponibilidade (férias, viagens):**
- _______

**Deadline de negócio (se houver):**
- Data crítica: ___/___/___ - Motivo: _______

---

## CHECKLIST FINAL - ANTES DA REUNIÃO

**Preparação para reunião com Bionexo (Segunda-feira, 14h):**

### Documentação
- [ ] Preenchi este levantamento interno
- [ ] Validei informações com Bruna (Comercial)
- [ ] Validei informações com Kamila (NetSuite)
- [ ] Li documento [01-PREPARACAO-REUNIAO.md](./01-PREPARACAO-REUNIAO.md)
- [ ] Imprimi [02-CHECKLIST-TECNICO-API.md](./02-CHECKLIST-TECNICO-API.md)

### Materiais
- [ ] Preparei diagrama de processo atual (PowerPoint/Visio/Draw.io)
- [ ] Consolidei volumes e estatísticas em planilha
- [ ] Fiz screenshots das telas do NetSuite relevantes
- [ ] Testei credenciais Bionexo (login manual)

### Logística
- [ ] Confirmei presença de Bruna e Kamila
- [ ] Reservei sala (se presencial) ou criei reunião Teams/Zoom
- [ ] Laptop carregado com acesso à Bionexo e NetSuite
- [ ] Testei conexão/internet
- [ ] Preparei bloco de notas ou documento para anotar

### Mental
- [ ] Li todas as perguntas do checklist técnico
- [ ] Sei identificar as perguntas críticas (top 10)
- [ ] Entendo o processo atual e as expectativas
- [ ] Estou preparado para conduzir/facilitar a reunião

---

## OBSERVAÇÕES ADICIONAIS

**Anotações livres:**
```
[PREENCHER - qualquer informação adicional relevante]
```

---

## APROVAÇÕES

**Este levantamento foi validado por:**

_______________________________________________
Bruna - Comercial
Data: ___/___/___

_______________________________________________
Kamila - TI NetSuite
Data: ___/___/___

_______________________________________________
Pedro - Inteligência Comercial
Data: ___/___/___

---

**Última atualização:** 2026-01-29
**Versão:** 1.0
**Status:** [ ] Rascunho [ ] Em revisão [ ] Aprovado
