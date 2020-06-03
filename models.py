import mysql.connector

from config import *


class Enum():
    '''
    Enum class for managing our enums
    '''

class AccessEnum(Enum):
    no_access = (0, "No Access")
    user_access = (1, "User Access")
    admin_access = (2, "Admin Access")


class BaseModel():
    '''
    SQLAlchemy seems overcomplicated and peewee isn't Python3 compatible

    So I decided to write a small manager for my models
    '''

    def __init__(self):
        self.db = mysql.connector.connect(host=MYSQL_HOST,
                                          user=MYSQL_USER,
                                          passwd=MYSQL_PASSWORD,
                                          db=MYSQL_DB)

    def _create_table(self, table, fields):
        '''
        table - string: name for the table
        fields - list of field objects
        '''
        query = "CREATE TABLE %s (" % table

        for f in fields:
            query += f"{f['name']} {f['type']}"
            if f != fields[-1]:
                query += ", "
        query += ");"

        cursor = self.db.cursor()
        cursor.execute(query)
        return query

    def create_table(self):
        return self._create_table(self.table, self.fields)


class Role(BaseModel):
    table = "Roles"

    fields = [
        {"name": "id", "type": "INT NOT NULL AUTO_INCREMENT"},
        {"name": "name", "type": "VARCHAR(255) NOT NULL"},
        {"name": "guild", "type": "VARCHAR(255) NOT NULL"},
        {"name": "access", "type": "INT NOT NULL"}
    ]
