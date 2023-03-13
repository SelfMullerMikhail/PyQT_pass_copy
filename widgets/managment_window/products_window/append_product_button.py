import os, shutil
from PyQt6.QtWidgets import QPushButton, QDialog, QFileDialog, QWidget, QGridLayout, QLineEdit, QComboBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, QSize

from functions.db_Helper import Db_helper
from widgets.ordersListWidget import OrdersListWidget
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.managment_window.products_window.customs_widgets import *
from func_get_path_icon import get_path_icon

class Append_product_button(QPushButton):
    def __init__(self, *args, window, products_window, central_wind):
        super().__init__(*args)
        self.helper = Db_helper("Alpha.db")
        self.wind = window
        self.central_window = central_wind
        self.products_window = products_window
        self.file_put = 'coffee.svg'
        self.feather = None
        self.clicked.connect(self.add_product_window)
        self.category = self.helper.get_one("""SELECT name FROM Category""")[0]

    def add_product_window(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[\w\s]{1,20}")))
        self.enter_price = QLineEdit()
        self.enter_price.setPlaceholderText("Price")
        self.enter_price.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,8}")))
        self.choose_category = QComboBox()
        self.append_category()
        self.choose_category.textActivated.connect(self.change_category)
        self.ingridients = OrdersListWidget(active_window = self.form)
        self.ingridients.setColumnCount(3) 
        self.ingridients.setLineCount("AddProductTransaction")
        self.ingridients.add_columns(((0, "Name"), (1, "Count "), (2, " ")))
        self.ingridients.settingSizeColumn((100, 100, 50))
        self.ingridients.settingSizeRow(35)
        self.drow_ingridients_transaction()
        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_append_func)
        self.form.setLayout(self.form_Layout)
        self.butt = QPushButton("Choose photo")
        self.butt.clicked.connect(self.choose_photo_func)
        self.butt.setIcon(get_path_icon(self.file_put))
        self.butt.setIconSize(QSize(50,50))
        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_price, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.choose_category, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.butt, 3, 0, 1, 2 )
        self.form_Layout.addWidget(self.ingridients, 6, 0 ,2, 2)
        self.form_Layout.addWidget(self.append_button , 8, 0)
        self.form_Layout.addWidget(self.cancel_button, 8, 1)
        self.form.show()

    def close_append_func(self):
        self.helper.insert("""DELETE FROM  AddProductTransaction;""")
        self.file_put = 'coffee.svg'
        self.form.close()
    
    def change_category(self, e):
        self.category = e

    def choose_photo_func(self):
            wind = QDialog()
            self.file = QFileDialog.getOpenFileName(wind, "Open file", "C:\\", "Image (*.png)")[0]
            self.file_put = self.file.split("/")[-1]
            if self.file_put == "":
                self.file_put = 'coffee.svg'
            self.feather = str(os.path.dirname( __file__ )).replace("widgets\managment_window\products_window" ,f"feather\{self.file_put}")
            if self.file!="":
                shutil.copyfile(self.file, self.feather)
                self.butt.setIcon(get_path_icon(self.file_put))
            
    def append_func(self):
        text = self.enter_name.text()
        price = self.enter_price.text()
        already_name_menu = self.helper.get_one(f"""SELECT count(id) FROM Menu WHERE name = '{text}';""")[0]
        if text != "" and already_name_menu == 0:
            if price == "":
                price = 0
            
            self.helper.insert(f"""INSERT INTO Menu (name, category, price, image)
                                    SELECT '{text}', Category.id, {price}, '{self.file_put}'
                                    FROM Category 
                                    WHERE Category.name = '{self.category}' """)
            max_numb = self.helper.get_one("""SELECT MAX(id) FROM Menu """)[0]
            self.helper.insert(f"""INSERT INTO TechnologyCard (id_menu, id_product, count)
                                SELECT {max_numb}, id, count FROM AddProduct_to_TechnologyCard""")
            self.helper.insert("""DELETE FROM AddProductTransaction""")
            self.products_window.drow_products()
            self.central_window.Main_widget.menuTabWidget.clear()
            self.central_window.Main_widget.menuTabWidget.create_full_menu()
            self.form.close()
    
    def append_category(self):
        categories = self.helper.get_list("SELECT name FROM Category;")
        for i in categories:
            self.choose_category.addItem(i[0])

    def drow_ingridients_transaction(self):
        self.ingridients.clearContents()
        self.ingridients.setLineCount("AddProductTransaction")
        info = self.helper.get_list(f"""SELECT name_product, count FROM AddProductTransaction;""")
        self.box = CustomComboBox()
        self.line = QLineEdit()
        self.line.setPlaceholderText("ml/g")
        self.line.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,7}")))
        self.row_line = 0
        for row in range(0, len(info)):
            self.row_line = row + 1
            self.ingridients.setItem(row, 0, CustomQTableWidgetItem(str(info[row][0])))
            self.ingridients.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.ingridients.setCellWidget(row, 2, CustomButtonDell(name = info[row][0], text="del", window = self))
        self.ingridients.setCellWidget(self.row_line, 0, self.box)
        self.ingridients.setCellWidget(self.row_line, 1, self.line)
        self.ingridients.setCellWidget(self.row_line, 2, CustomButtonAdd(name = self.box, count=self.line, text="add", window = self))


        