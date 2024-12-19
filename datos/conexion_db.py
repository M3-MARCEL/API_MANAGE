import pymysql
from auxiliares.config_db import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def obtener_conexion():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )