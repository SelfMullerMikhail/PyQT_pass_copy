from PyQt6.QtWidgets import QTabWidget, QWidget, QPushButton, QGridLayout
from PyQt6.QtCore import QSize

from widgets.main_window.customScrollArea import CustomScrollArea
from widgets.ordersListWidget import OrdersListWidget
from functions.db_Helper import Db_helper
from functions.active_tub import ActiveTable
from func_get_path_icon import get_path_icon


class MenuTabWidget(QTabWidget):
    def __init__(self, activeTab: ActiveTable, ordersListWidget: OrdersListWidget) -> None:
        """Widget of products button and page of products"""
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.activeTab = activeTab
        self.ordersListWidget = ordersListWidget
        self.setIconSize(QSize(35,35))
        self.setMovable(True)
        self.create_full_menu()

    def create_button(self, foodCategory: list) -> None:
        """Count row and column + addWidget"""
        counter_x = -1
        counter_y = 0
        for i in foodCategory:
            counter_x += 1
            btn = QPushButton(get_path_icon(i[2]), "")
            btn.setText(i[1])
            btn.setIconSize(QSize(80, 80))
            btn.clicked.connect(slot = self.buttonFunction(i[0]))
            self.loy.addWidget(btn, counter_y, counter_x)
            if counter_x == 3:
                counter_x = -1
                counter_y += 1
        

    def buttonFunctionComplex(self, i: int) -> None:
        """Insert into OpenOrder(id_client, id_table, id_menu, count=1)"""
        self.helper.insert(f"""INSERT INTO OpenOrder(id_client, id_table, id_menu, count)
                                VALUES({self.activeTab.activeUser[0]}, {self.activeTab.activeTab} ,{i}, 1)""")
        self.ordersListWidget.drow_orders()

        
    def buttonFunction(self, i: int) -> object:
        """Generation universal function for every button in menuTab"""
        return lambda: self.buttonFunctionComplex(i) 

    def createTab(self, icon: str, name: str, foodCategory: list) -> None:
        """Create QWidget, CustomScrollArea, QGridLayout and do functions: addWidget, setWidget, create_button, addTab"""
        self.wgt = QWidget() 
        self.tab = CustomScrollArea()
        self.loy = QGridLayout(self.wgt)
        self.loy.addWidget(QWidget(), 0, 0, 47, 4)
        self.tab.setWidget(self.wgt)
        self.create_button(foodCategory)
        self.addTab(self.tab , get_path_icon(icon), name)

    def create_full_menu(self) -> None:
        """Upgrade all products menu(buttons and page)"""
        self.clear()
        self.category = self.helper.get_list("SELECT id, name, image FROM Category")
        for i in self.category:
            self.new_menu = self.helper.get_list(f"SELECT id, name, image FROM Menu WHERE category = {i[0]}")
            self.createTab(i[2], i[1], self.new_menu)


        
        