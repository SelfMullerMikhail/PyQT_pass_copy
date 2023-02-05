from PyQt6.QtWidgets import QVBoxLayout, QGridLayout

from widgets.managment_window.stock_window.stock_window import Stock_window
from upMenuComboBox import UpMenu_comboBox
from widgets.managment_window.products_window.products_window import Products_window
from widgets.managment_window.suppliers_window.suppliers_window import Suppliers_window
from widgets.managment_window.category_window.category_widget import Category_widget



class Managment_widget(QVBoxLayout):
    def __init__(self, active_window, central_window):
        super().__init__()
        self.upMenu = UpMenu_comboBox()
        self.addWidget(self.upMenu)
        self.upMenu.create_tab("Products", "coffee.svg", Products_window(active_window = active_window, central_window = central_window)) 
        self.stock_window = Stock_window(active_window = active_window, central_window = central_window)
        self.upMenu.create_tab("Stock", "layers.svg", self.stock_window)
        self.upMenu.create_tab("Category", "file.svg", Category_widget(active_window = active_window, central_window = central_window))
        self.upMenu.create_tab("Suppliers", "truck.svg", Suppliers_window(active_window = active_window, central_window = central_window))
        # self.upMenu.create_tab("Statistic", "bar-chart-2.svg", QGridLayout())

        self.addWidget(self.upMenu.activate("Products"))

        

        
        

