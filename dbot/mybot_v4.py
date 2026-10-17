# ============================================================
# AVALBOT / PIRATE — VERSION 4.0
# ============================================================
#
# NOVA FEATURE:
#
#   $clear_all <quantidade | all>
#
# Exemplos:
#
#   $clear_all 10
#       Remove as 10 mensagens anteriores ao comando.
#
#   $clear_all 50
#       Remove as 50 mensagens anteriores ao comando.
#
#   $clear_all all
#       Remove todas as mensagens do canal, incluindo
#       a própria mensagem que contém o comando.
#
# ============================================================


# ============================
# IMPORTAÇÕES
# ============================

from dotenv import load_dotenv

import asyncio
import discord
import os
import requests
import re


# ============================
# CONFIGURAÇÃO
# ============================

# Identificação da versão atualmente em execução.
# Essa informação será exibida nos logs quando o bot iniciar.
BOT_VERSION = "4.0"


# Carrega as variáveis de ambiente definidas no arquivo .env.
#
# Exemplo:
#
# TOKEN=seu_token_do_discord
# GROQ_API_KEY=sua_chave_da_groq
load_dotenv()


# Token utilizado pelo bot para se conectar ao Discord.
DISCORD_TOKEN = os.getenv("TOKEN")


# Chave utilizada para autenticar as chamadas à API da Groq.
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# Endpoint da API da Groq compatível com o padrão OpenAI.
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


# Modelo atualmente utilizado pelo Pirate.
GROQ_MODEL = "openai/gpt-oss-20b"


# ============================
# PERSONALIDADE
# ============================

SYSTEM_PROMPT = """
Você é Pirate, um assistente virtual inteligente, educado e divertido.

Sua personalidade:

- Você tem o espírito de um capitão pirata experiente.
- É amigável e prestativo.
- Explica assuntos complexos de forma clara.
- Tem senso de humor leve.
- Responde preferencialmente em português.

Você pode usar ocasionalmente expressões como:

- Ahoy!
- Marujo
- Capitão
- Tesouro
- Navegar pelos mares

Mas sem exageros.

REGRAS IMPORTANTES:

- Nunca faça roleplay.
- Nunca descreva ações.
- Nunca escreva emoções.
- Nunca escreva indicações de cena.
- Nunca utilize texto entre parênteses para representar ações.

Nunca escreva:

(sorri)
(pausa)
(olha para o horizonte)
(in a pirate accent)
(laughs)

Responda sempre apenas com texto normal.

Seja útil antes de ser engraçado.
"""


# ============================
# UTILIDADES
# ============================

def clean_response(text):
    """
    Remove possíveis descrições ou ações entre parênteses e
    normaliza espaços extras na resposta recebida da IA.
    """

    # Remove conteúdos simples entre parênteses.
    #
    # Exemplo:
    # "Olá, marujo! (sorri)" -> "Olá, marujo!"
    text = re.sub(r"\([^)]*\)", "", text)

    # Substitui múltiplos espaços e quebras de linha
    # por um único espaço.
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================
# CHAMADA À GROQ
# ============================

def call_groq(question):
    """
    Envia uma pergunta para a API da Groq e retorna a resposta
    do modelo após o tratamento realizado por clean_response().
    """

    # Verifica se a chave da API foi configurada.
    if not GROQ_API_KEY:
        return "Erro: GROQ_API_KEY não configurada."

    # Cabeçalhos HTTP utilizados para autenticação e comunicação
    # com a API.
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    # Corpo da requisição enviado ao modelo.
    payload = {
        "model": GROQ_MODEL,
        "temperature": 0.7,
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ]
    }

    try:

        # Realiza a chamada à API.
        #
        # timeout=60 evita que o programa fique aguardando
        # indefinidamente em caso de problemas de comunicação.
        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        # Converte a resposta recebida para JSON.
        data = response.json()

        # ============================
        # DEBUG
        # ============================
        #
        # Essas informações aparecem apenas no terminal onde
        # o bot está sendo executado. Elas são úteis para
        # diagnóstico e acompanhamento das chamadas.
        print("\n========== GROQ ==========")
        print(f"HTTP Status: {response.status_code}")
        print(f"Model: {data.get('model')}")
        print(f"ID: {data.get('id')}")
        print(f"Tokens: {data.get('usage', {}).get('total_tokens')}")

        if "choices" in data:
            print("\nResposta:")
            print(data["choices"][0]["message"]["content"])

        if "error" in data:
            print("\nErro:")
            print(data["error"])

        print("==========================\n")

        # ============================
        # TRATAMENTO DE ERROS
        # ============================

        # Algumas respostas da API podem conter um objeto "error".
        if "error" in data:
            return (
                "Erro Groq: "
                f"{data['error'].get('message', 'Erro desconhecido')}"
            )

        # Verifica se a requisição HTTP foi concluída com sucesso.
        if not response.ok:
            return f"Erro Groq: HTTP {response.status_code}"

        # Extrai o texto produzido pelo modelo.
        answer = data["choices"][0]["message"]["content"]

        # Limpa a resposta antes de enviá-la ao Discord.
        return clean_response(answer)

    except requests.exceptions.Timeout:
        return (
            "Erro: a Groq demorou mais do que o tempo limite "
            "para responder."
        )

    except requests.exceptions.RequestException as e:
        return f"Erro ao consultar Groq: {str(e)}"

    except (KeyError, IndexError, TypeError) as e:
        return f"Erro ao processar a resposta da Groq: {str(e)}"


