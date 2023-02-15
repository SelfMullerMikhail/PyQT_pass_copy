from PyQt6.QtWidgets import QPushButton
from functions.db_Helper import Db_helper

class Del_user(QPushButton):
    def __init__(self, text, id_client, selfWidget, centalWidget):
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.centalWidget = centalWidget
        self.user_widget = selfWidget
        self.id_client = id_client
        self.clicked.connect(self.func_del)

    def func_del(self):
        self.helper.insert(f"""DELETE FROM Tables WHERE id_client = {self.id_client};""")
        self.helper.insert(f"""DELETE FROM OpenOrder WHERE id_client = {self.id_client};""")
        self.helper.insert(f"""DELETE FROM Client WHERE id = {self.id_client};""")
        self.user_widget.drow_clients()
        self.centalWidget.drowAllwOrders()
