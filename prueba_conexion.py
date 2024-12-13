from datos.conexion_db import obtener_conexion

def probar_conexion():
    try:
        conexion = obtener_conexion()
        print("¡Conexión exitosa a la base de datos!")
        conexion.close()
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    probar_conexion()