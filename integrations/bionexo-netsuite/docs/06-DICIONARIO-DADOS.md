# Dicionário de Dados - Integração Bionexo x NetSuite

**Data:** 2026-01-29
**Responsável:** Pedro (Inteligência Comercial)
**Status:** A completar após reunião com Bionexo

---

## OBJETIVO

Mapear campos e IDs entre NetSuite e Bionexo para garantir que **o mesmo ID usado na nossa base seja o mesmo na base deles**, permitindo relacionamento correto de dados.

---

## 1. IDENTIFICADORES ÚNICOS (IDs)

### 1.1 Cotação (RFQ - Request for Quote)

| Sistema | Campo/ID | Tipo | Formato | Exemplo | Observações |
|---------|----------|------|---------|---------|-------------|
| **NetSuite** | `internalid` | Integer | Numérico sequencial | `12345` | ID interno NetSuite (não mudar) |
| **NetSuite** | `tranid` | String | Formato: RFQ-AAAA-NNNN | `RFQ-2026-0001` | Número da transação (visível ao usuário) |
| **NetSuite** | `custbody_bionexo_rfq_id` | String | **A DEFINIR COM BIONEXO** | `bxo_rfq_abc123` | **Campo customizado** para armazenar ID da Bionexo |
| **Bionexo** | `rfq_id` ou `cotacao_id` | **A DEFINIR** | **A DEFINIR** | **A DEFINIR** | ID da cotação na Bionexo |
| **Middleware** | `integration_id` | UUID | UUID v4 | `550e8400-e29b-41d4-a716-446655440000` | ID de rastreamento da integração |

**Chave de relacionamento:**
```
NetSuite.custbody_bionexo_rfq_id = Bionexo.rfq_id
```

**Ação necessária:**
- [ ] Criar custom field no NetSuite: `custbody_bionexo_rfq_id` (Script ID)
- [ ] Confirmar formato do ID da Bionexo (numérico, UUID, string?)
- [ ] Definir se Bionexo pode receber nosso `tranid` como external_reference

---

### 1.2 Pedido de Compra (PO - Purchase Order)

| Sistema | Campo/ID | Tipo | Formato | Exemplo | Observações |
|---------|----------|------|---------|---------|-------------|
| **NetSuite** | `internalid` | Integer | Numérico sequencial | `67890` | ID interno NetSuite |
| **NetSuite** | `tranid` | String | Formato: PO-AAAA-NNNN | `PO-2026-0123` | Número do pedido |
| **NetSuite** | `custbody_bionexo_po_id` | String | **A DEFINIR COM BIONEXO** | `bxo_po_xyz789` | **Campo customizado** para ID Bionexo |
| **Bionexo** | `po_id` ou `pedido_id` | **A DEFINIR** | **A DEFINIR** | **A DEFINIR** | ID do pedido na Bionexo |

**Chave de relacionamento:**
```
NetSuite.custbody_bionexo_po_id = Bionexo.po_id
NetSuite.createdfrom = NetSuite_RFQ.internalid  (relação RFQ → PO)
```

---

### 1.3 Fornecedor (Vendor)

| Sistema | Campo/ID | Tipo | Formato | Exemplo | Observações |
|---------|----------|------|---------|---------|-------------|
| **NetSuite** | `internalid` | Integer | Numérico sequencial | `4567` | ID interno do fornecedor |
| **NetSuite** | `entityid` | String | Código do fornecedor | `FORN-001` | Código visível |
| **NetSuite** | `vatregnumber` | String | CNPJ | `12.345.678/0001-90` | CNPJ com formatação |
| **NetSuite** | `custentity_cnpj_limpo` | String | CNPJ sem formatação | `12345678000190` | **Recomendado criar** para facilitar match |
| **NetSuite** | `custentity_bionexo_vendor_id` | String | **A DEFINIR COM BIONEXO** | `bxo_vendor_123` | **Campo customizado** opcional |
| **Bionexo** | `vendor_id` ou `fornecedor_id` | **A DEFINIR** | **A DEFINIR** | **A DEFINIR** | ID do fornecedor na Bionexo |
| **Bionexo** | `cnpj` | String | CNPJ | **A DEFINIR FORMATO** | Usado para match |

