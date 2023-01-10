import os, sys

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

from functions.db_Helper import Db_helper

sys.path.append(os.path.dirname( __file__ ).replace("widgets/main_window", ""))
from widgets.func_get_path_icon import get_path_icon




class AddTableButton(QPushButton):
    def addTable(self):
        self.tableListWidget.add_table()

    def __init__(self, *args):
        super().__init__()
        self.tableListWidget = args[0]
        self.setText("ADD")
        self.setFixedWidth(100)
        self.setIcon(get_path_icon("file-plus.svg"))
        self.setIconSize(QSize(30, 30))

        self.clicked.connect(self.addTable)
        