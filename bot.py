import os
import re
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class PickMe(discord.Client):
    '''
    PickMe bot
    '''
    command_reg = "(.pickme {\d} {\D*})|(.pickme {\d})|(.pickme)"
    command_amount_role_reg = "(.pickme {\d} {\D*})"
    command_amount_reg = ".pickme {\d}"

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")

    async def on_message(self, message):
        message_content = message.content.lower()
        response = ""
        if ".help" in message_content:
            # Display our help message
            response = "Welcome to PickMe!\n"
            response += "\n"
            response += "Here is the command format:\n"
            response += "```\n"
            response += "Pick a single random person visible on this channel:\n"
            response += ".pickme\n"
            response += "\n"
            response += "Pick a number of random people visible on this channel:\n"
            response += ".pickme {amount}\n"
            response += "\n"
            response += "Pick a number of random people based on the role visible on this channel:\n"
            response += ".pickme {amount} {role}\n"
            response += "```\n"
            await message.channel.send(response)
        if re.match(self.command_reg, message_content):
            # The command was invoked
            visible_members = []
            for member in message.guild.members:
                if(member.permissions_in(message.channel).view_channel):
                    visible_members.append(member)
            
            if re.match(self.command_amount_role_reg, message_content):
                a_s = message_content.find("{") + 1
                a_e = message_content.find("}")
                amount = int(message_content[a_s:a_e])
                r_s = message_content.find("{", a_e) + 1
                r_e = message_content.find("}", r_s)
                role = message_content[r_s:r_e]

                pool = []
                for viable in visible_members:
                    for vrole in viable.roles:
                        if(role == vrole.name):
                            pool.append(viable)
                if(amount > 5):
                    response = "You can't pick more than 5 random users"
                elif(len(pool) == 0):
                    response = f"There are no users matching the role `{role}`"
                elif(len(pool) < amount):
                    response = "There aren't enough users to pick from!"
                else:
                    picked_users = []
                    for i in range(amount):
                        option = pool[random.randint(0, len(pool)-1)]
                        if option not in picked_users:
                            picked_users.append(option)
                    for picked in picked_users:
                        picked_name = picked.nick if picked.nick != None else picked.name
                        response += f"I have picked {picked_name}\n"
            elif re.match(self.command_amount_reg, message_content):
                a_s = message_content.find("{") + 1
                a_e = message_content.find("}")
                amount = message_content[a_s:a_e]
                response = f"You have chosen {amount} people"
                pool = visible_members
            else:
                pool = visible_members

            # picked = pool[random.randint(0, len(pool)-1)]
            # response = f"I choose {picked}"
            # response = message.channel
            await message.channel.send(response)

client = PickMe()
client.run(TOKEN)