**Chave de relacionamento (recomendado):**
```
NetSuite.custentity_cnpj_limpo = Bionexo.cnpj (sem formatação)
```

**Decisão arquitetural:**
- **CNPJ como chave natural** (recomendado): Evita criar campo customizado extra
- **ID Bionexo armazenado** (alternativa): Cria campo `custentity_bionexo_vendor_id`

**Ação necessária:**
- [ ] Confirmar formato CNPJ na Bionexo (com ou sem pontuação?)
- [ ] Definir estratégia de match (CNPJ ou ID)
- [ ] Verificar fornecedores duplicados (mesmo CNPJ, IDs diferentes)

---

### 1.4 Produto (Item)

| Sistema | Campo/ID | Tipo | Formato | Exemplo | Observações |
|---------|----------|------|---------|---------|-------------|
| **NetSuite** | `internalid` | Integer | Numérico sequencial | `8901` | ID interno do item |
| **NetSuite** | `itemid` | String | SKU interno | `MED-12345` | SKU da Amoveri |
| **NetSuite** | `upccode` | String | EAN-13 | `7891234567890` | Código de barras |
| **NetSuite** | `custitem_ncm` | String | NCM | `30049099` | Classificação fiscal |
| **NetSuite** | `custitem_bionexo_product_id` | String | **A DEFINIR COM BIONEXO** | `bxo_prod_456` | **Campo customizado** opcional |
| **Bionexo** | `product_id` ou `item_id` | **A DEFINIR** | **A DEFINIR** | **A DEFINIR** | ID do produto na Bionexo |
| **Bionexo** | `ean` ou `gtin` | String | EAN-13 | **A DEFINIR** | Código de barras |
| **Bionexo** | `sku` | String | SKU | **A DEFINIR** | Pode ser diferente do nosso |
| **CMED** | `ean` | String | EAN-13 | `7891234567890` | Chave na tabela CMED |

**Chave de relacionamento (recomendado):**
```
NetSuite.upccode = Bionexo.ean = CMED.ean
```

**Alternativa (se EAN não for confiável):**
```
NetSuite.custitem_bionexo_product_id = Bionexo.product_id
```

**Ação necessária:**
- [ ] Confirmar se Bionexo usa EAN como identificador principal
- [ ] Verificar qualidade dos dados: % de produtos com EAN cadastrado
- [ ] Definir estratégia para produtos sem EAN
- [ ] Mapear unidades de medida (UN, CX, FR, etc)

---

## 2. MAPEAMENTO DE CAMPOS - COTAÇÃO (RFQ)

### 2.1 Cabeçalho da Cotação

| Campo NetSuite | Script ID | Tipo | Campo Bionexo | Tipo Bionexo | Transformação | Obrigatório |
|----------------|-----------|------|---------------|--------------|---------------|-------------|
| Internal ID | `internalid` | Integer | `external_reference` | String | ToString() | Não |
| Transaction ID | `tranid` | String | `reference_number` | String | - | Sim |
| Customer | `entity` (internalid) | Integer | `cliente_id` | **A DEFINIR** | Lookup CNPJ | Sim |
| Customer Name | `entity` (name) | String | `cliente_nome` | String | - | Sim |
| Customer CNPJ | `entity.vatregnumber` | String | `cliente_cnpj` | String | Remover formatação | Sim |
| Transaction Date | `trandate` | Date | `data_criacao` | Date/Datetime | ISO 8601 | Sim |
| Due Date / Expected Date | `duedate` | Date | `data_entrega_esperada` | Date | ISO 8601 | Sim |
| Ship To Address | `shipaddress` | String | `endereco_entrega` | Object | **A MAPEAR** | Sim |
| Ship To State | `shipstate` | String | `uf_destino` | String | Sigla (ex: SP) | Sim |
| Ship To City | `shipcity` | String | `cidade_destino` | String | - | Não |
| Ship To Zip | `shipzip` | String | `cep_destino` | String | Remover hífen | Não |
| Payment Terms | `terms` | Integer | `condicao_pagamento` | **A DEFINIR** | **A MAPEAR** | Não |
| Memo / Notes | `memo` | String | `observacoes` | String | - | Não |
| Status | `status` | String | `status` | String | **A MAPEAR** | Sim |
| Bionexo RFQ ID | `custbody_bionexo_rfq_id` | String | `rfq_id` | String | - | Após envio |

