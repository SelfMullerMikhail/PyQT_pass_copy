from PyQt6.QtWidgets import QComboBox, QLineEdit, QPushButton, QGridLayout, QWidget
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression

from widgets.ordersListWidget import OrdersListWidget
from widgets.managment_window.sorting_QComboBox import Sorting_QComboBox
from widgets.managment_window.products_window.dell_product_button import Dell_product_button
from widgets.managment_window.stock_window.add_stock_button import Add_stock_button
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem

from functions.db_Helper import Db_helper



class Stock_window(QGridLayout):
    def __init__(self, active_window, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.central_window = central_window
        self.products_list = OrdersListWidget(active_window = active_window)
        self.products_list.setColumnCount(6) 
        self.products_list.add_columns(((0, "Name"), (1, "Count"), (2, "Price"), (3, "Total money"), (4, ""), (5, "")))
        self.products_list.settingSizeColumn((70, 70, 70, 70, 40, 40))
        self.products_list.settingSizeRow(50)
        self.products_list.setLineCount("Stock")
        self.drow_stock()

        self.quick_search = QLineEdit()
        self.quick_search.setPlaceholderText("Quick search")
        self.quick_search.textChanged.connect(self.printer)
        self.quick_search.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9]{1,10}")))

        self.sorting = Sorting_QComboBox() #Кастомить
        self.sorting.addItemCycle(("Name", "Count", "Price", "'Total money'"))
        self.sorting.textActivated.connect(self.sort)

        self.append_button = QPushButton(text="Append") # Кастомить
        self.append_button.clicked.connect(self.add_product_window)


        self.addWidget(self.products_list, 1, 0, 19, 20)
        self.addWidget(self.quick_search, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)
        self.addWidget(self.append_button, 0, 18, 1, 2)

    def printer(self, e):
        self.products_list.drow_stock(inf = e)

    def sort(self, e):
        self.products_list.drow_stock(category=e)

#####################################################################################
    def add_product_window(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9]{1,10}")))

        self.enter_price = QLineEdit()
        self.enter_price.setPlaceholderText("Price for 1 l/kg")
        self.enter_price.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,7}")))

        self.choose_diller = QComboBox()
        self.append_category()
        self.choose_diller.textActivated.connect(self.change_category)
        self.choose_diller.diller = self.choose_diller.itemText(0)


        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.form.close)

        self.form.setLayout(self.form_Layout)

        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_price, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.choose_diller, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 3, 0, 1, 1 )
        self.form_Layout.addWidget(self.cancel_button, 3, 3, 1, 1 )
        self.form.show()

    def append_category(self):
        info = self.helper.get_list("""SELECT name FROM Suppliers""")
        for i in info:
            self.choose_diller.addItem(i[0])

    def change_category(self, e):
        self.choose_diller.diller = e

    def append_func(self):
        name = self.enter_name.text()
        price = self.enter_price.text()
        if name != "":
            if price == "":
                price = 0
            diller = self.choose_diller.diller
            if diller == "":
                id_diller = 0
            else:
                print(f"--{diller}--")
                print(f"--{id_diller}--")
                id_diller = self.helper.get_tuple(f"""SELECT id FROM Suppliers WHERE name = '{diller}' """)[0]
            self.helper.insert(f"""INSERT INTO Stock(name, count, price, id_Suppiler) 
                                    VALUES ('{name}', 0, {price}, {id_diller}) """)
            self.products_list.setLineCount("Stock")
            self.drow_stock()
            self.form.close()

    def drow_stock(self, inf="", category = "Name"):
        self.products_list.clearContents()
        info = self.helper.get_list((f"""SELECT Name, Count, Price, (Count/1000*Price) as 'Total money', id_Suppiler, id 
                                                    FROM Stock
                                                    WHERE Name LIKE '%{inf}%'
                                                    ORDER BY {category};"""))
        for row in range(len(info)):
            for i in range(4):
                self.products_list.setItem(row, i, CustomQTableWidgetItem(str(info[row][i])))
            self.products_list.setCellWidget(row, 4, Add_stock_button(text="add count", id_suppiler=info[row][4], id_stock=info[row][5], orderList = self))
            self.products_list.setCellWidget(row, 5, Dell_product_button("del", name = info[row][0], order_window = self))