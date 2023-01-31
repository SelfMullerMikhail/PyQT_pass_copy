import os

from PyQt6.QtWidgets import QListWidget, QListWidgetItem, QGridLayout, QWidget, QListWidgetItem
from PyQt6.QtCore import QSize, Qt



class Products_list(QListWidget):
    def __init__(self) -> None:
        super().__init__()
        
        self.a = QListWidgetItem()
        self.b = QListWidget()
        self.a.setText("Test")
        self.addItem(self.a)
        # self.addItem(self.b)