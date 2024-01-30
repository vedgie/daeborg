import nextcord
import re
import random
import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(intents=intents)

image_counter = 0
post_amount = {}

def contains_url(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return bool(url_pattern.search(text))

post_amount = random.randint(15, 20)
print (f"Post Amount: {post_amount}")

@bot.event
async def on_message(message):
        if message.attachments or message.embeds or contains_url(message.content):
            global image_counter
            global post_amount
            image_counter += 1
            print(f"Image counter: {image_counter}")

            if image_counter == post_amount:
                image_counter = 0
                post_amount = random.randint(15, 20)
                print (f"Post Amount: {post_amount}")
                await message.channel.send("jfc bro")

        await bot.process_commands(message)

bot.run(os.getenv('BOT_TOKEN'))