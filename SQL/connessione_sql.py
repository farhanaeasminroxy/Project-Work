'''
import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)'''

import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    auth_plugin='mysql_native_password'  # Add this line
)

print("Connection successful!")
cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
print("Connected to database:", cursor.fetchone()[0])
cursor.close()
conn.close()