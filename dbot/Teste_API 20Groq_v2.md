# Teste_API Groq_v2

## 1. Finalidade

O `Teste_API Groq_v2.py` evolui o teste originalmente criado durante a correção do problema de indisponibilidade do modelo anterior do MoAPP.

A V2 foi concebida como uma **bancada inicial de avaliação de modelos** e tem dois objetivos distintos:

1. **Descobrir dinamicamente** quais modelos estão disponíveis para a API Key no momento da execução.
2. **Comparar de forma controlada** os modelos selecionados como candidatos para uma determinada necessidade ou perfil do MoAPP.

---

## 2. Contexto de origem

O procedimento surgiu a partir do erro:

```text
The model `llama-3.1-8b-instant` does not exist or you do not have access to it.
```

A investigação realizada mostrou que a conectividade com a Groq e a API Key eram válidas, mas o modelo anterior não estava disponível para aquela chave.

O procedimento então foi dividido conceitualmente em:

```text
API Key
   |
   v
Consulta /models
   |
   v
Modelos efetivamente disponíveis
   |
   v
Seleção de candidatos
   |
   v
Teste comparativo
```

O `openai/gpt-oss-20b` foi selecionado no teste inicial e passou a ser utilizado no `mybot_v3.py`, posteriormente validado no ambiente Azure e via Discord.

---

# 3. Arquitetura do procedimento V2

```text
GROQ_API_KEY
      |
      v
+------------------------+
| ETAPA 1                |
| GET /openai/v1/models  |
| Descoberta dinâmica    |
+------------------------+
      |
      v
Modelos acessíveis
      |
      v
+------------------------+
| MODELOS_TESTE          |
| Seleção controlada     |
+------------------------+
      |
      v
Validação contra a lista
retornada pela API
      |
      v
+------------------------+
| ETAPA 2                |
| Benchmark              |
| POST /chat/completions |
+------------------------+
      |
      v
HTTP + Tempo + Tokens + Resposta
      |
      v
Resumo comparativo
```

---

# 4. Segurança da API Key

A V2 não grava a chave diretamente no código.

Ela utiliza:

```text
GROQ_API_KEY
```

via variável de ambiente, normalmente através de um arquivo `.env`:

```text
GROQ_API_KEY=sua_chave_aqui
```

O `.env` não deve ser enviado ao GitHub.

---

# 5. Descoberta dinâmica dos modelos

O endpoint utilizado é:

```text
https://api.groq.com/openai/v1/models
```

A finalidade desta etapa é responder:

> **Quais modelos estão disponíveis para esta API Key agora?**

O script registra:

- status HTTP;
- tempo da consulta;
- IDs dos modelos retornados;
- quantidade total.

Isso evita depender de listas antigas ou de assumir que um modelo continuará disponível indefinidamente.

---

# 6. Descoberta não significa equivalência

A lista `/models` pode conter modelos especializados em:

- conversação;
- segurança;
- proteção de prompts;
- áudio;
- outras finalidades.

Por esse motivo, a V2 não testa automaticamente todos os modelos com a mesma pergunta.

Os candidatos são definidos explicitamente em:

```python
MODELOS_TESTE = [
    ...
]
```

Um modelo somente é benchmarkado quando:

```text
Está em MODELOS_TESTE
        E
Está disponível para a API Key atual
```

---

# 7. Benchmark controlado

Todos os modelos válidos recebem:

- o mesmo `SYSTEM_PROMPT`;
- a mesma pergunta;
- a mesma `temperature`;
- o mesmo `MAX_TOKENS`.

Isso produz uma comparação operacional inicial.

Entretanto, um único cenário não é suficiente para determinar definitivamente o melhor modelo. Qualidade e adequação dependem da tarefa e do perfil.

---

# 8. Métricas

## HTTP

Indica o resultado da chamada.

## Tempo

É o tempo total observado pelo script entre o envio da requisição e o recebimento da resposta completa.

Ele deve ser interpretado como:

> **latência observada neste cenário e nesta execução.**

Não representa isoladamente apenas o tempo interno do modelo.

## Prompt tokens

Tokens enviados ao modelo, incluindo o system prompt e a pergunta.

## Completion tokens

Tokens gerados pelo modelo na resposta.

## Total tokens

Total informado pela API, normalmente correspondente à soma:

```text
prompt_tokens + completion_tokens
```

---

# 9. Como interpretar os resultados

O modelo com menor latência não é necessariamente o melhor.

A escolha deve considerar:

```text
Adequação ao perfil
        +
Qualidade da resposta
        +
Aderência às instruções
        +
Latência
        +
Consumo
        +
Confiabilidade
```

