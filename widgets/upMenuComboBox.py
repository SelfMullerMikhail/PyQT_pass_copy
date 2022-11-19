import os

from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QIcon

from widgets.func_get_path_icon import get_path_icon

class UpMenu_comboBox(QComboBox):
    def __init__(self, *arg):
        super().__init__(*arg)
        self.setFixedHeight(40)
        self.addItem("Main")
        self.addItem("Settings")
        self.addItem("Archive")
        self.setItemIcon(0, get_path_icon("home.svg"))
        self.setItemIcon(1, get_path_icon("settings.svg"))
        self.setItemIcon(2, get_path_icon("archive.svg"))
        self.setIconSize(QSize(30,30))

        # self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignRight)
        self.activated.connect(self.printer)

    def printer(self, e):
        print(e)