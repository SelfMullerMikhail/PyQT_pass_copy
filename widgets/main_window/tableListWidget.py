import os

from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtCore import QSize, Qt
from func_get_path_icon import get_path_icon

from functions.db_Helper import Db_helper

class TablesListWidget(QListWidget):
    def __init__(self, *args, activeTab):
        super().__init__() 
        self.helper = Db_helper("Alpha.db")
        self.activeTab = activeTab
        self.ordersListWidget = args[0]
        self.getTabs()
        self.setFixedWidth(130)
        self.setIconSize(QSize(30, 30))
        self.itemClicked.connect(self.one_click)
        self.itemChanged.connect(self.change_name)
        self.table_name = ''

    def getTablesCount(self):
        return self.helper.get_list(f"SELECT COUNT(id) FROM Tables WHERE id_client = {self.activeTab.activeUser[0]}")[0][0]

    def getTabs(self):
        self.clear()
        count = int(self.helper.get_list(f"SELECT COUNT(id) from Tables WHERE id_client = {self.activeTab.activeUser[0]}")[0][0])
        if count == 0:
            self.create_table()
        self.inf = self.helper.get_list(f"SELECT id, id_client, tables_name FROM Tables WHERE id_client = {self.activeTab.activeUser[0]}")
        for i in self.inf:
            self.create_table(i[2], i[0])

    def getMaxTabId(self):
        return self.helper.get_list(f"SELECT MAX(id) FROM Tables WHERE id_client = {self.activeTab.activeUser[0]}")[0][0]

    def getMaxTabIdAll(self):
        return self.helper.get_list(f"SELECT MAX(id) FROM Tables")[0][0]

    def create_table(self, tab_name = "tab", id_tab = None):
        if id_tab == None:
            id_tab = int(self.getMaxTabIdAll())+1
        self.customItem = QListWidgetItem(self.customListWidgetItem(tab_name, id_tab))
        self.customItem.indx = id_tab
        self.customItem.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
        self.addItem(self.customItem)

    def customListWidgetItem(self, tab_name, id_tab):
        if(tab_name == "tab"):
            self.activeTabName = f"{tab_name}_{id_tab}"
        else:
            self.activeTabName = tab_name
        return QListWidgetItem(get_path_icon("tablet.svg"),  f"{self.activeTabName}")
        
    def del_table(self, pay = False):
        if ((pay == True) and (self.getTablesCount() == 1)):
                self.add_table()
        if 1 < self.getTablesCount():
            self.helper.insert(f"DELETE FROM Tables WHERE id = {self.activeTab.activeTab}")
            self.helper.insert(f"DELETE FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}")
            self.ordersListWidget.drow_orders()
            self.getTabs()
            self.activeTab.activeTab = self.helper.get_list("SELECT MIN(id) FROM Tables")[0][0]

    def add_table(self):
        self.helper.insert(f"""INSERT INTO Tables (id_client, tables_name)
                            VALUES ({self.activeTab.activeUser[0]}, 'tab')""")
        self.getTabs()

    def one_click(self, e):
        self.table_name = e.text()
        self.activeTab.activeTab = e.indx
        self.ordersListWidget.drow_orders()
        self.ordersListWidget.set_summ_label()

    def change_name(self, e):
        if len(e.text()) > 1 and len(e.text()) != 0:
            self.helper.insert(f"UPDATE Tables SET tables_name = '{e.text()}' WHERE id = {e.indx}")
        else:
            e.setText(self.table_name)