**Status - Mapeamento:**
| NetSuite Status | Código | Bionexo Status | A DEFINIR |
|-----------------|--------|----------------|-----------|
| Pending Approval | A | `pendente` | **A CONFIRMAR** |
| Pending Receipt | B | `aguardando_propostas` | **A CONFIRMAR** |
| Partially Received | D | `propostas_parciais` | **A CONFIRMAR** |
| Closed | H | `fechada` | **A CONFIRMAR** |
| Rejected | Reject | `rejeitada` | **A CONFIRMAR** |

---

### 2.2 Linhas da Cotação (Items)

| Campo NetSuite | Script ID | Tipo | Campo Bionexo | Tipo Bionexo | Transformação | Obrigatório |
|----------------|-----------|------|---------------|--------------|---------------|-------------|
| Line ID | `line` | Integer | `line_number` | Integer | - | Sim |
| Item ID | `item` (internalid) | Integer | - | - | Não enviar | Não |
| Item Name | `item` (itemid) | String | `produto_sku` | String | - | Não |
| Item EAN | `item.upccode` | String | `produto_ean` | String | - | Sim (recomendado) |
| Item Description | `item` (displayname) | String | `produto_descricao` | String | - | Sim |
| Quantity | `quantity` | Number | `quantidade` | Number | - | Sim |
| Unit | `units` | String | `unidade_medida` | String | **A MAPEAR** | Sim |
| Expected Price | `rate` | Number | `preco_referencia` | Number | - | Não |
| Amount | `amount` | Number | `valor_total_linha` | Number | - | Não |
| Vendor | `vendor` (internalid) | Integer | `fornecedor_preferencial` | **A DEFINIR** | **A MAPEAR** | Não |

**Unidades de Medida - Mapeamento:**
| NetSuite | Bionexo | A DEFINIR |
|----------|---------|-----------|
| `UN` | `unidade` | **A CONFIRMAR** |
| `CX` | `caixa` | **A CONFIRMAR** |
| `FR` | `frasco` | **A CONFIRMAR** |
| `BL` | `blister` | **A CONFIRMAR** |
| `CP` | `comprimido` | **A CONFIRMAR** |

---

## 3. MAPEAMENTO DE CAMPOS - PROPOSTA (PROPOSAL)

### 3.1 Cabeçalho da Proposta

| Campo Bionexo | Tipo Bionexo | Campo NetSuite | Script ID | Tipo NS | Transformação | Obrigatório |
|---------------|--------------|----------------|-----------|---------|---------------|-------------|
| `proposal_id` | **A DEFINIR** | Vendor Bill ID | `internalid` | Integer | Criar Vendor Bill | Sim |
| `rfq_id` | String | RFQ Reference | `custbody_bionexo_rfq_id` | String | Match | Sim |
| `vendor_id` ou CNPJ | **A DEFINIR** | Vendor | `entity` | Integer | Lookup | Sim |
| `vendor_nome` | String | - | - | - | Validação | Não |
| `data_proposta` | Date | Date | `trandate` | Date | - | Sim |
| `validade_proposta` | Date | Due Date | `duedate` | Date | - | Não |
| `valor_total` | Number | Amount | `usertotal` | Number | Soma linhas | Sim |
| `prazo_entrega_dias` | Integer | - | `custbody_prazo_entrega` | Integer | Criar campo | Não |
| `condicao_pagamento` | String | Payment Terms | `terms` | Integer | **A MAPEAR** | Não |
| `observacoes` | String | Memo | `memo` | String | - | Não |

---

### 3.2 Linhas da Proposta

