import sys, os

from PyQt6.QtWidgets import QPushButton

sys.path.append( os.path.dirname( __file__ ).replace("widgets\main_window", ""))
from functions.db_Helper import Db_helper

class Dell_Button_Suppliers(QPushButton):
    def __init__(self, name, text, wind):
        super().__init__(text=text)
        self.wind = wind
        self.name = name
        self.helper = Db_helper("Alpha.db")
        self.clicked.connect(self.func)

    def func(self):
        self.helper.insert(f"""DELETE FROM Suppliers WHERE name = '{self.name}' """)
        self.wind.suppliers_list.setLineCount("Suppliers")
        self.wind.get_suppliers()