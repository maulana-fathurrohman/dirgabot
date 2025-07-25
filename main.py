import discord
import openai
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

openai.api_key = OPENAI_KEY

@client.event
async def on_ready():
    print(f'DirgaBot aktif sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    prompt = message.content

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message.content
        await message.channel.send(reply)
    except Exception as e:
        await message.channel.send(f"Gagal membalas: {e}")
