import sys, os

from PyQt6.QtWidgets import QTableWidget, QListWidget, QTabWidget, QFrame
from PyQt6.QtWidgets import  QVBoxLayout, QGridLayout, QTableWidget, QHBoxLayout
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QAbstractItemView, QHeaderView, QAbstractItemDelegate, QSpinBox, QWidget, QVBoxLayout

sys.path.append( os.path.dirname( __file__ ).replace("widgets\main_window", ""))

from upMenuComboBox import UpMenu_comboBox
from products_window import Products_window



class Managment_widget(QVBoxLayout):
    def __init__(self, *args):
        super().__init__()
        self.helper = args[0]
        self.upMenu = UpMenu_comboBox(self)
        self.addWidget(self.upMenu)
        self.upMenu.create_tab("Products", "database.svg", Products_window()) # Кастом виндов
        self.upMenu.create_tab("Test", "coffee.svg", QGridLayout()) # Кастом виндов
        self.addWidget(self.upMenu.activate("Products"))

        

