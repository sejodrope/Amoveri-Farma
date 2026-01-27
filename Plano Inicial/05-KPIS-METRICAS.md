# KPIs e Métricas - Área Comercial

**Última atualização:** 2026-01-26

---

## Índice
1. [[#KPIs de Vendas]]
2. [[#KPIs de Performance Comercial]]
3. [[#KPIs de Produto]]
4. [[#KPIs de Cliente]]
5. [[#KPIs Operacionais]]
6. [[#KPIs Farmacêutico-Específicos]]

---

## KPIs de Vendas

### 1. Faturamento Bruto
**Descrição:** Valor total das vendas antes de impostos e descontos
**Fórmula:** `SUM(faturamento_bruto) WHERE cfop IN ('6.108', '5.405', ...)`
**Fonte de dados:** NetSuite - BASE VENDAS
**Frequência:** Diário
**Segmentações:**
- Por Regional
- Por Fabricante
- Por Categoria de Produto
- Por Vendedor

**Meta:** R$ ________ (mensal)
**Dashboard:** Gráfico de linha (evolução diária) + Card com valor acumulado do mês

---

### 2. Faturamento Líquido
**Descrição:** Faturamento após descontos e impostos
**Fórmula:** `faturamento_bruto - desconto - valor_icms - valor_impostos`
**Fonte de dados:** NetSuite
**Frequência:** Diário

**Meta:** R$ ________ (mensal)
**Dashboard:** Card + comparação com mês anterior

---

### 3. Atingimento de Meta
**Descrição:** Percentual de atingimento da meta de vendas
**Fórmula:** `(faturamento_realizado / meta) * 100`
**Fonte de dados:** NetSuite (realizado) + Excel SharePoint (meta)
**Frequência:** Diário
**Segmentações:**
- Por Vendedor
- Por Regional
- Por Produto

**Meta:** 100%
**Dashboard:** Gauge chart + tabela de ranking de vendedores

---

### 4. Ticket Médio
**Descrição:** Valor médio por transação de venda
**Fórmula:** `faturamento_total / numero_de_vendas`
**Fonte de dados:** NetSuite
**Frequência:** Semanal

**Meta:** R$ ________
**Dashboard:** KPI card + tendência

---

### 5. Crescimento vs Período Anterior
**Descrição:** Crescimento percentual em relação ao mesmo período do ano anterior
**Fórmula:** `((vendas_atual - vendas_ano_anterior) / vendas_ano_anterior) * 100`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Meta:** +15% YoY
**Dashboard:** Gráfico de barras comparativo

---

## KPIs de Performance Comercial

### 6. Margem de Contribuição
**Descrição:** Percentual de lucro após custos variáveis
**Fórmula:** `((faturamento - custo_produto - comissao - frete) / faturamento) * 100`
**Fonte de dados:** NetSuite + Planilha de custos
**Frequência:** Mensal
**Segmentações:**
- Por Fabricante
- Por Produto
- Por Regional

**Meta:** > 25%
**Dashboard:** Gráfico de barras por fabricante

---

### 7. Comissão Total
**Descrição:** Valor total de comissões pagas aos vendedores
**Fórmula:** Baseado na tabela de comissões (% sobre venda)
**Fonte de dados:** NetSuite + Excel (tabela comissão)
**Frequência:** Mensal

**Meta:** ≤ 5% do faturamento
**Dashboard:** Tabela por vendedor + total geral

---

### 8. Taxa de Conversão
**Descrição:** Percentual de propostas convertidas em vendas
**Fórmula:** `(vendas_fechadas / propostas_enviadas) * 100`
**Fonte de dados:** CRM / NetSuite
**Frequência:** Mensal

**Meta:** > 40%
**Dashboard:** Funil de vendas

---

### 9. Tempo Médio de Fechamento
**Descrição:** Tempo médio entre proposta e venda fechada
**Fórmula:** `AVG(data_venda - data_proposta)`
**Fonte de dados:** CRM / NetSuite
**Frequência:** Mensal

**Meta:** < 15 dias
**Dashboard:** Histograma de distribuição

---

## KPIs de Produto

### 10. Top 10 Produtos (Faturamento)
**Descrição:** Produtos que mais faturam
**Fórmula:** `SUM(faturamento) GROUP BY produto ORDER BY DESC LIMIT 10`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Dashboard:** Gráfico de barras horizontal

---

### 11. Curva ABC de Produtos
**Descrição:** Classificação de produtos por importância no faturamento
**Fórmula:**
- A: 80% do faturamento
- B: 15% do faturamento
- C: 5% do faturamento
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Dashboard:** Gráfico de Pareto

---

### 12. Produtos com Baixa Performance
**Descrição:** Produtos abaixo da meta de vendas
**Fórmula:** `vendas_produto < 50% da meta`
**Fonte de dados:** NetSuite + Metas
**Frequência:** Mensal

**Dashboard:** Tabela de alerta

---

### 13. Mix de Produtos
**Descrição:** Distribuição de vendas por categoria/fabricante
**Fórmula:** `(faturamento_categoria / faturamento_total) * 100`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Dashboard:** Gráfico de pizza ou treemap

---

## KPIs de Cliente

### 14. Top 10 Clientes
**Descrição:** Clientes que mais compram
**Fórmula:** `SUM(faturamento) GROUP BY cliente ORDER BY DESC LIMIT 10`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Dashboard:** Tabela + gráfico de barras

---

### 15. Churn de Clientes
**Descrição:** Taxa de clientes que pararam de comprar
**Fórmula:** `(clientes_que_nao_compraram_ultimos_90_dias / total_clientes_ativos) * 100`
**Fonte de dados:** NetSuite
**Frequência:** Trimestral

**Meta:** < 5%
**Dashboard:** KPI card + lista de clientes em risco

---

### 16. Frequência de Compra
**Descrição:** Número médio de compras por cliente
**Fórmula:** `total_vendas / total_clientes_unicos`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Meta:** > 2 compras/mês
**Dashboard:** Histograma

---

### 17. Segmentação Regional
**Descrição:** Faturamento por região geográfica
**Fórmula:** `SUM(faturamento) GROUP BY regiao`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Dashboard:** Mapa de calor do Brasil + tabela

---

## KPIs Operacionais

### 18. Taxa de Devolução
**Descrição:** Percentual de produtos devolvidos
**Fórmula:** `(valor_devolvido / faturamento_bruto) * 100`
**Fonte de dados:** NetSuite (CFOP de devolução)
**Frequência:** Mensal

**Meta:** < 2%
**Dashboard:** Gráfico de linha + alerta se > 3%

---

### 19. Prazo Médio de Entrega
**Descrição:** Tempo médio entre venda e entrega
**Fórmula:** `AVG(data_entrega - data_venda)`
**Fonte de dados:** NetSuite
**Frequência:** Semanal

**Meta:** < 5 dias úteis
**Dashboard:** KPI card + evolução semanal

---

### 20. Acurácia de Estoque
**Descrição:** Diferença entre estoque físico e sistema
**Fórmula:** `(estoque_sistema - estoque_fisico) / estoque_sistema * 100`
**Fonte de dados:** NetSuite + Inventário físico
**Frequência:** Mensal (após inventário)

**Meta:** > 98%
**Dashboard:** Gauge + lista de divergências

---

## KPIs Farmacêutico-Específicos

### 21. Ruptura de Produtos Críticos
**Descrição:** Produtos oncológicos/críticos em falta
**Fórmula:** `COUNT(produtos WHERE estoque = 0 AND categoria = 'Oncológico')`
**Fonte de dados:** NetSuite
**Frequência:** Diário

**Meta:** 0 produtos em ruptura
**Dashboard:** Alerta vermelho + lista de produtos

---

### 22. Produtos Próximos do Vencimento
**Descrição:** Produtos com validade < 90 dias
**Fórmula:** `SELECT * WHERE data_validade < DATEADD(day, 90, GETDATE())`
**Fonte de dados:** NetSuite (se rastreado por lote)
**Frequência:** Semanal

**Meta:** < 5% do estoque
**Dashboard:** Tabela de alerta + valor em risco

---

### 23. Compliance de Medicamentos Controlados
**Descrição:** Vendas de medicamentos da Portaria 344 com receita válida
**Fórmula:** `(vendas_com_receita / total_vendas_controlados) * 100`
**Fonte de dados:** NetSuite + Sistema de controle de receitas
**Frequência:** Mensal

**Meta:** 100%
**Dashboard:** Gauge + relatório de exceções

---

### 24. Cobertura de Estoque (Dias)
**Descrição:** Quantos dias o estoque atual aguenta com base na venda média
**Fórmula:** `estoque_atual / media_vendas_diarias_ultimos_30_dias`
**Fonte de dados:** NetSuite
**Frequência:** Diário

**Meta:** 15-30 dias (ideal)
**Dashboard:** Gráfico de barras por produto + alertas

---

### 25. Giro de Estoque
**Descrição:** Quantas vezes o estoque é renovado no período
**Fórmula:** `custo_mercadorias_vendidas / estoque_medio`
**Fonte de dados:** NetSuite
**Frequência:** Mensal

**Meta:** > 4x ao ano (para oncológicos de alto valor)
**Dashboard:** KPI card por categoria de produto

---

## Matriz de Priorização de KPIs

| # | KPI | Impacto | Facilidade | Prioridade | Status |
|---|-----|---------|------------|------------|--------|
| 1 | Faturamento Bruto | Alta | Alta | 🔥 Crítico | 🔴 Pendente |
| 3 | Atingimento de Meta | Alta | Média | 🔥 Crítico | 🔴 Pendente |
| 21 | Ruptura Críticos | Alta | Média | 🔥 Crítico | 🔴 Pendente |
| 2 | Faturamento Líquido | Alta | Média | ⭐ Alto | 🔴 Pendente |
| 6 | Margem Contribuição | Alta | Baixa | ⭐ Alto | 🔴 Pendente |
| ... | ... | ... | ... | ... | ... |

**Legenda:**
- 🔥 Crítico - Implementar primeiro (Fase 1)
- ⭐ Alto - Segunda fase
- 📋 Médio - Terceira fase
- 💡 Baixo - Backlog futuro

---

## Dashboards Planejados

### Dashboard 1: Visão Executiva (Diário)
**Público:** Diretoria Comercial
**Atualização:** 3x ao dia
**KPIs incluídos:**
- [ ] Faturamento Bruto do Dia/Mês
- [ ] Atingimento de Meta (%)
- [ ] Top 5 Vendedores
- [ ] Top 5 Produtos
- [ ] Alertas de Ruptura

---

### Dashboard 2: Performance por Regional (Semanal)
**Público:** Gerentes Regionais
**Atualização:** Diária
**KPIs incluídos:**
- [ ] Faturamento por Região
- [ ] Ranking de vendedores da região
- [ ] Mix de produtos
- [ ] Taxa de devolução

---

### Dashboard 3: Análise de Produtos (Mensal)
**Público:** Compras / Supply Chain
**Atualização:** Semanal
**KPIs incluídos:**
- [ ] Curva ABC
- [ ] Giro de estoque
- [ ] Produtos próximos vencimento
- [ ] Cobertura de estoque por produto

---

### Dashboard 4: Financeiro (Mensal)
**Público:** Financeiro / Controladoria
**Atualização:** Mensal
**KPIs incluídos:**
- [ ] Margem de contribuição
- [ ] Comissões totais
- [ ] Inadimplência (se aplicável)
- [ ] Análise de rentabilidade

---

## Cálculos Complexos

### Cálculo de Meta Proporcional
```sql
-- Meta ajustada por dias úteis do mês
DECLARE @dias_uteis_mes INT = 22
DECLARE @dia_atual INT = 15
DECLARE @meta_mensal DECIMAL(18,2) = 10000000

SELECT
    @meta_mensal / @dias_uteis_mes * @dia_atual AS meta_proporcional
```

### Cálculo de Margem por Produto
```sql
SELECT
    produto,
    SUM(faturamento) AS faturamento_total,
    SUM(custo_produto) AS custo_total,
    (SUM(faturamento) - SUM(custo_produto)) / SUM(faturamento) * 100 AS margem_pct
FROM vendas
WHERE data >= DATEADD(month, -1, GETDATE())
GROUP BY produto
ORDER BY margem_pct DESC
```

### Identificação de Churn
```sql
-- Clientes que não compraram nos últimos 90 dias mas eram ativos
SELECT
    c.cliente_id,
    c.nome,
    MAX(v.data_venda) AS ultima_compra,
    DATEDIFF(day, MAX(v.data_venda), GETDATE()) AS dias_sem_comprar
FROM clientes c
LEFT JOIN vendas v ON c.cliente_id = v.cliente_id
WHERE v.data_venda < DATEADD(day, -90, GETDATE())
  AND c.status = 'Ativo'
GROUP BY c.cliente_id, c.nome
ORDER BY dias_sem_comprar DESC
```

---

## Referências e Fontes

**Documentação NetSuite:**
-

**Planilhas de Metas:**
- SharePoint:

**Tabelas de Comissão:**
- SharePoint:

---

## Links Relacionados
- [[00-INDICE]] - Índice principal
- [[01-CHECKLIST-LEVANTAMENTO]] - Perguntas sobre KPIs
- [[04-REQUISITOS-TECNICOS]] - Infraestrutura para calcular esses KPIs

---

#kpis #metricas #dashboards #indicadores
