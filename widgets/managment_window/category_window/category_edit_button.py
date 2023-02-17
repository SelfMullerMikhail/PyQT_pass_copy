import os, shutil
from PyQt6.QtWidgets import QGridLayout, QWidget, QLineEdit, QPushButton, QDialog, QFileDialog
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QRegularExpression, QSize

from functions.db_Helper import Db_helper
from func_get_path_icon import get_path_icon

class CategoryEditButton(QPushButton):
    def __init__(self, id_category, selfWidget, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.central_window = central_window
        self.id_category = id_category
        self.category_widget = selfWidget
        self.setText("edit")
        self.clicked.connect(self.func)

    def func(self):
        self.form = QWidget()
        self.form.setGeometry(200, 200, 500, 500)
        self.form_Layout = QGridLayout()
        self.enter_name = QLineEdit()
        self.enter_name.setPlaceholderText('Name')
        self.enter_name.setValidator(QRegularExpressionValidator(QRegularExpression("[\w\s]{1,15}")))
        
        self.enter_picture = QPushButton("Change picture")
        self.enter_picture.clicked.connect(self.choose_photo) 
        self.enter_picture.setIconSize(QSize(40, 40))

        self.append_button = QPushButton("Change")
        self.append_button.clicked.connect(self.append_func)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close_func)
        self.form.setLayout(self.form_Layout)
        self.form_Layout.addWidget(self.enter_name, 0, 0, 1, 2)
        self.form_Layout.addWidget(self.enter_picture, 1, 0, 1, 2)
        self.form_Layout.addWidget(self.append_button , 3, 0)
        self.form_Layout.addWidget(self.cancel_button, 3, 1)
        self.insert_info()
        self.form.show()

    def insert_info(self):
        info = self.helper.get_list(f"""SELECT * FROM Category WHERE id = {self.id_category};""")[0]
        self.enter_name.setText(info[1])
        self.file_put = info[2]
        self.enter_picture.setIcon(get_path_icon(info[2]))

    def close_func(self):
        self.file_put = self.helper.get_list(f"""SELECT * FROM Category WHERE id = {self.id_category};""")[0][2]
        self.form.close()

    def choose_photo(self):
        wind = QDialog()
        self.file = QFileDialog.getOpenFileName(wind, "Open file", "C:\\", "Image (*.png)")[0]
        self.file_put = self.file.split("/")[-1]
        if self.file_put == "":
            self.file_put = 'book.svg'
        self.feather = str(os.path.dirname( __file__ )).replace("widgets\managment_window\category_window" ,f"feather\{self.file_put}")
        if self.file!="":
            shutil.copyfile(self.file, self.feather)
        self.enter_picture.setIcon(get_path_icon(self.file_put))
        

    def append_func(self):
        text = self.enter_name.text()
        if text != "":
            self.helper.insert(f"""UPDATE Category SET name = '{text}' WHERE id = {self.id_category};""")
            self.helper.insert(f"""UPDATE Category SET image ='{self.file_put}' WHERE id = {self.id_category};""")
            self.category_widget.drow_func()
            self.central_window.drowAllwOrders()
            self.form.close()
        