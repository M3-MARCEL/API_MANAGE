import pymysql

def obtener_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='api_manage',
        charset='utf8mb4'
    )