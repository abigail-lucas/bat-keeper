import os
from bot import PickMe
from dotenv import load_dotenv

from db_connector import cur
# from models import Role


def main():
    '''
    Main function for entry into the application

    - load db models
    - connect to db
    - load bot
    - start bot
    '''
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = PickMe()
    client.run(TOKEN)


if __name__ == '__main__':
    main()
