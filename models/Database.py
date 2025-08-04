import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

class Database:
    def __init__(self):
        BASEDIR = os.path.abspath(os.path.dirname(__file__))
        load_dotenv(os.path.join(BASEDIR, '../.env'))

        self.dsn = os.getenv("DSN")
        self.login = os.getenv("DB_LOGIN")
        self.password = os.getenv("DB_PASSWORD")

        self.conn = psycopg2.connect(
            dsn=self.dsn,
            user=self.login,
            password=self.password
        )

        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


    def query(self, query: str, params: list = None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)

            if query.lower().startswith("select"):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
                return self.cursor.rowcount

        except Exception as e:
            print(f"SQL Error : {e}")
            self.conn.rollback()
            return None