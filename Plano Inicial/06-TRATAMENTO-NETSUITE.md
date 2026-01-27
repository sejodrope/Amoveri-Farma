# Tratamento de Dados NetSuite - Relatório de Vendas

**Data:** 2026-01-27
**Relatório:** Base de Vendas - Janeiro/2026
**Status:** 🔴 Pendente validação com TI

---

## Problema Identificado

O relatório exportado do NetSuite apresenta fórmulas com arredondamento que precisam ser corrigidas para garantir precisão nos cálculos financeiros.

### Estrutura Atual das Colunas

| Coluna | Nome | Conteúdo | Observações |
|--------|------|----------|-------------|
| N | Desconto | Valor de desconto | Usado em cálculos |
| O | Jesoneracao | [A confirmar] | |
| P | [A definir] | Valor monetário | Usado em ADO TOTAL |
| Q | ADO TOTAL | Valor calculado | **COM ARREDONDAMENTO** |
| R | Pagamento Líquido | Valor final | Usa coluna P (incorreto) |
| S | Pedido | Número do pedido | |

---

## Correções Necessárias

### 1. Coluna Q - ADO TOTAL

**Problema:**
```excel
Fórmula atual: =ARRED(N2;2) + ARRED(P2;2)
```

- Arredondamento duplo causa perda de precisão
- Em grandes volumes, pequenas diferenças acumulam erros significativos

**Solução:**
```excel
Fórmula corrigida: = N2 + P2
```

**Justificativa:**
- O arredondamento deve ser feito apenas na apresentação final
- Cálculos intermediários devem manter precisão máxima
- Evita diferenças entre soma de parcelas vs total

**Exemplo de impacto:**
```
Caso 1 (COM arredondamento):
  N2 = R$10.085,12
  P2 = R$0.0822
  ADO = ARRED(10085,12 ; 2) + ARRED(0,0822 ; 2)
  ADO = 10085,12 + 0,08 = R$10.085,20

Caso 2 (SEM arredondamento):
  N2 = R$10.085,12
  P2 = R$0.0822
  ADO = 10085,12 + 0,0822 = R$10.085,20 (mais preciso)
```

---

### 2. Coluna R - Pagamento Líquido

**Problema:**
```excel
Fórmula atual: = N2 + P2 (referencia a P ao invés de Q)
```

**Solução:**
```excel
Fórmula corrigida: = N2 + Q2
```

**Impacto:**
- A coluna R (Pagamento Líquido) deve usar o valor consolidado de ADO TOTAL (coluna Q)
- Atualmente está somando diretamente N2 + P2, ignorando o cálculo da coluna Q
- Pode gerar inconsistências se houver lógica adicional em Q

---

## Validações Necessárias

Antes de aplicar as correções, confirmar com TI/Controladoria:

### Entendimento das Colunas
- [ ] O que representa exatamente a coluna P?
- [ ] A coluna "Jesoneracao" (O) entra em algum cálculo?
- [ ] ADO TOTAL é "Adiantamento" ou outro conceito?
- [ ] Pagamento Líquido é o valor final faturado?

### Regras de Negócio
- [ ] Existe alguma razão regulatória para o arredondamento?
- [ ] Como é feita a conciliação contábil desses valores?
- [ ] Os valores batem com DRE e contabilidade?
- [ ] Devoluções são tratadas na mesma base ou separado?

### Impacto da Mudança
- [ ] Quanto representa a diferença acumulada no mês?
- [ ] Houve reclamações sobre diferenças de centavos?
- [ ] A mudança afeta relatórios já emitidos?
- [ ] Precisa reprocessar histórico ou vale só daqui pra frente?

---

## Processo de Correção Proposto

### Opção 1: Correção Manual no Excel (Temporário)
**Quando usar:** Enquanto não temos pipeline automatizado

1. Exportar relatório do NetSuite
2. Abrir no Excel
3. Aplicar Find & Replace nas fórmulas:
   - Buscar: `=ARRED(N` → Substituir: `=N`
   - Buscar: `ARRED(P` → Substituir: `P`
   - Remover `;2)` extras
4. Ajustar coluna R para referenciar Q
5. Validar soma geral
6. Salvar como "BASE_VENDAS_JAN2026_TRATADA.xlsx"

**Desvantagens:**
- Manual e sujeito a erro
- Não escalável
- Precisa repetir todo mês

---