| Campo Bionexo | Tipo Bionexo | Campo NetSuite | Script ID | Tipo NS | Transformação | Obrigatório |
|---------------|--------------|----------------|-----------|---------|---------------|-------------|
| `proposal_line_id` | **A DEFINIR** | Line ID | `line` | Integer | Sequencial | Sim |
| `produto_ean` | String | Item | `item` | Integer | Lookup por EAN | Sim |
| `quantidade` | Number | Quantity | `quantity` | Number | - | Sim |
| `unidade_medida` | String | Unit | `units` | String | **A MAPEAR** | Sim |
| `preco_unitario` | Number | Rate | `rate` | Number | - | Sim |
| `valor_total_linha` | Number | Amount | `amount` | Number | qty × rate | Sim |
| `prazo_entrega_dias` | Integer | - | `custcol_prazo_entrega` | Integer | Criar campo | Não |
| `lote` | String | - | `custcol_lote` | String | Criar campo | Não |
| `validade` | Date | - | `custcol_validade` | Date | Criar campo | Não |

---

## 4. MAPEAMENTO DE CAMPOS - PEDIDO (PO)

### 4.1 Cabeçalho do Pedido

| Campo NetSuite | Script ID | Tipo | Campo Bionexo | Tipo Bionexo | Transformação | Obrigatório |
|----------------|-----------|------|---------------|--------------|---------------|-------------|
| Internal ID | `internalid` | Integer | `external_reference` | String | ToString() | Não |
| Transaction ID | `tranid` | String | `po_number` | String | - | Sim |
| Vendor | `entity` | Integer | `fornecedor_id` | **A DEFINIR** | Lookup CNPJ | Sim |
| Transaction Date | `trandate` | Date | `data_emissao` | Date | ISO 8601 | Sim |
| Due Date | `duedate` | Date | `data_entrega` | Date | ISO 8601 | Sim |
| Ship To | `shipaddress` | String | `endereco_entrega` | Object | **A MAPEAR** | Sim |
| Amount | `total` | Number | `valor_total` | Number | - | Sim |
| Payment Terms | `terms` | Integer | `condicao_pagamento` | **A DEFINIR** | **A MAPEAR** | Não |
| Memo | `memo` | String | `observacoes` | String | - | Não |
| Created From (RFQ) | `createdfrom` | Integer | `rfq_id` | String | Match `custbody_bionexo_rfq_id` | Não |
| Bionexo PO ID | `custbody_bionexo_po_id` | String | `po_id` | String | Após confirmação | Sim |

---

### 4.2 Linhas do Pedido

| Campo NetSuite | Script ID | Tipo | Campo Bionexo | Tipo Bionexo | Transformação | Obrigatório |
|----------------|-----------|------|---------------|--------------|---------------|-------------|
| Line ID | `line` | Integer | `line_number` | Integer | - | Sim |
| Item | `item` | Integer | `produto_ean` | String | Lookup | Sim |
| Quantity | `quantity` | Number | `quantidade` | Number | - | Sim |
| Unit | `units` | String | `unidade_medida` | String | **A MAPEAR** | Sim |
| Rate | `rate` | Number | `preco_unitario` | Number | - | Sim |
| Amount | `amount` | Number | `valor_total_linha` | Number | - | Sim |
| Expected Receipt Date | `expectedreceiptdate` | Date | `data_entrega_prevista` | Date | ISO 8601 | Não |

---

## 5. CAMPOS CUSTOMIZADOS NECESSÁRIOS - NETSUITE

### 5.1 Transaction Body (Purchase Order / RFQ)

| Label | Script ID | Tipo | Tamanho | Lista | Descrição | A criar? |
|-------|-----------|------|---------|-------|-----------|----------|
| Bionexo RFQ ID | `custbody_bionexo_rfq_id` | Free-Form Text | 100 | - | ID da cotação na Bionexo | ✅ SIM |
| Bionexo PO ID | `custbody_bionexo_po_id` | Free-Form Text | 100 | - | ID do pedido na Bionexo | ✅ SIM |
| Bionexo Status | `custbody_bionexo_status` | List/Record | - | **A CRIAR** | Status atual na Bionexo | ✅ SIM |
| Bionexo Link | `custbody_bionexo_link` | URL | 500 | - | Link direto para cotação/pedido | ❓ OPCIONAL |
| Prazo Entrega (dias) | `custbody_prazo_entrega` | Integer Number | - | - | Prazo de entrega em dias | ❓ Pode já existir |
| Data Última Sincronização | `custbody_bionexo_last_sync` | Date/Time | - | - | Timestamp da última sincronização | ✅ SIM |
| Erros de Integração | `custbody_bionexo_errors` | Long Text | 4000 | - | Log de erros (se houver) | ✅ SIM |

