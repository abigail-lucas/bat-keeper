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
    offline_reg = "?offline"

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")

    async def on_message(self, message):
        """
        The on_message call

        The bot handles 4 messages:
        .help
            Displays the help page
        .pickme
            Picks one user that is visible in that channel
        .pickme {amount}
            Picks users up to the amount visible in that channel (max 5)
        .pickme {amount} {role}
            Picks users up to the amount visible in that channel (max 5),
                filtered on the role.
        """
        message_content = message.content.lower()
        response = ""
        if message_content.startswith(".help"):
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

        if message_content.startswith(self.offline_reg):
            response += "Offline members:\n"
            for member in message.guild.members:
                # We filter based on viewing permissions
                if(member.permissions_in(message.channel).view_channel):
                    if(member.status.value == "offline"):
                        response += f"{member.name}\n"

        if re.match(self.command_reg, message_content):
            # The command was invoked
            # First we filter based on the visible users
            visible_members = []
            for member in message.guild.members:
                # We filter based on viewing permissions
                if(member.permissions_in(message.channel).view_channel):
                    visible_members.append(member)
            
            if re.match(self.command_amount_role_reg, message_content):
                # .pickme {amount} {role}

                # Get the amount by grabbing the index of it
                a_s = message_content.find("{") + 1
                a_e = message_content.find("}")
                amount = int(message_content[a_s:a_e])  # Between { and }

                # Get the role by grabbing the index it falls in
                # Use the end of amount as the beginning of our search
                r_s = message_content.find("{", a_e) + 1
                # Use the beginning of the role as the beginning of our search
                r_e = message_content.find("}", r_s)
                role = message_content[r_s:r_e]  # Between { and }

                pool = []
                for viable in visible_members:
                    for vrole in viable.roles:
                        if(role == vrole.name):
                            pool.append(viable)
                            break  # break makes it a bit quicker if they have a lot of roles
                if(amount > 5):  # Max 5
                    response = "You can't pick more than 5 random users"
                elif(len(pool) == 0):  # Pool needs to be more than 0
                    response = f"There are no users matching the role `{role}`"
                elif(len(pool) < amount):  # And bigger than the amount
                    response = "There aren't enough users to pick from!"
                else:
                    picked_users = []
                    i = 0
                    while i < amount:
                        # I opted for a while loop to exclude duplicates
                        option = pool[random.randint(0, len(pool)-1)]
                        if option not in picked_users:
                            picked_users.append(option)
                            i += 1
                    for picked in picked_users:
                        # Ping or we can do this:
                        # picked_name = picked.nick if picked.nick is not None else picked.name
                        response += f"I have picked <@{picked.id}>\n"
            elif re.match(self.command_amount_reg, message_content):
                # .pickme {amount}
                a_s = message_content.find("{") + 1
                a_e = message_content.find("}")
                amount = int(message_content[a_s:a_e])
                # The pool is all of the visible members
                pool = visible_members
                if(amount > 5):
                    response = "You can't pick more than 5 random users"
                elif(len(pool) < amount):
                    response = "There aren't enough users to pick from!"
                else:
                    # This could be moved to a function perhaps
                    # This is identical to the first if-statement
                    picked_users = []
                    i = 0
                    while i < amount:
                        option = pool[random.randint(0, len(pool)-1)]
                        if option not in picked_users:
                            picked_users.append(option)
                            i += 1
                    for picked in picked_users:
                        response += f"I have picked <@{picked.id}>\n"
            else:
                # .pickme
                pool = visible_members
                picked = pool[random.randint(0, len(pool)-1)]
                response = f"I have picked <@{picked.id}>"

        if response != "":
            await message.channel.send(response)

client = PickMe()
client.run(TOKEN)
