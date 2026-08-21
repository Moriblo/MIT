# Teste_API Groq_v3 — Framework de Benchmark, KPIs e Dimensionamento do Mo

## 1. Objetivo

O procedimento iniciado com `Teste_API Groq.py` evoluiu para uma **bancada de diagnóstico e benchmark da integração Groq**.

Seu objetivo não é apenas responder:

> “Este modelo funciona?”

A evolução proposta busca responder, com dados:

> **Qual modelo deve ser utilizado para qual perfil do Mo, para qual tipo de tarefa, com qual qualidade, latência, consumo, custo e restrição operacional?**

A premissa central é que o Mo poderá evoluir de uma arquitetura simples:

> **Um bot → um modelo**

para uma arquitetura orientada por decisão:

> **Perfil do Mo × Tipo de tarefa × Modelo × Qualidade × Latência × Consumo × Custo × Limites**

---

# 2. Princípio metodológico dos KPIs

Cada KPI deve ser documentado com seis elementos:

1. **Objetivo** — o que o indicador procura medir;
2. **Métrica ou fórmula** — como o valor é calculado;
3. **Variáveis** — quais dados participam do cálculo;
4. **Fonte das variáveis** — de onde cada dado é obtido;
5. **Exemplo** — aplicação prática da métrica;
6. **Uso na decisão** — como o resultado ajuda a escolher ou dimensionar um modelo.

## 2.1 Classificação das fontes de dados

| Tipo de dado | Fonte |
|---|---|
| **API** | Campos retornados pela resposta da Groq |
| **Script** | Valores calculados pelo `Teste_API Groq_v3.py` |
| **Configuração** | Parâmetros definidos na requisição ou no ambiente |
| **Groq Console** | Limites, consumo e informações exibidas no console |
| **Avaliação** | Nota atribuída manualmente ou, futuramente, por mecanismo automatizado |
| **Operação** | Dados coletados durante o uso real do Mo |

Essa separação é importante para garantir rastreabilidade. Um KPI calculado não deve ser confundido com um valor retornado diretamente pela API.

---

# 3. Contexto dos testes já realizados

Os primeiros testes comparativos utilizaram:

- `openai/gpt-oss-20b`
- `qwen/qwen3.6-27b`
- `groq/compound-mini`

Todos responderam com sucesso HTTP 200 ao mesmo cenário de teste.

## 3.1 Resultado inicial observado

| Modelo | Status | Tempo | Total Tokens |
|---|---:|---:|---:|
| `openai/gpt-oss-20b` | OK | 0,36 s | 265 |
| `qwen/qwen3.6-27b` | OK | 0,66 s | 371 |
| `groq/compound-mini` | OK | 0,63 s | 685 |

Esses números são uma **fotografia de um cenário específico**, e não uma conclusão definitiva sobre desempenho, eficiência ou custo.

Os resultados podem variar conforme:

- system prompt;
- tamanho da pergunta;
- contexto enviado;
- `temperature`;
- `max_tokens`;
- comportamento do modelo;
- tamanho da resposta;
- cenário de teste;
- disponibilidade e carga do serviço.

---

# 4. KPIs de disponibilidade e confiabilidade

## KPI 1 — Taxa de Sucesso

### Objetivo
Medir o percentual de requisições concluídas com resposta válida.

### Fórmula

```text
Taxa de Sucesso (%) =
(Requisições com sucesso / Total de requisições) × 100
```

### Variáveis e fontes

| Variável | Significado | Fonte |
|---|---|---|
| Requisições com sucesso | Chamadas com resposta considerada válida | Script/API |
| Total de requisições | Todas as tentativas realizadas | Script |

### Exemplo

Foram realizados 100 testes:

- 97 retornaram sucesso;
- 3 apresentaram erro.

```text
Taxa de Sucesso = (97 / 100) × 100 = 97%
```

### Uso
Permite comparar a confiabilidade operacional dos modelos.

---

## KPI 2 — Taxa de Erro

### Objetivo
Medir a proporção de requisições que falharam.

### Fórmula

```text
Taxa de Erro (%) =
(Requisições com erro / Total de requisições) × 100
```

### Variáveis e fontes

| Variável | Fonte |
|---|---|
| Requisições com erro | Script/API |
| Total de requisições | Script |

### Exemplo

```text
3 erros / 100 requisições = 3%
```

