import os

from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize


PATH_FEATHER = os.path.join( os.path.dirname( __file__ ), '' )

class TablesListWidget(QListWidget):
    def customIcon(self, numb):
        self.obj = QListWidgetItem(QIcon(PATH_FEATHER + "feather/table.svg"), f"table_{numb}")
        return self.obj

    def __init__(self):
        super().__init__()
        self.setFixedWidth(100)
        self.addItem(self.customIcon(1))
        self.addItem(self.customIcon(2))
        self.addItem(self.customIcon(3))
        self.setIconSize(QSize(30, 30))

        self.itemClicked.connect(self.printer)
    def printer(self, e):
        print(e.text())