from PyQt6.QtWidgets import QPushButton
from functions.db_Helper import Db_helper



class Dell_category_button(QPushButton):
    def __init__(self, name, text, wind):
        super().__init__(text=text)
        self.name = name
        self.wind = wind
        self.helper = Db_helper("Alpha.db")
        self.clicked.connect(self.func)


    def func(self):
        count_products = int(self.helper.get_list(f"""SELECT count(Menu.id) 
                                FROM Category, Menu 
                                WHERE Menu.category = Category.id AND
                                                    Category.name = '{self.name}' """)[0][0])
        if count_products == 0:
            numb = self.helper.get_list("""SELECT count(id) FROM Category""")[0][0]
            if numb > 1:
                self.helper.insert(f"""DELETE FROM Category WHERE name = '{self.name}'""")
                self.wind.get_category()
                self.wind.central_window.Main_widget.menuTabWidget.clear()
                self.wind.central_window.Main_widget.menuTabWidget.create_full_menu()