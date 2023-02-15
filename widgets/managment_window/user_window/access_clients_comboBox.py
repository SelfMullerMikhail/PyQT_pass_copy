from PyQt6.QtWidgets import QComboBox
from func_get_path_icon import get_path_icon
from functions.db_Helper import Db_helper

class Access_clients_ComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.access = ''
        self.helper = Db_helper("Alpha.db")
        self.currentTextChanged.connect(self.func)
        info = self.helper.get_list("""SELECT * FROM Access;""")
        for i in info:
            self.addItem(i[1])
        self.func(info[0][1])

    def func(self, e):
        self.access = e