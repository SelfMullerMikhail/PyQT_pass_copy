from PyQt6.QtWidgets import QGridLayout, QLineEdit, QTextEdit, QPushButton, QWidget
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from functions.db_Helper import Db_helper

class Append_Edit_widget(QWidget):
    def __init__(self, selfWidget, func_name, supplier_id = ...):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.suppiler_window = selfWidget
        self.supplier_id = supplier_id
        self.func_name = func_name
        self.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()

        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[\w\s]{1,20}")))
        self.enter_number = QLineEdit()
        self.enter_number.setPlaceholderText("Phone Number (90XXXXXXXXXX)")
        self.enter_number.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{11}")))
        self.enter_mail = QLineEdit()
        self.enter_mail.setPlaceholderText("Mail (XXXXX@XXXX.XXX)")
        self.enter_mail.setValidator(QRegularExpressionValidator(QRegularExpression("[\w]{3,20}@[a-zA-Z0-9]{2,10}[\.][a-z]{2,10}")))
        self.enter_IBAN = QLineEdit()
        self.enter_IBAN.setPlaceholderText("IBAN")
        self.enter_IBAN.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z]{2}[0-9]{27}")))
        self.enter_info = QTextEdit()
        self.enter_info.setPlaceholderText("Some info")

        self.append_button = QPushButton(self.func_name)
        self.append_button.clicked.connect(self.append_edit_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)

        self.setLayout(self.form_Layout)

        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_number, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_mail, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_IBAN, 3, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_info, 4, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 5, 0, 1, 1 )
        self.form_Layout.addWidget(self.cancel_button, 5, 3, 1, 1 )

    def append_edit_func(self):
        name = self.enter_name.text()
        enter_number = self.enter_number.text()
        enter_mail = self.enter_mail.text()
        enter_IBAN = self.enter_IBAN.text()
        enter_info = self.enter_info.toPlainText()

        if name != "":
            if enter_number == "":
                enter_number = 0
            if enter_mail =="":
                enter_mail = "None"
            if enter_IBAN == "":
                enter_IBAN == "None"
            if enter_info == "":
                enter_info == "None"
            functions = {"Change": self.edit_func, "Append":self.append_func}
            functions[self.func_name](name, enter_number, enter_mail, enter_IBAN, enter_info)
            self.suppiler_window.suppliers_list.setLineCount("Suppliers")
            self.suppiler_window.get_suppliers()
            self.close()


    def append_func(self, name, enter_number, enter_mail, enter_IBAN, enter_info):
        self.helper.insert(f"""INSERT INTO Suppliers(name, number, mail, iban, info) 
                        VALUES ('{name}', {enter_number}, '{enter_mail}', '{enter_IBAN}', '{enter_info}') """)

    def edit_func(self, name, enter_number, enter_mail, enter_IBAN, enter_info):
        self.helper.insert(f"""UPDATE Suppliers SET name = '{name}' WHERE id = {self.supplier_id}""")
        self.helper.insert(f"""UPDATE Suppliers SET number = {enter_number} WHERE id = {self.supplier_id}""")
        self.helper.insert(f"""UPDATE Suppliers SET mail = '{enter_mail}' WHERE id = {self.supplier_id}""")
        self.helper.insert(f"""UPDATE Suppliers SET iban = '{enter_IBAN}' WHERE id = {self.supplier_id}""")
        self.helper.insert(f"""UPDATE Suppliers SET info = '{enter_info}'WHERE id = {self.supplier_id}""")


