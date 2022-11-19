import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QListWidget, QFrame, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

from widgets.upMenuComboBox import UpMenu_comboBox
from widgets.tableListWidget import TablesListWidget
from widgets.ordersListWidget import OrdersListWidget
from widgets.menuTabWidget import MenuTabWidget
from widgets.payButton import PayButton
from widgets.clearButton import ClearButton

from cssStyleSheet.clearButtonStyle import clearButtonStyle
from cssStyleSheet.payButtonStyle import payButtonStyle
from cssStyleSheet.menuTabWidgetStyle import MenuTabWidgetStyle


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 800)
        self.main_Layout = QGridLayout()
        self.upMenu = UpMenu_comboBox()

        
        self.tablesListWidget = TablesListWidget()
        self.ordersListWidget = OrdersListWidget()
        self.menuTabWidget = MenuTabWidget()
        self.payButton = PayButton()
        self.clearButton = ClearButton() 

        self.clearButton.setStyleSheet(clearButtonStyle)
        self.payButton.setStyleSheet(payButtonStyle)
        self.menuTabWidget.setStyleSheet(MenuTabWidgetStyle)

        self.main_Layout.addWidget(self.upMenu, 0, 0, 1, 20)
        self.main_Layout.addWidget(self.tablesListWidget, 1, 0, 20, 0)
        self.main_Layout.addWidget(self.ordersListWidget, 1, 2, 13, 8)
        self.main_Layout.addWidget(self.menuTabWidget, 1, 10, 20, 10)
        

        
        
        
        self.main_Layout.addWidget(self.payButton, 15, 2, 1, 3)
        self.main_Layout.addWidget(self.clearButton, 15, 7, 1, 3)

        self.main_Widget = QWidget()
        self.main_Widget.setLayout(self.main_Layout)
        self.setCentralWidget(self.main_Widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet = ...
    window.show()
    sys.exit(app.exec())