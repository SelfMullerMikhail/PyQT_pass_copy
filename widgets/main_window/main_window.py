from PyQt6.QtWidgets import  QGridLayout, QLabel, QPushButton, QMainWindow
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from widgets.main_window.tableListWidget import TablesListWidget
from widgets.main_window.menuTabWidget import MenuTabWidget
from widgets.main_window.payButton import PayButton
from widgets.main_window.clearButton import ClearButton
from widgets.main_window.delTableButton import DelTableButton
from widgets.main_window.addTableButton import AddTableButton
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.control_button import Сontrol_button
from functions.db_Helper import Db_helper
from functions.active_tub import ActiveTable
from func_get_path_icon import get_path_icon


from cssStyleSheet.clearButtonStyle import clearButtonStyle
from cssStyleSheet.payButtonStyle import payButtonStyle
from cssStyleSheet.menuTabWidgetStyle import MenuTabWidgetStyle
from widgets.ordersListWidget import OrdersListWidget

class Main_widget(QGridLayout):
    """QGridLayout of first page of window """
    def __init__(self, activeTab: ActiveTable, centralWidget: QMainWindow) -> None:
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.centralWidget = centralWidget
        self.activeTab = activeTab
        self.ordersListWidget = OrdersListWidget(active_window = activeTab)
        self.ordersListWidget.setColumnCount(7)
        self.ordersListWidget.add_columns(((0, "name"), (1, "price"), (2, "count"), (3, "total"), (4, ""), (5, ""), (6, "")))
        self.ordersListWidget.settingSizeColumn(( 110, 110, 70, 100, 55, 55, 55))
        self.ordersListWidget.setRowCount(15)
        self.tablesListWidget = TablesListWidget(self, activeTab = activeTab)
        self.menuTabWidget = MenuTabWidget(activeTab = activeTab, ordersListWidget = self)
        self.payButton = PayButton(text="Payment", centralWidget = self.centralWidget, activeTab = activeTab, tablesListWidget = self.tablesListWidget)
        self.clearButton = ClearButton(activeTab = activeTab, selfWidget = self.centralWidget) 
        self.delTableButton = DelTableButton(self.tablesListWidget)
        self.addTableButton = AddTableButton(self.tablesListWidget)
        self.summ_lable = QLabel()
        self.summ_lable.setFont(QFont("Arial", 15))
        self.change_authorization = QPushButton("Out")
        self.change_authorization.setIcon(get_path_icon("log-out.svg"))
        self.change_authorization.setFont(QFont("Arial", 15))
        self.change_authorization.clicked.connect(self.change_authorization_func)

        self.clearButton.setStyleSheet(clearButtonStyle)
        self.payButton.setStyleSheet(payButtonStyle)
        self.menuTabWidget.setStyleSheet(MenuTabWidgetStyle)
        
        self.addWidget(self.tablesListWidget, 1, 0, 17, 2)
        self.addWidget(self.ordersListWidget, 1, 2, 16, 8)
        self.addWidget(self.menuTabWidget, 1, 10, 20, 10)                        
        self.addWidget(self.payButton, 18, 2, 1, 3)
        self.addWidget(self.clearButton, 18, 7, 1, 3)
        self.addWidget(self.delTableButton, 18, 0, 1, 3)
        self.addWidget(self.addTableButton, 19, 0, 1, 3)
        self.addWidget(self.change_authorization, 20, 0, 1, 3)
        self.addWidget(self.summ_lable, 17, 9, 1, 1)
        self.drow_orders()

    def change_authorization_func(self) -> None:
        """Doing set of first page in this window """
        self.centralWidget.setCentralWindow_authorization()

    def set_summ_label(self) -> None:
        """Doing count of summ for all products in choosed table  """
        summ_lable = 0
        summ = self.helper.get_list(f"""SELECT sum(Menu.price * OpenOrder.count)
                                    FROM  OpenOrder, Menu
                                    WHERE OpenOrder.id_menu = Menu.id 
                                    AND
                                    OpenOrder.id_table = {self.activeTab.activeTab}
                                    GROUP BY Menu.id;""")
        for i in summ:
            summ_lable += int(i[0])
        
        self.summ_lable.setText(f"sum: {summ_lable}")

    def drow_orders(self) -> None:
        self.id_client = self.activeTab.activeUser[0]

        """Drow all window of choosed table with buttons """
        self.ordersListWidget.clearContents()
        info = self.helper.get_list((f"""SELECT Menu.name as menu_name, 
                                        Menu.price as menu_prise, 
                                        count(count) as count, 
                                        (Menu.price * count(count)) as summ_position
                                        , Menu.id as id_menu,
                                        OpenOrder.id_table as id_table,
                                        OpenOrder.id_client
                                        FROM  OpenOrder, Menu
                                        WHERE OpenOrder.id_menu = Menu.id 
                                        AND OpenOrder.id_client = {self.id_client}
                                        AND OpenOrder.id_table = {self.activeTab.activeTab}
                                        GROUP BY id_menu;"""))
        self.set_summ_label()
        for row in range(len(info)):
            for i in range(4):
                self.ordersListWidget.setItem(row, i, CustomQTableWidgetItem(str(info[row][i])))
            self.ordersListWidget.setCellWidget(row, 4, Сontrol_button(name = "+", orderList = self, activeTab = self.activeTab, menu_id = info[row][4]))
            self.ordersListWidget.setCellWidget(row, 5, Сontrol_button(name = "-", orderList = self, activeTab = self.activeTab, menu_id = info[row][4]))
            self.ordersListWidget.setCellWidget(row, 6, Сontrol_button(name = "dell", orderList = self, activeTab = self.activeTab, menu_id = info[row][4]))
