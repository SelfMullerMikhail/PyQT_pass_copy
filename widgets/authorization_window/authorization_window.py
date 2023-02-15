from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from widgets.numbers_table import Numbers_table
from widgets.authorization_window.numbers_button import Number_button

class Authorization_window(QWidget):
    def __init__(self, selfWidget):
        super().__init__()
        self.selfWidget = selfWidget
        self.loy = QGridLayout()
        self.setLayout(self.loy)
        self.numbers = QLineEdit()
        self.numbers.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{0,4}"))) 
        self.numbers.setPlaceholderText("* * * *")
        self.numbers_table = Numbers_table(selfWidget=self, main_wdinow = self.selfWidget, tipe_of_button=Number_button)

        self.numbers_table.clear.clicked.connect(self.numbers_clear_func)
        self.numbers_table.clear.setText("Clear")
        self.numbers_table.close_button.clicked.connect(self.numbers_close_func)
        self.numbers_table.close_button.setText("Close")

        self.numbers.setMaximumWidth(100)
        self.loy.addWidget(QWidget(),0, 0, 13, 13)
        self.loy.addWidget(self.numbers, 1, 6)
        self.loy.addWidget(self.numbers_table, 2, 3, 7, 7)

    def set_authorization_window(self):
        self.selfWidget.setCentralWindow_authorization()

    def numbers_clear_func(self):
        self.numbers.clear()

    def numbers_close_func(self):
        self.selfWidget.close()