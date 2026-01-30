# Checklist de Levantamento - Área Comercial

**Objetivo:** Guiar as reuniões com analistas para extrair informações necessárias para automação e dashboards.

---

## 1. Fonte de Dados (NetSuite/Oracle)

### 1.1 Acesso e Extração
- [ ] Como os dados são extraídos hoje? (manual/automatizado)
- [ ] Qual a frequência de extração necessária? (diária/semanal/mensal)
- [ ] Existe acesso ao **SuiteAnalytics Connect** (ODBC/JDBC)?
- [ ] Temos credenciais para usar a API **SuiteTalk**?
- [ ] Quem é o responsável técnico pelo NetSuite na empresa?
- [ ] Existem limites de API ou restrições de acesso?

### 1.2 Relatórios Existentes
- [ ] Qual o nome oficial do relatório principal? (ex: CTR - BASE VENDAS DRE GERENCIAL)
- [ ] Este relatório é a "fonte única da verdade" (Source of Truth)?
- [ ] Os valores batem com a contabilidade?
- [ ] O relatório sofre alterações retroativas? (correções de vendas passadas)
- [ ] Existe documentação sobre as colunas e cálculos?

### 1.3 Granularidade dos Dados
- [ ] Qual o menor nível de detalhe disponível? (por item, por nota, por linha?)
- [ ] Qual o histórico disponível? (quantos anos de dados?)
- [ ] Existe auditoria/log de alterações nos dados?

---

## 2. Entendimento das Colunas (BASE VENDAS)

### 2.1 Campos Críticos
**Anotar para cada campo:**

#### CFOP (Código Fiscal de Operações)
- [ ] Quais CFOPs representam "venda efetiva" para metas? (6.108, 6.119, 5.405, etc.)
- [ ] Quais devem ser EXCLUÍDOS? (remessa, doação, transferência)
- [ ] Como tratar devoluções? (CFOP específico?)

#### Data
- [ ] Qual data usar como referência: Emissão, Saída ou Entrega?
- [ ] Como tratar vendas com entrega futura?
- [ ] Existe diferença entre data contábil e data comercial?

#### Cliente
- [ ] A coluna "CLIENTE: TAREFA" está sempre preenchida?
- [ ] Precisamos fazer de-para ou normalização de nomes?
- [ ] Existem clientes duplicados no sistema?
- [ ] Como identificar cliente pessoa física vs jurídica?

#### Localidade
- [ ] A coluna "Região" (Sudeste, etc.) está sempre correta?
- [ ] Precisamos criar um de-para baseado em UF/Cidade?
- [ ] Existe hierarquia regional? (Regional > Território > Rota)

#### Produto/Item
- [ ] O código UPC é único e confiável?
- [ ] Como funciona a categorização de produtos?
- [ ] Existe curva ABC definida?
- [ ] Precisamos rastrear lote/validade de medicamentos?

#### Valores Financeiros
- [ ] "Faturamento Bruto" é o valor usado para metas?
- [ ] Como calcular o valor líquido? (descontar ICMS, impostos?)
- [ ] Onde estão os descontos aplicados?
- [ ] Como calcular margem de contribuição?

#### Fabricante
- [ ] A coluna "ITEM: FABRICANTE" tem todos os laboratórios mapeados?
- [ ] Existe categorização de laboratórios? (próprios vs parceiros)
- [ ] Precisamos de análise por fabricante nos dashboards?

---

## 3. Regras de Negócio e KPIs

### 3.1 Indicadores Principais
- [ ] Quais os 3 KPIs mais importantes que o time olha diariamente?
  - [ ] KPI 1: _________________ (como calcular?)
  - [ ] KPI 2: _________________ (como calcular?)
  - [ ] KPI 3: _________________ (como calcular?)

### 3.2 Metas e Objetivos
- [ ] Como as metas são definidas? (por vendedor, regional, produto?)
- [ ] Onde estão as metas armazenadas? (NetSuite, Excel, outro?)
- [ ] Qual a periodicidade de acompanhamento? (diário, semanal, mensal)
- [ ] Como calcular o % de atingimento de meta?

### 3.3 Segmentações Necessárias
- [ ] Dashboard precisa de visão por Regional/Território?
- [ ] Análise por Fabricante/Laboratório é relevante?
- [ ] Precisamos segregar por tipo de cliente? (hospital, clínica, particular)
- [ ] Análise por categoria de produto é necessária?

