# Preparação para Reunião - Integração Bionexo x NetSuite

**Data da Reunião:** Segunda-feira, 14h
**Duração Estimada:** 90 minutos
**Status:** Em Preparação

---

## Participantes

### Bionexo
- **Gisele** - Gestora de Contas
- **Especialistas de Integração** - Equipe Técnica

### Amoveri Pontual
- **Bruna** - Comercial
- **Kamila** - TI NetSuite (Integração)
- **Pedro** - Inteligência Comercial (Dados e Automação)

---

## Objetivo da Reunião

Definir arquitetura técnica, cronograma e responsabilidades para integração via API entre Bionexo e NetSuite, viabilizando automação completa do fluxo de cotações e pedidos.

---

## Agenda Proposta (90 min)

### 1. Abertura e Alinhamento (10 min)
- Apresentação dos participantes e papéis
- Contextualização do projeto Amoveri
- Objetivos de negócio da integração

### 2. Mapeamento de Processos de Negócio (25 min)
**Facilitador:** Bruna (Comercial) + Pedro

**Fluxos a mapear:**
```
A. Fluxo de Cotações
   NetSuite → Bionexo: Envio de RFQ
   Bionexo → NetSuite: Retorno de propostas
   NetSuite: Análise e aprovação

B. Fluxo de Pedidos
   NetSuite → Bionexo: Criação de PO
   Bionexo → NetSuite: Confirmação e tracking

C. Dados Mestres
   - Cadastro de fornecedores
   - Sincronização de produtos/itens
   - Matriz de preços de referência
```

**Perguntas de negócio:**
- Quais status de cotação precisam sincronizar?
- Como tratar divergências de preço/prazo?
- Regras de roteamento: quando enviar para Bionexo vs outros portais?
- Aprovações: workflow permanece no NetSuite ou na Bionexo?

### 3. Arquitetura Técnica e API (35 min)
**Facilitadores:** Kamila (NetSuite) + Especialistas Bionexo + Pedro

#### 3.1 Descoberta da API Bionexo
**Ver documento:** [02-CHECKLIST-TECNICO-API.md](./02-CHECKLIST-TECNICO-API.md)

Pontos críticos:
- Documentação da API (Swagger/OpenAPI?)
- Ambiente de sandbox disponível?
- Modelo de autenticação
- Rate limits e quotas
- Webhooks vs polling

#### 3.2 Arquitetura de Integração
**Opções a discutir:**

```
Opção 1: Integração Direta
NetSuite (SuiteScript) ←──API REST──→ Bionexo

Opção 2: Middleware (Recomendado)
NetSuite ←──→ Integração (Python/Node) ←──→ Bionexo
              ↓
           Log/Monitoring
```

**Pedro precisa perguntar:**
- Qual opção a Bionexo recomenda?
- Existe SDK/biblioteca oficial?
- Como outros clientes fazem a integração?

#### 3.3 Mapeamento de Dados
**Kamila lidera esta parte:**
- Estrutura de dados do NetSuite (Purchase Order, RFQ, Vendor)
- Campos obrigatórios vs opcionais
- Campos customizados do NetSuite que precisam mapear
- Conversões: moeda, unidade de medida, timezone

### 4. Segurança e Compliance (10 min)
**Kamila + Especialistas Bionexo**

- Autenticação: OAuth2? API Key? JWT?
- Dados sensíveis: como são protegidos?
- Logs de auditoria disponíveis?
- LGPD: consentimento e tratamento de dados
- IPs whitelist necessários?

### 5. Plano de Implementação (10 min)
**Todos os participantes**

**Definir:**
- [ ] Cronograma (sprints de 2 semanas?)
- [ ] Milestones e entregas
- [ ] Ambientes: Dev → Homolog → Prod
- [ ] Critérios de aceite para go-live
- [ ] Plano de rollback

**Proposta de fases:**
```
Fase 1 (Sprint 1-2): Proof of Concept
- Autenticação funcionando
- 1 cotação de teste criada via API
- Leitura de propostas

Fase 2 (Sprint 3-4): Piloto
- 10 cotações reais processadas
- Monitoramento e logs
- Tratamento de erros básico

Fase 3 (Sprint 5-6): Produção
- Rollout gradual (20% → 50% → 100%)
- Treinamento de usuários
- Go-live
```

---

## Papéis e Responsabilidades na Reunião

### Pedro (Você)
**Seu papel:** Líder Técnico da Integração

**O que você deve fazer:**
1. **Facilitar discussões técnicas**
   - Fazer perguntas do checklist técnico
   - Anotar decisões de arquitetura
   - Capturar detalhes da API

