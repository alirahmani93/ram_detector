import sqlite3

DATABASE_FILE = "ram_data.db"


class Database:
    def __init__(self, database_file: str = DATABASE_FILE):
        self.database_file = database_file
        self.conn = None

    def __enter__(self):
        self.conn = self.connect()
        print("conn connected")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        print("conn closed")

    def connect(self):
        return sqlite3.connect(self.database_file)

    # Create the table if it doesn't exist
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ram_usage (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total INTEGER,
                free INTEGER,
                used INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def execute_and_commit(self, raw: str, parameters: tuple) -> [bool, Exception]:
        try:
            cursor = self.conn.cursor()
            cursor.execute(raw, parameters)
            self.conn.commit()
            return True, None
        except Exception as e:
            return False, e

    def get_all(self, raw: str, parameters: tuple):
        cursor = self.conn.cursor()
        cursor.execute(raw, parameters)
        data = cursor.fetchall()
        return data


connection = Database()
