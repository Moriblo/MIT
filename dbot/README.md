# dbot
Discord bot that answers like a pirate

# .env 
Update the .env with your discord bot token and the key from OpenAI<br>
Token for the discord bot: https://discord.com/developers/applications<br>
OpenAI key: https://platform.openai.com/account/api-keys

# hello bot
To start the bot, run the following commands:<br>
python discord_only.py

# pirate bot 
run the following commands:<br>
pip install -r requirements.txt<br>
python mybot.py

# azure agent bot
To run the bot using an Azure AI agent, use:

pip install -r requirements.txt
python mybot_azure_agent.py

Set the following environment variables in your .env file:
- TOKEN
- AZURE_AI_PROJECT_ENDPOINT
- AZURE_AI_AGENT_NAME
- AZURE_AI_AGENT_VERSION (optional, defaults to 1)

