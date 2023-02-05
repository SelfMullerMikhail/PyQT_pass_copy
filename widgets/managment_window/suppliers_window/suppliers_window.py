from PyQt6.QtWidgets import QGridLayout, QPushButton

from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.ordersListWidget import OrdersListWidget
from widgets.managment_window.suppliers_window.customWidgets import Dell_Button_Suppliers
from widgets.sorting_widgets import QLineEditSorting, QComboBoxSorting
from widgets.managment_window.suppliers_window.append_edit_widget import Append_Edit_widget
from widgets.managment_window.suppliers_window.suppiler_edit_button import SuppilerEditButton
from functions.db_Helper import Db_helper



class Suppliers_window(QGridLayout):
    def __init__(self, active_window, central_window):
        super().__init__()
        self.helper = Db_helper("Alpha.db")
        self.central_window = central_window
        self.suppliers_list = OrdersListWidget(active_window = active_window)
        self.suppliers_list.setColumnCount(7) 
        self.suppliers_list.add_columns(((0, "Name"), (1, "Number"), (2, "Mail"), (3, "IBAN"), (4, "Info"), (5, ""), (6, "")))
        self.suppliers_list.settingSizeColumn((70, 70, 70, 70, 150, 30, 30))
        self.suppliers_list.settingSizeRow(35)
        self.suppliers_list.setLineCount("Suppliers")
        self.quick_search = QLineEditSorting(selfWidget=self)
        sort_list = ["name", "number", "mail", "iban", "info"]
        self.sorting = QComboBoxSorting(sort_list=sort_list, selfWidget=self, quick_search = self.quick_search)
        self.append_button = QPushButton(text="Append") # Кастомить
        self.append_button.clicked.connect(self.add_supplier_window)
        self.addWidget(self.suppliers_list, 1, 0, 19, 20)
        self.addWidget(self.quick_search, 0, 0, 1, 3)
        self.addWidget(self.sorting, 0, 3, 1, 3)
        self.addWidget(self.append_button, 0, 18, 1, 2)
        self.get_suppliers()

    def drow_func(self):
        self.get_suppliers()

    def get_suppliers(self):
        self.suppliers_list.clearContents()
        info = self.helper.get_list(f"""SELECT * FROM Suppliers WHERE {self.sorting.category_search} LIKE'%{self.quick_search.quick_search_line}%' GROUP BY {self.sorting.category_search}""")
        self.draw_suppliers(info)

    def draw_suppliers(self, info):
        for row in range(len(info)):
            for i in range(1, 6):
                self.suppliers_list.setItem(row, i-1, CustomQTableWidgetItem(str(info[row][i])))
            self.suppliers_list.setCellWidget(row, 5, SuppilerEditButton(selfWidget=self, suppiler_id = info[row][0]))
            self.suppliers_list.setCellWidget(row, 6, Dell_Button_Suppliers(name = info[row][1] , text = "del", wind = self))

    def add_supplier_window(self):
        self.form = Append_Edit_widget(selfWidget=self, func_name = "Append")
        self.form.show()


   

