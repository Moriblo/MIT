# Correção do Bug de Integração com a Groq — mybot_v3

## 1. Objetivo

Esta versão corrige o erro apresentado pelo bot no Discord:

`The model llama-3.1-8b-instant does not exist or you do not have access to it.`

O diagnóstico confirmou que a API Key da Groq e a conectividade com a API continuam funcionando. O problema estava no modelo configurado no bot, que deixou de estar disponível para a API Key/projeto utilizado.

## 2. Diagnóstico realizado

Foi consultado o endpoint de modelos da Groq utilizando a mesma API Key usada pelo ambiente do bot.

Resultado:

- HTTP 200
- API Key válida
- Conectividade com a Groq funcionando
- 13 modelos disponíveis para a chave/projeto

O modelo `llama-3.1-8b-instant` não apareceu entre os modelos disponíveis.

Também foram realizados testes de chamada com:

- `openai/gpt-oss-20b`
- `qwen/qwen3.6-27b`
- `groq/compound-mini`

Os três responderam corretamente. O `openai/gpt-oss-20b` apresentou o melhor resultado inicial para substituição, combinando menor tempo de resposta, menor consumo de tokens no teste e resposta adequada.

## 3. Alteração principal

Modelo anterior:

`llama-3.1-8b-instant`

Novo modelo:

`openai/gpt-oss-20b`

Na versão 3, o nome do modelo foi centralizado na constante:

`GROQ_MODEL = "openai/gpt-oss-20b"`

A chamada à API passa a utilizar:

`"model": GROQ_MODEL`

Isso facilita futuras substituições de modelo, caso necessário.

## 4. Melhorias adicionais na integração com a Groq

Além da substituição do modelo, foram incluídas melhorias restritas ao tratamento da integração:

- validação da existência da variável `GROQ_API_KEY`;
- inclusão do código HTTP nas informações de debug;
- exibição mais clara de erros retornados pela API;
- tratamento específico para timeout;
- tratamento de erros de comunicação com a API;
- proteção contra respostas inesperadas ou incompletas da Groq.

## 5. O que não foi alterado

Esta versão não altera a lógica funcional existente do bot.

Permanecem inalterados:

- estrutura de integração com o Discord;
- `SYSTEM_PROMPT`;
- personalidade atual;
- comando `$question`;
- comando `$clear_bot`;
- função `clean_response()`;
- intents do Discord;
- eventos `on_ready()` e `on_message()`;
- fluxo de recebimento e envio de mensagens;
- estrutura do arquivo `.env`;
- arquitetura geral do bot.

As referências textuais existentes a `Pirate` também foram mantidas deliberadamente nesta correção, para não misturar a correção técnica da integração com a Groq com a evolução funcional e de identidade do Mo.

## 6. Token do Discord

Não é necessário reinserir o token do Discord no código.

O arquivo continua utilizando:

`DISCORD_TOKEN = os.getenv("TOKEN")`

Portanto, o token deve permanecer configurado no arquivo `.env` do ambiente onde o bot é executado, com uma estrutura equivalente a:

`TOKEN=seu_token_do_discord`

Da mesma forma, a chave da Groq continua sendo obtida por:

`GROQ_API_KEY = os.getenv("GROQ_API_KEY")`

com:

`GROQ_API_KEY=sua_chave_da_groq`

O arquivo `.env` não deve ser incluído no repositório público nem precisar ser modificado apenas para esta correção, desde que já contenha as variáveis corretas.

## 7. Próximo teste

Após substituir o arquivo executado pelo ambiente pela versão `mybot_v3.py`, o teste esperado é:

1. iniciar o bot;
2. confirmar a conexão com o Discord;
3. enviar uma pergunta utilizando `$question`;
4. verificar no console o retorno HTTP 200 da Groq;
5. confirmar que a resposta é enviada normalmente ao Discord.

## 8. Escopo da versão

A versão 3 representa uma correção de compatibilidade da integração com a Groq, acompanhada de melhorias de diagnóstico e tratamento de erro.

Não representa uma mudança funcional ou arquitetural do bot.
