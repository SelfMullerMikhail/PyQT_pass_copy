import os, shutil
from PyQt6.QtWidgets import QPushButton, QDialog, QFileDialog, QWidget, QGridLayout, QLineEdit, QComboBox
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, QSize

from widgets.managment_window.products_window.customs_widgets import *
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from func_get_path_icon import get_path_icon
from functions.db_Helper import Db_helper
# from widgets.managment_window.products_window.order_list_products import Order_list_products

class Product_edit(QPushButton):
    def __init__(self, text, menu_id, listWidget, window,  central_window):
        super().__init__(text=text)
        self.listWidget = listWidget
        self.helper = Db_helper("Alpha.db")
        self.feather = None
        self.id_menu = menu_id
        self.window_= window 
        self.central_window = central_window
        self.clicked.connect(self.add_product_window)
        self.info_db = self.helper.get_list(f"""SELECT Category.name, Menu.image, Category.id  
                                            FROM Category, Menu
                                            WHERE Category.id = Menu.category
                                            AND
                                            Menu.id = '{self.id_menu}';""")[0]
        self.file_put = self.info_db[1]
        self.file_put_b = self.info_db[1]
        self.category_name = self.info_db[0]
        self.category_id = self.info_db[2]

    def add_product_window(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9]{0,15}")))
        self.enter_price = QLineEdit()
        self.enter_price.setPlaceholderText("Price")
        self.enter_price.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,7}")))
        self.choose_category = QComboBox()
        self.append_category()
        self.choose_category.activated.connect(self.change_category)
        self.ingridients = self.listWidget(active_window = self.form)
        self.ingridients.setColumnCount(3) 
        self.ingridients.setLineCount("Stock")
        self.ingridients.add_columns(((0, "Name"), (1, "Count "), (2, " ")))
        self.ingridients.settingSizeColumn((100, 100, 50))
        self.ingridients.settingSizeRow(35)
        

        self.append_button = QPushButton("Change")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.form.close)
        self.form.setLayout(self.form_Layout)
        self.butt = QPushButton("Choose photo")
        self.butt.setIcon(get_path_icon(self.helper.get_list(f"""SELECT image FROM Menu WHERE id = {self.id_menu}""")[0][0]))
        self.butt.setIconSize(QSize(50, 50))

        self.butt.clicked.connect(self.choose_photo_func)
        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_price, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.choose_category, 2, 0, 1, 2)
        self.form_Layout.addWidget(self.butt, 3, 0, 1, 2 )
        self.form_Layout.addWidget(self.ingridients, 6, 0 ,2, 2)
        self.form_Layout.addWidget(self.append_button , 8, 0)
        self.form_Layout.addWidget(self.cancel_button, 8, 1)
        self.drow_ingridients_transaction()
        self.edit_product()
        self.form.show()
    
    def change_category(self, e):
        self.category_id = e + 1
        

    def choose_photo_func(self):
            wind = QDialog()
            self.file = QFileDialog.getOpenFileName(wind, "Open file", "C:\\", "Image (*.png)")[0]
            self.file_put = self.file.split("/")[-1]
            if self.file_put == "":
                self.file_put = self.file_put_b
            self.feather = str(os.path.dirname( __file__ )).replace("widgets\managment_window\products_window" ,f"feather\{self.file_put}")
            if self.file!="":
                shutil.copyfile(self.file, self.feather)
            self.butt.setIcon(get_path_icon(self.file_put))

    def append_func(self):
        if self.feather!=None:
            shutil.copyfile(self.file, self.feather)
        text = self.enter_name.text()
        price = self.enter_price.text()
        if text != "":
            if price == "":
                price = 0
            self.helper.insert(f"""UPDATE Menu SET name = '{text}' WHERE Menu.id = {self.id_menu} ;""")
            self.helper.insert(f"""UPDATE Menu SET category = {self.category_id} WHERE Menu.id = {self.id_menu} ;""")
            self.helper.insert(f"""UPDATE Menu SET price = {price} WHERE Menu.id = {self.id_menu} ;""")
            self.helper.insert(f"""UPDATE Menu SET image = '{self.file_put}' WHERE Menu.id = {self.id_menu} ;""")
            self.window_.drow_products()
            self.central_window.Main_widget.menuTabWidget.clear()
            self.central_window.Main_widget.menuTabWidget.create_full_menu()
            self.form.close()

    def append_category(self):
        categories = self.helper.get_list("SELECT name FROM Category;")
        categories_idx = {}
        counter = 0
        for i in categories:
            categories_idx[i[0]] = counter
            self.choose_category.addItem(i[0])
            counter += 1
        self.choose_category.setCurrentIndex(categories_idx[self.category_name])


    def edit_product(self):
        info = self.helper.get_list(f"""SELECT name, category, price, image FROM Menu WHERE id = {self.id_menu} """)[0]
        price = str(info[2])
        if price == "0":
            price = ""
        self.enter_name.setText(info[0])
        self.choose_category.setCurrentText(str(info[1]))
        self.enter_price.setText(price)

    def drow_ingridients_transaction(self):
        self.ingridients.clearContents()
        self.setLineCount()
        info = self.helper.get_list(f"""SELECT Stock.name, TechnologyCard.count, TechnologyCard.id
                                        FROM TechnologyCard, Stock
                                        WHERE TechnologyCard.id_product = Stock.id
                                        AND
                                        TechnologyCard.id_menu = {self.id_menu};""")
        self.box = CustomComboBoxEdit(id_menu=self.id_menu)
        self.line = QLineEdit()
        self.line.setPlaceholderText("ml/g")
        self.line.setValidator(QRegularExpressionValidator(QRegularExpression("[1-9][0-9]{0,7}")))
        self.row_line = 0
        for row in range(0, len(info)):
            self.row_line = row + 1
            self.ingridients.setItem(row, 0, CustomQTableWidgetItem(str(info[row][0])))
            self.ingridients.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.ingridients.setCellWidget(row, 2, CustomButtonDellEdit(TechnologyCard_id = info[row][2], text="del", window = self))
        self.ingridients.setCellWidget(self.row_line, 0, self.box)
        self.ingridients.setCellWidget(self.row_line, 1, self.line)
        self.ingridients.setCellWidget(self.row_line, 2, CustomButtonAddEdit(name = self.box, count=self.line, text="add", window = self, id_menu = self.id_menu))

    def setLineCount(self):
        count = int(self.helper.get_list(f"""SELECT count(id) FROM TechnologyCard WHERE id_menu = '{self.id_menu}';""")[0][0])
        stockIngridientsCount = int(self.helper.get_list("""SELECT COUNT(id) FROM Stock;""")[0][0])
        if stockIngridientsCount > count:
            count += 1
        self.ingridients.setRowCount(count)

