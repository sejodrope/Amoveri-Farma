# Checklist Técnico - API Bionexo

**Data:** 2026-01-29
**Responsável:** Pedro (Inteligência Comercial)
**Destinatário:** Especialistas de Integração Bionexo

---

## Como Usar Este Checklist

Este documento contém todas as perguntas técnicas essenciais sobre a API da Bionexo. Use-o durante a reunião para garantir que todos os pontos críticos sejam cobertos.

**Método sugerido:**
1. Imprimir este checklist ou ter em segunda tela
2. Ir marcando ✅ conforme as perguntas são respondidas
3. Anotar respostas diretamente neste documento (fazer cópia editável)
4. Sinalizar ⚠️ qualquer ponto que precisa follow-up

---

## 1. DOCUMENTAÇÃO E RECURSOS

### 1.1 Documentação da API

- [ ] **Onde está a documentação completa da API?**
  - URL: _______________
  - Formato: [ ] Swagger/OpenAPI [ ] Postman Collection [ ] PDF [ ] Outro: _______
  - Versão da documentação: _______
  - Última atualização: _______

- [ ] **A documentação está em português ou inglês?**
  - Idioma: _______

- [ ] **Existe changelog da API?**
  - URL: _______________
  - Como vocês comunicam breaking changes?

- [ ] **Há exemplos de código em diferentes linguagens?**
  - [ ] Python [ ] JavaScript/Node [ ] Java [ ] .NET [ ] PHP [ ] Outro: _______

### 1.2 Recursos de Apoio

- [ ] **Existe SDK ou biblioteca oficial?**
  - Linguagens disponíveis: _______
  - Repositório GitHub: _______________

- [ ] **Portal de desenvolvedor disponível?**
  - URL: _______________
  - Como obter acesso?

- [ ] **Sandbox/Ambiente de testes?**
  - [ ] Sim [ ] Não
  - URL: _______________
  - Como obter credenciais de teste: _______
  - Dados de teste disponíveis? (fornecedores, produtos fictícios)

- [ ] **Exemplos de payload (request/response)?**
  - [ ] Disponíveis na documentação
  - [ ] Podem ser compartilhados durante a reunião
  - [ ] Precisam ser solicitados separadamente

---

## 2. ARQUITETURA DA API

### 2.1 Tipo e Versão

- [ ] **Qual o tipo de API?**
  - [ ] REST [ ] GraphQL [ ] SOAP [ ] Outro: _______

- [ ] **Versão atual da API:**
  - Versão: _______
  - Base URL: _______________
  - Exemplo: `https://api.bionexo.com/v1` ou `https://api.bionexonew.com/api/v2`

- [ ] **Versionamento:**
  - Como é feito? [ ] URL [ ] Header [ ] Query param
  - Versões anteriores suportadas? _______
  - Quando uma versão é descontinuada? _______

### 2.2 Protocolo e Formato

- [ ] **Protocolo:**
  - [ ] HTTPS (TLS 1.2+) [ ] HTTP [ ] Outro: _______

- [ ] **Formato de dados:**
  - Request: [ ] JSON [ ] XML [ ] Form-data [ ] Outro: _______
  - Response: [ ] JSON [ ] XML [ ] Outro: _______

- [ ] **Content-Type esperado:**
  - Request: `_______`
  - Response: `_______`

- [ ] **Encoding:**
  - [ ] UTF-8 [ ] ISO-8859-1 [ ] Outro: _______

---

## 3. AUTENTICAÇÃO E SEGURANÇA

### 3.1 Modelo de Autenticação

- [ ] **Qual o método de autenticação?**
  - [ ] OAuth 2.0
  - [ ] API Key
  - [ ] JWT (JSON Web Token)
  - [ ] Basic Auth
  - [ ] Token Bearer
  - [ ] Outro: _______

### 3.2 OAuth 2.0 (se aplicável)

- [ ] **Fluxo OAuth utilizado:**
  - [ ] Client Credentials
  - [ ] Authorization Code
  - [ ] Password Grant
  - [ ] Outro: _______

- [ ] **Endpoints OAuth:**
  - Authorization URL: _______________
  - Token URL: _______________

- [ ] **Escopo (scopes) necessários:**
  - _______

- [ ] **Validade do Access Token:**
  - Duração: _______ (minutos/horas)

- [ ] **Refresh Token disponível?**
  - [ ] Sim [ ] Não
  - Validade: _______

