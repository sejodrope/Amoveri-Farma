# Scripts de Automação - Amoveri Farma

Pasta contendo todos os scripts Python para extração, tratamento e análise de dados.

---

## 📁 Estrutura

```
scripts/
├── README.md                           # Este arquivo
├── extraction_bionexo.py               # ✅ Extrator Bionexo
├── extraction_apoio.py                 # 🚧 TODO: Extrator Apoio Cotações
├── extraction_gtplan.py                # 🚧 TODO: Extrator GT Plan
├── pricing_engine.py                   # 🚧 TODO: Motor de precificação
├── netsuite_client.py                  # 🚧 TODO: Cliente NetSuite
├── test_netsuite_connection.py         # ✅ Teste de conexão NetSuite
└── ml_bidding_strategy.py              # 🚧 TODO: Modelo ML (Fase 3)
```

---

## 🚀 Scripts Disponíveis

### 1. extraction_bionexo.py

**Status:** ✅ Pronto para uso

**Descrição:**
Extrai cotações automaticamente do portal Bionexo usando Playwright.

**Uso:**
```bash
# Ativar ambiente virtual
.\venv\Scripts\Activate

# Executar
python scripts/extraction_bionexo.py
```

**Configurações necessárias (.env):**
- `BIONEXO_EMAIL`
- `BIONEXO_PASSWORD`
- `ONEDRIVE_PATH`

**Output:**
Arquivos JSON salvos em `01_Bronze/Bionexo/`

**Exemplo de saída:**
```
01_Bronze/Bionexo/
└── cotacao_12345_20260129_143022.json
```

---

### 2. test_netsuite_connection.py

**Status:** ✅ Pronto para uso

**Descrição:**
Testa conexão com NetSuite e valida Saved Searches.

**Uso:**
```bash
python scripts/test_netsuite_connection.py
```

**Configurações necessárias (.env):**
- `NETSUITE_ACCOUNT_ID`
- `NETSUITE_TOKEN_ID`
- `NETSUITE_TOKEN_SECRET`
- `NETSUITE_CONSUMER_KEY`
- `NETSUITE_CONSUMER_SECRET`
- `NETSUITE_SAVED_SEARCH_CUSTOS`
- `NETSUITE_SAVED_SEARCH_ESTOQUE`

**Output:**
Relatório de testes no console.

---

### 3. extraction_apoio.py (TODO)

**Status:** 🚧 Em desenvolvimento

**Descrição:**
Extrator para o portal Apoio Cotações.

**Implementação:**
Similar ao `extraction_bionexo.py`, ajustando seletores CSS e endpoints.

---

### 4. extraction_gtplan.py (TODO)

**Status:** 🚧 Em desenvolvimento

**Descrição:**
Extrator para o portal GT Plan.

---

### 5. pricing_engine.py (TODO)

**Status:** 🚧 Em desenvolvimento

**Descrição:**
Motor de precificação que calcula:
- ICMS-ST
- PIS/COFINS
- Margem de contribuição
- Preço sugerido

**Uso planejado:**
```bash
python scripts/pricing_engine.py \
  --input "01_Bronze/Bionexo/cotacao_12345.json" \
  --output "03_Gold/precos_calculados_12345.xlsx"
```

---

### 6. ml_bidding_strategy.py (Fase 3)

**Status:** 🚧 Planejado

**Descrição:**
Modelo de Machine Learning para otimizar lances em cotações.

---

## 🛠️ Desenvolvimento

### Adicionar Novo Extrator

1. Copiar `extraction_bionexo.py` como template
2. Renomear para `extraction_PORTAL.py`
3. Ajustar URLs e seletores CSS
4. Testar manualmente primeiro (HEADLESS_MODE=false)
5. Adicionar testes automatizados em `tests/`

### Padrões de Código

- **Logging:** Usar `loguru` para todos os logs
- **Config:** Usar variáveis de ambiente (.env)
- **Erros:** Sempre fazer try/except com logs detalhados
- **Docstrings:** Google style docstrings
- **Type hints:** Usar sempre que possível

### Exemplo de Código

```python
from loguru import logger
from typing import List, Dict

def extract_data(url: str) -> List[Dict]:
    """
    Extrai dados de uma URL

    Args:
        url: URL para extrair dados

    Returns:
        Lista de dicionários com dados extraídos

    Raises:
        ValueError: Se URL inválida
    """
    try:
        logger.info(f"Extraindo dados de {url}")
        # ... código ...
        return data
    except Exception as e:
        logger.error(f"Erro: {str(e)}")
        raise
```

---

## 🧪 Testes

Executar testes:
```bash
pytest tests/ -v
```

---

## 📝 Logs

Todos os scripts salvam logs em:
- Console (stdout)
- Arquivo: `logs/extraction_YYYY-MM-DD.log`

Retenção: 30 dias

---

## ⚙️ Configuração Inicial

Antes de executar qualquer script:

1. **Criar ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate
   ```

2. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

3. **Configurar .env:**
   ```bash
   cp .env.example .env
   # Editar .env com suas credenciais
   ```

4. **Testar conexões:**
   ```bash
   python scripts/test_netsuite_connection.py
   ```

---

## 🆘 Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'playwright'"

**Solução:**
```bash
pip install playwright
playwright install
```

### Problema: "BIONEXO_EMAIL not found in .env"

**Solução:**
1. Verificar se arquivo `.env` existe na raiz do projeto
2. Verificar se variáveis estão definidas sem espaços: `BIONEXO_EMAIL=email@exemplo.com`

### Problema: Script trava no login

**Solução:**
1. Executar com `HEADLESS_MODE=false` para ver o navegador
2. Verificar se credenciais estão corretas
3. Verificar se seletores CSS mudaram (site atualizou)

---

## 📞 Contato

**Dúvidas técnicas:** José Silva

---

**Última atualização:** 2026-01-29