### 5.2 Transaction Line (Item)

| Label | Script ID | Tipo | Tamanho | Descrição | A criar? |
|-------|-----------|------|---------|-----------|----------|
| Prazo Entrega Linha (dias) | `custcol_prazo_entrega` | Integer Number | - | Prazo específico do item | ❓ OPCIONAL |
| Lote | `custcol_lote` | Free-Form Text | 50 | Número do lote (se aplicável) | ❓ Pode existir |
| Validade | `custcol_validade` | Date | - | Data de validade do lote | ❓ Pode existir |
| Bionexo Line ID | `custcol_bionexo_line_id` | Free-Form Text | 100 | ID da linha na proposta Bionexo | ❓ OPCIONAL |

### 5.3 Vendor (Fornecedor)

| Label | Script ID | Tipo | Tamanho | Descrição | A criar? |
|-------|-----------|------|---------|-----------|----------|
| CNPJ Limpo | `custentity_cnpj_limpo` | Free-Form Text | 14 | CNPJ sem formatação (só números) | ✅ SIM |
| Bionexo Vendor ID | `custentity_bionexo_vendor_id` | Free-Form Text | 100 | ID do fornecedor na Bionexo | ❓ OPCIONAL |
| Cadastrado na Bionexo | `custentity_bionexo_active` | Check Box | - | Se está ativo na Bionexo | ❓ OPCIONAL |

### 5.4 Item (Produto)

| Label | Script ID | Tipo | Tamanho | Descrição | A criar? |
|-------|-----------|------|---------|-----------|----------|
| NCM | `custitem_ncm` | Free-Form Text | 10 | Classificação fiscal | ❓ Pode existir |
| Bionexo Product ID | `custitem_bionexo_product_id` | Free-Form Text | 100 | ID do produto na Bionexo | ❓ OPCIONAL |
| PMC CMED | `custitem_pmc_cmed` | Currency | - | Preço Máximo ao Consumidor | ✅ SIM |
| Data Vigência PMC | `custitem_pmc_vigencia` | Date | - | Data de vigência do PMC | ✅ SIM |
| Registro Anvisa | `custitem_registro_anvisa` | Free-Form Text | 20 | Número de registro Anvisa | ❓ Pode existir |

---

## 6. FORMATOS E TRANSFORMAÇÕES

### 6.1 Datas

**NetSuite → Bionexo:**
```javascript
// NetSuite retorna: Date object
// Bionexo espera: A DEFINIR (ISO 8601 recomendado)
function formatDate(nsDate) {
    // ISO 8601: "2026-01-29T14:00:00Z"
    return nsDate.toISOString();

    // OU formato BR: "29/01/2026"
    // return format.format({ value: nsDate, type: format.Type.DATE });
}
```

**Bionexo → NetSuite:**
```javascript
function parseDate(bxDate) {
    // Se vier ISO 8601
    return new Date(bxDate);

    // Se vier DD/MM/YYYY
    // return format.parse({ value: bxDate, type: format.Type.DATE });
}
```

### 6.2 Valores Monetários

**NetSuite → Bionexo:**
```javascript
// NetSuite: Number com 2 casas decimais
// Bionexo: A DEFINIR (number ou string?)
function formatCurrency(nsAmount) {
    // Se Bionexo aceita number:
    return parseFloat(nsAmount).toFixed(2);

    // Se Bionexo exige string:
    // return parseFloat(nsAmount).toFixed(2).toString();
}
```

**Moeda:**
- NetSuite: Configurado na transação (BRL, USD, etc)
- Bionexo: **A DEFINIR** - Assumir sempre BRL?

### 6.3 CNPJ

**NetSuite → Bionexo:**
```javascript
function formatCNPJ(cnpj) {
    // Remove tudo exceto números
    return cnpj.replace(/[^\d]/g, '');
    // "12.345.678/0001-90" → "12345678000190"
}
```

**Bionexo → NetSuite:**
```javascript
function parseCNPJ(cnpj) {
    // Se Bionexo envia sem formatação, adicionar:
    const clean = cnpj.replace(/[^\d]/g, '');
    return clean.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/,
                         '$1.$2.$3/$4-$5');
    // "12345678000190" → "12.345.678/0001-90"
}
```

