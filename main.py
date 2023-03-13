import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont
from widgets.main_window.main_window import Main_widget
from widgets.archive_window.archive_window import Archive_widget
from widgets.managment_window.managment_window import Managment_widget
from widgets.day_off.dayOf_widget import DayOf_widget
from functions.active_tub import ActiveTable
from upMenuComboBox import UpMenu_comboBox
from resize_module import ResizeModule
from widgets.authorization_window.authorization_window \
import Authorization_window
from functions.resize_func import resizeFunc


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        """ The main file gfor starting and use contorl"""
        self.setGeometry(50, 50, 1200, 800)
        self.activeTab = ActiveTable()
        self.upMenu: UpMenu_comboBox = UpMenu_comboBox()
        self.Main_widget: Main_widget = Main_widget(activeTab=self.activeTab, centralWidget=self)
        self.managment_window: Managment_widget = Managment_widget(active_window=self.activeTab, central_window=self)
        self.archive_widget: Archive_widget = Archive_widget(main_widget=self)
        self.dayOf_widget: DayOf_widget = DayOf_widget(mainWidget=self)
        self.authorization_window: Authorization_window = Authorization_window(selfWidget=self)
        self.upMenu.create_tab("Main", "home.svg", self.Main_widget)
        self.upMenu.create_tab("Managment", "user.svg", self.managment_window)
        self.upMenu.create_tab("Arhcive", "archive.svg", self.archive_widget)
        self.upMenu.create_tab("Day OFF", "power.svg", self.dayOf_widget)
        self.inf = self.upMenu.activate("Main")
        self.login_window: Login_window = Login_window()
        self.resizing_module = ResizeModule(self.upMenu, self.Main_widget, self.managment_window, self.archive_widget, self.dayOf_widget, self.authorization_window, self.login_window)
        self.setCentralWindow_authorization()
        # self.setCentralWindow()
        self.btnIconSize = {"width" : 35, "height": 35}
        self.btnFixSize = {"width" : 50, "height": 50}
        self.btnFixedWidth = 130
        self.constSize = self.size()
    
    def drowAllwOrders(self):
        self.Main_widget.ordersListWidget.clearContents()
        self.Main_widget.tablesListWidget.clear()
        self.Main_widget.drow_orders()
        self.Main_widget.set_summ_label()
        self.Main_widget.menuTabWidget.create_full_menu()

        self.managment_window.stock_window.drow_stock()
        self.archive_widget.drow_archive_all()
        self.Main_widget.tablesListWidget.getTabs()

    def setCentralWindow(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.inf)
        
    def setCentralWindow_authorization(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.authorization_window)

    def resizeEvent(self, event):
        self.iconSizeBtnW, self.iconSizeBtnH = resizeFunc(event, self.constSize, self.btnIconSize["width"], self.btnIconSize["height"])
        self.fixSizeBtnW, self.fixSizeBtnH = resizeFunc(event, self.constSize, self.btnFixSize["width"], self.btnFixSize["height"])
        self.fixWidthResize, _ = resizeFunc(event, self.constSize, sizeW=self.btnFixedWidth)
        self.btnQSize = QSize(self.iconSizeBtnW, self.iconSizeBtnH)
        self.fixSize = self.fixSizeBtnW, self.fixSizeBtnH

        self.managment_window.upMenu.setIconSize(self.btnQSize)

        self.Main_widget.ordersListWidget.setFont(QFont("Arial", resizeFunc(event, self.constSize, sizeW=10)[0]))
        self.upMenu.setFixedHeight(resizeFunc(event, self.constSize, sizeH=50)[1])
        self.upMenu.setIconSize(self.btnQSize)
        self.Main_widget.payButton.pay_widget.payment.setFixedHeight(resizeFunc(event, self.constSize, sizeH=180)[1])
        self.Main_widget.payButton.pay_widget.cancel.setFixedHeight(resizeFunc(event, self.constSize, sizeH=180)[1])
        self.Main_widget.payButton.pay_widget.comment.setFixedHeight(resizeFunc(event, self.constSize, sizeH=180)[1])
        self.Main_widget.payButton.pay_widget.summ.setMaximumSize(*resizeFunc(event, self.constSize, sizeH= 50,sizeW=50))
        self.Main_widget.payButton.pay_widget.summ_numb.setMaximumSize(*resizeFunc(event, self.constSize, sizeH= 50,sizeW=50))
        self.Main_widget.payButton.pay_widget.cardQLineEdit.setFixedHeight(resizeFunc(event, self.constSize, sizeH=50)[1])
        self.Main_widget.payButton.pay_widget.cashQLineEdit.setFixedHeight(resizeFunc(event, self.constSize, sizeH=50)[1])
        self.Main_widget.payButton.pay_widget.ordersListWidget.setFont(QFont("Arial", resizeFunc(event, self.constSize, sizeW=13)[0]))
        self.Main_widget.clearButton.setFixedSize(*self.fixSize)
        self.Main_widget.clearButton.setIconSize(self.btnQSize)
        self.Main_widget.clearButton.setFixedWidth(self.fixWidthResize)

        self.Main_widget.delTableButton.setFixedSize(*self.fixSize)
        self.Main_widget.delTableButton.setIconSize(self.btnQSize)
        self.Main_widget.delTableButton.setFixedWidth(self.fixWidthResize)

        self.Main_widget.addTableButton.setFixedSize(*self.fixSize)
        self.Main_widget.addTableButton.setIconSize(self.btnQSize)
        self.Main_widget.addTableButton.setFixedWidth(self.fixWidthResize)

        self.Main_widget.payButton.setFixedSize(*self.fixSize)
        self.Main_widget.payButton.setIconSize(self.btnQSize)
        self.Main_widget.payButton.setFixedWidth(self.fixWidthResize)

        self.Main_widget.change_authorization.setFixedSize(*self.fixSize)
        self.Main_widget.change_authorization.setIconSize(self.btnQSize)
        self.Main_widget.change_authorization.setFixedWidth(self.fixWidthResize)

        self.Main_widget.tablesListWidget.setFixedWidth(self.fixWidthResize)
        self.Main_widget.tablesListWidget.setIconSize(self.btnQSize)

        return super().resizeEvent(event)

                
class Login_window(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.setStyleSheet = ...
    window.show()
    sys.exit(app.exec())