### 3.4 Cálculos Específicos
- [ ] Como calcular margem de contribuição?
- [ ] Como tratar devoluções? (aparecem negativas ou relatório separado?)
- [ ] Existe cálculo de comissão? (onde está a regra?)
- [ ] Como calcular ticket médio?
- [ ] Como calcular ruptura de estoque?

---

## 4. Integração com Microsoft 365

### 4.1 Dados Complementares
- [ ] Existe alguma informação crítica que NÃO está no NetSuite?
- [ ] Quais planilhas Excel são usadas como "base de dados" paralela?
  - [ ] Metas dos vendedores
  - [ ] Categorização especial de clientes
  - [ ] Tabelas de comissão
  - [ ] Preços especiais
  - [ ] Outras: _________________
- [ ] Onde ficam armazenadas? (SharePoint, OneDrive, local?)

### 4.2 Ferramentas de Análise
- [ ] Qual ferramenta preferida para dashboards? (Power BI, Excel, outro)
- [ ] Já existe infraestrutura de Power BI na empresa?
- [ ] Quem são os usuários dos dashboards? (vendedores, gerentes, diretores)
- [ ] Preferem relatórios automáticos por e-mail/Teams?

### 4.3 SharePoint/OneDrive
- [ ] Existe estrutura de pastas padronizada?
- [ ] Precisamos integrar com SharePoint para buscar arquivos?
- [ ] Como é feita a governança de dados hoje?

---

## 5. Processos Atuais (Identificar Gargalos)

### 5.1 Rotina Diária/Semanal
- [ ] Qual a primeira tarefa do dia relacionada a dados?
- [ ] Quanto tempo é gasto "preparando" dados para análise?
- [ ] Qual a tarefa mais repetitiva e manual?
- [ ] Quais relatórios são gerados manualmente toda semana/mês?

### 5.2 Dores e Problemas
- [ ] Qual o maior problema com os dados hoje?
  - [ ] Dados incorretos/desatualizados
  - [ ] Processo manual demorado
  - [ ] Falta de visibilidade em tempo real
  - [ ] Dificuldade de consolidar múltiplas fontes
  - [ ] Outro: _________________
- [ ] O que faria o maior impacto se fosse automatizado?
- [ ] Existe algum processo que "trava" a análise hoje?

### 5.3 Exceções e Tratamentos
- [ ] Como são tratadas vendas canceladas?
- [ ] Como funciona o processo de devolução?
- [ ] Existe venda em consignação?
- [ ] Como tratar vendas para matriz/filial?

---

## 6. Requisitos Técnicos

### 6.1 Infraestrutura
- [ ] Existe servidor/ambiente para rodar pipelines de dados?
- [ ] Temos banco de dados próprio? (SQL Server, PostgreSQL, outro)
- [ ] Podemos usar Azure/AWS/GCP para processamento?
- [ ] Qual o orçamento disponível para ferramentas?

### 6.2 Segurança e Compliance
- [ ] Quais dados são sensíveis? (LGPD, dados de saúde?)
- [ ] Existem restrições de acesso por usuário?
- [ ] Precisamos de auditoria de acesso aos dados?
- [ ] Como fazer backup e recuperação?

### 6.3 Cronograma
- [ ] Existe urgência para algum dashboard específico?
- [ ] Qual a prioridade: automação ou dashboards?
- [ ] Existe algum evento importante próximo? (fechamento, reunião diretoria)

---

## 7. Farmacêutico Específico

### 7.1 Regulatório
- [ ] Precisamos rastrear número de lote dos medicamentos?
- [ ] Como controlar produtos próximos da validade?
- [ ] Existe controle de medicamentos especiais? (portaria 344, oncológicos)
- [ ] Como funciona o processo de logística reversa?

### 7.2 Estoque
- [ ] Precisamos cruzar vendas com estoque atual?
- [ ] Como calcular cobertura de estoque (dias de venda)?
- [ ] Existe previsão de demanda hoje? Como é feita?
- [ ] Como identificar ruptura de produtos críticos?

---

## Observações e Insights
_(Espaço para anotar insights durante as reuniões)_

---

**Última atualização:** 2026-01-26
**Próximo passo:** Usar [[02-TEMPLATE-REUNIAO]] para cada conversa

#checklist #levantamento #perguntas
