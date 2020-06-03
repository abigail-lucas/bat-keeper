from db_connector import cur


class Enum():
    '''
    Enum class for managing our enums
    '''

class AccessEnum(Enum):
    no_access = (0, "No Access")
    user_access = (1, "User Access")
    admin_access = (2, "Admin Access")

class Role():
    '''
    SQLAlchemy seems overcomplicated and peewee isn't Python3 compatible

    So I decided to write a small manager for this Role
    '''
    cursor = cur

    table = "Roles"
    name = "name"
    guild = "guild"
    access = "access"
    int_type = "int"
    varchar_255_type = "varchar(255)"

    def _get_create_query(self):
        query = f"""CREATE TABLE {self.table} (
            {self.name} {self.varchar_255_type},
            {self.guild} {self.varchar_255_type},
            {self.access} {self.int_type});
        """
        return query
    
    def _get_insert_query(self, name, guild, access):
        query = f"""INSERT INTO {self.table}
        ({self.name},{self.guild},{self.access})
        VALUES ({name}, {guild}, {access});
        """
        return query

    def create_table(self):
        self.cursor.execute(self._get_create_query())

    def add_row(self, name, guild, access=1):
        self.cursor.execute(self._get_insert_query(
            name=name, guild=guild, access=access
        ))

    def get_rows(self):
        self.cursor.execute(f"""SELECT *
        FROM {self.table}
        """)
