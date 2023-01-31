import re

from PyQt6.QtWidgets import QPushButton



class Cash_Card_clicker(QPushButton):
    def __init__(self, cash, card, summ_order, change):
        super().__init__()
        self.setText("CARD")
        self.summ_order = summ_order
        self.change = change
        self.cash = cash
        self.card = card
        self.active_line = self.cash

        self.cash_e = 0
        self.card_e = 0

        self.pressed.connect(self.func)

        self.cash.textChanged.connect(self.card_holder)
        self.card.textChanged.connect(self.cash_holder)

    def card_holder(self, e):
        if e == "":
            self.card.setPlaceholderText("Card")
            self.card_e = 0
        else:
            self.card_e = e
            self.card.setPlaceholderText(f"Card: {self.summ_order - int(e)}")
        self.change_func()
        

    def cash_holder(self, e):
        if e == "":
            self.cash.setPlaceholderText("Cash")
            self.cash_e = 0
        else:
            self.cash_e = e
            self.cash.setPlaceholderText(f"Cash: {self.summ_order - int(e)}")
        self.change_func()

    def change_func(self):
        numb = self.summ_order - (int(self.cash_e) + int(self.card_e))
        self.change.setText(str(numb))
        
    def func(self):
        if self.active_line == self.cash:
            self.active_line = self.card
            self.setText("CASH")
        else:
            self.active_line = self.cash
            self.setText("CARD")