### 3.3 API Key (se aplicável)

- [ ] **Como a API Key é passada?**
  - [ ] Header (nome: _______)
  - [ ] Query parameter (nome: _______)
  - [ ] Body

- [ ] **Formato da API Key:**
  - Exemplo (mascarado): `bxo_abc123...`

- [ ] **Como gerar/renovar API Key?**
  - [ ] Portal do desenvolvedor
  - [ ] Solicitar ao suporte
  - [ ] Automático

- [ ] **API Key tem validade/expiração?**
  - [ ] Sim (_____ dias) [ ] Não

### 3.4 Segurança Adicional

- [ ] **IP Whitelist necessário?**
  - [ ] Sim [ ] Não
  - Como adicionar IPs: _______

- [ ] **CORS configurado?**
  - [ ] Sim [ ] Não (somente server-side)

- [ ] **Certificados SSL/TLS:**
  - Alguma configuração especial? _______

- [ ] **Headers de segurança obrigatórios:**
  - Exemplo: `X-Request-ID`, `X-Company-ID`
  - _______

---

## 4. RATE LIMITS E QUOTAS

### 4.1 Limites de Taxa

- [ ] **Rate limit por minuto:**
  - Limite: _______ requisições/minuto

- [ ] **Rate limit por hora:**
  - Limite: _______ requisições/hora

- [ ] **Rate limit por dia:**
  - Limite: _______ requisições/dia

- [ ] **Rate limit diferenciado por endpoint?**
  - [ ] Sim [ ] Não
  - Exemplo de endpoints com limites diferentes: _______

### 4.2 Tratamento de Limites

- [ ] **Como é informado quando limite é atingido?**
  - Status HTTP: [ ] 429 Too Many Requests [ ] Outro: _______
  - Header de resposta: `_______` (ex: `X-RateLimit-Remaining`)

- [ ] **Headers informativos sobre rate limit:**
  - `X-RateLimit-Limit`: _______
  - `X-RateLimit-Remaining`: _______
  - `X-RateLimit-Reset`: _______

- [ ] **Retry-After header fornecido?**
  - [ ] Sim [ ] Não

- [ ] **Recomendação de retry strategy:**
  - Exponential backoff? [ ] Sim [ ] Não
  - Delay recomendado: _______

---

## 5. ENDPOINTS PRINCIPAIS

### 5.1 Gestão de Cotações (RFQ)

**Criar/Enviar Cotação:**
- [ ] **Endpoint:**
  - Método: [ ] POST [ ] PUT
  - URL: `_______`
  - Exemplo: `POST /api/v1/rfq`

- [ ] **Payload de exemplo:**
  ```json
  {
    // Solicitar exemplo completo
  }
  ```

- [ ] **Campos obrigatórios:**
  - _______

- [ ] **Resposta de sucesso:**
  - Status: [ ] 201 [ ] 200
  - Retorna: [ ] ID da cotação [ ] Objeto completo

**Listar Cotações:**
- [ ] **Endpoint:**
  - Método: [ ] GET
  - URL: `_______`

- [ ] **Parâmetros de filtro disponíveis:**
  - [ ] status (ativa, fechada, cancelada)
  - [ ] data_criacao
  - [ ] cliente_id
  - [ ] Outros: _______

- [ ] **Paginação:**
  - Como funciona? [ ] Offset/Limit [ ] Cursor-based [ ] Page number
  - Tamanho máximo de página: _______

**Obter Detalhes de uma Cotação:**
- [ ] **Endpoint:**
  - Método: [ ] GET
  - URL: `_______`
  - Exemplo: `GET /api/v1/rfq/{rfq_id}`

**Atualizar Cotação:**
- [ ] **Endpoint:**
  - Método: [ ] PUT [ ] PATCH
  - URL: `_______`

- [ ] **Quais campos podem ser atualizados?**
  - _______

**Cancelar Cotação:**
- [ ] **Endpoint:**
  - Método: [ ] DELETE [ ] POST [ ] PUT
  - URL: `_______`

### 5.2 Propostas de Fornecedores

**Listar Propostas de uma Cotação:**
- [ ] **Endpoint:**
  - Método: [ ] GET
  - URL: `_______`
  - Exemplo: `GET /api/v1/rfq/{rfq_id}/proposals`

