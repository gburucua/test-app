import mysql.connector
import os

class MySQLDatabase:
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect(self):
        try:
            self.db = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_DATABASE')
            )
            self.cursor = self.db.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db = None
            self.cursor = None

    def execute_query(self, query):
        self.connect()
        if not self.db or not self.cursor:
            return None
        self.cursor.execute(query)
        if query.strip().upper().startswith('SELECT'):
            result = self.cursor.fetchall()
        else:
            self.db.commit()
            result = None
        self.disconnect()
        return result
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()

    def __del__(self):
        self.disconnect()
