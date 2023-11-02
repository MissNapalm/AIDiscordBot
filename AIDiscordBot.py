pip install discord.py
pip install openai

import discord
import openai
import os

# Discord Bot Token (replace with your bot's token)
token = 'YOUR_DISCORD_BOT_TOKEN'

# Initialize the Discord client
client = discord.Client()

# OpenAI API Key (replace with your OpenAI API key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Don't respond to own messages

    if message.content.startswith('Hey bot'):
        # Extract the user's message after "Hey bot"
        user_input = message.content[len('Hey bot'):].strip()

        # Generate a response using ChatGPT
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"User: {user_input}\nBot:",
            max_tokens=50,  # Adjust the response length as needed
        )

        # Send the generated response to the Discord channel
        await message.channel.send(response.choices[0].text)

# Start the bot
client.run(token)
