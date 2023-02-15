from PyQt6.QtWidgets import QComboBox, QVBoxLayout
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QGridLayout

from func_get_path_icon import get_path_icon
from widgets.day_off.dayOf_widget import DayOf_widget

class UpMenu_comboBox(QComboBox):

    def __init__(self):
        super().__init__()
        self.setFixedHeight(40)
        self.setIconSize(QSize(30,30))
        self.textActivated.connect(self.change_active_window)
        self.all_windows_dickt = {}
        self.upMenuGrid, self.QVbox, self.main_widget = self.create_main_widget()


    def addItemTab(self, name, icon):
        self.addItem(name)
        self.setItemIcon(self.count()-1, get_path_icon(icon))

    def create_main_widget(self):
        upMenuGrid, QVbox, main_widget = QGridLayout(), QVBoxLayout(), QWidget()
        upMenuGrid.addWidget(self)
        QVbox.addLayout(upMenuGrid)
        main_widget.setLayout(QVbox)
        return upMenuGrid, QVbox, main_widget

    def create_Widget_Grid(self, obj,  *args):
        QWidget_local, QGridLayout_local = QWidget(), QGridLayout()
        QWidget_local.setLayout(obj)
        QGridLayout_local.addWidget(QWidget_local)
        self.QVbox.addLayout(QGridLayout_local)
        QWidget_local.hide()
        return QWidget_local

    def change_active_window(self, name):
        self.active_window.hide()
        self.active_window = self.all_windows_dickt[name]
        self.all_windows_dickt[name].show()
        obj = self.active_window.layout()
        if obj.__class__ == DayOf_widget:
            obj.upgrading()
        
        

    def create_tab(self, name, icon, obj):
        self.addItemTab(name, icon)
        self.all_windows_dickt[name] = self.create_Widget_Grid(obj)

    def activate(self, name):
        self.all_windows_dickt[name]
        self.active_window = self.all_windows_dickt[name]
        self.active_window.show()
        return self.main_widget




    