### Uso
Ajuda a identificar modelos instáveis ou problemas de integração.

---

## KPI 3 — Disponibilidade do Modelo

### Objetivo
Confirmar se o modelo está efetivamente acessível pela API Key e pelo projeto utilizados.

### Métrica

Classificação simples:

```text
Disponível / Indisponível / Erro de autenticação /
Erro de limite / Erro temporário
```

### Variáveis e fontes

| Variável | Fonte |
|---|---|
| HTTP Status | API |
| Corpo da resposta | API |
| Mensagem de erro | API |

### Exemplo

O modelo `llama-3.1-8b-instant` retornou:

```text
The model does not exist or you do not have access to it.
```

Classificação:

```text
Indisponível para a credencial/projeto atual
```

### Uso
É o primeiro filtro do processo. Um modelo indisponível não deve seguir para o benchmark funcional.

---

# 5. KPIs de performance

## KPI 4 — Tempo de Resposta

### Objetivo
Medir quanto tempo uma requisição leva para retornar.

### Fórmula

```text
Tempo de Resposta = Timestamp final - Timestamp inicial
```

### Variáveis e fontes

| Variável | Fonte |
|---|---|
| Timestamp inicial | Script |
| Timestamp final | Script |

### Exemplo observado

Para o `openai/gpt-oss-20b`:

```text
Tempo = 0,36 s
```

### Uso
Ajuda a decidir se um modelo é adequado para interação conversacional em tempo real.

---

## KPI 5 — Latência Média

### Objetivo
Reduzir o efeito de uma única execução isolada.

### Fórmula

```text
Latência Média =
Soma dos tempos de resposta / Número de execuções
```

### Exemplo

Cinco execuções:

```text
0,40 + 0,35 + 0,42 + 0,38 + 0,45 = 2,00 s

Latência média = 2,00 / 5 = 0,40 s
```

### Fonte das variáveis

Os tempos individuais são coletados pelo script.

### Uso
Permite comparação mais confiável entre modelos.

---

## KPI 6 — Variação de Latência

### Objetivo
Avaliar estabilidade de desempenho.

### Métrica inicial

```text
Variação = Tempo máximo - Tempo mínimo
```

### Exemplo

Tempos:

```text
0,35 s
0,40 s
0,75 s
0,38 s
```

```text
Variação = 0,75 - 0,35 = 0,40 s
```

### Uso
Dois modelos podem ter a mesma latência média, mas um deles pode apresentar picos mais imprevisíveis.

---

# 6. KPIs de consumo

## KPI 7 — Prompt Tokens

### Objetivo
Medir o consumo associado à entrada.

Inclui, conforme a requisição:

- system prompt;
- contexto;
- histórico;
- pergunta do usuário.

### Fonte

Campo retornado pela API:

```text
usage.prompt_tokens
```

### Uso
É especialmente importante para medir o impacto das personas e do contexto do Mo.

### Exemplo

Uma persona curta consome 200 Prompt Tokens.

Após adicionar contexto e regras:

```text
Prompt Tokens = 1.200
```

Mesmo com a mesma pergunta do usuário, o custo e o consumo potencialmente aumentam.

---

## KPI 8 — Completion Tokens

### Objetivo
Medir os tokens produzidos pelo modelo.

### Fonte

```text
usage.completion_tokens
```

### Uso
Ajuda a identificar modelos excessivamente verbosos ou respostas inadequadamente longas.

### Exemplo

Pedido:

> “Responda em uma frase.”

Resultado:

```text
Completion Tokens = 600
```

Esse valor pode indicar baixa objetividade ou comportamento inadequado ao cenário.

---

## KPI 9 — Total Tokens

### Objetivo
Medir o consumo total da interação.

### Fórmula

```text
Total Tokens =
Prompt Tokens + Completion Tokens
```

### Fonte

Preferencialmente:

```text
usage.total_tokens
```

A API pode fornecer diretamente esse valor.

### Exemplo

```text
Prompt Tokens = 300
Completion Tokens = 200

Total Tokens = 500
```

### Uso
É uma variável central para análise de consumo, limites e, quando houver precificação aplicável, custo.

> **Importante:** Total Tokens não é custo financeiro. É uma medida de consumo.

---

## KPI 10 — Relação Entrada/Saída

