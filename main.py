from servicios.servicio_album import obtener_albumes, obtener_fotos
from datos.data_album import insertar_album, obtener_albumes_db
from datos.data_photo import insertar_foto, obtener_fotos_db
from negocio.encriptacion import Encriptador
from servicios.serper_test import buscar_con_serper
from modelos.album import Album
from modelos.photo import Photo

def menu():
    encriptador = Encriptador()  # Instancia de la clase Encriptador

    while True:
        print("\nMenú Principal")
        print("1. Obtener y guardar álbumes de la API")
        print("2. Obtener y guardar fotos de la API")
        print("3. Ver álbumes en la base de datos")
        print("4. Ver fotos en la base de datos")
        print("5. Encriptar y desencriptar contraseña")
        print("6. Realizar búsqueda con la API de Google (Serper)")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            albumes = obtener_albumes()
            for a in albumes:
                album = Album(a["id"], a["userId"], a["title"])
                insertar_album(album)
            print("Álbumes guardados en la base de datos.")
        elif opcion == "2":
            fotos = obtener_fotos()
            for f in fotos:
                photo = Photo(f["id"], f["albumId"], f["title"], f["url"], f["thumbnailUrl"])
                insertar_foto(photo)
            print("Fotos guardadas en la base de datos.")
        elif opcion == "3":
            albumes = obtener_albumes_db()
            print("Álbumes en la base de datos:")
            for album in albumes:
                print(album)
        elif opcion == "4":
            fotos = obtener_fotos_db()
            print("Fotos en la base de datos:")
            for foto in fotos:
                print(foto)
        elif opcion == "5":
            contraseña = input("Ingrese la contraseña a encriptar: ")
            encriptada = encriptador.encriptar(contraseña)
            print(f"Contraseña encriptada: {encriptada}")

            desencriptada = encriptador.desencriptar(encriptada)
            if contraseña == desencriptada:
                print("¡La desencriptación fue exitosa! Las contraseñas coinciden.")
            else:
                print("Error: las contraseñas no coinciden.")
        elif opcion == "6":
            busqueda = input("Ingrese el término de búsqueda: ")
            resultados = buscar_con_serper(busqueda)
            print("Resultados de la búsqueda:")
            for resultado in resultados:
                print(f"- {resultado}")
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()