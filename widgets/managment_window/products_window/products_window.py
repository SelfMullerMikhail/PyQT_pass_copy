from PyQt6.QtWidgets import QGridLayout, QLineEdit
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from widgets.ordersListWidget import OrdersListWidget
from widgets.sorting_widgets import QLineEditSorting, QComboBoxSorting
from widgets.managment_window.products_window.append_product_button import Append_product_button
from widgets.managment_window.products_window.customs_widgets import *
from widgets.managment_window.products_window.product_edit import Product_edit
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from func_get_path_icon import get_path_icon



class Products_window(QGridLayout):

    def __init__(self, active_window, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.central_window = central_window
        self.products_list = self.create_product_list(active_window = active_window)
        self.quick_search = QLineEditSorting(selfWidget=self)
        self.quick_search.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9]{0,15}"))) 
        sort_list = ["name", "category", "cost", "price", "markup", "image"]
        self.sorting = QComboBoxSorting(sort_list=sort_list, selfWidget=self, quick_search=self.quick_search)
        self.append_button = Append_product_button("append", window=self, products_window = self, central_wind = self.central_window)

        self.addWidget(self.append_button, 0, 18, 1, 2)
        self.addWidget(self.products_list, 1, 0, 19, 20)
        self.addWidget(self.quick_search, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)
        self.drow_products()

    def drow_func(self):
        self.drow_products()

    def create_product_list(self, active_window):
        products_list = OrdersListWidget(active_window = active_window, central_window = self.central_window)
        products_list.setColumnCount(9) 
        products_list.setLineCount("Menu")
        products_list.add_columns(((0, ""), (1, "Name"), (2, "Category"), (3, "Cost"), (4, "Price"), (5, "Markup"), (6, ""), (7, ""), (8, "")))
        products_list.settingSizeColumn((40, 70, 70, 70, 70, 70, 30, 30, 30))
        products_list.settingSizeRow(50)
        return products_list

    def drow_products(self):
        self.products_list.clearContents()
        self.products_list.setLineCount("Menu")
        info = self.helper.get_list((f"""SELECT image, name, category, 0 as cost ,price, 0 as markup, id 
                                                    FROM MenuView 
                                                    WHERE {self.sorting.category_search} LIKE'%{self.quick_search.quick_search_line}%'
                                                    ORDER BY {self.sorting.category_search};"""))
        for row in range(len(info)):
            icon = CustomQTableWidgetItem()
            icon.setIcon(get_path_icon(info[row][0]))
            self.products_list.setItem(row, 0, icon)
            for i in range(1, 6):
                print(info[row][i])
                self.products_list.setItem(row, i, CustomQTableWidgetItem(str(info[row][i])))
            info_button = QPushButton("info")
            info_button.clicked.connect(self.info_drow(info[row][1]))
            edit_button = Product_edit(text="edit", id_menu=info[row][6], listWidget = OrdersListWidget, window=self, central_window = self.central_window )
            del_button = CustomButtonDellProduct(text="del", name=info[row][1], window=self, central_window = self.central_window)
            self.products_list.setCellWidget(row, 6, info_button)
            self.products_list.setCellWidget(row, 7, edit_button)
            self.products_list.setCellWidget(row, 8, del_button)

    def info_drow(self, name):
        return lambda: print(name)




