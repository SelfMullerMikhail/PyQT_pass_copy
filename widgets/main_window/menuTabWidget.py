from PyQt6.QtWidgets import QTabWidget, QWidgetAction, QWidget, \
    QTabBar, QFormLayout, QStackedWidget, QPushButton, QVBoxLayout,\
    QLabel, QGridLayout, QScrollArea
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction  
import copy

from widgets.main_window.customScrollArea import CustomScrollArea
from functions.db_Helper import Db_helper

from widgets.func_get_path_icon import get_path_icon


class MenuTabWidget(QTabWidget):
    def create_button(self, foodCategory):
        counter_x = -1
        counter_y = 0
        for i in foodCategory:
            counter_x += 1
            btn = QPushButton(get_path_icon(i[2]), "")
            btn.setText(i[1])
            btn.setIconSize(QSize(90, 90))
            btn.clicked.connect(slot = self.buttonFunction(i[0]))
            self.loy.addWidget(btn, counter_y, counter_x)
            if counter_x == 3:
                counter_x = -1
                counter_y += 1
        

    def buttonFunctionComplex(self, i):
        self.helper.insert(f"""INSERT INTO OpenOrder(id_client, id_table, id_menu, count)
                                VALUES({1},{self.activeTab.activeTab} ,{i}, 1)""")
        self.ordersListWidget.clearContents()
        self.ordersListWidget.drow_orders()

        
    def buttonFunction(self, i):
        return lambda: self.buttonFunctionComplex(i) 

    def createTab(self, icon, name, foodCategory):
        self.wgt = QWidget() 
        self.tab = CustomScrollArea()
        self.loy = QGridLayout(self.wgt)
        self.loy.addWidget(QWidget(), 0, 0, 47, 0)
        self.tab.setWidget(self.wgt)
        self.create_button(foodCategory)
        self.addTab(self.tab , get_path_icon(icon), name)

    def create_full_menu(self):
        self.category = self.helper.get_list("SELECT id, name, image FROM Category")
        for i in self.category:
            self.new_menu = self.helper.get_list(f"SELECT id, name, image FROM Menu WHERE category = {i[0]}")
            self.createTab(i[2], i[1], self.new_menu)

    def __init__(self, *args):
        super().__init__()
        self.helper = args[0]
        self.activeTab = args[1]
        self.ordersListWidget = args[2]
        self.setIconSize(QSize(35,35))
        self.setMovable(True)
        self.create_full_menu()
        