### Objetivo
Entender a proporção entre o contexto enviado e a resposta gerada.

### Fórmula

```text
Relação Entrada/Saída =
Prompt Tokens / Completion Tokens
```

### Exemplo

```text
Prompt Tokens = 800
Completion Tokens = 200

Relação = 800 / 200 = 4
```

Interpretação:

```text
Para cada token gerado, foram enviados 4 tokens de contexto.
```

### Uso
Ajuda a identificar personas ou contextos excessivamente grandes.

---

## KPI 11 — Tamanho Médio da Resposta

### Objetivo
Comparar o volume de saída dos modelos.

### Fórmula

```text
Tamanho Médio =
Soma dos Completion Tokens / Número de respostas
```

### Fonte

Completion Tokens retornados pela API e número de execuções registrado pelo script.

### Uso
Ajuda a selecionar modelos para interações que exigem respostas curtas e objetivas.

---

# 7. KPIs de qualidade e aderência

Estes KPIs inicialmente dependem de **avaliação estruturada**, porque a API não retorna automaticamente uma nota universal de qualidade.

No futuro, parte da avaliação poderá ser automatizada.

## KPI 12 — Score de Qualidade

### Objetivo
Avaliar o valor geral da resposta.

### Componentes sugeridos

Cada resposta pode receber notas de 0 a 10 para:

- precisão;
- clareza;
- relevância;
- completude.

### Fórmula inicial

```text
Score de Qualidade =
(Precisão + Clareza + Relevância + Completude) / 4
```

### Fonte

Avaliação manual ou avaliador automatizado futuro.

### Exemplo

```text
Precisão = 9
Clareza = 8
Relevância = 10
Completude = 9

Score = (9 + 8 + 10 + 9) / 4 = 9,0
```

### Uso
Permite comparar modelos que apresentam respostas aparentemente semelhantes.

---

## KPI 13 — Aderência à Pergunta

### Objetivo
Medir se o modelo respondeu efetivamente ao que foi solicitado.

### Escala inicial

```text
0 = não respondeu
5 = respondeu parcialmente
10 = respondeu completamente e de forma adequada
```

### Fonte

Avaliação manual ou automatizada.

### Exemplo

Pedido:

> “Explique em uma frase.”

O modelo responde com 12 parágrafos.

Mesmo que o conteúdo esteja correto, a aderência à instrução pode receber nota baixa.

### Uso
Evita que qualidade conceitual seja confundida com cumprimento da tarefa.

---

## KPI 14 — Aderência à Persona

### Objetivo
Medir se o modelo respeita a identidade do perfil do Mo.

### Variáveis avaliadas

Exemplo para Pirate:

- tom adequado;
- uso moderado dos elementos da persona;
- português natural;
- ausência de roleplay;
- ausência de descrições de ações.

### Fonte

System prompt configurado + avaliação da resposta.

### Exemplo

Um modelo responde corretamente, mas:

```text
(sorri e olha para o horizonte)
```

Isso viola uma regra explícita da persona.

### Uso
É essencial para decidir qual modelo se adapta melhor a cada perfil do Mo.

---

## KPI 15 — Objetividade

### Objetivo
Medir se o tamanho da resposta é proporcional ao pedido.

### Métrica inicial

Escala de 0 a 10 baseada na diferença entre:

- extensão solicitada;
- extensão entregue;
- utilidade do conteúdo.

### Exemplo

Pedido:

> “Responda em uma frase.”

Resposta A:

```text
1 frase útil
```

Resposta B:

```text
600 tokens e múltiplos tópicos
```

A resposta A tende a obter maior score de objetividade.

### Uso
Especialmente importante para o Pirate e para interações rápidas.

---

## KPI 16 — Capacidade de Seguimento de Instruções

### Objetivo
Medir quantas instruções explícitas foram corretamente cumpridas.

### Fórmula

```text
Instruction Following (%) =
(Instruções cumpridas / Total de instruções avaliadas) × 100
```

### Exemplo

Foram avaliadas 5 instruções:

1. responder em português;
2. responder em uma frase;
3. não fazer roleplay;
4. ser breve;
5. explicar corretamente.

O modelo cumpriu 4.

```text
(4 / 5) × 100 = 80%
```

### Fonte

Regras definidas no cenário + avaliação.

### Uso
Permite medir objetivamente uma característica crítica para o funcionamento das personas.