### 6.4 EAN (Código de Barras)

**Validação:**
```javascript
function validateEAN(ean) {
    // Remove espaços e hífens
    const clean = ean.replace(/[\s-]/g, '');

    // EAN-13 tem 13 dígitos
    if (clean.length !== 13) return false;

    // Valida dígito verificador (algoritmo módulo 10)
    // ... implementar validação

    return true;
}
```

### 6.5 Endereço

**NetSuite → Bionexo:**
```javascript
// NetSuite retorna objeto Address
// Bionexo espera: A DEFINIR

function formatAddress(nsAddress) {
    return {
        logradouro: nsAddress.addr1,
        numero: nsAddress.addr2, // ou extrair de addr1
        complemento: nsAddress.addr3,
        bairro: nsAddress.city, // Ou campo customizado?
        cidade: nsAddress.city,
        uf: nsAddress.state, // "SP"
        cep: nsAddress.zip.replace(/[^\d]/g, ''), // "01234567"
        pais: "BR" // Assumir Brasil
    };
}
```

---

## 7. TABELAS AUXILIARES - DATABASE MIDDLEWARE

### 7.1 Tabela: `tbl_cmed_pmc`

Armazena PMC (Preço Máximo ao Consumidor) da CMED (Anvisa).

| Coluna | Tipo | PK | Descrição |
|--------|------|----|-----------|
| `ean` | VARCHAR(13) | ✅ | Código EAN do produto |
| `registro_anvisa` | VARCHAR(20) | | Número de registro Anvisa |
| `produto_nome` | VARCHAR(500) | | Nome do produto |
| `apresentacao` | VARCHAR(200) | | Apresentação (ex: "30 cápsulas") |
| `laboratorio` | VARCHAR(200) | | Nome do laboratório |
| `pmc_0` | DECIMAL(10,2) | | PMC sem imposto |
| `pmc_12` | DECIMAL(10,2) | | PMC com ICMS 12% |
| `pmc_17` | DECIMAL(10,2) | | PMC com ICMS 17% |
| `pmc_18` | DECIMAL(10,2) | | PMC com ICMS 18% |
| `pmc_19` | DECIMAL(10,2) | | PMC com ICMS 19% |
| `pmc_20` | DECIMAL(10,2) | | PMC com ICMS 20% |
| `data_vigencia` | DATE | ✅ | Data de vigência (1º abril) |
| `data_atualizacao` | TIMESTAMP | | Data de importação |

**Índices:**
- PK: `ean` + `data_vigencia`
- INDEX: `registro_anvisa`

**Fonte:** Importação anual da lista CMED (todo 1º de abril)

---

### 7.2 Tabela: `tbl_operadora_logistica_descontos`

Armazena descontos de Operadoras Logísticas (OL). **Atualização frequente!**

| Coluna | Tipo | PK | Descrição |
|--------|------|----|-----------|
| `id` | INT | ✅ | ID autoincremente |
| `operadora_nome` | VARCHAR(100) | | Nome da OL |
| `operadora_cnpj` | VARCHAR(14) | | CNPJ da OL |
| `laboratorio_nome` | VARCHAR(200) | | Laboratório específico (ou NULL para geral) |
| `ean` | VARCHAR(13) | | Produto específico (ou NULL para categoria) |
| `ncm` | VARCHAR(10) | | NCM específico (ou NULL) |
| `desconto_percentual` | DECIMAL(5,2) | | % de desconto (ex: 5.50 = 5.5%) |
| `desconto_fixo` | DECIMAL(10,2) | | Valor fixo de desconto (ou NULL) |
| `condicao` | VARCHAR(500) | | Condição (ex: "acima de 100 unidades") |
| `data_vigencia_inicio` | DATE | | Data início vigência |
| `data_vigencia_fim` | DATE | | Data fim vigência (ou NULL para indeterminado) |
| `ativo` | BOOLEAN | | Se regra está ativa |
| `data_atualizacao` | TIMESTAMP | | Data da última atualização |
| `atualizado_por` | VARCHAR(100) | | Quem atualizou (analista) |

