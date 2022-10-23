import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'user': os.getenv("MYSQL_USER"),
    'host': os.getenv("MYSQL_HOST"),
    'port': os.getenv("MYSQL_PORT"),
    'database': os.getenv("MYSQL_DATABASE"),
    'password': os.getenv("MYSQL_PASSWORD")
}