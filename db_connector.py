import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

db = mysql.connector.connect(host=MYSQL_HOST,
                             user=MYSQL_USER,
                             passwd=MYSQL_PASSWORD,
                             db=MYSQL_DB)
cur = db.cursor()
