from PyQt6.QtWidgets import QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QRadioButton, QAbstractItemView
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QFont

from widgets.ordersListWidget import OrdersListWidget
from functions.db_Helper import Db_helper
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.main_window.pay_window.clock_face import Сlock_face
from widgets.main_window.pay_window.insert_all_button import Insert_all_button

                


class Pay_widget(QWidget):
    def __init__(self, activeTab, centralWidget, tablesListWidget):
        super().__init__()
        self.pay_widget_grid = QGridLayout()
        self.setLayout(self.pay_widget_grid)
        self.helper = Db_helper("Alpha.db")
        self.tablesListWidget = tablesListWidget
        self.activeTab = activeTab
        self.centralWidget = centralWidget

        self.ordersListWidget = OrdersListWidget(active_window = self.activeTab)
        self.ordersListWidget.setColumnCount(4)
        self.ordersListWidget.add_columns(((0, "name"), (1, "price"), (2, "count"), (3, "total")))
        self.ordersListWidget.settingSizeColumn(( 200, 130, 100, 100))
        self.ordersListWidget.setRowCount(15)

        try:
            self.summ_order = int(self.helper.get_list(f"""SELECT SUM(price)
                                        FROM  OpenOrder, Menu
                                        WHERE OpenOrder.id_menu = Menu.id AND id_table = {self.activeTab.activeTab}
                                        GROUP BY OpenOrder.id_table;""")[0][0])
        except:
            self.summ_order = 0

        self.summ = QLabel(text="Summ")
        self.summ.setFont(QFont("Arial", 15))
        self.summ_numb = QLabel(text="tl")
        self.summ_numb.setFont(QFont("Arial", 15))
        self.comment = QTextEdit()
        self.comment.setPlaceholderText("'Info' this function in progress...")
        self.comment.setFont(QFont("Arial", 20))

        self.cashQLineEdit = InsertMoneyQLineEdit(nameLine="Cash")
        self.cashQLineEdit.focusInEvent = self.changeQLineEditCash
        

        self.cardQLineEdit = InsertMoneyQLineEdit(nameLine="Card")
        self.cardQLineEdit.focusInEvent = self.changeQLineEditCard


        self.activeQLineEdit = ActiveQLineEdit(cash=self.cashQLineEdit, card=self.cardQLineEdit)
        self.cashQLineEdit.textChanged.connect(self.writeHandlerCash)
        self.cardQLineEdit.textChanged.connect(self.writeHandlerCard)

        self.payment = QPushButton("Paymant")
        self.payment.setFont(QFont("Arial", 20))
        self.payment.clicked.connect(self.payment_func)
        self.cancel = QPushButton("Cancel")
        self.cancel.setFont(QFont("Arial", 20))
        self.cancel.clicked.connect(self.setCentralWidget)
        self.time_open = QLabel()
        self.time_open.setFont(QFont("Arial", 15))
        self.change = QLabel()
        self.change.setFont(QFont("Arial", 15))
        self.clicker = Сlock_face(cash_line=self.cashQLineEdit, card_line=self.cardQLineEdit, summ_order = self.summ_order, change = self.change, activeQLineEdit=self.activeQLineEdit)
        self.textLabelDiscount = QLabel(text="Discount")
        self.textLabelDiscount.setFont(QFont("Arial", 15))
        self.textLabelTl = QLabel(text="tl")
        self.textLabelTl.setFont(QFont("Arial", 15))
        self.textLabelTimeOpen = QLabel(text="Time open")
        self.textLabelTimeOpen.setFont(QFont("Arial", 15))

        self.pay_widget_grid.addWidget(self.cashQLineEdit, 7, 11, 2, 2)
        self.pay_widget_grid.addWidget(self.cardQLineEdit, 9, 11, 2, 2)
        self.pay_widget_grid.addWidget(self.payment, 12, 8, 1, 3)
        self.pay_widget_grid.addWidget(self.cancel, 12, 11, 1, 2)
        self.pay_widget_grid.addWidget(self.comment, 12, 1, 1, 2)
        self.pay_widget_grid.addWidget(self.clicker, 1, 8, 6, 5)
        self.pay_widget_grid.addWidget(self.summ, 9, 8)
        self.pay_widget_grid.addWidget(self.summ_numb, 9, 9)
        self.pay_widget_grid.addWidget(self.textLabelDiscount, 10, 8)
        self.pay_widget_grid.addWidget(self.textLabelTl, 10, 9)
        self.pay_widget_grid.addWidget(self.ordersListWidget, 1, 1, 10, 2)
        self.pay_widget_grid.addWidget(self.textLabelTimeOpen, 8, 8)
        self.pay_widget_grid.addWidget(self.time_open, 8, 9)
        self.pay_widget_grid.addWidget(self.change, 11, 11,)
        self.drow_pay_orders()

    def writeHandlerCash(self, event):
        self.numb = str(self.activeQLineEdit.getCashMoney() - self.summ_order)
        self.setShangeSumm()
        if event == "":
            self.cardQLineEdit.setPlaceholderText(self.cardQLineEdit.nameLine)
        else:
            self.cardQLineEdit.setPlaceholderText(str(self.numb))

    def writeHandlerCard(self, event):
        self.numb = str(self.activeQLineEdit.getCardMoney() - self.summ_order)
        self.setShangeSumm()
        if event == "":
            self.cashQLineEdit.setPlaceholderText(self.cashQLineEdit.nameLine)
        else:
            self.cashQLineEdit.setPlaceholderText(self.numb)

    def setShangeSumm(self):
        self.changeSumm = str(self.activeQLineEdit.getCashMoney() + self.activeQLineEdit.getCardMoney() - self.summ_order)
        self.change.setText(f"Money: {self.changeSumm}")

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
        try:
            self.time_open.setText(f"{time}")
            self.summ_numb.setText(f"{self.summ_order} TL")
        except:
            ...

    def setCentralWidget(self):
        self.cashQLineEdit.clear()
        self.cardQLineEdit.clear()
        self.change.clear()
        self.centralWidget.takeCentralWidget()
        self.centralWidget.setCentralWindow()

    def payment_func(self, e):
        self.cash_insert = 0
        self.card_insert = 0
        self.card_insert = self.activeQLineEdit.getCardMoney()
        self.cash_insert = self.activeQLineEdit.getCashMoney()

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
            self.centralWidget.drowAllwOrders()
            self.change.setText("")
            self.activeQLineEdit.cash.clear()
            self.activeQLineEdit.card.clear()
            self.setCentralWidget()

    def changeQLineEditCash(self, event):
        self.activeQLineEdit.insertNewActiveLine(self.cashQLineEdit)
    
    def changeQLineEditCard(self, event):
        self.activeQLineEdit.insertNewActiveLine(self.cardQLineEdit)



class ActiveQLineEdit():
    def __init__(self, cash, card):
        self.cash = cash
        self.card = card
        self.activeLine = cash
        self.oldActiveLine = card
    
    def getActiveLine(self) -> QLineEdit:
        return self.activeLine
    
    def getOldLine(self) -> QLineEdit:
        return self.oldActiveLine
    
    def insertNewActiveLine(self, line: QLineEdit) -> None:
        if self.activeLine != line:
            self.oldActiveLine = self.activeLine
            self.activeLine = line

    def getCardMoney(self) -> int:
        if self.card.text() == "":
            return 0
        return int(self.card.text())
    
    def getCashMoney(self) -> int:
        if self.cash.text() == "":
            return 0
        return int(self.cash.text())

    


class InsertMoneyQLineEdit(QLineEdit):
    def __init__(self, nameLine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nameLine = nameLine
        self.setFont(QFont("Arial", 20))
        self.setPlaceholderText(nameLine)
        self.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{7}")))