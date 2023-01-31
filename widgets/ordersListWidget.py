from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QPushButton
from PyQt6.QtCore import Qt, QSize

from functions.db_Helper import Db_helper
from widgets.managment_window.products_window.customs_widgets import *



class OrdersListWidget(QTableWidget):
    def __init__(self, active_window = '', central_window = ''):
        super().__init__()
        self.const = self.size().height() + 100
        self.helper = Db_helper("Alpha.db")
        self.activeTab = active_window
        self.functions = {}
        self.central_window = central_window
        self.setIconSize(QSize(50, 50))
        self.basikSetting()

    def setLineCount(self, table):
            count = int(self.helper.get_list(f"""SELECT COUNT(id) FROM {table};""")[0][0])
            if table == "AddProductTransaction":
                addProductTransactionCount = int(self.helper.get_list("""SELECT COUNT(id) FROM AddProductTransaction;""")[0][0])
                stockIngridientsCount = int(self.helper.get_list("""SELECT COUNT(id) FROM Stock;""")[0][0])
                if stockIngridientsCount > addProductTransactionCount:
                    count += 1
            self.setRowCount(count)

    def settingSizeColumn(self, settings):
        self.sizing = settings

    def settingSizeColumnActive(self, inf = (0, 0), const = 1):
        counter = 0
        for i in inf:
            b = round(i * const)
            self.setColumnWidth(counter, b)
            counter += 1

    def settingSizeRow(self, size):
        for i in range(self.rowCount()):
            self.setRowHeight(i, size)

    def add_columns(self, columns):
        for i, b in columns:
            self.setHorizontalHeaderItem(i, QTableWidgetItem(b))

    def basikSetting(self):
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setShowGrid(False)

    def resizeEvent(self, event):
        self.coef = event.size().width()
        self.coef = self.coef / self.const
        self.settingSizeColumnActive(self.sizing, self.coef)
    