---

# 8. KPIs de custo e sustentabilidade econômica

## Princípio fundamental

Tokens são **consumo**, não custo.

Para calcular custo financeiro, é necessário conhecer uma regra de precificação aplicável ao modelo.

Essa informação pode vir de:

- tabela oficial de preços;
- plano contratado;
- billing;
- créditos;
- preço informado pela plataforma.

A fonte da precificação deve ser registrada juntamente com o período de validade.

---

## KPI 17 — Custo de Entrada

### Objetivo
Estimar o custo dos Prompt Tokens.

### Fórmula

```text
Custo de Entrada =
(Prompt Tokens / Unidade de precificação)
× Preço da entrada
```

### Variáveis

| Variável | Fonte |
|---|---|
| Prompt Tokens | API |
| Unidade de precificação | Política de preços |
| Preço de entrada | Groq/plano/billing |

### Exemplo hipotético

> Exemplo apenas metodológico. O valor não representa necessariamente o preço da conta atual.

```text
Prompt Tokens = 2.000
Preço = US$ 1,00 por 1.000.000 tokens
```

```text
Custo = (2.000 / 1.000.000) × 1,00
Custo = US$ 0,002
```

---

## KPI 18 — Custo de Saída

### Objetivo
Estimar o custo dos Completion Tokens.

### Fórmula

```text
Custo de Saída =
(Completion Tokens / Unidade de precificação)
× Preço da saída
```

### Fonte das variáveis

- Completion Tokens: API;
- unidade e preço: política comercial aplicável.

---

## KPI 19 — Custo por Requisição

### Objetivo
Medir o custo estimado de uma interação.

### Fórmula

```text
Custo por Requisição =
Custo de Entrada + Custo de Saída
```

### Exemplo hipotético

```text
Custo de Entrada = US$ 0,002
Custo de Saída = US$ 0,006

Custo por Requisição = US$ 0,008
```

### Uso
Permite comparar economicamente modelos diferentes.

---

## KPI 20 — Custo Médio por Conversa

### Objetivo
Estimar o custo de uma interação completa com múltiplas chamadas.

### Fórmula

```text
Custo Médio por Conversa =
Custo total das chamadas da conversa /
Número de conversas
```

### Fonte

- consumo por requisição: API;
- preço: fonte de precificação;
- agrupamento das chamadas: script/operação.

### Exemplo

10 conversas consumiram US$ 2,00.

```text
Custo médio = 2,00 / 10 = US$ 0,20
```

### Uso
É mais realista que analisar uma pergunta isolada quando houver contexto e histórico.

---

## KPI 21 — Custo por Resposta Útil

### Objetivo
Relacionar gasto à qualidade efetivamente entregue.

### Fórmula

```text
Custo por Resposta Útil =
Custo Total /
Número de respostas aprovadas
```

### Variáveis

| Variável | Fonte |
|---|---|
| Custo Total | Cálculo |
| Respostas aprovadas | Avaliação de qualidade |

### Exemplo

Foram gastos US$ 10 para gerar 80 respostas aprovadas.

```text
US$ 10 / 80 = US$ 0,125
```

### Uso
Um modelo barato que gera muitas respostas inadequadas pode ter pior desempenho econômico que um modelo aparentemente mais caro.

---

## KPI 22 — Projeção de Custo Mensal

### Objetivo
Estimar sustentabilidade econômica em escala.

### Fórmula simples

```text
Projeção Mensal =
Custo Médio por Requisição
× Requisições esperadas por dia
× Dias do período
```

### Exemplo hipotético

```text
Custo médio = US$ 0,008
Uso = 500 requisições/dia
Período = 30 dias
```

```text
0,008 × 500 × 30 = US$ 120/mês
```

### Fonte

- custo por requisição: cálculo;
- volume esperado: estimativa operacional ou dados históricos.

### Uso
Permite avaliar antecipadamente o impacto financeiro de crescimento do Mo.

---

## KPI 23 — Eficiência Econômica

### Objetivo
Relacionar qualidade ao custo.

### Fórmula inicial

```text
Eficiência Econômica =
Score de Qualidade /
Custo Médio por Requisição
```

### Exemplo

Modelo A:

```text
Qualidade = 9
Custo = US$ 0,03

Eficiência = 9 / 0,03 = 300
```

Modelo B:

