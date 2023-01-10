import os

from PyQt6.QtWidgets import QComboBox, QGridLayout, QWidget, QPushButton, QVBoxLayout, QLineEdit
from PyQt6.QtCore import QSize, Qt

from products_list import Products_list



class Products_window(QGridLayout):
    def __init__(self) -> None:
        super().__init__()
        # self.setVerticalSpacing(20)
        # self.setHorizontalSpacing(20)
        self.append_button = QPushButton(text="append") # Кастомить
        self.products_list = Products_list() # Кастомить
        self.text = QLineEdit() # Кастомить
        self.sorting = QComboBox() #Кастомить
        self.sorting.addItem("Name")
        self.sorting.addItem("Price")
        self.text.setPlaceholderText("Quick search")
        self.text.textChanged.connect(self.printer)
        self.addWidget(self.append_button, 0, 18, 1, 2)
        self.addWidget(self.products_list, 1, 0, 19, 20)
        self.addWidget(self.text, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)

    def printer(self, e):
        print(e)