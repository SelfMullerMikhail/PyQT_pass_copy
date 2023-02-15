import hashlib
from PyQt6.QtWidgets import QPushButton, QGridLayout

from functions.db_Helper import Db_helper

class Number_button(QPushButton):
    def __init__(self, text, selfWidget=..., main_wdinow=...):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.main_wdinow = main_wdinow
        self.text_ = text
        self.setMinimumHeight(90)
        self.selfWidget = selfWidget
        self.loy = QGridLayout()
        self.setText(self.text_)
        self.clicked.connect(self.func)

    def func(self):
        self.selfWidget.numbers.insert(str(self.text_))
        if len(self.selfWidget.numbers.text()) == 4:
            clients_password = hashlib.sha1(self.selfWidget.numbers.text().encode('UTF-8')).hexdigest()
            password = self.helper.get_list("""SELECT id, name, password, access 
                                                FROM Client;""")
            for i in password:
                if i[2] == clients_password:
                    self.main_wdinow.setCentralWindow()
                    self.main_wdinow.activeTab.activeUser = (i[0], i[1], i[3])
                    self.main_wdinow.drowAllwOrders()
                else:
                    self.selfWidget.numbers.clear()