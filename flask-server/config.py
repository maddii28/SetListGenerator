import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_NAME = os.getenv("name")
    DB_USER = os.getenv("user")
    DB_PASSWORD = os.getenv("password")
    DB_HOST = os.getenv("host", "localhost")
    DB_PORT = os.getenv("port", "1234")