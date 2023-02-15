import hashlib

from PyQt6.QtWidgets import QGridLayout, QPushButton, QWidget, QLineEdit, QMessageBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from functions.db_Helper import Db_helper
from widgets.sorting_widgets import QLineEditSorting, QComboBoxSorting
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.ordersListWidget import OrdersListWidget
from widgets.managment_window.user_window.access_clients_comboBox import Access_clients_ComboBox
from widgets.managment_window.user_window.del_user import Del_user


class User_widget(QGridLayout):
    def __init__(self, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.central_window = central_window
        self.clients_list = OrdersListWidget()
        self.clients_list.setColumnCount(7) 
        self.clients_list.add_columns(((0, ""), (1, "Name"), (2, "Birthday"), (3, "Number"), (4, "Access"), (5, ""), (6, "")))
        self.clients_list.settingSizeColumn((70, 70, 70, 70, 70, 70, 70))
        self.clients_list.settingSizeRow(35)

        self.quick_search = QLineEditSorting(selfWidget=self)
        sort_list = ["Name", "Birthday", "Number", "Access"]
        self.sorting = QComboBoxSorting(sort_list=sort_list, selfWidget=self, quick_search = self.quick_search)
        self.append_button = QPushButton("Append") 
        self.append_button.clicked.connect(self.append_func)


        self.addWidget(self.clients_list, 1, 0, 19, 20)
        self.addWidget(self.quick_search, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)
        self.addWidget(self.append_button, 0, 18, 1, 2)

        self.drow_clients()

    def append_func(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[\w\s]{1,15}")))

        self.enter_birthday = QLineEdit()
        self.enter_birthday.setPlaceholderText('Birthday YYYY-MM-DD')
        self.enter_birthday.setValidator(QRegularExpressionValidator(QRegularExpression("[1-2][0-9]{3,3}-[0-9]{2,2}-[0-9]{0,2}")))

        self.enter_password = QLineEdit() 
        self.enter_password.setPlaceholderText('Password XXXX')
        self.enter_password.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{4,4}")))

        self.enter_number = QLineEdit() 
        self.enter_number.setPlaceholderText('Number')
        self.enter_number.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{10,12}")))

        self.enter_access = Access_clients_ComboBox()

        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_client)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.form.close)
        self.form.setLayout(self.form_Layout)

        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_access, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_birthday, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_password, 3, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_number, 4, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 5, 0)
        self.form_Layout.addWidget(self.cancel_button, 5, 1)
        self.form.show()

    def append_client(self):
        name = self.enter_name.text()
        birthday =  self.enter_birthday.text()
        number = self.enter_number.text()
        password = self.enter_password.text()
        access = self.enter_access.access
        if name != "" and birthday != "" and len(password) == 4:
            password = hashlib.sha1(password.encode('UTF-8')).hexdigest()
            allready_pass = self.helper.get_list("""SELECT password FROM Client;""")
            flag = True
            for i in allready_pass:
                if password == i[0]:
                    flag = False
            if flag == True:
                self.helper.insert(f"""INSERT INTO Client(name, birthday, password, number, access)
                                        VALUES('{name}', '{birthday}', '{password}', {number}, '{access}') """)
                self.form.close()
                self.clients_list.clearContents()
                self.drow_clients()
                self.central_window.Main_widget.tablesListWidget.add_table()
            else:
                    msgBox = QMessageBox()
                    msgBox.setText(f"Password not available")
                    msgBox.exec()

    def drow_func(self):
        self.drow_clients()

    def drow_clients(self):
        self.clients_list.clearContents()
        self.clients_list.setLineCount("Client")
        info = self.helper.get_list(f"""SELECT * FROM Client WHERE {self.sorting.category_search} LIKE'%{self.quick_search.quick_search_line}%' ORDER BY {self.sorting.category_search}""")
        for row in range(len(info)):
            self.clients_list.setCellWidget(row, 0, QPushButton("info....."))
            self.clients_list.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.clients_list.setItem(row, 2, CustomQTableWidgetItem(str(info[row][2])))
            self.clients_list.setItem(row, 3, CustomQTableWidgetItem(str(info[row][4])))
            self.clients_list.setItem(row, 4, CustomQTableWidgetItem(str(info[row][5])))
            self.clients_list.setCellWidget(row, 5, QPushButton('edit....'))
            self.clients_list.setCellWidget(row, 6, Del_user(centalWidget=self.central_window, text = 'del', id_client= info[row][0], selfWidget=self))



