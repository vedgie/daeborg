import nextcord
import re
import random
import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.messages = True
bot = commands.Bot(intents=intents)

image_counter = {}

def contains_url(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(text))

@bot.event
async def on_message(message):
        if message.attachments or message.embeds or contains_url(message.content):
            channel_id = message.channel.id

            if channel_id not in image_counter:
                 image_counter[channel_id] = 0

            image_counter[channel_id] += 1
            print(f"Image counter for channel {channel_id}: {image_counter[channel_id]}")

            if image_counter[channel_id] == random.randint(20, 30):
                image_counter[channel_id] = 0
                await message.channel.send("jfc bro")

        
        await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))