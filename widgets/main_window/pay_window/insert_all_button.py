from PyQt6.QtWidgets import QPushButton



class Insert_all_button(QPushButton):
    def __init__(self, text, summ, active_line):
        super().__init__(text = text)
        self.summ = summ
        self.active_line = active_line
        self.clicked.connect(self.func)

    def func(self, e):
        if self.active_line.cash.active_line == self.active_line.cash:
            numb = self.summ - int(self.active_line.cash.cash_e)
            self.active_line.cash.active_line.setText(str(numb))
        else:
            numb = self.summ - int(self.active_line.cash.card_e)
            self.active_line.cash.active_line.setText(str(numb))