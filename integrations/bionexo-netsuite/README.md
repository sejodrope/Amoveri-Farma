# Integração Bionexo x NetSuite

**Projeto:** Automação de Fluxo de Cotações
**Cliente:** Amoveri Pontual
**Responsável:** Pedro (Inteligência Comercial)
**Status:** Planejamento

---

## Visão Geral

Este projeto visa integrar o ERP NetSuite com a plataforma Bionexo via API, automatizando o fluxo completo de cotações e pedidos de compra.

### Objetivo
Reduzir tempo de processamento de cotações de **2 horas para 15 minutos**, eliminando entrada manual de dados e minimizando erros.

### Escopo
- Envio automático de cotações (RFQ) do NetSuite para Bionexo
- Retorno automático de propostas da Bionexo para NetSuite
- Criação automática de pedidos de compra (PO)
- Sincronização de dados mestres (fornecedores, produtos)

---

## Estrutura do Projeto

```
bionexo-netsuite/
├── docs/               # Documentação do projeto
│   ├── 01-PREPARACAO-REUNIAO.md      # Guia completo de preparação
│   ├── 02-CHECKLIST-TECNICO-API.md   # Perguntas técnicas sobre API
│   ├── 03-TEMPLATE-ATA-REUNIAO.md    # Template de ata
│   └── 04-LEVANTAMENTO-INTERNO.md    # Levantamento interno pré-reunião
├── specs/              # Especificações técnicas (após reunião)
├── tests/              # Testes e validações
├── config/             # Arquivos de configuração
├── logs/               # Logs de execução
└── README.md           # Este arquivo
```

---

## Próximos Passos

### Antes da Reunião (até Domingo)
- [ ] Preencher [04-LEVANTAMENTO-INTERNO.md](docs/04-LEVANTAMENTO-INTERNO.md)
- [ ] Validar informações com Bruna (Comercial)
- [ ] Validar informações com Kamila (TI NetSuite)
- [ ] Preparar diagrama de processo atual
- [ ] Testar credenciais Bionexo

### Reunião (Segunda-feira, 14h)
- [ ] Seguir agenda do [01-PREPARACAO-REUNIAO.md](docs/01-PREPARACAO-REUNIAO.md)
- [ ] Usar [02-CHECKLIST-TECNICO-API.md](docs/02-CHECKLIST-TECNICO-API.md)
- [ ] Documentar em [03-TEMPLATE-ATA-REUNIAO.md](docs/03-TEMPLATE-ATA-REUNIAO.md)

### Após Reunião (até Terça)
- [ ] Enviar ata para todos participantes
- [ ] Acessar sandbox da Bionexo
- [ ] Baixar documentação da API
- [ ] Configurar ambiente de desenvolvimento
- [ ] Fazer primeira chamada de API (autenticação)

---

## Documentos Principais

### Para Preparação
1. **[Preparação para Reunião](docs/01-PREPARACAO-REUNIAO.md)**
   - Agenda completa da reunião
   - Papéis e responsabilidades
   - Materiais necessários
   - Perguntas-chave por perfil

2. **[Checklist Técnico API](docs/02-CHECKLIST-TECNICO-API.md)**
   - Perguntas técnicas detalhadas sobre API Bionexo
   - Seções: Documentação, Arquitetura, Autenticação, Endpoints, etc.
   - Top 10 perguntas críticas destacadas

3. **[Levantamento Interno](docs/04-LEVANTAMENTO-INTERNO.md)**
   - Processo atual de cotações
   - Volumes e estatísticas
   - Configuração NetSuite
   - Regras de negócio
   - **IMPORTANTE: Preencher antes da reunião**

### Para Execução
4. **[Template de Ata](docs/03-TEMPLATE-ATA-REUNIAO.md)**
   - Estrutura para documentar reunião
   - Seções para decisões técnicas e de negócio
   - Action items e responsabilidades

---

## Participantes

### Reunião de Kickoff (Segunda, 14h)

**Bionexo:**
- Gisele - Gestora de Contas
- Especialistas de Integração

**Amoveri Pontual:**
- Bruna - Comercial
- Kamila - TI NetSuite
- Pedro - Inteligência Comercial (você)

---

## Tecnologias (Proposta Inicial)

**A definir após reunião com Bionexo:**
- Linguagem: Python / Node.js / SuiteScript
- Hospedagem: Azure / AWS / On-premise
- Banco de dados: PostgreSQL / MongoDB (se necessário)
- Monitoramento: Application Insights / Datadog

---

## Cronograma Preliminar

**Fase 1: Proof of Concept (PoC)**
- Duração: 2 semanas
- Entregável: 1 cotação criada e lida via API

**Fase 2: Piloto**
- Duração: 4 semanas
- Entregável: 10-20 cotações reais processadas

**Fase 3: Rollout Produção**
- Duração: 2 semanas
- Entregável: 100% das cotações automatizadas

**Total estimado:** 8-10 semanas

---

## Contatos

**Amoveri Pontual:**
- Pedro (Inteligência Comercial): pedro@amoverifarma.com.br
- Bruna (Comercial): bruna@amoverifarma.com.br
- Kamila (TI NetSuite): kamila@amoverifarma.com.br

**Bionexo:**
- Gisele (Gestora de Contas): [A PREENCHER NA REUNIÃO]
- Suporte Técnico: [A PREENCHER NA REUNIÃO]

---

## Recursos Úteis

**Documentação:**
- [NetSuite Help Center](https://system.netsuite.com/app/help/helpcenter.nl)
- [NetSuite SuiteTalk (Web Services)](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_1540391670.html)
- [Bionexo API Docs](https://api.bionexo.com/docs) - [A CONFIRMAR]

**Ferramentas:**
- [Postman](https://www.postman.com/) - Testar APIs
- [Draw.io](https://app.diagrams.net/) - Diagramas
- [DBeaver](https://dbeaver.io/) - Cliente SQL (se necessário)

---

## Notas

- **Confidencialidade:** Todos os documentos contêm informações sensíveis. Não compartilhar publicamente.
- **Credenciais:** Armazenar em cofre seguro (Azure Key Vault, 1Password, etc). Nunca versionar no Git.
- **Backup:** Fazer backup regular de documentação e código.

---

**Última atualização:** 2026-01-29
**Versão:** 1.0
