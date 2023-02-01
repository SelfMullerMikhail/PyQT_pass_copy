from PyQt6.QtWidgets import QPushButton, QDialog, QGridLayout
from PyQt6.QtCore import QSize

from functions.db_Helper import Db_helper
from func_get_path_icon import get_path_icon
from widgets.ordersListWidget import OrdersListWidget
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem

class InfoProductsOrder(QPushButton):
    def __init__(self, id_table, row, selfWidget):
        super().__init__(text=id_table)
        self.helper = Db_helper("Alpha.db")
        self.row = row
        self.selfWidget = selfWidget
        self.id_table = id_table
        self.setIcon(get_path_icon('tablet.svg'))
        self.setIconSize(QSize(25, 25))
        self.clicked.connect(self.func)

    def func(self):
        test = QDialog()
        loyaout = QGridLayout()

        self.info_products = OrdersListWidget(active_window=...)
        self.info_products.setColumnCount(4) 
        self.info_products.add_columns(((0, "name"), (1, "count"), (2, "price"), (3, "summ")))
        self.info_products.settingSizeColumn((200, 120, 120, 120))
        self.info_products.settingSizeRow(30)

        loyaout.addWidget(self.info_products, 0, 0)
        test.setLayout(loyaout)
        self.drow_ingridients_info()
        test.exec()


    def drow_ingridients_info(self):
        info = self.helper.get_list(f"""SELECT menu_name, count, (menu_price), (count * menu_price)
                                        FROM CloseOrderView 
                                        WHERE id_table = {self.id_table};""")
        self.info_products.setRowCount(len(info))
        for row in range(len(info)):
            self.info_products.setItem(row, 0, CustomQTableWidgetItem(str(info[row][0])))
            self.info_products.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.info_products.setItem(row, 2, CustomQTableWidgetItem(str(info[row][2])))
            self.info_products.setItem(row, 3, CustomQTableWidgetItem(str(info[row][3])))