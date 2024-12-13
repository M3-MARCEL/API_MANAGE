from servicios.serper_test import buscar_con_serper

if __name__ == "__main__":
    termino = input("Ingrese el término de búsqueda: ")
    resultados = buscar_con_serper(termino)
    print("Resultados:")
    for resultado in resultados:
        print(f"- {resultado}")