# ============================
# DISCORD — CONFIGURAÇÃO
# ============================

# Os intents definem quais tipos de eventos o bot pode receber.
intents = discord.Intents.default()

# Permite que o bot leia o conteúdo das mensagens.
#
# Essa permissão também precisa estar habilitada para o bot
# no Discord Developer Portal.
intents.message_content = True


# Cria o cliente que manterá a conexão com o Discord.
bot = discord.Client(intents=intents)


# ============================
# EVENTOS DO DISCORD
# ============================

@bot.event
async def on_ready():
    """
    Executado quando o Pirate consegue se conectar ao Discord.
    """

    print(
        f"🏴‍☠️ Pirate V{BOT_VERSION} está navegando como {bot.user}"
    )


# ============================
# MENSAGENS DO DISCORD
# ============================

@bot.event
async def on_message(message):
    """
    Executado sempre que uma nova mensagem é enviada em um
    canal que o Pirate consegue acompanhar.
    """

    # Evita que o bot processe as próprias mensagens como
    # novas solicitações.
    if message.author == bot.user:
        return


    # =========================================================
    # FEATURE V4 — LIMPEZA DO HISTÓRICO DO CANAL
    # =========================================================
    #
    # Sintaxe:
    #
    #   $clear_all <quantidade>
    #   $clear_all all
    #
    # Exemplos:
    #
    #   $clear_all 10
    #       Remove as 10 mensagens anteriores ao comando.
    #
    #   $clear_all all
    #       Remove todas as mensagens disponíveis no canal,
    #       incluindo a mensagem que contém o próprio comando.
    #
    # IMPORTANTE:
    #
    # O Pirate precisa possuir a permissão:
    #
    #   "Manage Messages" / "Gerenciar mensagens"
    #
    # para remover mensagens de outros usuários.
    # =========================================================

    if message.content.startswith("$clear_all"):

        # Divide a mensagem em partes.
        #
        # Exemplo:
        # "$clear_all 10" -> ["$clear_all", "10"]
        #
        # "$clear_all all" -> ["$clear_all", "all"]
        parts = message.content.strip().split()

        # -----------------------------------------------------
        # VALIDAÇÃO DA SINTAXE
        # -----------------------------------------------------
        #
        # O comando exige exatamente um argumento:
        #
        # uma quantidade numérica ou a palavra "all".
        if len(parts) != 2:

            await message.channel.send(
                "⚠️ Uso correto: `$clear_all <quantidade | all>`\n"
                "Exemplos: `$clear_all 10` ou `$clear_all all`"
            )

            return

        argument = parts[1].lower()


        # -----------------------------------------------------
        # OPÇÃO: CLEAR ALL
        # -----------------------------------------------------
        #
        # Remove todo o histórico disponível no canal.
        #
        # Como o próprio comando faz parte do histórico,
        # ele também será removido.
        if argument == "all":

            try:

                # purge(limit=None) percorre todo o histórico
                # disponível e remove as mensagens que puderem
                # ser removidas pelo bot.
                deleted = await message.channel.purge(
                    limit=None
                )

                print(
                    f"🧹 $clear_all all: "
                    f"{len(deleted)} mensagens removidas."
                )

            except discord.Forbidden:

                await message.channel.send(
                    "⚠️ Não tenho permissão para apagar mensagens "
                    "neste canal. Verifique a permissão "
                    "'Gerenciar mensagens' do Pirate."
                )

            except discord.HTTPException as e:

                print(f"Erro ao limpar o canal: {e}")

                await message.channel.send(
                    "⚠️ Ocorreu um erro ao tentar limpar o canal."
                )

            # Encerra o processamento para que o comando nunca
            # seja enviado à Groq.
            return


        # -----------------------------------------------------
        # OPÇÃO: QUANTIDADE NUMÉRICA
        # -----------------------------------------------------
        #
        # Exemplo:
        #
        #   $clear_all 10
        #
        # Significa:
        #
        #   "Apague as 10 mensagens imediatamente anteriores
        #    a esta mensagem de comando."
        #
        # A mensagem do comando também será apagada ao final,
        # deixando o canal sem o registro visual da solicitação.
        # -----------------------------------------------------

        if argument.isdigit():

            quantity = int(argument)

            # Uma quantidade igual a zero não faz sentido para
            # a operação, portanto informamos o usuário.
            if quantity <= 0:

                await message.channel.send(
                    "⚠️ Informe uma quantidade maior que zero."
                )

                return

            try:

                # history(limit=quantity + 1) inclui a mensagem
                # atual do comando dentro do conjunto recuperado.
                #
                # O +1 é necessário porque queremos selecionar
                # as mensagens ANTERIORES ao comando e também
                # remover o próprio comando no final.
                messages_to_delete = []

                async for msg in message.channel.history(
                    limit=quantity + 1,
                    oldest_first=False
                ):

                    messages_to_delete.append(msg)

                # Remove as mensagens encontradas.
                #
                # A lista normalmente conterá:
                #
                # - a mensagem "$clear_all <quantidade>";
                # - até <quantidade> mensagens anteriores.
                #
                # Portanto, se houver histórico suficiente,
                # "$clear_all 10" removerá 11 mensagens no total:
                # 10 anteriores + o próprio comando.
                deleted_count = 0

                for msg in messages_to_delete:

                    try:
                        await msg.delete()
                        deleted_count += 1

                    except discord.Forbidden:
                        print(
                            "O bot não possui permissão para "
                            "apagar uma das mensagens."
                        )
                        break

                    except discord.HTTPException as e:
                        print(
                            f"Erro ao apagar uma mensagem: {e}"
                        )

                # A confirmação é enviada somente depois que a
                # limpeza termina.
                confirmation = await message.channel.send(
                    f"🧹 Limpeza concluída: "
                    f"{deleted_count} mensagens foram removidas."
                )

                # A confirmação desaparece após 5 segundos para
                # não deixar uma mensagem permanente no histórico.
                await confirmation.delete(delay=5)

            except discord.Forbidden:

                await message.channel.send(
                    "⚠️ Não tenho permissão para apagar mensagens "
                    "neste canal. Verifique a permissão "
                    "'Gerenciar mensagens' do Pirate."
                )

            except discord.HTTPException as e:

                print(f"Erro ao limpar mensagens: {e}")

                await message.channel.send(
                    "⚠️ Ocorreu um erro ao tentar remover "
                    "as mensagens."
                )

            # Encerra o processamento para que "$clear_all"
            # nunca seja interpretado como uma pergunta à IA.
            return


        # -----------------------------------------------------
        # ARGUMENTO INVÁLIDO
        # -----------------------------------------------------
        #
        # Caso o usuário informe algo diferente de um número
        # ou da palavra "all".
        await message.channel.send(
            "⚠️ Argumento inválido.\n"
            "Use `$clear_all <quantidade | all>`.\n"
            "Exemplos: `$clear_all 10` ou `$clear_all all`."
        )

        return


    # =========================================================
    # PERGUNTA AO PIRATE
    # =========================================================
    #
    # Formato:
    #
    #   $question <sua pergunta>
    #
    # Apenas mensagens iniciadas com "$question" são enviadas
    # ao modelo de IA.
    # =========================================================

    if message.content.startswith("$question"):

        # Remove o comando "$question" e mantém somente
        # o conteúdo da pergunta.
        user_question = (
            message.content
            .split("$question", 1)[1]
            .strip()
        )

        # Verifica se o usuário realmente digitou uma pergunta.
        if not user_question:

            await message.channel.send(
                "Ahoy, marujo! Faça uma pergunta após o comando."
            )

            return

        # Exibe o indicador "digitando..." enquanto a IA
        # processa a pergunta.
        async with message.channel.typing():

            # A biblioteca requests é síncrona.
            #
            # Por isso, executamos a chamada em uma thread
            # separada para não bloquear o loop de eventos
            # assíncrono utilizado pelo Discord.
            response = await asyncio.to_thread(
                call_groq,
                user_question
            )

        # Envia a resposta produzida pela IA ao canal.
        await message.channel.send(response)


# ============================
# INICIALIZAÇÃO DO BOT
# ============================

# Inicia o Pirate e mantém sua conexão com o Discord.
bot.run(DISCORD_TOKEN)