# Integrações - Amoveri Farma

Este diretório contém todos os projetos de integração da Amoveri Farma com sistemas externos.

---

## Projetos de Integração

### 1. [Bionexo x NetSuite](bionexo-netsuite/)
**Status:** Em Planejamento
**Responsável:** Pedro (Inteligência Comercial)
**Descrição:** Automação de fluxo de cotações entre NetSuite e plataforma Bionexo

**Próxima Ação:** Reunião de kickoff - Segunda-feira, 14h
- Ver: [Preparação para Reunião](bionexo-netsuite/docs/01-PREPARACAO-REUNIAO.md)

---

## Estrutura Padrão de Projetos

Cada projeto de integração segue esta estrutura:

```
nome-integracao/
├── docs/           # Documentação (preparação, atas, specs)
├── specs/          # Especificações técnicas
├── tests/          # Testes automatizados
├── config/         # Configurações
├── logs/           # Logs de execução
└── README.md       # Visão geral do projeto
```

---

## Boas Práticas

1. **Documentação First:** Sempre documente antes de implementar
2. **Segurança:** Nunca versione credenciais. Use cofres (Key Vault, .env)
3. **Logs:** Mantenha logs detalhados para troubleshooting
4. **Testes:** Sempre teste em sandbox antes de produção
5. **Versionamento:** Use Git para controle de versão

---

**Última atualização:** 2026-01-29
