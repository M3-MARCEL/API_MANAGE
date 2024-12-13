from negocio.encriptacion import Encriptador

def prueba_encriptacion():
    encriptador = Encriptador()
    texto = "mi_contraseña_segura"
    
    # Encriptar
    texto_cifrado = encriptador.encriptar(texto)
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Desencriptar
    texto_desencriptado = encriptador.desencriptar(texto_cifrado)
    print(f"Texto desencriptado: {texto_desencriptado}")

    # Comparar los resultados
    if texto == texto_desencriptado:
        print("¡La desencriptación fue exitosa!")
    else:
        print("Error en la desencriptación.")

if __name__ == "__main__":
    prueba_encriptacion()