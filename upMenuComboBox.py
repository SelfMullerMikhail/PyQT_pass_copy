from PyQt6.QtWidgets import QComboBox, QVBoxLayout, QLayout
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QGridLayout

from func_get_path_icon import get_path_icon
from widgets.day_off.dayOf_widget import DayOf_widget

class UpMenu_comboBox(QComboBox):

    def __init__(self) -> None:
        super().__init__()
        """Important class for creating new windows """
        self.setFixedHeight(40)
        self.setIconSize(QSize(30,30))
        self.textActivated.connect(self.__change_active_window)
        self.all_windows_dickt: dict = {}
        self.upMenuGrid, self.QVbox, self.main_widget = self.__create_main_widget()

    def __addItemTab(self, name: str, icon: str) -> None:
        self.addItem(name)
        self.setItemIcon(self.count()-1, get_path_icon(icon))

    def __create_main_widget(self) -> tuple:
        upMenuGrid, QVbox, main_widget = QGridLayout(), QVBoxLayout(), QWidget()
        upMenuGrid.addWidget(self)
        QVbox.addLayout(upMenuGrid)
        main_widget.setLayout(QVbox)
        return upMenuGrid, QVbox, main_widget

    def __create_Widget_Grid(self, obj: QLayout) -> QGridLayout:
        QWidget_local, QGridLayout_local = QWidget(), QGridLayout()
        QWidget_local.setLayout(obj)
        QGridLayout_local.addWidget(QWidget_local)
        self.QVbox.addLayout(QGridLayout_local)
        QWidget_local.hide()
        return QWidget_local

    def __change_active_window(self, name: str) -> None:
        self.active_window.hide()
        self.active_window = self.all_windows_dickt[name]
        self.all_windows_dickt[name].show()
        obj = self.active_window.layout()
        if obj.__class__ == DayOf_widget:
            obj.upgrading()
        
        

    def create_tab(self, name: str, icon: str, obj: QGridLayout) -> None:
        """Whis function create QWidget for addWidget in Layout"""
        self.__addItemTab(name, icon)
        self.all_windows_dickt[name] = self.__create_Widget_Grid(obj)

    def activate(self, name: str) -> QWidget:
        """Return activity Widget """
        self.all_windows_dickt[name]
        self.active_window = self.all_windows_dickt[name]
        self.active_window.show()
        return self.main_widget




    