**Índices:**
- INDEX: `operadora_cnpj`
- INDEX: `laboratorio_nome`
- INDEX: `ean`
- INDEX: `data_vigencia_inicio`, `data_vigencia_fim`

**Prioridade de aplicação:**
1. Produto específico (EAN)
2. Laboratório específico
3. NCM
4. Geral da OL

---

### 7.3 Tabela: `tbl_regras_laboratorios`

Armazena regras especiais de cada laboratório. **Mantido pelas analistas comerciais.**

| Coluna | Tipo | PK | Descrição |
|--------|------|----|-----------|
| `id` | INT | ✅ | ID autoincremente |
| `laboratorio_nome` | VARCHAR(200) | | Nome do laboratório |
| `laboratorio_cnpj` | VARCHAR(14) | | CNPJ (se disponível) |
| `tipo_regra` | ENUM | | `desconto_progressivo`, `margem_minima`, `prazo_diferenciado`, `restricao_uf`, `outro` |
| `regra_json` | JSON | | Definição da regra em JSON |
| `descricao` | TEXT | | Descrição legível da regra |
| `ativo` | BOOLEAN | | Se regra está ativa |
| `data_inicio` | DATE | | Data início vigência |
| `data_fim` | DATE | | Data fim vigência (ou NULL) |
| `cadastrado_por` | VARCHAR(100) | | Analista que cadastrou |
| `data_cadastro` | TIMESTAMP | | Data de cadastro |
| `observacoes` | TEXT | | Observações adicionais |

**Exemplo de `regra_json` para desconto progressivo:**
```json
{
  "tipo": "desconto_progressivo",
  "faixas": [
    { "quantidade_min": 10, "quantidade_max": 49, "desconto_percentual": 2.5 },
    { "quantidade_min": 50, "quantidade_max": 99, "desconto_percentual": 5.0 },
    { "quantidade_min": 100, "quantidade_max": null, "desconto_percentual": 7.5 }
  ]
}
```

**Exemplo de `regra_json` para margem mínima:**
```json
{
  "tipo": "margem_minima",
  "margem_percentual": 12.5,
  "aplicar_em": "todos_produtos"
}
```

---

### 7.4 Tabela: `tbl_matriz_tributaria`

Armazena matriz tributária (ICMS-ST, PIS, COFINS). **Mantido por Thiago.**

| Coluna | Tipo | PK | Descrição |
|--------|------|----|-----------|
| `id` | INT | ✅ | ID autoincremente |
| `ncm` | VARCHAR(10) | | Classificação NCM |
| `uf_origem` | CHAR(2) | | UF origem (ex: SP) |
| `uf_destino` | CHAR(2) | | UF destino (ex: RJ) |
| `mva_ajustada` | DECIMAL(5,2) | | MVA ajustada (%) |
| `aliq_interna` | DECIMAL(4,2) | | Alíquota interna (%) |
| `aliq_origem` | DECIMAL(4,2) | | Alíquota origem (%) |
| `pis_percentual` | DECIMAL(4,2) | | PIS (%) ou NULL se monofásico |
| `cofins_percentual` | DECIMAL(4,2) | | COFINS (%) ou NULL se monofásico |
| `monofasico` | BOOLEAN | | Se tributo é monofásico |
| `observacao` | VARCHAR(500) | | Observações |
| `data_vigencia` | DATE | | Data de vigência |
| `data_atualizacao` | TIMESTAMP | | Data da última atualização |
| `atualizado_por` | VARCHAR(100) | | Thiago |

**Índices:**
- INDEX: `ncm` + `uf_destino`

---

### 7.5 Tabela: `tbl_integration_log`

Log de todas as integrações.

