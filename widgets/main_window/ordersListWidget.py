from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QAbstractItemView, QHeaderView, QAbstractItemDelegate, QSpinBox, QWidget, QVBoxLayout
from functions.db_Helper import Db_helper


class CustomQTableWidgetItem(QTableWidgetItem):

    def __init__(self, *args):
        super().__init__(*args)
        self.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)

class OrdersListWidget(QTableWidget):

    def settingSize(self, settings):
        for i in settings:
            self.setColumnWidth(*i)

    def add_columns(self, columns):
        for i, b in columns:
            self.setHorizontalHeaderItem(i, QTableWidgetItem(b))

    def addOrderInfo(self, info):
        for row in range(len(info)):
            for i in range(4):
                self.setItem(row, i, CustomQTableWidgetItem(str(info[row][i])))

    def drow_orders(self):
        self.order = self.helper.get_list(f"""SELECT Menu.name, Menu.price, count(count), (Menu.price * count(count))
                                            FROM  OpenOrder, Menu
                                            WHERE OpenOrder.id_menu = Menu.id AND id_table = {self.activeTab.activeTab}
                                            GROUP BY id_menu;""")
        self.addOrderInfo(self.order)
        
    def basikSetting(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setColumnCount(6)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setShowGrid(False)
        self.setRowCount(10)
        self.add_columns(((0, "name"), (1, "price"), (2, "count"), (3, "total"), (4, ""), (5, "")))
        self.settingSize(((0, 100),(1, 70),(2, 100), (3, 70), (4, 2), (5, 2)))

    def __init__(self, *args):
        super().__init__()
        self.helper = args[0]
        self.activeTab = args[1]
        self.basikSetting()
        self.drow_orders()

        # Доработать добавление или уменьшение товара
        # self.itemClicked.connect()
        # self.itemDoubleClicked.connect()
    
