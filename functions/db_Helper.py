import os
import sqlite3

class Db_helper():
    def __init__(self, BD):
        self.PATH = os.path.join( os.path.dirname( __file__ ))
        self.PATH = self.PATH.replace("functions", BD)
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()

    def get_list(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return self.result

    def get_one(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        return self.result

    def insert(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def select_magic(self, selector, from_table = None, where = None, group = None, order = None):
        if from_table == None:
            result = self.cursor.execute(f"""SELECT {selector};""")
        elif where == None and group == None and order == None :
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table};""")
        elif where == None and group == None and order != None :
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} ORDER BY {order};""")
        elif where != None and group == None and order == None:
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} WHERE {where};""")
        elif where != None and group == None and order != None:
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} WHERE {where} ORDER BY {order};""")
        elif where == None and group != None and order == None:
            result =self.cursor.execute(f"""SELECT {selector} FROM {from_table} GROUP BY {group};""")
        elif where == None and group != None and order != None:
            result =self.cursor.execute(f"""SELECT {selector} FROM {from_table} GROUP BY {group} ORDER BY {order};""")
        elif where != None and group != None and order == None:
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} WHERE {where} GROUP BY '{group}';""")
        elif where != None and group != None and order != None:
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} WHERE {where} GROUP BY '{group}' ORDER BY {order};""")       
        elif where != None and group != None and order == None:
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} WHERE {where} GROUP BY '{group}';""")
        elif where != None and group != None and order != None:
            result = self.cursor.execute(f"""SELECT {selector} FROM {from_table} WHERE {where} GROUP BY '{group}' ORDER BY {order};""")
        result = self.cursor.fetchall()
        return result