2. **Ser ponte entre negócio e técnico**
   - Traduzir requisitos de Bruna em specs técnicas
   - Explicar viabilidade técnica para Bruna
   - Alinhar com Kamila sobre capacidades do NetSuite

3. **Documentar tudo**
   - Usar template de ata (ver documento 03)
   - Fotografar/capturar qualquer diagrama
   - Solicitar documentos e credenciais

4. **Definir próximos passos**
   - Quem faz o quê até quando
   - Agendar próxima reunião de checkpoint
   - Confirmar canais de comunicação

**Postura recomendada:**
- Seja assertivo: "Precisamos da documentação da API hoje"
- Seja específico: "Qual o rate limit exato?"
- Seja prático: "Podemos testar isso no sandbox agora?"

### Kamila (TI NetSuite)
**Papel dela:** Especialista NetSuite

**Ela deve cobrir:**
- Capacidades técnicas do NetSuite para integração
- SuiteScript: RESTlets, SuiteTalk, workflows
- Campos e registros customizados existentes
- Saved Searches para exportar dados
- Permissões e roles necessários

**Pedro deve apoiá-la em:**
- Perguntas sobre volumes de dados
- Performance e escalabilidade
- Logs e troubleshooting

### Bruna (Comercial)
**Papel dela:** Dona do Processo de Negócio

**Ela deve cobrir:**
- Fluxo atual de cotações (as-is)
- Fluxo desejado (to-be)
- Regras de negócio e exceções
- Critérios de sucesso

**Pedro deve apoiá-la em:**
- Traduzir regras em requisitos técnicos
- Avaliar viabilidade de automações

---

## Materiais para Levar na Reunião

### Preparados pela Amoveri
- [ ] **Diagrama de processo atual** (PowerPoint ou Visio)
- [ ] **Volumes de transações**
  - Cotações/mês: _______
  - Pedidos/mês: _______
  - Fornecedores ativos: _______
- [ ] **Screenshots do NetSuite**
  - Tela de cotação
  - Tela de pedido
  - Campos customizados relevantes
- [ ] **Credenciais já obtidas**
  - Bionexo Apoio Cotações: ✅
  - Bionexo GT Plan: ✅

### Solicitar da Bionexo (durante a reunião)
- [ ] **Documentação da API**
  - URL da documentação
  - Postman Collection ou Swagger
  - Exemplos de payloads
- [ ] **Credenciais de sandbox**
  - URL do ambiente de homologação
  - API Key ou Client ID/Secret
  - Dados de teste (fornecedor fictício, produtos)
- [ ] **Diagramas de arquitetura**
  - Fluxo de dados
  - Modelo de segurança
- [ ] **SLA e Suporte**
  - Horário de suporte técnico
  - Canal de comunicação (Slack, Teams, Email)
  - Tempo de resposta esperado

---

## Perguntas-Chave por Perfil

### Para a Gisele (Gestora de Contas)
**Objetivo:** Alinhamento comercial e expectativas

1. Qual o prazo que a Bionexo vê como realista para essa integração?
2. Existe custo adicional para acesso à API ou suporte técnico?
3. Outros clientes já integraram Bionexo com NetSuite? Podemos falar com eles?
4. Qual o SLA de suporte para integrações via API?
5. Quem será nosso ponto focal técnico após essa reunião?

### Para Especialistas de Integração (Técnicos Bionexo)
**Ver lista completa em:** [02-CHECKLIST-TECNICO-API.md](./02-CHECKLIST-TECNICO-API.md)

**Top 5 mais críticas:**
1. A API é RESTful ou SOAP? Versão atual?
2. Qual modelo de autenticação? (OAuth2, API Key, JWT?)
3. Rate limit: quantas requisições por minuto/hora?
4. Webhooks disponíveis para eventos em tempo real?
5. Existe SDK ou biblioteca oficial para facilitar integração?

### Para Kamila (nossa TI NetSuite)
**Pedro deve perguntar para ela antes da reunião:**

1. Quais integrações já existem no NetSuite? Há risco de conflito?
2. Temos ambientes separados (sandbox, produção) no NetSuite?
3. Você prefere SuiteScript (interno) ou integração externa via middleware?
4. Campos customizados de Purchase Order que precisam ser mapeados?
5. Há workflows automáticos no NetSuite que podem ser impactados?

---

## Checklist Pré-Reunião (Fazer até Domingo)

### Técnico
- [ ] Ler documentação pública da Bionexo (se houver)
- [ ] Revisar arquitetura de integração NetSuite (SuiteTalk, RESTlets)
- [ ] Preparar diagrama de processo atual em ferramenta visual
- [ ] Testar credenciais Bionexo existentes (login manual)
- [ ] Instalar Postman ou Insomnia (para testar APIs)

