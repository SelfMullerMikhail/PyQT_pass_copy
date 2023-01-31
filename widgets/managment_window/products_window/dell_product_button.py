from PyQt6.QtWidgets import QPushButton, QMessageBox

from functions.db_Helper import Db_helper


# sys.path.append( os.path.dirname( __file__ ).replace("widgets\main_window", ""))



class Dell_product_button(QPushButton):
    def __init__(self,*args, name, order_window):
        super().__init__(*args)
        self.helper = Db_helper("Alpha.db")
        self.name = name
        self.order_window = order_window
        self.clicked.connect(self.dell_function)

    def dell_function(self):
        msgBox = QMessageBox()
        msgBox.setText(f"Do you want delete product: '{self.name}'?.")
        yes = QMessageBox.StandardButton.Ok
        msgBox.setStandardButtons(yes | QMessageBox.StandardButton.Cancel)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setWindowTitle("Delete product")
        result = msgBox.exec()
        
        if result == yes:
            check_product = self.helper.get_list(f"""SELECT Menu.name FROM TechnologyCard, Stock, Menu
                                                    WHERE TechnologyCard.id_product = Stock.id
                                                    AND TechnologyCard.id_menu = Menu.id
                                                    AND Stock.name = '{self.name}'
                                                    ;""")
            if check_product == []:
                self.helper.insert(f"DELETE FROM Stock WHERE name = '{self.name}'")
                self.order_window.drow_stock()
            else:
                text = ""
                for i in check_product:
                    text += i[0] + ", "
                msgBox = QMessageBox()
                msgBox.setText(f"You can not delete: '{self.name}' becouse menu still  has this ingridient.")
                msgBox.setDetailedText(text)
                msgBox.exec()