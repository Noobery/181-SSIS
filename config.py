from os import getenv

class Config:
    MYSQL_HOST = getenv("MYSQL_HOST")
    MYSQL_USER = getenv("MYSQL_USER")
    MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
    MYSQL_DATABASE = getenv("MYSQL_DATABASE")