### Opção 2: Script Python (Automação)
**Quando usar:** A partir do mês que vem, quando pipeline estiver pronto

```python
import pandas as pd

# Carregar relatório bruto
df = pd.read_excel('BASE_VENDAS_NETSUITE_RAW.xlsx')

# Recalcular ADO TOTAL sem arredondamento
df['ADO_TOTAL'] = df['DESCONTO'] + df['COLUNA_P']

# Recalcular Pagamento Líquido usando ADO TOTAL
df['PAGAMENTO_LIQUIDO'] = df['ADO_TOTAL']  # ou outra regra a definir

# Validar
assert df['ADO_TOTAL'].sum() > 0, "Erro: ADO TOTAL zerado"
print(f"Total processado: R$ {df['ADO_TOTAL'].sum():,.2f}")

# Salvar tratado
df.to_excel('BASE_VENDAS_TRATADA.xlsx', index=False)
```

**Vantagens:**
- Automatizado e repetível
- Rastreável (código versionado)
- Pode adicionar validações extras
- Escalável para grande volume

---

### Opção 3: Correção na Origem (NetSuite)
**Quando usar:** Solução ideal de longo prazo

1. Solicitar à Oracle/NetSuite ajuste na Saved Search
2. Modificar fórmula customizada diretamente no NetSuite
3. Todos os usuários passam a receber o relatório correto

**Requisitos:**
- Acesso de administrador NetSuite
- Conhecimento de SuiteScript ou fórmulas NetSuite
- Testes em ambiente de sandbox antes de produção

---

## Impacto Financeiro Estimado

**Cenário hipotético:**
- Volume mensal: 10.000 transações
- Diferença média por arredondamento: R$ 0,01 a R$ 0,05
- **Impacto mensal estimado:** R$ 100 a R$ 500

**Recomendação:** Mesmo que o valor seja pequeno, a **precisão** é crítica para:
- Conciliação contábil
- Auditoria
- Compliance
- Confiança nos dados

---

## Checklist de Implementação

### Antes de Implementar
- [ ] Reunião com TI para entender sistema NetSuite
- [ ] Validar com Controladoria o impacto contábil
- [ ] Confirmar com coordenadora comercial as regras de negócio
- [ ] Exportar base de Janeiro/2026 como "versão original"
- [ ] Documentar mapeamento completo das colunas

### Durante Implementação
- [ ] Aplicar correção (manual ou script)
- [ ] Validar soma geral vs relatório original
- [ ] Comparar com DRE / contabilidade
- [ ] Testar em amostra pequena primeiro
- [ ] Documentar diferenças encontradas

### Após Implementação
- [ ] Apresentar resultados para stakeholders
- [ ] Atualizar documentação do processo
- [ ] Se aprovado, aplicar para meses seguintes
- [ ] Planejar automação definitiva

---

## Próximos Passos

1. **Reunião com TI** (Esta semana)
   - Entender acesso ao NetSuite
   - Validar colunas e fórmulas
   - Confirmar se podemos alterar a Saved Search

2. **Validação com Coordenadora** (Esta semana)
   - Apresentar o problema identificado
   - Validar regras de cálculo
   - Obter aprovação para correção

3. **Teste Piloto** (Próxima semana)
   - Aplicar correção em Janeiro/2026
   - Comparar com contabilidade
   - Documentar resultados

4. **Automação** (Fase 2 do projeto)
   - Criar pipeline Python
   - Agendar execução automática
   - Integrar com Data Warehouse

---

## Referências

**Documentos relacionados:**
- [[00-INDICE]] - Índice do projeto
- [[04-REQUISITOS-TECNICOS]] - Acesso NetSuite
- [[01-CHECKLIST-LEVANTAMENTO]] - Perguntas sobre colunas

**Arquivos:**
- Base original: `Base de Dados/NETSUITE_JAN2026_ORIGINAL.xlsx` (quando disponível)
- Base tratada: `Base de Dados/NETSUITE_JAN2026_TRATADA.xlsx` (após correção)

---

## Observações

- Sempre manter backup do arquivo original exportado do NetSuite
- Documentar qualquer ajuste manual realizado
- Validar com múltiplas fontes antes de considerar "fonte da verdade"
- Este tratamento é temporário até termos pipeline automatizado

---

**Última atualização:** 2026-01-27
**Responsável:** José Silva
**Status:** Aguardando reuniões de validação

#netsuite #etl #tratamento-dados #excel
