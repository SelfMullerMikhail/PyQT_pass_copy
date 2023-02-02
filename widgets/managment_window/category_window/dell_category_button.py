from PyQt6.QtWidgets import QPushButton, QMessageBox
from functions.db_Helper import Db_helper



class Dell_category_button(QPushButton):
    def __init__(self, name, text, wind, id_category):
        super().__init__(text=text)
        self.name = name
        self.wind = wind
        self.id_category = id_category
        self.helper = Db_helper("Alpha.db")
        self.clicked.connect(self.func)


    def func(self):
        msgBox = QMessageBox()
        msgBox.setText(f"""Do you want delete category: '{self.name}'?.
                            You will lost all products from this category""")
        yes = QMessageBox.StandardButton.Ok
        msgBox.setStandardButtons(yes | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setWindowTitle("Delete category")
        result = msgBox.exec()      
        if result == yes:
            count_category = self.helper.get_list(f"""SELECT count(id) 
                                                    FROM Category; """)[0][0]
                                                        
            if count_category > 1:
                products_in_category = self.helper.get_list(f"""SELECT * 
                                                                FROM Menu
                                                                WHERE Menu.category = {self.id_category};""")
                if products_in_category == []:
                    self.helper.insert(f"""DELETE FROM Category WHERE id = {self.id_category};""")
                    self.wind.get_category()
                    self.wind.central_window.Main_widget.menuTabWidget.clear()
                    self.wind.central_window.Main_widget.menuTabWidget.create_full_menu()
                else:
                    check_products = self.helper.get_list(f"""SELECT * 
                                                            FROM MenuViewId
                                                            WHERE id_category = {self.id_category}
                                                            GROUP BY name_menu;""")
                    text = ""
                    for i in check_products:
                        text += f"{i[1]}_{i[0]} " + ", "
                    print(check_products)
                    print(text)
                    print(self.id_category)
                    msgBox = QMessageBox()
                    msgBox.setText(f"You can not delete: '{self.name}' becouse it is not empty:")
                    msgBox.setDetailedText(text)
                    msgBox.exec()










