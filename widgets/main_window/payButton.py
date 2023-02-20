import os, sys

from PyQt6.QtWidgets import QPushButton, QMessageBox
from PyQt6.QtCore import QSize

sys.path.append( os.path.dirname( __file__ ).replace("main_window", ""))

from func_get_path_icon import get_path_icon
from widgets.main_window.pay_window.pay_widget import Pay_widget
from functions.db_Helper import Db_helper


class PayButton(QPushButton):
    def __init__(self, text, centralWidget, activeTab, tablesListWidget) -> None:
        """This Button open new window(QWidget) for creating pay"""
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.tablesListWidget = tablesListWidget
        self.centralWidget = centralWidget
        self.activeTab = activeTab
        self.setFixedHeight(40)
        self.setIcon(get_path_icon("credit-card.svg"))
        self.setIconSize(QSize(25,25))
        self.clicked.connect(self.anyFunction)
        

    def anyFunction(self, e: bool) -> None:
        """Overload for clicked this Button. 
            1. SELECT strftime("%Y-%m-%d", datetime('now', '-1 day')).
            2. SELECT id FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}.
            3. SELECT * FROM ClosedOrder WHERE time_close LIKE '%{date}%' """
        date = self.helper.get_list("""SELECT strftime("%Y-%m-%d", datetime('now', '-1 day'))""")[0][0]
        self.proof = self.helper.get_list(f"""SELECT id FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}""")
        self.closed_day = self.helper.get_list(f"""SELECT * FROM ClosedOrder WHERE time_close LIKE '%{date}%';""")
        if self.closed_day == []:
            if self.proof != []:
                self.centralWidget.takeCentralWidget()
                self.pay_widget = Pay_widget(self.activeTab, centralWidget = self.centralWidget, tablesListWidget = self.tablesListWidget)
                self.centralWidget.setCentralWidget(self.pay_widget)
        else:
                msgBox = QMessageBox()
                msgBox.setText(f"You need close this day.")
                msgBox.exec()
