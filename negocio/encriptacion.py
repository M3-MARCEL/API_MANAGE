from cryptography.fernet import Fernet

class Encriptador:
    def __init__(self, clave_path: str = "clave.key"):
        self.clave_path = clave_path
        self.key = None
        self.cipher_suite = None
        self.cargar_clave()  # Carga la clave si existe, o genera una nueva

    def generar_clave(self):
        """Genera una nueva clave y la guarda en el archivo especificado."""
        self.key = Fernet.generate_key()
        with open(self.clave_path, "wb") as archivo_clave:
            archivo_clave.write(self.key)
        self.cipher_suite = Fernet(self.key)

    def cargar_clave(self):
        """Carga la clave desde el archivo, o genera una nueva si no existe."""
        try:
            with open(self.clave_path, "rb") as archivo_clave:
                self.key = archivo_clave.read()
            self.cipher_suite = Fernet(self.key)
        except FileNotFoundError:
            print(f"No se encontró el archivo {self.clave_path}. Generando una nueva clave...")
            self.generar_clave()

    def encriptar(self, texto_claro: str) -> str:
        """Encripta un texto claro y devuelve el texto cifrado."""
        texto_claro_bytes = texto_claro.encode('utf-8')
        texto_cifrado_bytes = self.cipher_suite.encrypt(texto_claro_bytes)
        return texto_cifrado_bytes.decode('utf-8')

    def desencriptar(self, texto_cifrado: str) -> str:
        """Desencripta un texto cifrado y devuelve el texto claro."""
        texto_cifrado_bytes = texto_cifrado.encode('utf-8')
        texto_claro_bytes = self.cipher_suite.decrypt(texto_cifrado_bytes)
        return texto_claro_bytes.decode('utf-8')