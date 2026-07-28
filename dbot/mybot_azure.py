from dotenv import load_dotenv
from openai import OpenAI
import discord
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

DISCORD_TOKEN = os.getenv("TOKEN")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY") or "EPXIcPA5yOtlp5HxuGyH0DvWw9B3weZtJ43CrBWBOk1OETCj9GM8JQQJ99CGACYeBjFXJ3w3AAABACOGq0Cz"
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT") or "https://openai-dbot.openai.azure.com/"
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
AZURE_OPENAI_DEPLOYMENT = (os.getenv("AZURE_OPENAI_DEPLOYMENT") or "gpt-4o-mini").strip()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_KEY") or AZURE_OPENAI_API_KEY
OPENAI_MODEL = os.getenv("OPENAI_MODEL", AZURE_OPENAI_DEPLOYMENT)
AI_PROVIDER = (os.getenv("AI_PROVIDER") or "openai").strip().lower()

openai_client = None
config_error = None
ai_mode = None


def resolve_provider(env=None):
    env = env or os.environ
    azure_openai_endpoint = env.get("AZURE_OPENAI_ENDPOINT")
    azure_openai_key = env.get("AZURE_OPENAI_API_KEY")
    azure_openai_deployment = env.get("AZURE_OPENAI_DEPLOYMENT")
    openai_key = env.get("OPENAI_API_KEY") or env.get("OPENAI_KEY")

    if AI_PROVIDER == "openai" and openai_key:
        return "openai", None, None
    if AI_PROVIDER == "azure_openai" and azure_openai_endpoint and azure_openai_key and azure_openai_deployment:
        return "azure_openai", azure_openai_endpoint, azure_openai_deployment
    if AI_PROVIDER == "azure_agent":
        return "azure_agent", env.get("AZURE_AI_PROJECT_ENDPOINT"), env.get("AZURE_AI_AGENT_NAME", "pirate-agent")

    if azure_openai_endpoint and azure_openai_key and azure_openai_deployment:
        return "azure_openai", azure_openai_endpoint, azure_openai_deployment
    if openai_key:
        return "openai", None, None
    return None, None, None


if not DISCORD_TOKEN:
    config_error = "Configure a variável de ambiente TOKEN para o Discord."
else:
    ai_mode, ai_target, ai_model = resolve_provider()

    if ai_mode == "openai":
        try:
            openai_client = OpenAI(
                api_key=OPENAI_API_KEY,
                base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1/",
            )
        except Exception as exc:
            config_error = f"Falha ao inicializar o cliente OpenAI Foundry: {exc}"
    elif ai_mode == "azure_openai":
        try:
            openai_client = OpenAI(
                api_key=AZURE_OPENAI_API_KEY,
                base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip('/')}/openai/v1/",
            )
        except Exception as exc:
            config_error = f"Falha ao inicializar o cliente Azure OpenAI: {exc}"
    else:
        config_error = (
            "Configure as variáveis de ambiente para uma das opções abaixo:\n"
            "- OpenAI: OPENAI_API_KEY ou OPENAI_KEY\n"
            "- Azure OpenAI: AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT e AZURE_OPENAI_DEPLOYMENT\n"
            "- Azure AI Agent: AZURE_AI_PROJECT_ENDPOINT e AZURE_AI_AGENT_NAME"
        )

    if openai_client is not None:
        ai_mode = ai_mode or "unknown"


def call_openai(question):
    if openai_client is None:
        error_message = config_error or "Cliente Azure indisponível."
        print(error_message)
        return error_message

    if ai_mode == "azure_openai" and not AZURE_OPENAI_DEPLOYMENT:
        error_message = (
            "Configure AZURE_OPENAI_DEPLOYMENT com o nome exato do deployment criado no recurso Azure OpenAI."
        )
        print(error_message)
        return error_message

    model_name = AZURE_OPENAI_DEPLOYMENT or OPENAI_MODEL
    print(f"Using Foundry endpoint: {AZURE_OPENAI_ENDPOINT}")
    print(f"Using model/deployment: {model_name}")

    try:
        completion = openai_client.chat.completions.create(
            model=model_name,
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
    except Exception as exc:
        error_message = f"Falha ao chamar a API: {exc}"
        print(error_message)
        return error_message


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


if __name__ == "__main__":
    if not DISCORD_TOKEN:
        raise RuntimeError("Configure a variável de ambiente TOKEN para o Discord.")

    client.run(DISCORD_TOKEN)
