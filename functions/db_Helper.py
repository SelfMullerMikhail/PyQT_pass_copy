import os
import sqlite3

class Db_helper():
    def __init__(self):
        self.PATH = os.path.join( os.path.dirname( __file__ ))
        self.PATH = self.PATH.replace("functions", "drinks.db")

    def get_list(self, query):
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.conn.close()
        return self.result

    def get_tuple(self, query):
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        self.conn.close()
        return self.result

    def insert(self, query):
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()

## EXAMPLE

helper = Db_helper()
# helper.insert("INSERT INTO drinksMenu (name, price) VALUES ('Cacao', 300);")
print(helper.get_list("SELECT id, name, price FROM drinksMenu"))