from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QMainWindow
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QResizeEvent

from functions.db_Helper import Db_helper
from widgets.managment_window.products_window.customs_widgets import *
from functions.active_tub import ActiveTable



class OrdersListWidget(QTableWidget):
    def __init__(self, active_window: ActiveTable = None, central_window: QMainWindow = None) -> None:
        super().__init__()
        """Widget for drowing some info"""
        self.const = self.size().height() + 100
        self.helper = Db_helper("Alpha.db")
        self.activeTab = active_window
        self.functions = {}
        self.central_window = central_window
        self.setIconSize(QSize(50, 50))
        self.basikSetting()

    def setLineCount(self, table: str) -> None:
            """Insert next id (cointer) for table in DB """
            count = int(self.helper.get_list(f"""SELECT COUNT(id) FROM {table};""")[0][0])
            if table == "AddProductTransaction":
                addProductTransactionCount = int(self.helper.get_list("""SELECT COUNT(id) FROM AddProductTransaction;""")[0][0])
                stockIngridientsCount = int(self.helper.get_list("""SELECT COUNT(id) FROM Stock;""")[0][0])
                if stockIngridientsCount > addProductTransactionCount:
                    count += 1
            self.setRowCount(count)

    def settingSizeColumn(self, settings: int) -> None:
        self.sizing = settings

    def settingSizeColumnActive(self, inf: tuple = (0, 0), const: int = 1) -> None:
        """Creating one size for all columns """
        counter = 0
        for i in inf:
            b = round(i * const)
            self.setColumnWidth(counter, b)
            counter += 1

    def settingSizeRow(self, size: int):
        """Creating one size for all rows """
        for i in range(self.rowCount()):
            self.setRowHeight(i, size)

    def add_columns(self, columns: tuple) -> None:
        """Appending column from tuple(number, name:str) """
        for i, b in columns:
            self.setHorizontalHeaderItem(i, QTableWidgetItem(b))

    def basikSetting(self) -> None:
        """Settings basics viesual options """
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setShowGrid(False)

    def resizeEvent(self, event: QResizeEvent):
        """Method overload for interactive resizing"""
        self.coef = event.size().width()
        self.coef = self.coef / self.const
        self.settingSizeColumnActive(self.sizing, self.coef)
    

