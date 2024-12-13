Sistema de Gestión de Álbumes y Fotos usando API y Base de Datos
Este sistema permite gestionar álbumes y fotos obtenidos de una API (jsonplaceholder.typicode.com)
y almacenarlos en una base de datos MySQL. Además, incluye funcionalidades para encriptar datos
y realizar búsquedas con la API de Serper.

Requisitos:

- Dependencias
Instalar las siguientes librerías mediante "pip":

pip install pymysql cryptography requests

- Software Requerido:

Python 3.9 o superior
MySQL (Se recomienda usar XAMPP phpMyAdmin para la gestión de la base de datos)
Visual Studio Code

- Configuración de la Base de Datos:

Script de Base de Datos
Crear la base de datos y las tablas ejecutando el siguiente script en MySQL:

-- Crear base de datos:
CREATE DATABASE api_manage CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

USE api_manage;

-- Crear tabla para álbumes
CREATE TABLE albums (
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL
);

-- Crear tabla para fotos
CREATE TABLE photos (
    id INT PRIMARY KEY,
    album_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    thumbnail_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (album_id) REFERENCES albums(id)
);

Archivos Necesarios:

1. conexion_db.py Este archivo permite conectar Python con la base de datos MySQL.

   import pymysql

   def obtener_conexion():
       return pymysql.connect(
           host="localhost",
           user="root",
           password="",
           database="api_manage"
       )

2. main.py Contiene el menú principal para ejecutar las funciones del sistema.

   Uso:
   Ejecute main.py desde el terminal:

   python main.py

   Siga las opciones del menú:
   - 1 : Obtener y guardar álbumes desde la API.
   - 2 : Obtener y guardar fotos desde la API.
   - 3 : Ver álbumes almacenados en la base de datos.
   - 4 : Ver fotos almacenadas en la base de datos.
   - 5 : Salir del programa.

3. prueba_conexion.py Verifica si la conexión con la base de datos es exitosa.

   from datos.conexion_db import obtener_conexion

   try:
       conexion = obtener_conexion()
       print("Conexión exitosa a la base de datos.")
       conexion.close()
   except Exception as e:
       print(f"Error al conectar: {e}")

   Uso:
   Ejecute prueba_conexion.py desde el terminal:

   python prueba_conexion.py

4. prueba_encriptacion.py Prueba las funciones de encriptación y desencriptación del sistema.

   from negocio.encriptacion import Encriptador

   encriptador = Encriptador()
   texto = "Texto de prueba"
   cifrado = encriptador.encriptar(texto)
   print(f"Texto encriptado: {cifrado}")
   descifrado = encriptador.desencriptar(cifrado)
   print(f"Texto desencriptado: {descifrado}")

   Uso:
   Ejecuta prueba_encriptacion.py desde la terminal:

   python prueba_encriptacion.py

5. serper_test.py Prueba la API de Serper para realizar búsquedas en Google.

   from servicios.serper_test import buscar_con_serper

   consulta = "Python programming"
   resultados = buscar_con_serper(consulta)
   print("Resultados de la búsqueda:")
   for resultado in resultados:
       print(resultado)

   Uso:
   Asegúrese de haber configurado su API Key ( https://serper.dev/api-key ) en serper_test.py. Luego ejecute:

   python serper_test.py

- Observaciones

Clave para Encriptación:
Si el archivo clave.key no existe, el sistema generará uno automáticamente.

API Key de Serper:
Asegúrese de configurar su clave de API en el archivo servicios/serper_test.py.

Menú de main.py:
El menú indicará un error si se ejecuta la opción 2 antes de la 1.
Ejecute la 1 para resolver.