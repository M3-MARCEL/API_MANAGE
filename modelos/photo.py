# Importar la clase Album
from modelos.album import Album

class Photo(Album):
    def __init__(self, id, album_id, user_id, title, url, thumbnail_url):
        # Inicializar propiedades de la clase Album
        super().__init__(album_id, user_id, None)  # 'None' porque el título del álbum no aplica aquí
        # Inicializar propiedades específicas de la clase Photo
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    def __str__(self):
        return (
            f"Photo(id={self.id}, album_id={self.album_id}, user_id={self.user_id}, "
            f"title={self.title}, url={self.url}, thumbnail_url={self.thumbnail_url})"
        )