from PyQt6.QtWidgets import QPushButton
from functions.db_Helper import Db_helper

class Сontrol_button(QPushButton):
    def __init__(self, orderList, activeTab, menu_id, name = "", *args):
        super().__init__(*args)
        self.helper = Db_helper("Alpha.db")
        self.activeTab = activeTab
        self.menu_id = menu_id
        self.orderList = orderList
        self.setText(name)
        self.functions ={"+": self.add_position, 
                        "-": self.minus_position, 
                        "dell": self.dell_position,
                        "": self.default}
        self.clicked.connect(self.functions[name])

    def default(self):
        print("default")

    def add_position(self, e):
        self.helper.insert(
            f"""INSERT INTO OpenOrder(id_client, id_table, id_menu, count)
                                VALUES({1},{self.activeTab.activeTab} ,{self.menu_id}, 1)""")
        self.orderList.drow_orders()

    def dell_position(self, e):
        self.helper.insert(
                f"""DELETE FROM OpenOrder
                    WHERE id_table = {self.activeTab.activeTab} and id_menu = {self.menu_id}""")
        self.orderList.drow_orders()

    def minus_position(self, e):
        id_position = self.helper.get_list(F"""SELECT MAX(id) 
                                        FROM OpenOrder 
                                        WHERE id_table = {self.activeTab.activeTab} 
                                        AND id_menu = {self.menu_id}""")[0][0]

        self.helper.insert(f"""DELETE FROM OpenOrder
                            WHERE id = {id_position}""")
        self.orderList.drow_orders()