| Coluna | Tipo | PK | Descrição |
|--------|------|----|-----------|
| `id` | INT | ✅ | ID autoincremente |
| `integration_id` | UUID | | UUID único da operação |
| `timestamp` | TIMESTAMP | | Data/hora |
| `tipo_operacao` | ENUM | | `create_rfq`, `get_proposals`, `create_po`, etc |
| `sistema_origem` | VARCHAR(50) | | `NetSuite`, `Bionexo`, `Middleware` |
| `sistema_destino` | VARCHAR(50) | | `NetSuite`, `Bionexo`, `Middleware` |
| `netsuite_id` | INT | | ID interno NetSuite |
| `netsuite_tranid` | VARCHAR(50) | | Transaction ID (RFQ-2026-0001) |
| `bionexo_id` | VARCHAR(100) | | ID da Bionexo |
| `status` | ENUM | | `success`, `error`, `warning`, `pending` |
| `erro_mensagem` | TEXT | | Mensagem de erro (se houver) |
| `request_payload` | JSON | | Payload enviado |
| `response_payload` | JSON | | Resposta recebida |
| `tempo_resposta_ms` | INT | | Tempo de resposta (milissegundos) |
| `usuario` | VARCHAR(100) | | Usuário que iniciou (se aplicável) |

**Índices:**
- INDEX: `timestamp`
- INDEX: `netsuite_tranid`
- INDEX: `bionexo_id`
- INDEX: `status`

**Retenção:** 90 dias (configurável)

---

## 8. PERGUNTAS CRÍTICAS PARA BIONEXO

**IMPORTANTE: Essas perguntas devem ser feitas na reunião de segunda-feira!**

### Identificadores
- [ ] Qual o formato e tipo do ID de cotação (`rfq_id`)? (UUID, numérico, string?)
- [ ] Qual o formato e tipo do ID de pedido (`po_id`)?
- [ ] Vocês podem receber nosso `tranid` do NetSuite como `external_reference`?
- [ ] Como identificam fornecedores? (CNPJ, ID próprio, ambos?)
- [ ] Como identificam produtos? (EAN, SKU, ID próprio?)

### Formatos
- [ ] Formato de data esperado? (ISO 8601, DD/MM/YYYY, timestamp?)
- [ ] Formato de CNPJ? (com ou sem formatação?)
- [ ] Formato de valores monetários? (number ou string? quantas casas decimais?)
- [ ] Moeda sempre BRL ou precisa informar?
- [ ] Como são as unidades de medida? (UN, CX, tabela própria?)

### Campos Obrigatórios
- [ ] Quais campos são obrigatórios na criação de RFQ?
- [ ] Quais campos são obrigatórios na criação de PO?
- [ ] Há validações específicas (tamanho campo, regex, etc)?

### Relacionamentos
- [ ] Como relacionar RFQ → Propostas → PO?
- [ ] Vocês armazenam nosso `external_reference` para rastreamento?
- [ ] Há limite de itens por cotação?

---

## 9. AÇÕES NECESSÁRIAS PÓS-REUNIÃO

### NetSuite
- [ ] Criar custom fields listados na Seção 5
- [ ] Criar Saved Search para exportar custos, estoque, fiscal
- [ ] Configurar Token Based Authentication (TBA)
- [ ] Desenvolver SuiteScript (se integração direta) ou RESTlet (se middleware)

### Middleware
- [ ] Criar tabelas auxiliares (Seções 7.1 a 7.5)
- [ ] Importar tabela CMED inicial
- [ ] Popular matriz tributária (input de Thiago)
- [ ] Desenvolver motor de precificação
- [ ] Implementar validação PMC

### Bionexo
- [ ] Obter credenciais de API (sandbox e produção)
- [ ] Fazer primeiro teste de autenticação
- [ ] Validar mapeamento de campos com dados reais

---

## RESUMO

**Chaves de Relacionamento Principais:**

```
COTAÇÃO:
NetSuite.custbody_bionexo_rfq_id ←→ Bionexo.rfq_id

PEDIDO:
NetSuite.custbody_bionexo_po_id ←→ Bionexo.po_id

FORNECEDOR:
NetSuite.custentity_cnpj_limpo ←→ Bionexo.cnpj (sem formatação)

PRODUTO:
NetSuite.upccode ←→ Bionexo.ean ←→ CMED.ean

REGRAS:
NetSuite.item.upccode → CMED.ean → PMC
NetSuite.item.custitem_ncm + Customer.shipstate → Matriz Tributária → ICMS-ST
```

---

**Próximo documento:** [Especificação Técnica](07-ESPECIFICACAO-TECNICA.md) (após reunião)

**Última atualização:** 2026-01-29
**Status:** Aguardando reunião para completar campos "A DEFINIR"
