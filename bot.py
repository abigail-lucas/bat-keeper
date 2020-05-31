import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class PickMe(discord.Client):
    '''
    PickMe bot
    '''

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")

client = PickMe()
client.run(TOKEN)
