from PyQt6.QtWidgets import QPushButton, QGridLayout, QLineEdit, QLabel, QWidget, QMessageBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from widgets.ordersListWidget import OrdersListWidget
from widgets.numbers_table import Numbers_table
from widgets.archive_window.info_products_order import InfoProductsOrder
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from functions.db_Helper import Db_helper

class DayOf_widget(QGridLayout):
    def __init__(self, mainWidget):
        super().__init__()
        self.mainWidget = mainWidget
        self.helper = Db_helper("Alpha.db")
        self.helper_beta = Db_helper("Beta.db")
        self.money = 0

        self.list_ = {1: "Cash", 2: "Card"}
        self.i = 1
        self.e_card = 0
        self.e_cash = 0
        self.changer = next(self.changer_genetarion())
        
        self.fact_cash = QLineEdit()
        self.fact_cash.textChanged.connect(self.fact_cash_func)
        self.fact_card = QLineEdit()
        self.fact_card.textChanged.connect(self.fact_card_func)

        self.teory_cash = QLabel()
        self.teory_card =QLabel()
        self.teory_summ = QLabel()

        self.difference_cash = QLabel()
        self.difference_card = QLabel()
        self.difference_sum = QLabel('333')

        for i in (self.fact_cash, self.fact_card):
            i.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]{0,7}")))

        for i in ((self.fact_cash, "Total cash"), (self.fact_card, "Total card")):
            i[0].setPlaceholderText(i[1])
            i[0].setMaximumWidth(150)

 

        self.numbers_table = Numbers_table(selfWidget=self, tipe_of_button=DayOf_buttons)

        self.numbers_table.clear.setText("Clear")
        self.numbers_table.clear.clicked.connect(self.numbers_clear_func)
        self.numbers_table.close_button.clicked.connect(self.numbers_change_func)
        self.numbers_change_func()

        self.transaction_button = QPushButton("DAY OFF")
        self.transaction_button.setMinimumHeight(50)
        self.transaction_button.clicked.connect(self.transaction_func)

        self.functions = {"Cash": self.fact_cash, 
                        "Card": self.fact_card}
        
        self.all_days_transactions = OrdersListWidget(active_window = ...)
        self.all_days_transactions.setColumnCount(9) 
        self.all_days_transactions.add_columns(((0, "id_table"), (1, "name_table"), (2, "client_name"), (3, "cash"), (4, "card"), (5, "total"), (6, "time open"), (7, "time close"), (8, "") ))
        self.all_days_transactions.settingSizeColumn((50, 70, 80, 45, 45, 45, 85, 85, 50))
        self.all_days_transactions.settingSizeRow(30)
        self.drow_history()
        self.fact_cash_func(0)
        self.fact_card_func(0)

        widgets_list = ((QWidget(), 0, 0, 22, 10),
                        (self.fact_cash, 0, 0, 1, 1),
                        (self.teory_cash, 0, 1, 1, 1),
                        (self.difference_cash, 0, 2, 1, 1), 

                        (self.fact_card, 1, 0, 1, 1),
                        (self.teory_card, 1, 1, 1, 1),
                        (self.difference_card, 1, 2, 1, 1),

                        (self.teory_summ, 2, 1, 1, 1),
                        (self.difference_sum, 2, 2, 1, 1),
                        
                        (self.numbers_table, 4, 7, 10, 3),
                        (self.transaction_button, 18, 2, 2, 5),
                         (self.all_days_transactions, 4, 0, 12, 7))
        
        for i in widgets_list:
            self.addWidget(i[0], i[1], i[2], i[3], i[4])
        self.e_cash = 0
        self.e_card = 0

    def fact_cash_func(self, e):
        if e == "":
            e = 0
        self.e_cash = int(e)
        try:
            self.money = int(e) - int(self.all_summ[0][0])
        except:
            ...
        self.difference_cash.setText(str(self.money))
        self.set_difference_summ()

    def fact_card_func(self, e):
        try:
            if e == "":
                e = 0
            self.e_card = int(e)
            self.money = int(e) - int(self.all_summ[0][1])
            self.difference_card.setText(str(self.money))
            self.set_difference_summ()
        except:
            ...

    def set_difference_summ(self):
        try:
            difference = (self.e_cash + self.e_card) - int(self.all_summ[0][0]+int(self.all_summ[0][1]))
            self.difference_sum.setText(str(difference))
        except:
            ...
    def changer_genetarion(self):
        while True:
            self.i += 1
            if self.i == 3:
                self.i = 1
            yield self.list_[self.i]

    def numbers_clear_func(self):
        self.fact_cash.clear()
        self.fact_card.clear()

    def numbers_change_func(self):
        self.changer = next(self.changer_genetarion())
        self.numbers_table.close_button.setText(self.changer)

    def drow_history(self):
        self.all_days_transactions.clearContents()
        self.all_summ = self.helper.get_list(f"""SELECT sum(cash), sum(card) FROM CloseOrderView;""")
        self.teory_cash.setText(f"Cash: {self.all_summ[0][0]}")
        self.teory_card.setText(f"Card: {self.all_summ[0][1]}")
        try:
            self.teory_summ.setText(f"Sum: {int(self.all_summ[0][0]) + int(self.all_summ[0][1])}")
        except:
            ...

        info = self.helper.get_list(f"""SELECT * FROM CloseOrderView GROUP BY id_table ORDER BY id;""")
        self.all_days_transactions.setRowCount(len(info))
        for row in range(len(info)):
            self.all_days_transactions.setCellWidget(row, 0, InfoProductsOrder(row = row, id_table = str(info[row][1]), db="Alpha.db"))# id_table
            self.all_days_transactions.setItem(row, 1, CustomQTableWidgetItem(str(info[row][2]))) # name_table
            self.all_days_transactions.setItem(row, 2, CustomQTableWidgetItem(str(info[row][3]))) # client_name
            self.all_days_transactions.setItem(row, 3, CustomQTableWidgetItem(str(info[row][6]))) # cash
            self.all_days_transactions.setItem(row, 4, CustomQTableWidgetItem(str(info[row][7]))) # card
            self.all_days_transactions.setItem(row, 5, CustomQTableWidgetItem(str(info[row][6]+info[row][7] ))) # total 
            self.all_days_transactions.setItem(row, 6, CustomQTableWidgetItem(str(info[row][8]))) # time_open
            self.all_days_transactions.setItem(row, 7, CustomQTableWidgetItem(str(info[row][9]))) # time_close

    def upgrading(self):
        self.drow_history()
        self.fact_cash_func(0)
        self.fact_card_func(0)  

    def transaction_func(self):
        msgBox = QMessageBox()
        msgBox.setText(f"Are you sure?")
        yes = QMessageBox.StandardButton.Ok
        msgBox.setStandardButtons(yes | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setWindowTitle("Close day")
        result = msgBox.exec()
        if result == yes:
            if self.e_cash == "":
                self.e_cash = 0
            if self.e_card == "":
                self.e_card = 0
            history_of_alpha = self.helper.get_list("""SELECT * FROM ClosedOrder;""")
            for i in history_of_alpha:
                self.helper_beta.insert(f"""INSERT INTO HistoryTable VALUES(
                            {i[0]}, {i[1]}, '{i[2]}', '{i[3]}', '{i[4]}', {i[5]}, {i[6]}, {i[7]}, '{i[8]}', '{i[9]}', {i[10]});""")
            self.helper_beta.insert(f"""INSERT INTO MoneyStory(cash_teory,cash_fact, card_teory, card_fact) 
                                    VALUES({self.all_summ[0][0]}, {self.e_cash}, {self.all_summ[0][1]}, {self.e_card});""") 
            self.helper.get_list(f"""DELETE FROM ClosedOrder;""")
            self.mainWidget.setCentralWindow_authorization()



    

class DayOf_buttons(QPushButton):
    def __init__(self, text, selfWidget=..., main_wdinow =...):
        super().__init__()
        self.text_ = text
        self.selfWidget = selfWidget
        self.setText(text)
        self.clicked.connect(self.func)

    def func(self):
        self.selfWidget.functions[self.selfWidget.changer].insert(self.text_)



       
       
       
       
        # self.addWidget(QTableWidget(), 0, 0, 3, 1)