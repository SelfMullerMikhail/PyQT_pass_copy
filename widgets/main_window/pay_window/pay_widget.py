from PyQt6.QtWidgets import QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QRadioButton
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from widgets.ordersListWidget import OrdersListWidget
from functions.db_Helper import Db_helper
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.main_window.pay_window.clock_face import Сlock_face
from widgets.main_window.pay_window.insert_all_button import Insert_all_button

                


class Pay_widget(QWidget):
    def __init__(self, activeTab, centralWidget, tablesListWidget):
        super().__init__()
        self.reg = QRegularExpression("[1-9][0-9]{7}")
        self.pay_widget_grid = QGridLayout()
        self.setLayout(self.pay_widget_grid)
        self.helper = Db_helper("Alpha.db")
        self.tablesListWidget = tablesListWidget

        self.activeTab = activeTab
        self.centralWidget = centralWidget

        self.ordersListWidget = OrdersListWidget(active_window = self.activeTab)
        self.ordersListWidget.setColumnCount(4)
        self.ordersListWidget.add_columns(((0, "name"), (1, "price"), (2, "count"), (3, "total")))
        self.ordersListWidget.settingSizeColumn(( 100, 100, 100, 70))
        self.ordersListWidget.setRowCount(15)

        self.summ_order = self.helper.get_list(f"""SELECT SUM(price)
                                        FROM  OpenOrder, Menu
                                        WHERE OpenOrder.id_menu = Menu.id AND id_table = {self.activeTab.activeTab}
                                        GROUP BY OpenOrder.id_table;""")[0][0]

        self.summ = QLabel(text="Summ")
        self.summ.setMaximumSize(50,50)

        self.summ_numb = QLabel(text="tl")
        self.summ_numb.setMaximumSize(50,50)

        self.comment = QTextEdit()
        self.comment.setPlaceholderText("SHEOFIN")

        self.cash = QLineEdit()
        self.cash.setPlaceholderText("Cash")
        self.cash.setMinimumHeight(50)
        self.cash.setValidator(QRegularExpressionValidator(self.reg))
        
        self.card = QLineEdit()
        self.card.setPlaceholderText("Card")
        self.card.setMinimumHeight(50)
        self.card.setValidator(QRegularExpressionValidator(self.reg))

        payment = QPushButton("Paymant")
        payment.setMinimumHeight(180)
        payment.clicked.connect(self.payment_func)
        
        cancel = QPushButton("Cancel")
        cancel.setMinimumHeight(180)
        cancel.clicked.connect(self.setCentralWidget)

        self.time_open = QLabel()
        self.change = QLabel()

        self.clicker = Сlock_face(cash_line=self.cash, card_line=self.card, summ_order = self.summ_order, change = self.change)

        self.insert_all = Insert_all_button(text = "Insert all", summ = self.summ_order, active_line=self.clicker)
        self.insert_all.setMinimumHeight(40)

        self.pay_widget_grid.addWidget(self.cash, 7, 11, 2, 2)
        self.pay_widget_grid.addWidget(self.card, 9, 11, 2, 2)
        self.pay_widget_grid.addWidget(payment, 12, 8, 1, 3)
        self.pay_widget_grid.addWidget(cancel, 12, 11, 1, 2)
        self.pay_widget_grid.addWidget(self.comment, 12, 1, 1, 2)
        self.pay_widget_grid.addWidget(self.clicker, 1, 8, 6, 5)
        self.pay_widget_grid.addWidget(self.summ, 9, 8)
        self.pay_widget_grid.addWidget(self.summ_numb, 9, 9)
        self.pay_widget_grid.addWidget(QLabel(text="Discount"), 10, 8)
        self.pay_widget_grid.addWidget(QLabel(text="0 tl"), 10, 9)
        self.pay_widget_grid.addWidget(self.ordersListWidget, 1, 1, 10, 2)
        self.pay_widget_grid.addWidget(QLabel(text="Time open"), 8, 8)
        self.pay_widget_grid.addWidget(self.time_open, 8, 9)
        self.pay_widget_grid.addWidget(self.change, 11, 11,)
        self.pay_widget_grid.addWidget(self.insert_all, 7, 8, 1, 2)

        self.drow_pay_orders()

    def drow_pay_orders(self):
        info = self.helper.get_list(f"""SELECT Menu.name, Menu.price, count(count), (Menu.price * count(count)), Menu.id 
                                            FROM  OpenOrder, Menu
                                            WHERE OpenOrder.id_menu = Menu.id AND id_table = {self.activeTab.activeTab}
                                            GROUP BY id_menu;""")
        for row in range(len(info)):
            self.ordersListWidget.setItem(row, 0, CustomQTableWidgetItem(str(info[row][0])))
            self.ordersListWidget.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.ordersListWidget.setItem(row, 2, CustomQTableWidgetItem(str(info[row][2])))
            self.ordersListWidget.setItem(row, 3, CustomQTableWidgetItem(str(info[row][3])))

            time = self.helper.get_list(f"""SELECT time_open
                                            FROM Tables
                                            WHERE Tables.id = {self.activeTab.activeTab};""")[0][0]
        self.time_open.setText(f"{time}")
        self.summ_numb.setText(f"{self.summ_order} TL")


    def setCentralWidget(self):
        self.centralWidget.takeCentralWidget()
        self.centralWidget.setCentralWindow()

    def payment_func(self, e):
        self.cash_insert = 0
        self.card_insert = 0
        if self.card.text() != "":
            self.card_insert = int(self.card.text())
            
        if self.cash.text() != "":
            self.cash_insert = int(self.cash.text())

        cash = self.summ_order - int(self.card_insert)

        if ((self.cash_insert + self.card_insert) >= self.summ_order) and (self.card_insert <= self.summ_order):

            self.helper.insert(f"""INSERT INTO ClosedOrder (id_table, name_table, client_name, menu_name, count, cash, card, time_open, menu_price)
                                SELECT OpenOrder.id_table, Tables.tables_name, Client.name, Menu.name, COUNT(OpenOrder.count), {cash}, {self.card_insert}, Tables.time_open, Menu.price
                                FROM OpenOrder, Menu, Client, Tables
                                WHERE OpenOrder.id_menu = Menu.id AND OpenOrder.id_client = Client.id
                                AND OpenOrder.id_table = Tables.id AND Tables.id_client = Client.id
                                AND OpenOrder.id_table = {self.activeTab.activeTab}
                                GROUP BY Menu.name;""")
            all_ingridients = self.helper.get_list(f"""SELECT id_product FROM TransactionStock WHERE id_table = {self.activeTab.activeTab} """)
            for i in all_ingridients:
                self.helper.insert(f"""UPDATE Stock SET count = (SELECT (StockCount-count) 
                                    FROM TransactionStock
                                    WHERE TransactionStock.id_table = {self.activeTab.activeTab} AND id_product = {i[0]}) WHERE id = {i[0]}; """)

            self.tablesListWidget.del_table(pay = True)
            self.centralWidget.managment_window.stock_window.drow_stock()
            self.centralWidget.archive_widget.drow_archive_all()
            self.setCentralWidget()
