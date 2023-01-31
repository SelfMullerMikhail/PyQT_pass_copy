from PyQt6.QtWidgets import QGridLayout, QLineEdit, QLabel, QComboBox, QPushButton, QMessageBox
from PyQt6.QtCore import QSize

from widgets.ordersListWidget import OrdersListWidget
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from func_get_path_icon import get_path_icon
from functions.db_Helper import Db_helper

class Archive_widget(QGridLayout):
    def __init__(self,):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.archive_list = OrdersListWidget(active_window = ...)
        self.archive_list.setColumnCount(9) 
        self.archive_list.setLineCount("ClosedOrder")
        self.archive_list.add_columns(((0, "id_table"), (1, "name_table"), (2, "client_name"), (3, "cash"), (4, "card"), (5, "total"), (6, "time open"), (7, "time close"), (8, "") ))
        self.archive_list.settingSizeColumn((50, 70, 80, 45, 45, 45, 85, 85, 50))
        self.archive_list.settingSizeRow(30)

        self.quick_search = QLineEdit()
        self.quick_search.setPlaceholderText("Quick search")
        self.quick_search.setMaximumWidth(170)
        self.quick_search.textChanged.connect(self.quick_search_func)

        self.sorting = QComboBox()
        sort_list = ["id_table", "name_table", "client_name", "cash", "card", "total", "time_open", "time_close"]
        for i in sort_list:
            self.sorting.addItem(f"{i}")
        self.category_search = sort_list[0]
        self.quick_search_line = ""

        self.sorting.textActivated.connect(self.sorting_func)

        self.total_cash = QLabel()
        self.total_card = QLabel()
        self.total_money = QLabel()

        self.addWidget(self.quick_search, 0, 0, 1, 1)
        self.addWidget(self.sorting, 0, 2, 1, 3)
        self.addWidget(self.archive_list, 2, 0, 16, 12)
        self.addWidget(self.total_cash, 19, 9, 1, 1)
        self.addWidget(self.total_card, 19, 10, 1, 1)
        self.addWidget(self.total_money, 19, 11, 1, 1)
        self.drow_archive_all()

    def sorting_func(self, e):
        self.category_search = e
        self.drow_archive_all()

    def quick_search_func(self, e):
        self.quick_search_line = e
        self.drow_archive_all()

    def drow_archive_all(self):
        self.archive_list.clearContents()
        all_money = self.helper.get_list("""SELECT sum(cash), sum(card), (sum(cash)+sum(card))  
                                            FROM CloseOrderView;""")[0]
        info = self.helper.get_list(f"""SELECT * FROM CloseOrderView WHERE {self.category_search} LIKE '%{self.quick_search_line}%' ORDER BY {self.category_search}""")
        self.total_cash.setText(f"cash: {all_money[0]}")
        self.total_card.setText(f"card: {all_money[1]}")
        self.total_money.setText(f"total: {all_money[2]}")
        for row in range(len(info)):
            icon = QPushButton(str(info[row][0]))
            icon.setIcon(get_path_icon('tablet.svg'))
            icon.setIconSize(QSize(25, 25))
            self.archive_list.setCellWidget(row, 0, icon) # id_table
            self.archive_list.setItem(row, 1, CustomQTableWidgetItem(str(info[row][2]))) 
            self.archive_list.setItem(row, 2, CustomQTableWidgetItem(str(info[row][3]))) 
            self.archive_list.setItem(row, 3, CustomQTableWidgetItem(str(info[row][6]))) 
            self.archive_list.setItem(row, 4, CustomQTableWidgetItem(str(info[row][7]))) 

            self.archive_list.setItem(row, 5, CustomQTableWidgetItem(str(info[row][10])))
            self.archive_list.setItem(row, 6, CustomQTableWidgetItem(str(info[row][8]))) 
            self.archive_list.setItem(row, 7, CustomQTableWidgetItem(str(info[row][9]))) 
            self.archive_list.setCellWidget(row, 8, DelCloseOrderButton(text = "del", id_closeOrder=info[row][0], archive_widget = self))

    def drow_arhive_info(self):
        ...

class DelCloseOrderButton(QPushButton):
    def __init__(self, text, id_closeOrder, archive_widget):
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.archive_widget = archive_widget
        self.id_closeOrder = id_closeOrder
        self.clicked.connect(self.del_func)

    def del_func(self):
        msgBox = QMessageBox()
        msgBox.setText(f"""Do you want delete this order? \nid_table:'{self.id_closeOrder}""")
        yes = QMessageBox.StandardButton.Ok
        msgBox.setStandardButtons(yes | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setWindowTitle("Delete order")
        result = msgBox.exec()
        if result == yes:
            self.helper.insert(f"""DELETE FROM ClosedOrder WHERE id = {self.id_closeOrder} """)
            self.archive_widget.drow_archive_all()