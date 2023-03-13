from PyQt6.QtWidgets import QTabWidget, QWidget, QPushButton, QGridLayout, QSizePolicy, QBoxLayout, QVBoxLayout, QLabel, QMenu
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QResizeEvent

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
        self.btnIconSize = {"width" : 110, "height": 110}
        self.tabIconSize = {"width" : 50, "height": 50}
        self.constSize = self.size()
        self.btns = []
        self.setIconSize(QSize(35,35))
        self.setMovable(True)
        self.create_full_menu()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.fixSizeWitdh = round(self.btnIconSize["width"] * (a0.size().width() / self.constSize.width()))
        self.fixSizeHeight = round(self.btnIconSize["height"] * (a0.size().height() / self.constSize.height()))
        self.fixSizeTabWidth = round(self.tabIconSize["width"] * (a0.size().width() / self.constSize.width()))
        self.fixSizeTabHeight = round(self.tabIconSize["height"] * (a0.size().height() / self.constSize.height()))
        self.setIconSize(QSize(self.fixSizeTabWidth, self.fixSizeTabHeight))
        for btn in self.btns:
            btn.setIconSize(QSize(self.fixSizeWitdh, self.fixSizeHeight))
            btn.setBaseSize(self.fixSizeWitdh ,self.fixSizeHeight)
        return super().resizeEvent(a0)

    def create_button(self, foodCategory: list) -> None:
        """Count row and column + addWidget"""
        counter_x = -1
        counter_y = 0
        for i in foodCategory:
            counter_x += 1
            btn = QPushButton()
            layout = QVBoxLayout(btn)
            layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
            btn.setIcon(get_path_icon(i[2]))
            btn.setIconSize(QSize(self.btnIconSize["width"], self.btnIconSize["height"]))
            layout.addWidget(btn)
            layout.addWidget(QLabel(i[1]))
            btn.clicked.connect(slot = self.buttonFunction(i[0]))
            self.btns.append(btn)
            self.loy.addWidget(btn, counter_y, counter_x)
            if counter_x == 4:
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

    def create_full_menu(self) -> None:
        """Upgrade all products menu(buttons and page)"""
        self.clear()
        self.category = self.helper.get_list("SELECT id, name, image FROM Category")
        for i in self.category:
            self.new_menu = self.helper.get_list(f"SELECT id, name, image FROM Menu WHERE category = {i[0]}")
            self.wgt = QWidget()  
            self.loy = QGridLayout(self.wgt)
            self.tab = CustomScrollArea()
            self.loy.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            self.tab.setWidget(self.wgt)
            self.create_button(self.new_menu)
            self.addTab(self.tab , get_path_icon(i[2]), i[1])


