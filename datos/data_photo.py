# Archivo: datos/data_photo.py
from datos.conexion_db import obtener_conexion

def insertar_foto(photo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO photos (id, album_id, title, url, thumbnail_url) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (photo.id, photo.album_id, photo.title, photo.url, photo.thumbnail_url))
        conexion.commit()
    except Exception as e:
        print(f"Error al insertar la foto: {e}")
    finally:
        conexion.close()

def obtener_fotos_db():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM photos")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener las fotos: {e}")
        return []
    finally:
        conexion.close()