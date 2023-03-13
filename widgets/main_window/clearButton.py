import os, sys

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

sys.path.append( os.path.dirname( __file__ ).replace("main_window", ""))
from functions.db_Helper import Db_helper
from func_get_path_icon import get_path_icon
from functions.active_tub import ActiveTable


class ClearButton(QPushButton):
    """This button do clear choosed order."""
    def __init__(self, activeTab: ActiveTable, selfWidget) -> None:
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.activeTab = activeTab
        self.selfWidget = selfWidget
        self.setText("Clear")
        self.setFont(QFont("Arial", 15))
        self.setIcon(get_path_icon("x-octagon.svg"))
        self.clicked.connect(self.clear)

    def clear(self, e):
        self.helper.insert(f"DELETE FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}")
        self.selfWidget.drowAllwOrders()
