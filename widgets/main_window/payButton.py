import os, sys

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

sys.path.append( os.path.dirname( __file__ ).replace("main_window", ""))

from func_get_path_icon import get_path_icon
from widgets.main_window.pay_window.pay_widget import Pay_widget
from functions.db_Helper import Db_helper


class PayButton(QPushButton):
    def __init__(self, text, centralWidget, activeTab, tablesListWidget):
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.tablesListWidget = tablesListWidget
        self.centralWidget = centralWidget
        self.activeTab = activeTab
        self.setFixedHeight(40)
        self.setIcon(get_path_icon("credit-card.svg"))
        self.setIconSize(QSize(25,25))
        self.clicked.connect(self.anyFunction)
        

    def anyFunction(self, e):
        self.proof = self.helper.get_list(f"""SELECT id FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}""")
        if self.proof != []:
            self.centralWidget.takeCentralWidget()
            self.pay_widget = Pay_widget(self.activeTab, centralWidget = self.centralWidget, tablesListWidget = self.tablesListWidget)
            self.centralWidget.setCentralWidget(self.pay_widget)
