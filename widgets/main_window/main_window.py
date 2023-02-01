from PyQt6.QtWidgets import  QGridLayout

from widgets.main_window.tableListWidget import TablesListWidget
from widgets.main_window.menuTabWidget import MenuTabWidget
from widgets.main_window.payButton import PayButton
from widgets.main_window.clearButton import ClearButton
from widgets.main_window.delTableButton import DelTableButton
from widgets.main_window.addTableButton import AddTableButton
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.control_button import Сontrol_button
from functions.db_Helper import Db_helper


from cssStyleSheet.clearButtonStyle import clearButtonStyle
from cssStyleSheet.payButtonStyle import payButtonStyle
from cssStyleSheet.menuTabWidgetStyle import MenuTabWidgetStyle
from widgets.ordersListWidget import OrdersListWidget

class Main_widget(QGridLayout):
    def __init__(self, activeTab, centralWidget):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.centralWidget = centralWidget
        self.activeTab = activeTab
        self.ordersListWidget = OrdersListWidget(active_window = activeTab)
        self.ordersListWidget.setColumnCount(7)
        self.ordersListWidget.add_columns(((0, "name"), (1, "price"), (2, "count"), (3, "total")))
        self.ordersListWidget.settingSizeColumn(( 110, 110, 70, 100, 55, 55, 55))
        self.ordersListWidget.setRowCount(15)
        self.drow_orders()

        self.tablesListWidget = TablesListWidget(self, activeTab = activeTab)
        self.menuTabWidget = MenuTabWidget(activeTab = activeTab, ordersListWidget = self)
        self.payButton = PayButton(text="Payment", centralWidget = self.centralWidget, activeTab = activeTab, tablesListWidget = self.tablesListWidget)
        self.clearButton = ClearButton(activeTab = activeTab, ordersListWidget = self.ordersListWidget) 
        self.delTableButton = DelTableButton(self.tablesListWidget)
        self.addTableButton = AddTableButton(self.tablesListWidget)

        self.clearButton.setStyleSheet(clearButtonStyle)
        self.payButton.setStyleSheet(payButtonStyle)
        self.menuTabWidget.setStyleSheet(MenuTabWidgetStyle)
        
        self.addWidget(self.tablesListWidget, 1, 0, 18, 2)
        self.addWidget(self.ordersListWidget, 1, 2, 13, 8)
        self.addWidget(self.menuTabWidget, 1, 10, 20, 10)                        
        self.addWidget(self.payButton, 15, 2, 1, 3)
        self.addWidget(self.clearButton, 15, 7, 1, 3)
        self.addWidget(self.delTableButton, 19, 0, 1, 3)
        self.addWidget(self.addTableButton, 20, 0, 1, 3)

    def drow_orders(self):
        self.ordersListWidget.clearContents()
        info = self.helper.get_list((f"""SELECT Menu.name, Menu.price, count(count), (Menu.price * count(count)), Menu.id 
                                            FROM  OpenOrder, Menu
                                            WHERE OpenOrder.id_menu = Menu.id AND id_table = {self.activeTab.activeTab}
                                            GROUP BY id_menu;"""))
        for row in range(len(info)):
            for i in range(4):
                self.ordersListWidget.setItem(row, i, CustomQTableWidgetItem(str(info[row][i])))
            self.ordersListWidget.setCellWidget(row, 4, Сontrol_button(name = "+", orderList = self, activeTab = self.activeTab, menu_id = info[row][4]))
            self.ordersListWidget.setCellWidget(row, 5, Сontrol_button(name = "-", orderList = self, activeTab = self.activeTab, menu_id = info[row][4]))
            self.ordersListWidget.setCellWidget(row, 6, Сontrol_button(name = "dell", orderList = self, activeTab = self.activeTab, menu_id = info[row][4]))