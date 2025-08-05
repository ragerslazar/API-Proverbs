from api.v1.models.Database import Database

class ProverbsController:
    def __init__(self):
        self.db = Database()

    def getProverbById(self, id: int):
        return self.db.query("SELECT * FROM proverbs WHERE id_proverb = %s", [id])

    def deleteProverbById(self, id: int):
        return self.db.query("DELETE FROM proverbs WHERE id_proverb = %s", [id])

    def getRandomProverb(self):
        return self.db.query("SELECT * FROM proverbs ORDER BY RANDOM() LIMIT 1")

    def addProverb(self, proverb: str, author: str):
        return self.db.query("INSERT INTO proverbs (proverb, author) VALUES (%s, %s)", [proverb, author])