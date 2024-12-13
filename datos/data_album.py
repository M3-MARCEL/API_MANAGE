from datos.conexion_db import obtener_conexion

def insertar_album(album):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO albums (id, user_id, title) VALUES (%s, %s, %s)"
            cursor.execute(sql, (album.id, album.user_id, album.title))
        conexion.commit()
    finally:
        conexion.close()

def obtener_albumes_db():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM albums")
            return cursor.fetchall()
    finally:
        conexion.close()