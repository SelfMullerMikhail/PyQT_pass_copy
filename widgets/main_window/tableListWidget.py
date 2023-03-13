from PyQt6.QtWidgets import QListWidget, QListWidgetItem
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QIcon

from functions.active_tub import ActiveTable
from func_get_path_icon import get_path_icon
from functions.db_Helper import Db_helper

class TablesListWidget(QListWidget):
    def __init__(self, *args:tuple, activeTab:ActiveTable):
        super().__init__() 
        self.helper = Db_helper("Alpha.db")
        self.activeTab = activeTab
        self.ordersListWidget = args[0]
        self.getTabs()
        self.itemClicked.connect(self.one_click)
        self.itemChanged.connect(self.change_name)
        self.table_name = ''
        # self.setSizeAdjustPolicy(QListWidget.SizeAdjustPolicy.AdjustToContents)

    def getTablesCount(self) -> int:
        """Return max id from Table's DB where id clients == ActiveTable.activeUser"""
        return self.helper.get_list(f"SELECT COUNT(id) FROM Tables WHERE id_client = {self.activeTab.activeUser[0]}")[0][0]

    def getTabs(self) -> None:
        """Upgrade widget's info"""
        self.clear()
        count = int(self.helper.get_list(f"SELECT COUNT(id) from Tables WHERE id_client = {self.activeTab.activeUser[0]}")[0][0])
        if count == 0:
            self.create_table()
        self.inf = self.helper.get_list(f"SELECT id, id_client, tables_name FROM Tables WHERE id_client = {self.activeTab.activeUser[0]}")
        for i in self.inf:
            self.create_table(i[2], i[0])

    def getMaxTabId(self) -> None:
        """Select max id from tables where id_client = activeTab.activaUser"""
        return self.helper.get_list(f"SELECT MAX(id) FROM Tables WHERE id_client = {self.activeTab.activeUser[0]}")[0][0]

    def getMaxTabIdAll(self) -> None:
        """Select max id form tables"""
        return self.helper.get_list(f"SELECT MAX(id) FROM Tables")[0][0]

    def create_table(self, tab_name:str = "tab", id_tab: int = None) -> None:
        """addItem QListWidgetItem"""
        if id_tab == None:
            id_tab = int(self.getMaxTabIdAll())+1
        self.customItem = QListWidgetItem(self.customListWidgetItem(tab_name, id_tab))
        self.customItem.indx = id_tab
        self.customItem.setFont(QFont("Ariel", 15))
        self.customItem.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)
        self.addItem(self.customItem)

    def customListWidgetItem(self, tab_name:str, id_tab:int) -> QListWidgetItem:
        """Return custom QListWidgetItem(picture(name_picture:str), activeTabNmae:str), """
        if(tab_name == "tab"):
            self.activeTabName = f"{tab_name}_{id_tab}"
        else:
            self.activeTabName = tab_name
        return QListWidgetItem(get_path_icon("tablet.svg"),  f"{self.activeTabName}")
        
    def del_table(self, pay = False) -> None:
        """Delete table if count(table) >= 2"""
        if ((pay == True) and (self.getTablesCount() == 1)):
                self.add_table()
        if 1 < self.getTablesCount():
            self.helper.insert(f"DELETE FROM Tables WHERE id = {self.activeTab.activeTab}")
            self.helper.insert(f"DELETE FROM OpenOrder WHERE id_table = {self.activeTab.activeTab}")
            self.ordersListWidget.drow_orders()
            self.getTabs()
            self.activeTab.activeTab = self.helper.get_list("SELECT MIN(id) FROM Tables")[0][0]

    def add_table(self) -> None:
        """Insert into Tables (id_client, tables_name)
        and call getTabs function"""
        self.helper.insert(f"""INSERT INTO Tables (id_client, tables_name)
                            VALUES ({self.activeTab.activeUser[0]}, 'tab')""")
        self.getTabs()

    def one_click(self, e: QListWidgetItem) -> None:
        """Overload function. This doing:
        1. Save last name of tab.
        2. Save indx of this tab.
        3. Call function drow_orders.
        4. Call function ser_sum_label"""
        self.table_name = e.text()
        self.activeTab.activeTab = e.indx
        self.ordersListWidget.drow_orders()
        self.ordersListWidget.set_summ_label()

    def change_name(self, e: QListWidgetItem) -> None:
        """Overload function. Update Tables SET tables_name = str WHERE id = e.indx
        or e.setText(str)"""
        if len(e.text()) > 1 and len(e.text()) != 0:
            self.helper.insert(f"UPDATE Tables SET tables_name = '{e.text()}' WHERE id = {e.indx}")
        else:
            e.setText(self.table_name)

