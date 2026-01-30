# Inicio Rapido - Integracao Bionexo x NetSuite

**Guia rapido para comecar**

---

## Voce esta aqui

Reuniao de kickoff com Bionexo: **Segunda-feira, 14h**

---

## O Que Fazer AGORA (em ordem)

### 1. Ler o Indice
[docs/00-INDICE.md](docs/00-INDICE.md)

Entenda a estrutura da documentacao e qual documento e para voce.

### 2. Preencher Levantamento Interno (ate Domingo)
[docs/04-LEVANTAMENTO-INTERNO.md](docs/04-LEVANTAMENTO-INTERNO.md)

**Secoes por pessoa:**
- **Bruna**: Secoes 1, 2, 6, 8 (Processo, Volumes, Regras de Negocio, Treinamento)
- **Kamila**: Secao 3 (NetSuite completa)
- **Pedro**: Todas as outras + consolidacao final

### 3. Estudar Preparacao da Reuniao
[docs/01-PREPARACAO-REUNIAO.md](docs/01-PREPARACAO-REUNIAO.md)

Entenda:
- Agenda da reuniao
- Seu papel especifico
- O que perguntar

### 4. Ter em Maos na Reuniao
[docs/02-CHECKLIST-TECNICO-API.md](docs/02-CHECKLIST-TECNICO-API.md)

Use durante a reuniao para garantir que nada seja esquecido.

---

## Timeline

### Ate Domingo (Antes da Reuniao)
- [ ] Levantamento interno preenchido
- [ ] Validacoes com Bruna e Kamila feitas
- [ ] Credenciais Bionexo testadas (login manual)

### Segunda-feira, 14h (Reuniao)
- [ ] Abrir [RESUMO-EXECUTIVO.md](docs/RESUMO-EXECUTIVO.md) para apresentacao
- [ ] Usar [02-CHECKLIST-TECNICO-API.md](docs/02-CHECKLIST-TECNICO-API.md) para perguntas
- [ ] Preencher [03-TEMPLATE-ATA-REUNIAO.md](docs/03-TEMPLATE-ATA-REUNIAO.md)

### Ate Terca (Pos-Reuniao)
- [ ] Ata enviada para todos
- [ ] Acesso a sandbox obtido
- [ ] Documentacao da API baixada

---

## Estrutura de Documentos

```
integrations/bionexo-netsuite/
|
|-- INICIO-RAPIDO.md          <- VOCE ESTA AQUI
|-- README.md                 <- Visao geral do projeto
|
|-- docs/
|   |-- 00-INDICE.md                    <- Navegacao
|   |-- 01-PREPARACAO-REUNIAO.md        <- Guia completo
|   |-- 02-CHECKLIST-TECNICO-API.md     <- Perguntas tecnicas
|   |-- 03-TEMPLATE-ATA-REUNIAO.md      <- Documentar reuniao
|   |-- 04-LEVANTAMENTO-INTERNO.md      <- PREENCHER URGENTE
|   |-- 05-DIAGRAMAS-FLUXOS.md          <- Diagramas Mermaid
|   |-- 06-DICIONARIO-DADOS.md          <- Mapeamento de dados
|   |-- RESUMO-EXECUTIVO.md             <- Apresentacao reuniao
|   +-- GUIA-VISUAL-DIAGRAMAS.md        <- Como usar diagramas
```

---

## ESCOPO CORRETO da Integracao

**Bionexo precisa ENXERGAR os PRECOS do NetSuite.**

- Direcao: NetSuite -> Bionexo (precos)
- Pre-requisito: Criar tabela de precos (nao existe hoje)
- Dimensoes: Produto x UF (27 estados) x Laboratorio (4-5)

Ver detalhes em [PLANO-PROJETO.md](../../PLANO-PROJETO.md)

---

## Perguntas Top 3 para a Reuniao

1. **Onde esta a documentacao da API de precos e como acessar sandbox?**
2. **Qual o formato esperado para envio de tabela de precos?**
3. **Ja tem algum cliente com NetSuite integrado?**

---

## Contatos

**Amoveri Pontual:**
- Bruna (Comercial): bruna@amoverifarma.com.br
- Kamila (NetSuite): kamila@amoverifarma.com.br
- Pedro (Tech Lead): pedro@amoverifarma.com.br

**Bionexo:**
- Gisele (Gestora): [preencher na reuniao]

---

**Proximo passo:**
1. Abra [docs/00-INDICE.md](docs/00-INDICE.md)
2. Depois, abra [docs/04-LEVANTAMENTO-INTERNO.md](docs/04-LEVANTAMENTO-INTERNO.md)
3. Comece a preencher!
