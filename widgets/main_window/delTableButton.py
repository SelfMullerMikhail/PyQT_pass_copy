from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from func_get_path_icon import get_path_icon

class DelTableButton(QPushButton):
    def delTable(self):
        self.tableListWidget.del_table()

    def __init__(self, *args):
        super().__init__()
        self.tableListWidget = args[0]
        self.setFont(QFont("Arial", 15))
        self.setText("DEL")
        self.setIcon(get_path_icon("file-minus.svg"))

        self.clicked.connect(self.delTable)
