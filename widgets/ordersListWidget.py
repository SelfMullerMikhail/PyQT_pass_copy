from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QAbstractItemView, QHeaderView, QAbstractItemDelegate



class CustomQTableWidgetItem(QTableWidgetItem):
    def __init__(self, *args):
        super().__init__(*args)
        self.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)

class OrdersListWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        # self.setFixedHeight(500)
        # self.setFixedWidth(400)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setColumnCount(6)
        self.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setShowGrid(False)

        self.setRowCount(3)
        
        name = QTableWidgetItem("name")
        price = QTableWidgetItem("price")
        minus = QTableWidgetItem("")
        count = QTableWidgetItem("count")
        plus = QTableWidgetItem("")
        total = QTableWidgetItem("total")
        self.setHorizontalHeaderItem (0, name)
        self.setHorizontalHeaderItem (1, price)
        self.setHorizontalHeaderItem (2, minus)
        self.setHorizontalHeaderItem (3, count)
        self.setHorizontalHeaderItem (4, plus)
        self.setHorizontalHeaderItem (5, total)

        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 100)
        self.setColumnWidth(2, 2)
        self.setColumnWidth(3, 50)
        self.setColumnWidth(4, 2)
        self.setColumnWidth(5, 70)


        self.insertRow(1)

        self.setItem(0, 0, CustomQTableWidgetItem("Americano"))
        self.setItem(0, 1, CustomQTableWidgetItem("140"))
        self.setItem(0, 2, CustomQTableWidgetItem("-"))
        self.setItem(0, 3, CustomQTableWidgetItem("2"))
        self.setItem(0, 4, CustomQTableWidgetItem("+"))
        self.setItem(0, 5, CustomQTableWidgetItem("280"))
        
        self.itemClicked.connect(self.printer)

    def printer(self, e):
        print("ee", e)