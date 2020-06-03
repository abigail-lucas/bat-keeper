from config import DISCORD_TOKEN
from bot import PickMe

# from db_connector import cur
# from models import Role


def main():
    '''
    Main function for entry into the application

    - load db models
    - connect to db
    - load bot
    - start bot
    '''

    client = PickMe()
    client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
