import hashlib

from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator, QFont
from PyQt6.QtCore import QRegularExpression

from widgets.numbers_table import Numbers_table
from widgets.authorization_window.numbers_button import Number_button
from functions.db_Helper import Db_helper

class Authorization_window(QWidget):
    def __init__(self, selfWidget) -> None:
        """Window for authorization (choose) client"""
        super().__init__()
        self.selfWidget = selfWidget
        self.helper: Db_helper = Db_helper("Alpha.db")
        self.loy: QGridLayout = QGridLayout()
        self.setLayout(self.loy)
        self.numbers: QLineEdit = QLineEdit()
        self.numbers.setFont(QFont("Arial", 20))
        self.numbers.textChanged.connect(self.change_text)
        self.numbers.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{0,4}"))) 
        self.numbers.setPlaceholderText("* * * *")

        self.numbers_table: Numbers_table = Numbers_table(selfWidget=self, main_wdinow = self.selfWidget, tipe_of_button=Number_button)

        self.numbers_table.clear.clicked.connect(self.numbers_clear_func)
        self.numbers_table.clear.setText("Clear")
        self.numbers_table.close_button.clicked.connect(self.numbers_close_func)
        self.numbers_table.close_button.setText("Close")

        self.numbers.setMaximumWidth(100)
        self.loy.addWidget(QWidget(),0, 0, 13, 13)
        self.loy.addWidget(self.numbers, 1, 6)
        self.loy.addWidget(self.numbers_table, 2, 3, 7, 7)

    def change_text(self, e: str) -> None:
        """Change and text validation"""
        if len(e) == 4:
            clients_password = hashlib.sha1(e.encode('UTF-8')).hexdigest()
            password = self.helper.get_list("""SELECT id, name, password, access 
                                                FROM Client;""")
            for i in password:
                if i[2] == clients_password:
                    self.selfWidget.activeTab.activeUser = (i[0], i[1], i[3])
                    self.selfWidget.activeTab.createFirstMinTable(i[0])
                    self.selfWidget.drowAllwOrders()
                    self.selfWidget.setCentralWindow()
                    self.numbers.clear()
                    
                else:
                    self.numbers.clear()

    def set_authorization_window(self) -> None:
        """Function for change window on authorization"""
        self.selfWidget.setCentralWindow_authorization()

    def numbers_clear_func(self) -> None:
        """Clear QLabel with password"""
        self.numbers.clear()

    def numbers_close_func(self) -> None:
        """Close this window (QWidget)"""
        self.selfWidget.close()