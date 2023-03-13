from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from func_get_path_icon import get_path_icon




class AddTableButton(QPushButton):
    def addTable(self):
        self.tableListWidget.add_table()

    def __init__(self, *args):
        super().__init__()
        self.tableListWidget = args[0]
        self.setFont(QFont("Arial", 15))
        self.setText("ADD")
        self.setIcon(get_path_icon("file-plus.svg"))

        self.clicked.connect(self.addTable)
        