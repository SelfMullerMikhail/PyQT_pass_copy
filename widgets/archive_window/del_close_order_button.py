from PyQt6.QtWidgets import QPushButton, QMessageBox

from functions.db_Helper import Db_helper


class DelCloseOrderButton(QPushButton):
    def __init__(self, text, id_closeOrder, archive_widget):
        super().__init__(text=text)
        self.helper = Db_helper("Alpha.db")
        self.archive_widget = archive_widget
        self.id_closeOrder = id_closeOrder
        self.clicked.connect(self.del_func)

    def del_func(self):
        msgBox = QMessageBox()
        msgBox.setText(f"""Do you want delete this order? \nid_table:'{self.id_closeOrder}""")
        yes = QMessageBox.StandardButton.Ok
        msgBox.setStandardButtons(yes | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setWindowTitle("Delete order")
        result = msgBox.exec()
        if result == yes:
            self.helper.insert(f"""DELETE FROM ClosedOrder WHERE id = {self.id_closeOrder} """)
            self.archive_widget.drow_archive_all()