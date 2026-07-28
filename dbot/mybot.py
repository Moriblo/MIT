from dotenv import load_dotenv
import discord
import os
import requests

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_groq(question):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": f"Respond like a pirate: {question}"}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    # ============================
    # DEBUG COLORIDO (OPÇÃO 3)
    # ============================

    def color(text, code):
        return f"\033[{code}m{text}\033[0m"

    print(color("\n=== GROQ RESPONSE ===", "94"))  # azul
    print(color(f"ID: {data.get('id')}", "92"))     # verde
    print(color(f"Model: {data.get('model')}", "93"))  # amarelo
    print(color(f"Tokens: {data.get('usage', {}).get('total_tokens')}", "95"))  # magenta
    print(color("Message:", "96"))  # ciano

    if "choices" in data:
        print(color(data["choices"][0]["message"]["content"], "97"))  # branco
    else:
        print(color("<< SEM 'choices' — provavelmente erro da API >>", "91"))  # vermelho

    print(color("=====================\n", "94"))

    # ============================
    # RETORNO PARA O DISCORD
    # ============================

    if "error" in data:
        return f"Groq error: {data['error']['message']}"

    return data["choices"][0]["message"]["content"]


# ============================
# DISCORD BOT
# ============================

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # ==========================================
    # COMANDO: LIMPAR TODAS AS MENSAGENS DO BOT
    # ==========================================

    if message.content.startswith("$clear_bot"):
        deleted = 0

        async for msg in message.channel.history(limit=None):
            if msg.author == bot.user:
                try:
                    await msg.delete()
                    deleted += 1
                except:
                    pass

        await message.channel.send(f"Apaguei {deleted} mensagens do bot.")
        return

    # ==========================================
    # COMANDO NORMAL DO BOT
    # ==========================================

    if message.content.startswith("$question"):
        user_question = message.content.split("$question", 1)[1].strip()
        response = call_groq(user_question)
        await message.channel.send(response)

bot.run(DISCORD_TOKEN)
