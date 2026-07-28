from dotenv import load_dotenv
from openai import AzureOpenAI
import discord
import os

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

if not all([DISCORD_TOKEN, AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT]):
    raise RuntimeError(
        "Configure as variáveis de ambiente: TOKEN, AZURE_OPENAI_API_KEY, "
        "AZURE_OPENAI_ENDPOINT e AZURE_OPENAI_DEPLOYMENT"
    )

# Initialize the Azure OpenAI client
openai_client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
)


def call_openai(question):
    completion = openai_client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that answers in pirate style.",
            },
            {
                "role": "user",
                "content": f"Respond like a pirate to the following question: {question}",
            },
        ],
    )
    response = completion.choices[0].message.content or ""
    print(response)
    return response


# Set up discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$question"):
        print(f"Message: {message.content}")
        message_content = message.content[len("$question"):].strip()
        print(f"Question: {message_content}")
        response = call_openai(message_content)
        print(f"Assistant: {response}")
        print("---")
        await message.channel.send(response)


client.run(DISCORD_TOKEN)
