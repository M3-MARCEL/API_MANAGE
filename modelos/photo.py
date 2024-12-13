class Photo:
    def __init__(self, id, album_id, title, url, thumbnail_url):
        self.id = id
        self.album_id = album_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    def __str__(self):
        return f"Photo(id={self.id}, album_id={self.album_id}, title={self.title}, url={self.url}, thumbnail_url={self.thumbnail_url})"