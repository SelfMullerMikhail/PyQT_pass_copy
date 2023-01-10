import sys, os

from PyQt6.QtWidgets import QTableWidget, QListWidget, QTabWidget
from PyQt6.QtWidgets import  QVBoxLayout, QGridLayout, QTableWidget
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtWidgets import QAbstractItemView, QHeaderView, QAbstractItemDelegate, QSpinBox, QWidget, QVBoxLayout
from functions.db_Helper import Db_helper

# sys.path.append(os.path.dirname( __file__ ).replace("widgets/main_window", ""))

class Setting_widget(QGridLayout):
    def __init__(self, *args):
        super().__init__()
        self.addWidget(QTableWidget(), 0, 0, 3, 1)
        self.addWidget(QListWidget(), 0, 2, 13, 8)