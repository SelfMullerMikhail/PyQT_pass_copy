from PyQt6.QtWidgets import QTabWidget, QWidgetAction, QWidget, QTabBar
from PyQt6.QtCore import QSize

from widgets.func_get_path_icon import get_path_icon


class MenuTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.main_tab = QTabBar()
        self.drinks_tab = QTabBar()
        self.food_tab = QTabBar()
        self.insertTab(0, self.main_tab, get_path_icon("book.svg"), "Main")
        self.addTab(self.drinks_tab, get_path_icon("coffee"),"Drinks")
        self.addTab(self.food_tab, get_path_icon("pie-chart.svg"), "Food")
        self.setIconSize(QSize(30,30))

        # self.setFixedWidth(200)
        # self.setFixedHeight(200)

