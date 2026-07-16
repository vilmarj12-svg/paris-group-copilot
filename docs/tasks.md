# Tasknotes — Paris Group Copilot

> Rastreamento de tarefas no espírito do Tasknotes CLI (`tn`). Uma tarefa por bloco,
> com status e checklist. Versionado junto com o código.

## TN-1 · Estrutura inicial do repositório e páginas — `done`

Estrutura Next.js + páginas de produto navegáveis (Módulo 1).

- [x] Inicializar Next.js + TypeScript + Tailwind + App Router
- [x] Criar rota `/projeto` com conteúdo mínimo
- [x] Criar rota `/hipotese` com conteúdo mínimo
- [x] `docs/enquadramento.md` com hipótese de valor testável

## TN-2 · Backend FastAPI + contrato OpenAPI — `in-progress`

API em `api/` com entidades Projeto e Hipótese, contrato OpenAPI em `/docs`.

- [x] Modelos SQLAlchemy (Projeto, Hipotese) + schemas Pydantic
- [x] Endpoints `/projetos` e `/hipoteses` (OpenAPI automático)
- [x] Docker Compose (Postgres + Redis) subindo sem erros
- [ ] Testes cobrindo caminho feliz **e** falhas de LLM (timeout > 10s) — pendente
- [ ] Persistência conectada ao frontend Next.js — pendente

## TN-3 · Página "Decisões Técnicas" — `open`

Lista as decisões de arquitetura com status (pendente / decidida / revisada).

- [ ] Definir estrutura de dados da decisão (id, título, status, justificativa)
- [ ] Scaffold da rota `/decisoes` (Claude Code)
- [ ] Conectar ao backend (novo endpoint `/decisoes`)
- [ ] Critério de aceite: página lista decisões com status filtrável
