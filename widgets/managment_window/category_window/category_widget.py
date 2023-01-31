import os, shutil
from PyQt6.QtWidgets import QGridLayout, QWidget, QLineEdit, QPushButton, QDialog, QFileDialog
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, QSize

from widgets.ordersListWidget import OrdersListWidget
from widgets.managment_window.sorting_QComboBox import Sorting_QComboBox
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from functions.db_Helper import Db_helper
from widgets.managment_window.category_window.dell_category_button import Dell_category_button
from func_get_path_icon import get_path_icon

class Category_widget(QGridLayout):
    def __init__(self, active_window, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.feather = None
        self.file_put = "book.svg"
        self.central_window = central_window
        self.products_list = OrdersListWidget(active_window = active_window)
        self.products_list.setColumnCount(4) 
        self.products_list.setLineCount("Category")
        self.products_list.add_columns(((0, ""), (1, "Name"), (2, ""), (3, "")))
        self.products_list.settingSizeColumn((40, 100, 40, 40))
        self.products_list.settingSizeRow(50)
        self.get_category()
        self.quick_search = QLineEdit()
        self.quick_search.setPlaceholderText("Quick search")
        self.quick_search.textChanged.connect(self.printer)
        self.quick_search.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z0-9]{0,20}")))
        self.sorting = Sorting_QComboBox() #Кастомить
        self.sorting.addItemCycle(("name", "image"))
        self.sorting.textActivated.connect(self.sort)
        self.append_button = QPushButton(text="Append") # Кастомить
        self.append_button.clicked.connect(self.add_product_window)
        self.addWidget(self.products_list, 1, 0, 19, 20)
        self.addWidget(self.quick_search, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)
        self.addWidget(self.append_button, 0, 18, 1, 2)

    def printer(self, e):
        self.get_category(inf = e)

    def sort(self, e):
        self.get_category(category=e)

    def get_category(self, inf ="", category = "Name"):
        self.products_list.clearContents()
        info = self.helper.get_list(f"""SELECT * FROM Category WHERE name LIKE '%{inf}%' ORDER BY {category}""")
        for row in range(len(info)):
            icon = CustomQTableWidgetItem()
            icon.setIcon(get_path_icon(info[row][2]))
            self.products_list.setItem(row, 0, icon)
            self.products_list.setItem(row, 1, CustomQTableWidgetItem(str(info[row][1])))
            self.products_list.setCellWidget(row, 2, QPushButton("edit"))
            self.products_list.setCellWidget(row, 3, Dell_category_button(text = "del", name = info[row][1], wind = self))

    def add_product_window(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 800, 500)
        self.form_Layout = QGridLayout()
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[a-zA-Z]{1,15}")))
        self.enter_picture = QPushButton("Add picture")
        self.enter_picture.clicked.connect(self.choose_photo) 
        self.enter_picture.setIcon(get_path_icon(self.file_put))
        self.enter_picture.setIconSize(QSize(40, 40))
        self.append_button = QPushButton("Append")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_func)
        self.form.setLayout(self.form_Layout)
        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_picture, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 3, 0)
        self.form_Layout.addWidget(self.cancel_button, 3, 1)
        self.form.show()

    def close_func(self):
        self.form.close()
        self.file_put = 'book.svg'


    def choose_photo(self):
        wind = QDialog()
        self.file = QFileDialog.getOpenFileName(wind, "Open file", "C:\\", "Image (*.png)")[0]
        self.file_put = self.file.split("/")[-1]
        if self.file_put == "":
            self.file_put = 'book.svg'
        self.feather = str(os.path.dirname( __file__ )).replace("widgets\managment_window\category_window" ,f"feather\{self.file_put}")
        self.enter_picture.setIcon(get_path_icon(self.file_put))


    def append_func(self):
        name = self.enter_name.text()
        if name != "":
            if self.feather!=None:
                shutil.copyfile(self.file, self.feather)

            self.helper.insert(f"""INSERT INTO Category(name, image) 
                                    VALUES ('{name}', '{self.file_put}')""")
            
            self.products_list.setLineCount("Category")
            self.get_category()
            self.central_window.Main_widget.menuTabWidget.clear()
            self.central_window.Main_widget.menuTabWidget.create_full_menu()
            self.file_put = 'book.svg'
            self.form.close()

        