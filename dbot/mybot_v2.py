from dotenv import load_dotenv
import discord
import os
import requests
import re

# ============================
# CONFIGURAÇÃO
# ============================

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# ============================
# PERSONALIDADE DO PIRATE
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
- Nunca escreva:
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
    Remove ações e descrições indesejadas.
    """

    # remove qualquer coisa entre parênteses
    text = re.sub(r'\([^)]*\)', '', text)

    # remove múltiplos espaços
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# ============================
# CHAMADA AO GROQ
# ============================

def call_groq(question):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
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

        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload,
            timeout=60
        )

        data = response.json()

        # ============================
        # DEBUG
        # ============================

        print("\n========== GROQ ==========")
        print(f"Model: {data.get('model')}")
        print(f"ID: {data.get('id')}")
        print(f"Tokens: {data.get('usage', {}).get('total_tokens')}")

        if "choices" in data:
            print("\nResposta:")
            print(data["choices"][0]["message"]["content"])

        print("==========================\n")

        # ============================
        # ERROS
        # ============================

        if "error" in data:
            return f"Erro Groq: {data['error']['message']}"

        answer = data["choices"][0]["message"]["content"]

        return clean_response(answer)

    except Exception as e:
        return f"Erro ao consultar Groq: {str(e)}"

# ============================
# DISCORD
# ============================

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# ============================
# EVENTOS
# ============================

@bot.event
async def on_ready():
    print(f"Pirate está navegando como {bot.user}")

# ============================
# MENSAGENS
# ============================

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    # ============================
    # LIMPA MENSAGENS DO BOT
    # ============================

    if message.content.startswith("$clear_bot"):

        deleted = 0

        async for msg in message.channel.history(limit=None):

            if msg.author == bot.user:

                try:
                    await msg.delete()
                    deleted += 1
                except:
                    pass

        confirmation = await message.channel.send(
            f"🧹 Apaguei {deleted} mensagens do Pirate."
        )

        await confirmation.delete(delay=3)

        return

    # ============================
    # PERGUNTA AO PIRATE
    # ============================

    if message.content.startswith("$question"):

        user_question = (
            message.content
            .split("$question", 1)[1]
            .strip()
        )

        if not user_question:
            await message.channel.send(
                "Ahoy, marujo! Faça uma pergunta após o comando."
            )
            return

        async with message.channel.typing():

            response = call_groq(user_question)

        await message.channel.send(response)

# ============================
# INICIALIZAÇÃO
# ============================

bot.run(DISCORD_TOKEN)