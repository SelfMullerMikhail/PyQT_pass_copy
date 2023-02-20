from PyQt6.QtWidgets import QGridLayout, QGridLayout, QMainWindow

from widgets.ordersListWidget import OrdersListWidget
from widgets.custom_QTableWidgetItem import CustomQTableWidgetItem
from widgets.sorting_widgets import QComboBoxSorting, QLineEditSorting
from widgets.archive_window.del_close_order_button import DelCloseOrderButton
from widgets.archive_window.info_products_order import InfoProductsOrder
from widgets.archive_window.archive_widget_page import Archive_widget_page, Archive_widget_page2
from upMenuComboBox import UpMenu_comboBox
from functions.db_Helper import Db_helper


class Archive_widget(QGridLayout):
    def __init__(self, main_widget):
        super().__init__()
        self.upMenu: UpMenu_comboBox = UpMenu_comboBox()
        self.helper_alpha: Db_helper = Db_helper("Alpha.db")
        self.helper_beta: Db_helper = Db_helper("Beta.db")
        self.main_widget:QMainWindow = main_widget
        self.today_archive_widget_page: Archive_widget_page = Archive_widget_page(main_widget = main_widget)
        self.past_archive_widget_page: Archive_widget_page2 = Archive_widget_page2(main_widget = main_widget)
        self.upMenu.create_tab("Today", "sunrise.svg", self.today_archive_widget_page)
        self.upMenu.create_tab("Past", "clock.svg", self.past_archive_widget_page)
        self.addWidget(self.upMenu.activate("Today"))

    def drow_archive_all(self):
        self.today_archive_widget_page.drow_archive_all()
        self.past_archive_widget_page.drow_archive_all()