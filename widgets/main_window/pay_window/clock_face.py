from PyQt6.QtWidgets import QWidget, QGridLayout
from widgets.main_window.pay_window.cash_card_clicker import Cash_Card_clicker
from widgets.main_window.pay_window.calculaters_number import Calculaters_number
from widgets.main_window.pay_window.cash_crad_clier import Cash_Card_clear


class Сlock_face(QWidget):
    def __init__(self, cash_line, card_line, summ_order, change):
        super().__init__()
        self.change = change
        self.summ_order = summ_order
        self.cash_line = cash_line
        self.card_line = card_line

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.numbers = []

        self.cash = Cash_Card_clicker(cash=self.cash_line, card=self.card_line, summ_order= self.summ_order, change = self.change)
        self.cash.setMinimumHeight(90)
        self.zero = Calculaters_number("0", active_line=self.cash)
        self.zero.setMinimumHeight(90)
        self.clear = Cash_Card_clear(text="CLEAR", card_line=self.card_line, cash_line=self.cash_line)
        self.clear.setMinimumHeight(90)

        self.flag = False
        self.numb = 1
        for i in range(4):
            for b in range(3):
                btn = Calculaters_number(text = f"{self.numb}", active_line=self.cash)
                btn.setMinimumHeight(90)
                self.grid.addWidget(btn, i, b)
                if self.numb == 9:
                    self.flag = True
                    break
                self.numb += 1
            if self.flag == True:



                self.grid.addWidget(self.cash, 3, 0)
                self.grid.addWidget(self.zero, 3, 1)
                self.grid.addWidget(self.clear, 3, 2)
                break