```text
Qualidade = 10
Custo = US$ 0,10

Eficiência = 10 / 0,10 = 100
```

### Interpretação

Segundo essa fórmula simples, o Modelo A entrega mais qualidade por unidade monetária.

> A fórmula poderá ser normalizada posteriormente para evitar distorções quando os custos forem muito pequenos.

---

# 9. KPIs estratégicos para o ecossistema Mo

## KPI 24 — Modelo × Perfil Fit

### Objetivo
Medir o grau de adequação de um modelo a uma persona específica.

### Fórmula sugerida

```text
Modelo × Perfil Fit =
(Qualidade × peso)
+ (Aderência à Persona × peso)
+ (Objetividade × peso)
+ (Seguimento de Instruções × peso)
```

### Variáveis

As notas vêm do framework de avaliação.

Os pesos serão definidos conforme o perfil.

### Exemplo

Para o Pirate:

```text
Qualidade = 9
Persona = 10
Objetividade = 9
Instruções = 8
```

Com pesos iguais:

```text
Fit = (9 + 10 + 9 + 8) / 4 = 9,0
```

### Uso
Permite escolher o modelo mais adequado para cada perfil, e não apenas o modelo com maior capacidade geral.

---

## KPI 25 — Modelo × Tarefa Fit

### Objetivo
Medir adequação a um tipo específico de demanda.

### Cenários possíveis

- conversa rápida;
- explicação conceitual;
- análise;
- resposta estruturada;
- contexto longo;
- segurança/triagem.

### Fórmula

Score médio obtido pelo modelo naquele cenário.

### Exemplo

Um modelo pode obter:

```text
Conversa rápida = 9,5
Análise complexa = 7,0
```

Outro:

```text
Conversa rápida = 7,5
Análise complexa = 9,5
```

### Uso
Fornece base para roteamento por tipo de tarefa.

---

## KPI 26 — Score Geral do Modelo

### Objetivo
Consolidar múltiplas dimensões.

### Fórmula conceitual

```text
Score Geral =
(Qualidade × peso)
+ (Persona Fit × peso)
+ (Latência Normalizada × peso)
+ (Eficiência de Tokens × peso)
+ (Eficiência Econômica × peso)
+ (Confiabilidade × peso)
```

### Fonte

Combinação dos demais KPIs.

### Importante

Os pesos não devem ser universais.

Para o Pirate, latência e objetividade podem receber maior peso.

Para um perfil analítico, qualidade e profundidade podem ser prioritárias.

---

# 10. Limites operacionais observados na conta Groq

Na tela **Organization Limits**, observada em agosto de 2026, foram identificados os seguintes limites para modelos relevantes:

| Modelo | Requests/min | Requests/dia | Tokens/min | Tokens/dia |
|---|---:|---:|---:|---:|
| `openai/gpt-oss-120b` | 30 | 1K | 8K | 200K |
| `openai/gpt-oss-20b` | 30 | 1K | 8K | 200K |
| `qwen/qwen3.6-27b` | 30 | 1K | 8K | 200K |
| `groq/compound-mini` | 30 | 250 | 70K | No limit |

Esses valores devem ser tratados como:

> **Limites observados na organização/projeto naquele momento.**

Eles não devem ser assumidos como limites universais ou permanentes.

---

# 11. KPIs de utilização dos limites

## KPI 27 — Utilização Diária de Requisições

### Fórmula

```text
Utilização de Requests (%) =
Requests utilizados / Limite diário × 100
```

### Exemplo

Para um limite de 1.000 requests/dia:

```text
Requests utilizados = 650

650 / 1.000 × 100 = 65%
```

### Fonte

- uso: logs/script/operação;
- limite: Groq Console.

---

## KPI 28 — Utilização Diária de Tokens

### Fórmula

```text
Utilização de Tokens (%) =
Tokens utilizados / Limite diário × 100
```

### Exemplo

```text
Uso = 120.000 tokens
Limite = 200.000 tokens

Utilização = 60%
```

### Uso
Permite identificar proximidade de saturação operacional.

---

## KPI 29 — Capacidade Diária Estimada

### Objetivo
Estimar quantas interações podem ser atendidas antes de atingir o limite de tokens.

### Fórmula

```text
Capacidade estimada =
Limite diário de tokens /
Tokens médios por requisição
```

### Exemplo

