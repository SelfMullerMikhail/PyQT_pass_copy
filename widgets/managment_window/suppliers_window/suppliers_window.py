from PyQt6.QtWidgets import QGridLayout, QLineEdit, QTextEdit, QPushButton, QWidget
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.ordersListWidget import OrdersListWidget
from widgets.managment_window.suppliers_window.customWidgets import Dell_Button_Suppliers
from widgets.sorting_widgets import QLineEditSorting, QComboBoxSorting
from functions.db_Helper import Db_helper



class Suppliers_window(QGridLayout):
    def __init__(self, active_window, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.central_window = central_window
        self.suppliers_list = OrdersListWidget(active_window = active_window)
        self.suppliers_list.setColumnCount(7) 
        self.suppliers_list.add_columns(((0, "Name"), (1, "Number"), (2, "Mail"), (3, "IBAN"), (4, "Info"), (5, ""), (6, "")))
        self.suppliers_list.settingSizeColumn((70, 70, 70, 70, 150, 30, 30))
        self.suppliers_list.settingSizeRow(35)
        self.suppliers_list.setLineCount("Suppliers")
        self.quick_search = QLineEditSorting(selfWidget=self)
        sort_list = ["name", "number", "mail", "iban", "info"]
        self.sorting = QComboBoxSorting(sort_list=sort_list, selfWidget=self, quick_search = self.quick_search)
        self.append_button = QPushButton(text="Append") # Кастомить
        self.append_button.clicked.connect(self.add_supplier_window)
        self.addWidget(self.suppliers_list, 1, 0, 19, 20)
        self.addWidget(self.quick_search, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)
        self.addWidget(self.append_button, 0, 18, 1, 2)
        self.get_suppliers()


    def drow_func(self):
        self.get_suppliers()

    def add_supplier_window(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()

        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[\w]{30}")))
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

        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.form.close)

        self.form.setLayout(self.form_Layout)

        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_number, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_mail, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_IBAN, 3, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_info, 4, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 5, 0, 1, 1 )
        self.form_Layout.addWidget(self.cancel_button, 5, 3, 1, 1 )
        self.form.show()


    def append_func(self):
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
            self.helper.insert(f"""INSERT INTO Suppliers(name, number, mail, iban, info) 
                                    VALUES ('{name}', {enter_number}, '{enter_mail}', '{enter_IBAN}', '{enter_info}') """)
            self.suppliers_list.setLineCount("Suppliers")
            self.get_suppliers()
            self.form.close()

    def get_suppliers(self):
        self.suppliers_list.clearContents()
        info = self.helper.get_list(f"""SELECT * FROM Suppliers WHERE {self.sorting.category_search} LIKE'%{self.quick_search.quick_search_line}%' GROUP BY {self.sorting.category_search}""")
        self.draw_suppliers(info)

    def draw_suppliers(self, info):
        for row in range(len(info)):
            for i in range(1, 6):
                self.suppliers_list.setItem(row, i-1, CustomQTableWidgetItem(str(info[row][i])))
            self.suppliers_list.setCellWidget(row, 5, QPushButton("edit"))
            self.suppliers_list.setCellWidget(row, 6, Dell_Button_Suppliers(name = info[row][1] , text = "del", wind = self))

        