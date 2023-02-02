from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton, QMessageBox, QGridLayout

from widgets.ordersListWidget import OrdersListWidget
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.sorting_widgets import QComboBoxSorting, QLineEditSorting
from widgets.archive_window.del_close_order_button import DelCloseOrderButton
from widgets.archive_window.info_products_order import InfoProductsOrder
from functions.db_Helper import Db_helper

class Archive_widget(QGridLayout):
    def __init__(self,):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.archive_list = OrdersListWidget(active_window = ...)
        self.archive_list.setColumnCount(9) 
        self.archive_list.add_columns(((0, "id_table"), (1, "name_table"), (2, "client_name"), (3, "cash"), (4, "card"), (5, "total"), (6, "time open"), (7, "time close"), (8, "") ))
        self.archive_list.settingSizeColumn((50, 70, 80, 45, 45, 45, 85, 85, 50))
        self.archive_list.settingSizeRow(30)



        self.quick_search = QLineEditSorting(selfWidget=self)
        self.quick_search.setMaximumWidth(170)

        sort_list = ["id_table", "name_table", "client_name", "cash", "card", "total", "time_open", "time_close"]
        self.sorting = QComboBoxSorting(selfWidget = self, sort_list = sort_list, quick_search=self.quick_search)

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

    def drow_func(self):
        self.drow_archive_all()


    def drow_archive_all(self):
        self.archive_list.clearContents()
        all_money = self.helper.get_list("""SELECT sum(cash), sum(card), (sum(cash)+sum(card))
                                            FROM CloseOrderView;""")[0]
        info = self.helper.get_list(f"""SELECT * FROM CloseOrderView WHERE {self.sorting.category_search} LIKE '%{self.quick_search.quick_search_line}%' GROUP BY id_table ORDER BY {self.sorting.category_search}""")
        self.archive_list.setRowCount(len(info))
        self.total_cash.setText(f"cash: {all_money[0]}")
        self.total_card.setText(f"card: {all_money[1]}")
        self.total_money.setText(f"total: {all_money[2]}")
        for row in range(len(info)):
            self.archive_list.setCellWidget(row, 0, InfoProductsOrder(selfWidget=self, row = row, id_table = str(info[row][1])))# id_table
            self.archive_list.setItem(row, 1, CustomQTableWidgetItem(str(info[row][2]))) # name_table
            self.archive_list.setItem(row, 2, CustomQTableWidgetItem(str(info[row][3]))) # client_name
            self.archive_list.setItem(row, 3, CustomQTableWidgetItem(str(info[row][6]))) # cash
            self.archive_list.setItem(row, 4, CustomQTableWidgetItem(str(info[row][7]))) # card
            self.archive_list.setItem(row, 5, CustomQTableWidgetItem(str(info[row][6]+info[row][7] ))) # total 
            self.archive_list.setItem(row, 6, CustomQTableWidgetItem(str(info[row][8]))) # time_open
            self.archive_list.setItem(row, 7, CustomQTableWidgetItem(str(info[row][9]))) # time_close
            self.archive_list.setCellWidget(row, 8, DelCloseOrderButton(text = "del", id_closeOrder=info[row][0], archive_widget = self)) # del
    def drow_arhive_info(self):
        ...
