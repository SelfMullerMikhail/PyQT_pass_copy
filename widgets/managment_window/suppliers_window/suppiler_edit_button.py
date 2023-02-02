from PyQt6.QtWidgets import QPushButton

from widgets.managment_window.suppliers_window.append_edit_widget import Append_Edit_widget
from functions.db_Helper import Db_helper

class SuppilerEditButton(QPushButton):
    def __init__(self, selfWidget, suppiler_id):
        super().__init__()
        self.setText("edit")
        self.helper = Db_helper("Alpha.db")
        self.suppiler_window = selfWidget
        self.suppiler_id = suppiler_id
        self.clicked.connect(self.edit_func)
        self.edit_widget = Append_Edit_widget(selfWidget=self.suppiler_window, func_name = "Change", supplier_id=self.suppiler_id)

    def edit_func(self):
        info = self.helper.get_list(f"""SELECT * FROM Suppliers WHERE id = {self.suppiler_id} """)[0]
        self.edit_widget.enter_name.setText(str(info[1]))
        self.edit_widget.enter_number.setText(str(info[2]))
        self.edit_widget.enter_mail.setText(str(info[3]))
        self.edit_widget.enter_IBAN.setText(str(info[4]))
        self.edit_widget.enter_info.setText(str(info[5]))
        self.edit_widget.show()