class CustomButtonDellEdit(QPushButton):
    def __init__(self,text, window, TechnologyCard_id):
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.window_ = window
        self.TechnologyCard_id = TechnologyCard_id
        self.clicked.connect(self.func)


    def func(self):
        self.helper.insert(f"""DELETE FROM TechnologyCard WHERE id = {self.TechnologyCard_id} """)
        self.window_.drow_ingridients_transaction()


class CustomButtonAddEdit(QPushButton):
    def __init__(self,text, window, count, id_menu, name):
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.count = count
        self.id_menu = id_menu
        self.name = name
        self.window_ = window
        self.clicked.connect(self.func)

    def func(self):
        id_product = int(self.helper.get_list(f"""SELECT id FROM Stock WHERE name = '{self.name.custText}' """)[0][0])
        count = int(self.count.text())

        self.helper.insert(f"""INSERT INTO TechnologyCard (id_menu, id_product, count)
                            VALUES({self.id_menu}, {id_product}, {count}) """)
        print(self.id_menu, id_product, count)
        
        self.window_.drow_ingridients_transaction()

class CustomComboBoxEdit(QComboBox):
    def __init__(self, id_menu):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.id_menu = id_menu
        self.currentTextChanged.connect(self.func)
        self.ingridients = self.helper.get_list("""SELECT name FROM Stock;""")
        self.ingridients_transaction = self.helper.get_list(f"""SELECT Stock.name FROM 
                                                    TechnologyCard, Stock
                                                    WHERE TechnologyCard.id_product = Stock.id
                                                    AND
                                                    TechnologyCard.id_menu = {self.id_menu};""")
        
        self.all_ingridients = []
        self.already_ingridients = []

        for i in self.ingridients:
            self.all_ingridients.append(i[0])

        for i in self.ingridients_transaction:
            self.already_ingridients.append(i[0])

        for i in self.all_ingridients:
            if i not in self.already_ingridients:
                self.addItem(i)
        self.custText = self.itemText(0)
        

    def func(self, e):
        self.custText = e

    