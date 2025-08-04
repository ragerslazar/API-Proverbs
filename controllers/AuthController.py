from models.Database import Database

class AuthController:
    def __init__(self):
        self.db = Database()

    def login(self, username: str, password: str):
        return self.db.query("SELECT * FROM users WHERE username = %s AND password = %s", [username, password])