- [ ] **Estrutura da proposta:**
  - Campos retornados: _______
  - Inclui histórico de alterações? [ ] Sim [ ] Não

**Aceitar/Rejeitar Proposta:**
- [ ] **Endpoint:**
  - Método: [ ] POST [ ] PUT
  - URL: `_______`

### 5.3 Pedidos de Compra (Purchase Orders)

**Criar Pedido:**
- [ ] **Endpoint:**
  - Método: [ ] POST
  - URL: `_______`

- [ ] **Campos obrigatórios:**
  - _______

- [ ] **Pode criar PO a partir de cotação aprovada?**
  - [ ] Sim, automaticamente
  - [ ] Sim, via endpoint específico
  - [ ] Não, precisa ser manual

**Consultar Status de Pedido:**
- [ ] **Endpoint:**
  - Método: [ ] GET
  - URL: `_______`

- [ ] **Status possíveis:**
  - [ ] Aguardando confirmação
  - [ ] Confirmado
  - [ ] Em separação
  - [ ] Enviado
  - [ ] Entregue
  - [ ] Cancelado
  - Outros: _______

### 5.4 Dados Mestres

**Fornecedores (Vendors):**
- [ ] **Listar fornecedores:**
  - Endpoint: `_______`

- [ ] **Criar/Atualizar fornecedor:**
  - Endpoint: `_______`
  - Campos obrigatórios: _______

**Produtos (Items):**
- [ ] **Listar produtos do catálogo:**
  - Endpoint: `_______`

- [ ] **Buscar produto por SKU/EAN:**
  - Endpoint: `_______`

- [ ] **Sincronização de produtos:**
  - Como funciona? [ ] Push (enviamos) [ ] Pull (buscamos) [ ] Ambos

---

## 6. WEBHOOKS E NOTIFICAÇÕES

### 6.1 Disponibilidade

- [ ] **Webhooks disponíveis?**
  - [ ] Sim [ ] Não [ ] Roadmap futuro

### 6.2 Configuração (se disponível)

- [ ] **Eventos disponíveis para webhook:**
  - [ ] Nova cotação recebida
  - [ ] Proposta recebida
  - [ ] Cotação fechada
  - [ ] Pedido confirmado
  - [ ] Status de entrega atualizado
  - Outros: _______

- [ ] **Como configurar webhook?**
  - [ ] API
  - [ ] Portal de desenvolvedor
  - [ ] Solicitar ao suporte

- [ ] **Formato do payload de webhook:**
  - JSON Schema: _______

- [ ] **Segurança de webhook:**
  - [ ] HMAC signature
  - [ ] IP whitelist
  - [ ] Outro: _______

- [ ] **Retry de webhook em caso de falha?**
  - [ ] Sim (______ tentativas)
  - [ ] Não

### 6.3 Alternativa (se webhook não disponível)

- [ ] **Polling recomendado?**
  - Frequência máxima: _______ segundos
  - Endpoint para polling: `_______`

---

## 7. TRATAMENTO DE ERROS

### 7.1 Códigos HTTP

- [ ] **Códigos de sucesso:**
  - [ ] 200 OK
  - [ ] 201 Created
  - [ ] 204 No Content
  - Outros: _______

- [ ] **Códigos de erro do cliente (4xx):**
  - [ ] 400 Bad Request
  - [ ] 401 Unauthorized
  - [ ] 403 Forbidden
  - [ ] 404 Not Found
  - [ ] 422 Unprocessable Entity
  - [ ] 429 Too Many Requests
  - Outros: _______

- [ ] **Códigos de erro do servidor (5xx):**
  - [ ] 500 Internal Server Error
  - [ ] 503 Service Unavailable
  - Outros: _______

### 7.2 Estrutura de Erro

- [ ] **Formato de resposta de erro:**
  ```json
  {
    // Solicitar exemplo
  }
  ```

- [ ] **Campos de erro retornados:**
  - [ ] `error_code` (código da API)
  - [ ] `message` (mensagem legível)
  - [ ] `details` (array de erros específicos)
  - [ ] `field` (qual campo causou erro)
  - Outros: _______

- [ ] **Erros de validação:**
  - Como são estruturados? _______

### 7.3 Logs e Troubleshooting

- [ ] **Request ID para rastreamento:**
  - Header: `_______` (ex: `X-Request-ID`)
  - Gerado por: [ ] Cliente [ ] Servidor

