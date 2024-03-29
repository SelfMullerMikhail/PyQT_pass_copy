import os
import sqlite3
from loger_func.decoration import func_loger

class Db_helper():
    def __init__(self, BD) -> None:
        self.PATH = os.path.join( os.path.dirname( __file__ ))
        self.PATH = self.PATH.replace("functions", BD)

    @func_loger
    def get_list(self, query) -> list:
        self.conn = sqlite3.connect(self.PATH) 
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return self.result
    
    def get_one_obj(self, query) -> int:
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        if self.result != None:
            return self.result[0]
        else:
            return 0
    
    

    @func_loger
    def get_one(self, query) -> tuple:
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        return self.result

    @func_loger
    def insert(self, query) -> None:
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def select_magic(self, selector, from_table = None, where = None, group = None, order = None):
        self.conn = sqlite3.connect(self.PATH)
        self.cursor = self.conn.cursor()
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
        self.cursor.close()
        self.conn.close()
        return result