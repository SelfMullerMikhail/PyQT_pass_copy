import os, sys

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

sys.path.append( os.path.dirname( __file__ ).replace("main_window", ""))

from functions.db_Helper import Db_helper
from func_get_path_icon import get_path_icon


class ClearButton(QPushButton):
    
    def clear(self, e):
        self.helper.insert(f"DELETE FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}")
        self.ordersListWidget.clearContents()

    def __init__(self, activeTab, ordersListWidget):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.activeTab = activeTab
        self.ordersListWidget = ordersListWidget
        self.setText("Clear")
        self.setFixedHeight(40)
        self.setIcon(get_path_icon("x-octagon.svg"))
        self.setIconSize(QSize(25,25))

        self.clicked.connect(self.clear)