### Negócio
- [ ] Reunir com Bruna: mapear fluxo de cotações em detalhes
- [ ] Levantar volumes: quantas cotações/pedidos por dia/semana/mês
- [ ] Identificar pain points do processo atual
- [ ] Definir métricas de sucesso (% automação, tempo economizado)

### Documentação
- [ ] Criar pasta compartilhada (SharePoint/OneDrive)
- [ ] Preparar template de ata
- [ ] Preparar checklist técnico impresso
- [ ] Preparar laptop com acesso à Bionexo e NetSuite (para demonstração)

---

## Durante a Reunião

### O que Pedro deve fazer:
1. **Cronometrar** (usar temporizador discreto)
   - Manter agenda no timing
   - Alertar se algum tópico está tomando muito tempo

2. **Anotar TUDO** (preferencialmente em notebook compartilhado)
   - Decisões técnicas
   - URLs e credenciais (mascarar senhas)
   - Prazos e responsáveis
   - Dúvidas não resolvidas

3. **Pedir demonstração**
   - "Podemos ver um exemplo de payload da API agora?"
   - "Vocês podem mostrar o portal de desenvolvedor?"

4. **Confirmar entendimento**
   - "Deixa eu confirmar: a autenticação é OAuth2 com refresh token, correto?"
   - Repetir decisões importantes para validação

5. **Puxar próximos passos**
   - Últimos 10 minutos: resumir e definir ações
   - "Quem vai enviar a documentação? Até quando?"

---

## Pós-Reunião (Fazer até Terça)

### Imediato (24h após reunião)
- [ ] Enviar ata para todos os participantes
- [ ] Solicitar confirmação de decisões via email
- [ ] Acessar ambiente de sandbox da Bionexo
- [ ] Baixar documentação da API

### Primeira Semana
- [ ] Fazer primeira chamada de API (autenticação)
- [ ] Criar projeto de integração no Git
- [ ] Configurar ambiente de desenvolvimento
- [ ] Agendar reunião de checkpoint (7-10 dias)

### Segunda Semana
- [ ] Implementar Proof of Concept
- [ ] Documentar aprendizados técnicos
- [ ] Identificar gaps/riscos
- [ ] Atualizar cronograma se necessário

---

## Riscos e Planos de Contingência

### Risco 1: API não é RESTful (é SOAP ou muito limitada)
**Impacto:** Alto - pode dificultar implementação
**Mitigação:** Avaliar web scraping como fallback
**Decisão na reunião:** Perguntar sobre limitações conhecidas

### Risco 2: Rate limit muito baixo
**Impacto:** Médio - pode lentificar sincronização
**Mitigação:** Implementar fila e processamento assíncrono
**Decisão na reunião:** Entender limites exatos

### Risco 3: Sem ambiente de sandbox
**Impacto:** Alto - dificulta testes sem impactar produção
**Mitigação:** Solicitar criação de ambiente ou usar conta demo
**Decisão na reunião:** Confirmar disponibilidade

### Risco 4: Falta de webhooks (só polling)
**Impacto:** Médio - sincronização não será em tempo real
**Mitigação:** Polling inteligente (intervalo adaptativo)
**Decisão na reunião:** Confirmar se há webhooks

### Risco 5: Documentação incompleta ou desatualizada
**Impacto:** Médio - aumenta tempo de desenvolvimento
**Mitigação:** Solicitar suporte técnico direto da Bionexo
**Decisão na reunião:** Definir canal direto com time técnico

---

## Glossário para a Reunião

**Para usar com stakeholders não-técnicos:**

| Termo Técnico | Tradução para Negócio |
|---------------|----------------------|
| API | "Canal de comunicação automático entre sistemas" |
| Webhook | "Notificação automática quando algo acontece" |
| Rate limit | "Limite de quantas vezes podemos consultar por minuto" |
| Sandbox | "Ambiente de testes, onde podemos errar sem problemas" |
| Payload | "Pacote de dados que enviamos/recebemos" |
| OAuth2 | "Sistema de login seguro entre sistemas" |
| Middleware | "Sistema intermediário que facilita a comunicação" |

---

## Próximos Documentos

1. **[02-CHECKLIST-TECNICO-API.md](./02-CHECKLIST-TECNICO-API.md)** - Perguntas técnicas detalhadas sobre a API
2. **[03-TEMPLATE-ATA-REUNIAO.md](./03-TEMPLATE-ATA-REUNIAO.md)** - Template para documentar a reunião
3. **[04-LEVANTAMENTO-INTERNO.md](./04-LEVANTAMENTO-INTERNO.md)** - Dados internos para preparar antes da reunião

---

**Última atualização:** 2026-01-29
**Responsável:** Pedro (Inteligência Comercial)
**Status:** Aguardando reunião (Segunda-feira, 14h)
