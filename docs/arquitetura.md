# Arquitetura do Stack — Paris Group Copilot

Este documento justifica cada peça do stack em relação aos dois ativos centrais do
modelo de **Venture Studio**: **velocidade de criação de MVPs** e **reutilização
entre produtos**. A regra é: decidir uma vez, padronizar, reutilizar. O que muda
entre produtos é o problema — não a infraestrutura.

## Visão geral

```
Next.js (frontend)  ──consome OpenAPI──▶  FastAPI (api/)
                                              │
                              ┌───────────────┼───────────────┐
                              ▼                               ▼
                        PostgreSQL (dados)              Redis (cache/filas)
```

O contrato entre frontend e backend é o **schema OpenAPI** gerado automaticamente
pelo FastAPI (`/openapi.json`). Ele é a fonte de verdade que mantém os dois lados
sincronizados sem acoplamento manual.

## Decisões

### Next.js (frontend) — por que não Remix/CRA?

- **Velocidade de MVP:** roteamento por arquivo (App Router) + `create-next-app`
  entregam um app tipado e navegável em minutos. Novo MVP começa produtivo no dia 1.
- **Reutilização:** o mesmo shell de UI (layout, auth, componentes) é reaproveitado
  entre produtos do studio; só as páginas de domínio mudam.
- **Manutenção:** SSR + CSR no mesmo framework evita manter duas stacks de render.
  Remix é excelente, mas o ecossistema Next (deploy, exemplos, contratações) reduz o
  custo de onboarding de um time que roda vários produtos em paralelo.

### FastAPI (backend) — por que não Express/Django?

- **Velocidade de MVP:** o schema **OpenAPI é gerado de graça** a partir dos modelos
  Pydantic — sem escrever spec à mão. Menos retrabalho de integração com o frontend.
- **Reutilização:** Python é a língua franca de IA. Integrar LLMs, embeddings e libs
  de ML (OpenAI SDK, LangChain) é nativo — o próximo MVP com IA herda a mesma base.
  Em Express, essa camada de IA viveria fora, num serviço Python à parte de qualquer
  jeito. Django traria um ORM e admin pesados demais para um MVP enxuto.
- **Manutenção:** validação declarativa (Pydantic) concentra as regras de entrada num
  só lugar; erros de contrato aparecem cedo, não na integração.

### PostgreSQL — por que não SQLite/MongoDB?

- **Velocidade de MVP:** um Postgres em Docker Compose sobe em segundos e é idêntico
  ao de produção — zero surpresa no deploy.
- **Reutilização:** JSON nativo (`jsonb`) guarda dados semiestruturados de IA (saídas
  de LLM, metadados) sem trocar de banco quando o produto amadurece.
- **Manutenção:** SQLite não aguenta concorrência real nem roda igual em produção;
  migrar depois é retrabalho. Relacional + migrações (Alembic) dá integridade a dados
  de projetos e hipóteses que precisam ser rastreados entre MVPs.

### Redis — por que já incluir?

- **Velocidade de MVP:** chamadas a LLM são caras e lentas. Cachear respostas
  determinísticas corta custo e latência desde o primeiro produto.
- **Reutilização:** serve como broker de tarefas assíncronas (ex.: gerar relatório em
  background) — infra que todo MVP com IA vai precisar, pronta de antemão.
- **Manutenção:** um componente simples e estável; incluí-lo no stack padrão evita
  que cada produto reinvente cache e filas de formas incompatíveis.

## Segredos e ambiente

Nenhum segredo entra no repositório. O `.env.example` é o template público; o `.env`
real fica fora do controle de versão (ver `.gitignore`). O Docker Compose injeta as
variáveis (`DATABASE_URL`, `REDIS_URL`, `POSTGRES_PASSWORD`) nos serviços.

## Como subir

```bash
cp .env.example .env      # ajuste os valores se necessário
docker compose up --build # sobe db + redis + api
# API e contrato: http://localhost:8000/docs
```
