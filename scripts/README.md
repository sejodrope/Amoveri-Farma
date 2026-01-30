# Scripts - Amoveri Farma

Scripts Python para o middleware local de precificacao e integracao.

---

## Status

Scripts serao desenvolvidos apos:
1. Reuniao com Bionexo (segunda 14h) - obter documentacao da API
2. Inputs de Thiago (matriz tributaria)
3. Definicao da tabela de precos com Kamila (NetSuite)

---

## Scripts Planejados

| Script | Funcao | Fase |
|--------|--------|------|
| `pricing_engine.py` | Motor de precificacao (Custo + ICMS + Margem - OL, validar PMC) | Fase 1-2 |
| `netsuite_client.py` | Conexao com NetSuite via REST/SuiteScript (TBA) | Fase 2 |
| `bionexo_client.py` | Integracao com API Bionexo (envio de precos) | Fase 3 |
| `import_gtplan.py` | Importar relatorios/CSV do GT Plan | Fase 4 |
| `import_apoio.py` | Importar relatorios/CSV do Apoio Cotacoes | Fase 4 |
| `cmed_updater.py` | Atualizar tabela CMED/PMC (anual, 1 abril) | Fase 2 |
| `scheduler.py` | Orquestrador para Windows Task Scheduler | Fase 2 |

---

## Setup (quando iniciar desenvolvimento)

```bash
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env com credenciais
```

---

## Arquivos anteriores

Templates antigos (Playwright/scraping) foram movidos para `_archive/`.
A abordagem mudou para integracao via API (Bionexo) e download de relatorios (GT Plan, Apoio).

---

**Ultima atualizacao:** 2026-01-30