- [ ] **Logs disponíveis no portal?**
  - [ ] Sim [ ] Não
  - Retenção: _______ dias

- [ ] **Como reportar bugs/problemas da API?**
  - Canal: _______
  - SLA de resposta: _______

---

## 8. PERFORMANCE E LIMITES

### 8.1 Timeouts

- [ ] **Timeout de conexão:**
  - Recomendado: _______ segundos

- [ ] **Timeout de leitura:**
  - Recomendado: _______ segundos

- [ ] **Operações longas (long-polling/async):**
  - [ ] Suportado [ ] Não suportado
  - Como funciona: _______

### 8.2 Tamanhos de Requisição

- [ ] **Tamanho máximo de request:**
  - _______ MB / KB

- [ ] **Tamanho máximo de response:**
  - _______ MB / KB

- [ ] **Limite de itens por cotação:**
  - _______ itens

- [ ] **Upload de arquivos suportado?**
  - [ ] Sim [ ] Não
  - Tamanho máximo: _______
  - Formatos aceitos: _______

### 8.3 Batch Operations

- [ ] **Operações em lote suportadas?**
  - [ ] Sim [ ] Não

- [ ] **Endpoints de batch:**
  - Exemplo: `_______`
  - Limite por batch: _______

---

## 9. AMBIENTES

### 9.1 Ambientes Disponíveis

- [ ] **Sandbox/Homologação:**
  - URL: _______________
  - Credenciais: _______
  - Diferenças vs produção: _______

- [ ] **Produção:**
  - URL: _______________
  - Processo de obter credenciais: _______

### 9.2 Dados de Teste

- [ ] **Fornecedores de teste disponíveis?**
  - [ ] Sim [ ] Não
  - IDs/CNPJs fictícios: _______

- [ ] **Produtos de teste disponíveis?**
  - [ ] Sim [ ] Não
  - SKUs fictícios: _______

- [ ] **Pode criar dados de teste via API?**
  - [ ] Sim [ ] Não

---

## 10. MAPEAMENTO DE DADOS

### 10.1 Formatos e Conversões

- [ ] **Formato de datas:**
  - [ ] ISO 8601 (ex: `2026-01-29T14:00:00Z`)
  - [ ] Unix timestamp
  - [ ] Outro: _______

- [ ] **Timezone:**
  - [ ] UTC
  - [ ] America/Sao_Paulo
  - Outro: _______

- [ ] **Formato de moeda:**
  - [ ] BRL
  - [ ] USD
  - Outro: _______
  - Como são representados valores monetários? (ex: `100.50` ou `10050`)

- [ ] **Formato de números decimais:**
  - Separador decimal: [ ] `.` (ponto) [ ] `,` (vírgula)
  - Separador de milhar: _______

### 10.2 Unidades de Medida

- [ ] **Unidades suportadas:**
  - [ ] UN (unidade)
  - [ ] CX (caixa)
  - [ ] FR (frasco)
  - [ ] KG, L, etc.
  - Outros: _______

- [ ] **Conversão de unidades:**
  - Feita pela API? [ ] Sim [ ] Não
  - Cliente deve fazer? [ ] Sim [ ] Não

### 10.3 Identificadores

- [ ] **Identificadores únicos utilizados:**
  - Cotação: _______
  - Pedido: _______
  - Fornecedor: _______
  - Produto: [ ] SKU [ ] EAN [ ] ID interno [ ] Outro: _______

- [ ] **UUIDs ou IDs numéricos?**
  - _______

---

## 11. COMPLIANCE E REGULAMENTAÇÃO

### 11.1 LGPD

- [ ] **Dados pessoais processados pela API:**
  - Quais? _______

- [ ] **Base legal para tratamento:**
  - _______

- [ ] **DPO (Data Protection Officer):**
  - Contato: _______

### 11.2 Auditoria

- [ ] **Logs de auditoria disponíveis?**
  - [ ] Sim [ ] Não
  - Retenção: _______ meses
  - Endpoint: `_______`

- [ ] **Rastreabilidade de alterações:**
  - [ ] Sim (quem, quando, o quê)
  - [ ] Não

---

## 12. SUPORTE E SLA

### 12.1 Canais de Suporte

- [ ] **Suporte técnico:**
  - Email: _______________
  - Telefone: _______________
  - [ ] Slack [ ] Teams [ ] Portal
  - URL do portal de suporte: _______________

