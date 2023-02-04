import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from widgets.main_window.main_window import Main_widget
from widgets.archive_window.archive_window import Archive_widget
from widgets.managment_window.managment_window import Managment_widget
from widgets.setting_window.setting_window import Setting_widget
from functions.active_tub import ActiveTable
from upMenuComboBox import UpMenu_comboBox

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 800)
        self.activeTab = ActiveTable()
        self.upMenu = UpMenu_comboBox()
        self.Main_widget = Main_widget(activeTab = self.activeTab, centralWidget = self)
        self.managment_window = Managment_widget(active_window = self.activeTab, central_window = self)
        self.upMenu.create_tab("Main", "home.svg", self.Main_widget)
        self.upMenu.create_tab("Managment", "user.svg", self.managment_window)
        self.archive_widget = Archive_widget()
        self.upMenu.create_tab("Arhcive", "archive.svg", self.archive_widget)
        self.upMenu.create_tab("Settings", "settings.svg", Setting_widget())
        self.inf = self.upMenu.activate("Main")
        self.setCentralWindow()

    def setCentralWindow(self):
        self.setCentralWidget(self.inf)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet = ...
    window.show()
    sys.exit(app.exec())