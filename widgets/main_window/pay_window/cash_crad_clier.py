from PyQt6.QtWidgets import QPushButton



class Cash_Card_clear(QPushButton):
    def __init__(self, text, cash_line, card_line):
        super().__init__(text=text)
        self.cash_line = cash_line
        self.card_line = card_line
        self.clicked.connect(self.func)

    def func(self):
        self.cash_line.clear()
        self.card_line.clear()