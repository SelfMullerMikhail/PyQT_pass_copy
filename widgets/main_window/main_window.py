import sys, os

from PyQt6.QtWidgets import  QVBoxLayout, QGridLayout

sys.path.append(os.path.dirname( __file__ ))

from tableListWidget import TablesListWidget
from ordersListWidget import OrdersListWidget
from menuTabWidget import MenuTabWidget
from payButton import PayButton
from clearButton import ClearButton
from delTableButton import DelTableButton
from addTableButton import AddTableButton

from cssStyleSheet.clearButtonStyle import clearButtonStyle
from cssStyleSheet.payButtonStyle import payButtonStyle
from cssStyleSheet.menuTabWidgetStyle import MenuTabWidgetStyle


class Main_widget(QGridLayout):
    def __init__(self, *args):
        super().__init__()
        self.helper = args[0]
        self.activeTab = args[1]

        self.ordersListWidget = OrdersListWidget(self.helper, self.activeTab)
        self.tablesListWidget = TablesListWidget(self.helper, self.ordersListWidget, self.activeTab)
        self.menuTabWidget = MenuTabWidget(self.helper, self.activeTab, self.ordersListWidget)
        self.payButton = PayButton()
        self.clearButton = ClearButton(self.helper, self.activeTab, self.ordersListWidget) 
        self.delTableButton = DelTableButton(self.tablesListWidget)
        self.addTableButton = AddTableButton(self.tablesListWidget) 
        
        self.clearButton.setStyleSheet(clearButtonStyle)
        self.payButton.setStyleSheet(payButtonStyle)
        self.menuTabWidget.setStyleSheet(MenuTabWidgetStyle)
        
        self.addWidget(self.tablesListWidget, 1, 0, 18, 0)
        self.addWidget(self.ordersListWidget, 1, 2, 13, 8)
        self.addWidget(self.menuTabWidget, 1, 10, 20, 10)                        
        self.addWidget(self.payButton, 15, 2, 1, 3)
        self.addWidget(self.clearButton, 15, 7, 1, 3)
        self.addWidget(self.delTableButton, 19, 0, 1, 2)
        self.addWidget(self.addTableButton, 20, 0, 1, 2)