# Enquadramento — Paris Group Copilot

> Contrato intelectual do produto. Toda feature futura deve ser justificável por este documento.

## Contexto

O **Paris Group Copilot** é usado por times de um **venture studio** que criam múltiplos MVPs em paralelo. O usuário principal é a **Product Manager (Marina)**, no momento de **discovery de um novo produto** — em sessões com stakeholders, sob pressão de tempo, decidindo o que construir antes de comprometer o time de engenharia.

Nesse ambiente, cada produto percorre o mesmo ciclo (Descoberta → MVP → Instrumentação → Qualidade do Modelo → Evolução), mas o aprendizado de um MVP raramente é reaproveitado no próximo.

## Dor do Usuário

**Marina perde cerca de 40 minutos por sessão de discovery reformulando hipóteses de valor do zero**, porque não existe hoje um lugar onde as hipóteses, métricas e resultados de MVPs anteriores fiquem rastreáveis e reutilizáveis. O conhecimento fica espalhado em docs soltos, Slack e na cabeça das pessoas — e some entre um produto e outro.

Isso atrasa o início do MVP e faz o studio repetir erros que já tinham sido aprendidos.

## Hipótese de Valor

**Se** o copiloto sugerir enquadramentos e hipóteses baseados em MVPs anteriores do studio,
**então** a PM conseguirá formular uma hipótese de valor testável em menos tempo e com maior consistência,
**porque** o mecanismo reaproveita o aprendizado institucional acumulado em vez de partir de uma folha em branco a cada produto.

## Métrica de Validação

- **O que melhora:** tempo para produzir uma hipótese de valor testável numa sessão de discovery.
- **Baseline:** ~40 minutos (observado hoje, sem o copiloto).
- **Meta:** menos de 10 minutos.
- **Como medir:** cronometrar a sessão de criação de hipótese com 5 PMs reais em onboarding.
- **Critério de aceite:** 4 de 5 PMs completam uma hipótese válida (o que melhora + para quem + como medir) em menos de 10 minutos.

## Fora de Escopo (MVP)

O que o produto **não fará** nesta primeira versão — delimitar é tão importante quanto construir:

1. **Não** executa nem prioriza o backlog do produto — o copiloto apoia a *formulação* da hipótese, não o gerenciamento de tarefas.
2. **Não** integra com ferramentas externas (Jira, Linear, Notion) no MVP — o foco é validar a hipótese central antes de investir em integrações.
3. **Não** gera código nem MVPs automaticamente — a IA sugere enquadramentos; a decisão e a execução seguem com o time.