A V2 mede diretamente os componentes quantitativos e apresenta a resposta completa para avaliação qualitativa.

---

# 10. Aplicação aos futuros perfis do MoAPP

O objetivo do procedimento é evitar que o MoAPP fique preso a uma escolha única de modelo.

A evolução esperada é:

```text
MoAPP
 |
 +-- Perfil Pirate
 |      |
 |      +-- modelo selecionado por benchmark
 |
 +-- Perfil Governança de IA
 |      |
 |      +-- modelo selecionado por benchmark
 |
 +-- Futuro Perfil X
        |
        +-- modelo selecionado por benchmark
```

Perfis diferentes podem priorizar critérios diferentes.

Um perfil conversacional pode valorizar mais:

- baixa latência;
- naturalidade;
- eficiência.

Um perfil analítico pode dar maior peso a:

- capacidade de análise;
- precisão;
- consistência;
- aderência a instruções.

---

# 11. Roadmap de evolução

## V2.0 — Descoberta + benchmark básico

**Implementado**

Inclui:

- leitura da chave por variável de ambiente;
- descoberta dinâmica;
- validação dos candidatos;
- benchmark controlado;
- HTTP;
- latência observada;
- prompt tokens;
- completion tokens;
- total tokens;
- resposta completa;
- resumo comparativo.

---

## V2.1 — Múltiplos cenários

Substituir a pergunta única por uma bateria, por exemplo:

```text
Cenário 1 — Conversação simples
Cenário 2 — Análise
Cenário 3 — Instrução complexa
Cenário 4 — Resposta curta
Cenário 5 — Aderência à persona
```

---

## V2.2 — Benchmark por perfil

Criar conjuntos de cenários próprios para cada perfil:

```python
PERFIS = {
    "pirate": {...},
    "governanca_ia": {...}
}
```

---

## V2.3 — Execuções repetidas

Executar cada cenário diversas vezes e calcular:

- mínimo;
- máximo;
- média;
- variação;
- consumo médio;
- taxa de sucesso.

Isso reduz a influência de uma execução isolada.

---

## V2.4 — Persistência histórica

Gravar os resultados em JSON ou CSV.

Campos sugeridos:

```text
data_hora
modelo
perfil
cenario
execucao
status
http
tempo
prompt_tokens
completion_tokens
total_tokens
resposta
```

---

## V2.5 — Avaliação qualitativa

Adicionar critérios como:

| Critério | Escala |
|---|---|
| Correção | 1–5 |
| Clareza | 1–5 |
| Aderência à instrução | 1–5 |
| Aderência ao perfil | 1–5 |
| Objetividade | 1–5 |

Essa camada é necessária porque latência e tokens não determinam sozinhos a qualidade.

---

## V2.6 — Relatório automático

Gerar um relatório consolidado com:

- modelos;
- cenários;
- métricas;
- respostas;
- comparativos;
- histórico;
- recomendação baseada em critérios definidos.

---

## V3.0 — Bancada formal de avaliação de modelos

A proposta final é transformar o procedimento em uma ferramenta de governança da seleção de modelos:

```text
MODELOS DISPONÍVEIS
        |
        v
CATÁLOGO DE CANDIDATOS
        |
        v
PERFIS DO MoAPP
        |
        v
CENÁRIOS DE TESTE
        |
        v
EXECUÇÕES REPETIDAS
        |
        v
MÉTRICAS QUANTITATIVAS
        +
AVALIAÇÃO QUALITATIVA
        |
        v
MATRIZ DE DECISÃO
        |
        v
MODELO RECOMENDADO POR PERFIL
```

---

# 12. Procedimento de uso

1. Garantir que `GROQ_API_KEY` esteja disponível no `.env`.
2. Executar `Teste_API Groq_v2.py`.
3. Verificar a lista de modelos retornada.
4. Ajustar `MODELOS_TESTE`, se necessário.
5. Executar o benchmark.
6. Avaliar métricas e respostas.
7. Registrar a decisão adotada para o perfil em avaliação.

---

# 13. Conclusão

A principal evolução da V2 é separar duas perguntas:

> **Quais modelos estão disponíveis para a API Key agora?**

e:

> **Qual desses candidatos é mais adequado para este perfil e esta necessidade?**

A primeira é respondida dinamicamente pela API.

A segunda deve evoluir progressivamente para uma metodologia baseada em cenários, métricas quantitativas, avaliação qualitativa e histórico de resultados.

Assim, o MoAPP passa a ter uma base reutilizável para revisar e selecionar modelos à medida que novos perfis e novas demandas forem incorporados.
