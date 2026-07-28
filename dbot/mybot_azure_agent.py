from dotenv import load_dotenv
from azure.identity import ClientSecretCredential, DefaultAzureCredential
from azure.ai.projects import AIProjectClient
import discord
import os

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")
DEFAULT_PROJECT_ENDPOINT = "https://moacyrblondet-3724-resource.services.ai.azure.com/api/projects/moacyrblondet-3724"
DEFAULT_AGENT_NAME = "pirate-agent"
AZURE_AI_PROJECT_ENDPOINT = os.getenv("AZURE_AI_PROJECT_ENDPOINT", DEFAULT_PROJECT_ENDPOINT)
AZURE_AI_AGENT_NAME = os.getenv("AZURE_AI_AGENT_NAME", DEFAULT_AGENT_NAME)
AZURE_AI_AGENT_VERSION = os.getenv("AZURE_AI_AGENT_VERSION", "1")
AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

if not DISCORD_TOKEN:
    raise RuntimeError("Configure a variável de ambiente TOKEN para o Discord.")

# Initialize the Azure AI Project client and the OpenAI-compatible client
project_client = None
openai_client = None

print("Initializing Azure connectors...")


def build_credential():
    if all([AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET]):
        return ClientSecretCredential(
            tenant_id=AZURE_TENANT_ID,
            client_id=AZURE_CLIENT_ID,
            client_secret=AZURE_CLIENT_SECRET,
        )
    return DefaultAzureCredential()


try:
    credential = build_credential()
    project_client = AIProjectClient(
        endpoint=AZURE_AI_PROJECT_ENDPOINT,
        credential=credential,
    )
    openai_client = project_client.get_openai_client()
    print("Azure AI Projects agent connector ready.")
except Exception as exc:
    print(f"Azure AI Projects connector unavailable: {exc}")


def call_agent(question):
    if openai_client is None:
        error_message = (
            "Não foi possível criar o cliente do agente Azure. "
            "Configure AZURE_TENANT_ID, AZURE_CLIENT_ID e AZURE_CLIENT_SECRET para um service principal "
            "ou faça login com 'az login'."
        )
        print(error_message)
        return error_message

    try:
        response = openai_client.responses.create(
            input=[
                {
                    "role": "user",
                    "content": f"Respond like a pirate to the following question: {question}",
                }
            ],
            extra_body={
                "agent_reference": {
                    "name": AZURE_AI_AGENT_NAME,
                    "version": AZURE_AI_AGENT_VERSION,
                    "type": "agent_reference",
                }
            },
        )

        response_text = response.output_text or ""
        print(response_text)
        return response_text
    except Exception as exc:
        error_message = (
            f"Falha ao chamar o agente Azure: {exc}. "
            "Verifique se o agente existe, a versão está correta e a identidade tem acesso ao projeto."
        )
        print(error_message)
        return error_message


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        question = " ".join(sys.argv[2:]) or "hi"
        print(call_agent(question))
    else:
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
                response = call_agent(message_content)
                print(f"Assistant: {response}")
                print("---")
                await message.channel.send(response)

        client.run(DISCORD_TOKEN)
