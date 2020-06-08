from config import DISCORD_TOKEN
from bot import PickMe
from models import Role

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

    # role = Role()

    # role.insert(("staff", "Lifechoices", "2"))

    client = PickMe()#table=role.get_all_data())
    client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
