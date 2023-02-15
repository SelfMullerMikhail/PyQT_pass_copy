import sys

from PyQt6.QtWidgets import QMainWindow, QApplication,QWidget

from widgets.main_window.main_window import Main_widget
from widgets.archive_window.archive_window import Archive_widget
from widgets.managment_window.managment_window import Managment_widget
from widgets.day_off.dayOf_widget import DayOf_widget
from functions.active_tub import ActiveTable
from upMenuComboBox import UpMenu_comboBox
from widgets.authorization_window.authorization_window import Authorization_window

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 800)
        self.activeTab = ActiveTable()
        
        self.upMenu = UpMenu_comboBox()
        self.Main_widget = Main_widget(activeTab = self.activeTab, centralWidget = self)
        self.managment_window = Managment_widget(active_window = self.activeTab, central_window = self)
        self.archive_widget = Archive_widget(main_widget = self)
        self.dayOf_widget = DayOf_widget(mainWidget=self)
        self.authorization_window = Authorization_window(selfWidget = self)

        self.upMenu.create_tab("Main", "home.svg", self.Main_widget)
        self.upMenu.create_tab("Managment", "user.svg", self.managment_window)
        self.upMenu.create_tab("Arhcive", "archive.svg", self.archive_widget)
        self.upMenu.create_tab("Day OFF", "power.svg", self.dayOf_widget)
        self.inf = self.upMenu.activate("Main")
        
        
        self.login_window = Login_window()

        self.setCentralWindow_authorization()
        # self.setCentralWindow()
    
    def drowAllwOrders(self):
        self.Main_widget.ordersListWidget.clearContents()
        self.Main_widget.tablesListWidget.clear()
        self.Main_widget.drow_orders()
        self.Main_widget.set_summ_label()

        self.managment_window.stock_window.drow_stock()
        self.archive_widget.drow_archive_all()
        self.Main_widget.tablesListWidget.getTabs()

    def setCentralWindow(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.inf)
        
    def setCentralWindow_authorization(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.authorization_window)
        self.authorization_window.numbers.clear()





                
class Login_window(QWidget):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet = ...
    window.show()
    sys.exit(app.exec())