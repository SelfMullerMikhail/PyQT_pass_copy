from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QGridLayout, QDialog, QPushButton

from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.ordersListWidget import OrdersListWidget
from functions.db_Helper import Db_helper
from func_get_path_icon import get_path_icon


class InfoProductsMenu(QPushButton):
    def __init__(self, icon, id_menu):
        super().__init__()
        self.setIcon(get_path_icon(icon))
        self.setIconSize(QSize(40, 40))
        self.id_menu = id_menu
        self.clicked.connect(self.func)

    def func(self):
        self.helper = Db_helper("Alpha.db")
        self.info_products = OrdersListWidget(central_window=...)
        self.info_widget = QDialog()
        self.info_widget.setMinimumSize(500, 300)
        self.loy = QGridLayout()
        self.loy.addWidget(self.info_products)
        self.info_products.setColumnCount(5) 
        self.info_products.add_columns(((0, "product"), (1, "supplier"), (2, "count"), (3, "price"), (4, "cost")))
        self.info_products.settingSizeColumn((120, 120, 100, 100, 100))
        self.info_products.settingSizeRow(30)
        self.drow_ingridients_info()
        self.info_widget.setLayout(self.loy)
        self.info_widget.exec()

    def drow_ingridients_info(self):
        info = self.helper.get_list(f"""SELECT * FROM TechnologyCardView WHERE id_menu = {self.id_menu};""")
        self.info_products.setRowCount(len(info))
        for row in range(len(info)):
            self.info_products.setItem(row, 0, CustomQTableWidgetItem(str(info[row][0])))
            self.info_products.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.info_products.setItem(row, 2, CustomQTableWidgetItem(str(info[row][2])))
            self.info_products.setItem(row, 3, CustomQTableWidgetItem(str(info[row][3])))
            self.info_products.setItem(row, 4, CustomQTableWidgetItem(str(round(info[row][4], 3))))