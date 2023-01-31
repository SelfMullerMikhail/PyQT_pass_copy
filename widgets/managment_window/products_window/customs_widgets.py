from PyQt6.QtWidgets import QPushButton, QComboBox
from functions.db_Helper import Db_helper

class CustomButtonDell(QPushButton):
    def __init__(self, name, window, text = ''):
        super().__init__(text = text)
        self.window_ = window
        self.helper = Db_helper("Alpha.db")
        self.name = name
        self.clicked.connect(self.func)

    def func(self):
        self.helper.insert(f"""DELETE FROM AddProductTransaction WHERE name_product = '{self.name}'""")
        self.window_.drow_ingridients_transaction()

class CustomButtonAdd(QPushButton):
    def __init__(self, name, count, window, id_menu = None, text = ''):
        super().__init__(text = text)
        self.window_ = window
        self.helper = Db_helper("Alpha.db")
        self.count = count
        self.name = name
        self.id_menu = id_menu
        self.clicked.connect(self.func_add_product)

    def func_add_product(self):
        count = self.count.text()
        if count == "":
            count = 0
        self.helper.insert(f"""INSERT INTO AddProductTransaction (name_product, count) VALUES ('{self.name.custText}', {count})""")
        self.window_.drow_ingridients_transaction()

class CustomComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.currentTextChanged.connect(self.func)
        self.ingridients = self.helper.get_list("""SELECT name FROM Stock;""")
        self.ingridients_transaction = self.helper.get_list("""SELECT name_product FROM AddProductTransaction;""")
        
        self.all_ingridients = []
        self.already_ingridients = []

        for i in self.ingridients:
            self.all_ingridients.append(i[0])

        for i in self.ingridients_transaction:
            self.already_ingridients.append(i[0])

        for i in self.all_ingridients:
            if i not in self.already_ingridients:
                self.addItem(i)
        self.custText = self.itemText(0)

    def func(self, e):
        self.custText = e

class CustomButtonDellProduct(QPushButton):
    def __init__(self, name, window, central_window, text = ''):
        super().__init__(text = text)
        self.window_ = window
        self.helper = Db_helper("Alpha.db")
        self.name = name
        self.central_window = central_window
        self.clicked.connect(self.func)

    def func(self):
        self.helper.insert(f"""DELETE FROM Menu WHERE name = '{self.name}'""")
        self.window_.drow_products()
        self.central_window.Main_widget.menuTabWidget.clear()
        self.central_window.Main_widget.menuTabWidget.create_full_menu()