```text
Limite = 200.000 tokens/dia
Média = 500 tokens/requisição

Capacidade ≈ 400 requisições/dia
```

### Fonte

- limite: Groq Console;
- média de tokens: API/script.

### Uso
Mostra que o limite real pode ser atingido por tokens antes mesmo de atingir o número máximo de requests.

---

# 12. Matriz proposta para dimensionamento do Mo

O resultado dos testes deverá alimentar uma matriz semelhante a esta:

| Perfil | Tarefa | Modelo | Qualidade | Persona Fit | Latência | Tokens | Custo/Req. | Limites | Score |
|---|---|---|---:|---:|---:|---:|---:|---|---:|
| Pirate | Conversa | GPT-OSS-20B | A medir | A medir | A medir | A medir | A medir | A avaliar | A calcular |
| Governança IA | Conceitual | A definir | A medir | A medir | A medir | A medir | A medir | A avaliar | A calcular |
| Analítico | Análise | A definir | A medir | A medir | A medir | A medir | A medir | A avaliar | A calcular |
| Rápido | Pergunta curta | A definir | A medir | A medir | A medir | A medir | A medir | A avaliar | A calcular |

A matriz não deve ser preenchida por impressão isolada. Cada valor deverá ter origem identificável.

---

# 13. Roadmap da bancada de diagnóstico

## Fase 1 — Disponibilidade

**Pergunta:** o modelo funciona para a credencial atual?

Dados:

- HTTP Status;
- mensagem de erro;
- identificação do modelo.

Fonte: API.

---

## Fase 2 — Benchmark básico

**Pergunta:** como modelos diferentes se comportam diante do mesmo cenário?

Métricas:

- sucesso;
- tempo;
- Prompt Tokens;
- Completion Tokens;
- Total Tokens.

Fonte: API + script.

---

## Fase 3 — Catálogo de modelos

Objetivo:

1. consultar modelos disponíveis;
2. registrar catálogo;
3. testar candidatos;
4. registrar indisponibilidades.

---

## Fase 4 — Benchmark por cenário

Criar cenários padronizados:

- pergunta curta;
- pergunta conceitual;
- resposta estruturada;
- contexto longo;
- instruções restritivas.

---

## Fase 5 — Benchmark por persona

Cada perfil do Mo terá:

- system prompt próprio;
- conjunto de testes;
- critérios;
- pesos específicos.

---

## Fase 6 — Benchmark de custo

Quando houver precificação aplicável e verificável:

- custo de entrada;
- custo de saída;
- custo por requisição;
- custo por resposta útil;
- projeção mensal;
- eficiência econômica.

A fonte da precificação deverá ser sempre registrada.

---

## Fase 7 — Dimensionamento do Mo

Construir a matriz:

> **Perfil × Tarefa × Modelo**

A decisão poderá resultar em:

- modelo preferencial;
- modelo alternativo;
- modelo para tarefas simples;
- modelo para tarefas complexas;
- regras de roteamento.

---

## Fase 8 — Teste de carga

Avaliar:

- requests/minuto;
- requests/dia;
- tokens/minuto;
- tokens/dia;
- concorrência;
- erros por limite;
- degradação de latência.

---

## Fase 9 — Observabilidade em produção

Registrar, por requisição:

- perfil do Mo;
- tarefa/cenário;
- modelo;
- Prompt Tokens;
- Completion Tokens;
- Total Tokens;
- latência;
- sucesso/erro;
- custo estimado, quando aplicável.

O objetivo é comparar o benchmark controlado com o comportamento real.

---

# 14. Conclusão

O `Teste_API Groq_v3.py` e sua documentação passam a representar o início de um **framework de avaliação e dimensionamento do Mo**.

A questão deixa de ser:

> “Qual é o melhor modelo?”

E passa a ser:

> **Qual modelo oferece a melhor combinação de qualidade, aderência, velocidade, consumo, custo e capacidade operacional para determinado perfil e determinada tarefa?**

Os KPIs descritos neste documento fornecem uma estrutura inicial para responder essa pergunta de forma rastreável.

A evolução esperada é transformar a atual bancada de testes em uma fonte contínua de dados para decisões arquiteturais sobre o Mo, permitindo selecionar, comparar e eventualmente rotear modelos com base em evidências mensuráveis, e não apenas em percepção subjetiva.
