from PyQt6.QtWidgets import QGridLayout, QWidget, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, QSize

from functions.db_Helper import Db_helper


class Edit_stock_button(QPushButton):
    def __init__(self, text, id_stock, central_window):
        super().__init__(text=text)
        self.helper = Db_helper('Alpha.db')
        self.id_stock = id_stock
        self.central_window = central_window
        self.clicked.connect(self.edit_func)


    def edit_func(self):
            self.form = QWidget()
            self.form.setGeometry(200, 200, 500, 500)
            self.form_Layout = QGridLayout()
            self.enter_name = QLineEdit()
            self.enter_name.setPlaceholderText('Name')
            self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[\w\s]{1,15}")))

            self.choose_diller = QComboBox()
            self.append_category()
            self.choose_diller.textActivated.connect(self.change_category)
            self.choose_diller.diller = self.choose_diller.itemText(0)

            self.append_button = QPushButton("Change")
            self.append_button.clicked.connect(self.change_func)
            self.cancel_button = QPushButton("Cancel")
            self.cancel_button.clicked.connect(self.close_func)
            self.form.setLayout(self.form_Layout)
            self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
            self.form_Layout.addWidget(self.choose_diller, 2, 0, 1, 2)
            self.form_Layout.addWidget(self.append_button , 3, 0)
            self.form_Layout.addWidget(self.cancel_button, 3, 1)
            self.insert_all_information()
            self.form.show()

    def close_func(self):
        self.form.close()
        self.enter_name.clear()   

    def insert_all_information(self):
        info = self.helper.get_list(f"""SELECT * FROM StockView WHERE id = {self.id_stock};""")[0]
        self.enter_name.setText(info[0])
        self.choose_diller.setCurrentText(info[6])

    def append_category(self):
        info = self.helper.get_list("""SELECT name FROM Suppliers""")
        for i in info:
            self.choose_diller.addItem(i[0])

    def change_category(self, e):
        self.choose_diller.diller = e

    def change_func(self):
        name = self.enter_name.text()
        if name != "":
            id_suppiler = self.helper.get_one(f"""SELECT id FROM Suppliers WHERE name = '{self.choose_diller.diller}';""")[0]
            self.helper.insert(f"""UPDATE Stock SET name = '{name}' WHERE id = {self.id_stock};""")
            self.helper.insert(f"""UPDATE Stock SET id_Suppiler = {id_suppiler} WHERE id = {self.id_stock};""")
            self.central_window.drowAllwOrders()
            self.form.close()

    