- [ ] **Horário de atendimento:**
  - _______ às _______ (fuso: _______)
  - [ ] 24/7 [ ] Comercial [ ] Outro: _______

### 12.2 SLA

- [ ] **SLA de disponibilidade da API:**
  - Uptime: _______% (ex: 99.9%)

- [ ] **Janela de manutenção:**
  - Quando ocorre? _______
  - Comunicado com antecedência? [ ] Sim (______ dias) [ ] Não

- [ ] **SLA de resposta a incidentes:**
  - Crítico: _______ horas
  - Alto: _______ horas
  - Médio: _______ horas
  - Baixo: _______ horas

### 12.3 Status da API

- [ ] **Página de status disponível?**
  - URL: _______________
  - [ ] Histórico de incidentes
  - [ ] Notificações por email/SMS

---

## 13. INTEGRAÇÕES EXISTENTES

### 13.1 Casos de Sucesso

- [ ] **Clientes que já integraram Bionexo com ERP:**
  - Qual ERP? [ ] SAP [ ] TOTVS [ ] NetSuite [ ] Outro: _______

- [ ] **Podemos falar com algum cliente referência?**
  - [ ] Sim [ ] Não
  - Contato: _______

### 13.2 Parceiros de Integração

- [ ] **Parceiros certificados para integração:**
  - Empresa: _______
  - Contato: _______

- [ ] **Bionexo oferece serviço de integração?**
  - [ ] Sim [ ] Não
  - Custo: _______

---

## 14. ROADMAP E FUTURO

### 14.1 Novos Recursos

- [ ] **Recursos em roadmap que podem nos ajudar:**
  - _______

- [ ] **Breaking changes previstos?**
  - [ ] Sim (quando: _______) [ ] Não

### 14.2 Feedback

- [ ] **Como podemos sugerir melhorias na API?**
  - _______

- [ ] **Programa de early adopters/beta testers:**
  - [ ] Sim [ ] Não

---

## 15. QUESTÕES ESPECÍFICAS NETSUÍTE

### 15.1 Integrações Conhecidas

- [ ] **Bionexo já integrou com NetSuite antes?**
  - [ ] Sim [ ] Não
  - Quantos clientes: _______

- [ ] **SuiteApp/Bundle disponível?**
  - [ ] Sim (Bundle ID: _______) [ ] Não

- [ ] **Recomendações específicas para NetSuite:**
  - [ ] SuiteScript RESTlet
  - [ ] SuiteTalk (SOAP)
  - [ ] Middleware externo
  - Outro: _______

### 15.2 Mapeamento NetSuite

- [ ] **Campos NetSuite que precisam mapear:**
  - Transaction (Purchase Order): _______
  - Vendor: _______
  - Item: _______

- [ ] **Custom Fields do NetSuite:**
  - Como tratar? _______

---

## RESUMO - TOP 10 PERGUNTAS CRÍTICAS

**Se o tempo for curto, priorize estas:**

1. [ ] **Onde está a documentação da API e como acessar sandbox?**
2. [ ] **Qual o modelo de autenticação e como obter credenciais?**
3. [ ] **Quais são os rate limits (req/min, req/hora)?**
4. [ ] **Webhooks disponíveis ou precisamos fazer polling?**
5. [ ] **Endpoints principais: criar cotação, listar propostas, criar PO**
6. [ ] **Formato de datas, moedas e timezone utilizados**
7. [ ] **Como são retornados os erros? (estrutura de error response)**
8. [ ] **Existe SDK/biblioteca ou Postman Collection?**
9. [ ] **SLA de suporte e canal de comunicação direto com time técnico**
10. [ ] **Algum cliente já integrou NetSuite + Bionexo? Podemos ver exemplo?**

---

## AÇÕES PÓS-REUNIÃO

**Baseado nas respostas, definir:**

- [ ] Arquitetura de integração: [ ] Direta [ ] Middleware
- [ ] Linguagem de desenvolvimento: [ ] Python [ ] Node.js [ ] SuiteScript [ ] Outro: _______
- [ ] Responsável desenvolvimento: _______
- [ ] Cronograma: Sprint 1 inicia em: _______
- [ ] Próxima reunião técnica: _______

---

**Última atualização:** 2026-01-29
**Responsável:** Pedro (Inteligência Comercial)
**Status:** Aguardando reunião
