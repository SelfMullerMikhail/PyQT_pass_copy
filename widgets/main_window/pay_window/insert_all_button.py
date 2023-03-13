from PyQt6.QtWidgets import QPushButton



class Insert_all_button(QPushButton):
    def __init__(self, text, summ, activeQLineEdit):
        super().__init__(text = text)
        self.summ = int(summ)
        self.activeQLineEdit = activeQLineEdit
        self.clicked.connect(self.func)

    def func(self, e):
        self.activeLine = self.activeQLineEdit.getActiveLine()

        if self.activeLine.nameLine == "Cash":
            self.numb = self.summ - self.activeQLineEdit.getCardMoney()
            self.activeLine.setText(str(self.numb))
        else:
            self.numb = self.summ - self.activeQLineEdit.getCashMoney()
            self.activeLine.setText(str(self.numb))