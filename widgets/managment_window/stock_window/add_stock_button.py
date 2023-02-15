from PyQt6.QtWidgets import QPushButton, QWidget, QGridLayout, QLineEdit, QComboBox, QCalendarWidget
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression
from functions.db_Helper import Db_helper


class Add_stock_button(QPushButton):
    def __init__(self, text, id_stock, id_suppiler, orderList) -> None:
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.id_stock = id_stock
        self.id_suppiler = id_suppiler
        self.orderList = orderList
        self.clicked.connect(self.func)

    def func(self, e):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()

        self.enter_price = QLineEdit()
        self.enter_price.setPlaceholderText('Price tl for 1 kg,L')
        self.enter_price.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,10}")))

        self.enter_count = QLineEdit()
        self.enter_count.setPlaceholderText('Count ml/gr')
        self.enter_count.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,10}")))

        self.enter_data = QCalendarWidget()
        self.enter_data.clicked.connect(self.enterdata)
        self.enterdata()


        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.form.close)

        self.form.setLayout(self.form_Layout)

        self.form_Layout.addWidget(self.enter_price, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_count, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_data, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 3, 0, 1, 1 )
        self.form_Layout.addWidget(self.cancel_button, 3, 3, 1, 1 )
        self.form.show()
    
    def enterdata(self, e = ''):
        dat = self.enter_data.selectedDate()
        self.day = dat.day()
        self.month = dat.month()
        self.year = dat.year()

    def append_func(self, e):
        price = int(self.enter_price.text())
        count = int(self.enter_count.text())
        self.helper.insert(f"""INSERT INTO SupplyOfProducts(id_stock, id_suppiler, price, count, date_supply)
                             VALUES({self.id_stock}, {self.id_suppiler}, {price}, {count}, date('{self.year}-{self.month}-{self.day}'));""")
        
        self.helper.insert(f"""UPDATE Stock SET count = (count + {count}) WHERE id = {self.id_stock};""")

        price_count = self.helper.get_list(f"""SELECT price, count FROM Stock WHERE id = {self.id_stock} """)[0]
        fact_price = int(price_count[0])
        fact_count = int(price_count[1])
        if fact_price != 0:
            self.count_new_price(fact_count, fact_price, count, price)
        else:
            self.helper.insert(f"""UPDATE Stock SET price = {price} WHERE id = {self.id_stock};""")
        self.orderList.drow_stock()
        self.form.close() 

    def count_new_price(self, fact_count, fact_price, count, price):
        A_koef = fact_count / (fact_count + count)
        B_koef = count / (fact_count + count )
        A_price_g = (fact_price * 0.001) * A_koef
        B_price_g = (price * 0.001) * B_koef
        normal_price = (A_price_g + B_price_g) * 1000
        self.helper.insert(f"""UPDATE Stock SET price = {normal_price} WHERE id = {self.id_stock};""")