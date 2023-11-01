from os import getenv

class cloudConfig:
    CLOUD_NAME = getenv("CLOUD_NAME")
    API_KEY = getenv("API_KEY")
    API_SECRET = getenv("API_SECRET")
class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    MYSQL_HOST = getenv("MYSQL_HOST")
    MYSQL_USER = getenv("MYSQL_USER")
    MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = getenv("MYSQL_DATABASE")
    

