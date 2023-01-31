import sys

from widgets.main_window.main_window import Main_widget
from widgets.archive_window.archive_window import Archive_widget
from widgets.managment_window.managment_window import Managment_widget
from widgets.setting_window.setting_window import Setting_widget

from PyQt6.QtWidgets import QMainWindow, QApplication

from upMenuComboBox import UpMenu_comboBox
from functions.db_Helper import Db_helper


class ActiveTable():
    def get_active(self):
        return self.activeTab

    def __init__(self, *args):
        self.helper = args[0]
        self.activeTab = self.helper.get_list("SELECT MIN(id) FROM Tables")[0][0]

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 800)
        self.helper = Db_helper("Alpha.db")
        self.activeTab = ActiveTable(self.helper)
        self.upMenu = UpMenu_comboBox()
        self.upMenu.create_tab("Main", "home.svg", Main_widget(self.helper, self.activeTab))
        self.upMenu.create_tab("Managment", "user.svg", Managment_widget(self.helper))
        self.upMenu.create_tab("Settings", "settings.svg", Archive_widget())
        self.upMenu.create_tab("Arhcive", "archive.svg", Setting_widget())
        self.setCentralWidget(self.upMenu.activate("Managment"))
    
    def test(self):
        ...
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet = ...
    window.show()
    sys.exit(app.exec())