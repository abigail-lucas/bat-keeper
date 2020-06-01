import os
import random
import discord
import re as reg_match
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class PickMe(discord.Client):
    '''
    PickMe bot
    '''
    # regex for the commands
    command_reg = "(\?pickme {\d} {\D*})|(\?pickme {\d})|(\?pickme)"
    command_amount_role_reg = "(\?pickme {\d} {\D*})"
    command_amount_reg = "\?pickme {\d}"
    offline_reg = "(\?offline)|(\?offline {\D*})"
    offline_role_reg = "\?offline {\D*}"
    help_reg = "\?help"

    # help response
    help_response = """Welcome to PickMe!

Here is the command format:
```
?pickme                 - returns a single random user
?pickme {amount}        - returns as many random users as the amount (max 5)
?pickme {amount} {role} - returns as many random users with the role as the amount (max 5)

?offline                - returns the list of offline members
?offline {role}         - returns the lift of offline members with the given role

?help                   - returns this help message
```
"""

    def _get_members_by_role(self, role, members):
        """
        An internal method to filter member objects based on their role

        - role: string
        - members: array of Member objects

        returns array of Member objects
        """
        response = []
        for member in members:
            for member_role in member.roles:
                if(role == member_role.name):
                    response.append(member)
                    break
        return response
    
    def _get_visible_members(self, chnl, members):
        """
        An internal method to filter member objects based on their permissions
        for the channel.
        This method filters based on the view_channel permission

        - channel: Channel object
        - members: array of Member objects

        returns array of Member objects
        """
        response = []
        for member in members:
            if(member.permissions_in(chnl).view_channel):
                response.append(member)
        return response
    
    def _pick_members(self, amount, members):
        """
        An internal method to randomly pick members based on the amount given.
        The amount must exceed the length of members.
        
        - amount: int
        - members: array of Member objects

        returns array of Member objects or False if error
        """
        picked_members = []
        i = 0
        # a while loop allows us to loop until we have enough members
        if amount >= len(members):
            return picked_members
        while i < amount:
            chosen = members[random.randint(0, len(members)-1)]
            if chosen not in picked_members:
                picked_members.append(chosen)
                i += 1
        return picked_members
    
    def _get_amount_index(self, command):
        """
        A small internal method to grab the amount index.
        We can confidently grab a single character since we will never
        have more than 5 for the amount. (regex also limits to 1 digit)

        - command: string

        returns index of amount
        """
        return command.find("{") + 1

    def _get_role_indexes(self, command, start):
        """
        A small internal method to grab the indexes of the role.
        Start should be the index of the amount.

        - command: string
        - start: int

        returns array of start and stop indexes of the role
        """
        response = []
        response.append(command.find("{", start) + 1)
        response.append(command.find("}", response[0]))
        return response

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")

    async def on_message(self, message):
        """
        The on_message call
        """
        message_content = message.content.lower()

        # Help message
        if reg_match.match(self.help_reg, message_content):
            response = self.help_response
            await message.channel.send(response)

        # Offline command
        if reg_match.match(self.offline_reg, message_content):
            response = "The following members are offline:\n"
            visible_members = self._get_visible_members(chnl=message.channel,
                                                        members=message.guild.members)

            # We either filter on role or don't
            if reg_match.match(self.offline_role_reg, message_content):
                rs, re = self._get_role_indexes(message_content, 0)
                role = message_content[rs:re]

                members = self._get_members_by_role(role=role, members=visible_members)
            else:
                members = visible_members

            for member in members:
                if(member.status.value == "offline"):
                    name = member.nick if member.nick is not None else member.name
                    response += f"{name}\n"

            if response == "The following members are offline:\n":
                response += "No members are offline!"
            await message.channel.send(response)

        if reg_match.match(self.command_reg, message_content):
            response = ""
            visible_members = self._get_visible_members(chnl=message.channel,
                                                        members=message.guild.members)

            if reg_match.match(self.command_amount_role_reg, message_content):
                # Get our amount
                amount_index = self._get_amount_index(message_content)
                amount = int(message_content[amount_index])
                # Get our role
                rs, re = self._get_role_indexes(message_content, amount_index)
                role = message_content[rs:re]

                # Filter our members
                members = self._get_members_by_role(role=role, members=visible_members)
            elif reg_match.match(self.command_amount_reg, message_content):
                # Get our amount
                amount_index = self._get_amount_index(message_content)
                amount = int(message_content[amount_index])

                # No member filtering
                members = visible_members
            else:
                # Amount defaults to 1 when it isn't passed
                amount = 1
                # No member filtering
                members = visible_members

            if(amount > 5):
                response = "You can't pick more than 5 random users"
            else:
                # DUN DUN DUUUN
                chosen_members = self._pick_members(amount=amount, members=members)
                for member in chosen_members:
                    name = member.nick if member.nick is not None else member.name
                    response += f"I have picked {name}\n"
            if response == "":
                response = "No members found!"
            await message.channel.send(response)


client = PickMe()
client.run(TOKEN)
