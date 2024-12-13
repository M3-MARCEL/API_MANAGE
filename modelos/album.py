class Album:
    def __init__(self, id, user_id, title):
        self.id = id
        self.user_id = user_id
        self.title = title

    def __str__(self):
        return f"Album(id={self.id}, user_id={self.user_id}, title={self.title})"