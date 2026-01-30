# Resumo Executivo - Integração Bionexo x NetSuite

**Apresentação para abertura da reuniao de kickoff**

---

## O Problema

**Situacao Atual:**
- Nao temos tabela de precos integrada com a Bionexo
- Precificacao e feita manualmente (Excel/planilhas) a cada cotacao
- Analista precisa consultar custo, ICMS, OL, PMC separadamente
- Precos variam por estado (UF), laboratorio e tipo de operacao

**Impacto:**
- Tempo excessivo por cotacao (consultas manuais)
- Risco de erro no calculo de impostos (ICMS-ST)
- Risco de ultrapassar PMC (multa Anvisa)
- Impossibilidade de escalar volume de cotacoes

---

## A Solucao

**Bionexo enxergando precos do NetSuite automaticamente**

```
ANTES (Manual):
Cotacao chega -> Analista consulta custo -> Calcula ICMS -> Verifica PMC -> Digita preco na Bionexo
[Processo manual, propenso a erros]

DEPOIS (Automatizado):
Tabela de precos (Produto x UF x Lab) -> API -> Bionexo consulta automaticamente
[Precos pre-calculados, validados contra PMC]
```

**Direcao principal:** NetSuite -> Bionexo (precos)
**Direcao secundaria:** Bionexo -> NetSuite (pedidos aceitos)

---

## Pre-requisito Critico

**NAO TEMOS tabela de precos no NetSuite hoje.**

Antes de integrar com Bionexo, precisamos:
1. Criar estrutura de tabela de precos no NetSuite
2. Montar matriz tributaria (NCM x UF) com Thiago
3. Popular tabela com precos calculados e validados contra PMC

**Dimensoes da tabela:** Produto x UF (27 estados) x Laboratorio (4-5 principais)

---

## Escopo da Integracao

### Fase 1: Tabela de Precos
- Criar estrutura no NetSuite (Kamila)
- Montar matriz tributaria (Thiago)
- Popular e validar contra PMC

### Fase 2: Middleware + Integracao
- Motor de precificacao local (Python)
- Conectar com API Bionexo
- Piloto com 10-20 produtos, 1-2 UFs, 1 laboratorio

### Fase 3: Producao
- Expandir para todos os produtos, UFs e laboratorios

---

## O Que Precisamos Descobrir na Reuniao

### 1. Tecnico (Especialistas Bionexo)
- Como funciona a API de precos?
- Documentacao e sandbox disponiveis?
- Autenticacao e rate limits?
- Como enviar tabela de precos? (endpoint, formato, batch?)

### 2. Processo (Gisele)
- Qual formato a Bionexo espera para tabela de precos?
- Frequencia de atualizacao suportada?
- Casos de sucesso com NetSuite?

### 3. Mapeamento (Todos)
- Como mapear produtos? (EAN como chave?)
- Como mapear fornecedores? (CNPJ?)
- Como tratar precos por UF na API?

---

## Nosso Time

**Amoveri Pontual:**
- **Pedro** (Inteligencia Comercial) - Tech Lead
- **Kamila** (TI NetSuite) - Especialista NetSuite
- **Bruna** (Comercial) - Dona do Processo

**Bionexo:**
- **Gisele** - Gestora de Contas
- **Especialistas** - Time Tecnico

---

## Proximos Passos (Apos Reuniao)

**Imediato (24h):**
- Ata documentada e distribuida
- Acesso a sandbox e documentacao da API

**Semana 1:**
- Coletar inputs de Thiago (matriz tributaria)
- Definir estrutura da tabela de precos com Kamila
- Primeiras chamadas de API (autenticacao)

**Semana 2:**
- Tabela de precos piloto criada
- Primeiro envio de precos teste para sandbox Bionexo

---

## Perguntas Top 3

1. **Onde esta a documentacao da API de precos e como acessar sandbox?**
2. **Qual o formato esperado para envio de tabela de precos? (campos, estrutura)**
3. **Ja tem algum cliente com NetSuite integrado? Podemos ver exemplo?**

---

## Expectativas

**Sair desta reuniao com:**
- Documentacao da API em maos
- Acesso a sandbox configurado
- Entendimento do formato de envio de precos
- Cronograma inicial acordado
- Responsaveis definidos
- Proxima reuniao agendada

---

*Documentacao completa disponivel em:*
*[integrations/bionexo-netsuite/docs](../)*
