from PyQt6.QtWidgets import QWidget, QGridLayout
from PyQt6 import QtGui

from widgets.main_window.pay_window.insert_all_button import Insert_all_button
from widgets.main_window.pay_window.cash_card_clicker import Cash_Card_clicker
from widgets.main_window.pay_window.calculaters_number import Calculaters_number
from widgets.main_window.pay_window.cash_crad_clier import Cash_Card_clear
from functions.resize_func import resizeFunc


class Сlock_face(QWidget):
    def __init__(self, cash_line, card_line, summ_order, change, activeQLineEdit):
        super().__init__()
        self.change = change
        self.activeQLineEdit = activeQLineEdit
        self.summ_order = summ_order
        self.cash_line = cash_line
        self.card_line = card_line
        self.constSize = self.size()

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.numbers = []
        self.btns =[]
        self.insertAll = Insert_all_button(text = "Insert all", summ = self.summ_order, activeQLineEdit=self.activeQLineEdit)
        self.insertAll.setFont(QtGui.QFont("Arial", 20))
        self.zero = Calculaters_number("0", active_line=self.activeQLineEdit)
        self.zero.setFont(QtGui.QFont("Arial", 20))
        self.clear = Cash_Card_clear(text="CLEAR", card_line=self.card_line, cash_line=self.cash_line)
        self.clear.setFont(QtGui.QFont("Arial", 20))
        self.flag = False
        self.numb = 1
        for i in range(4):
            for b in range(3):
                self.btn = Calculaters_number(text = f"{self.numb}", active_line=self.activeQLineEdit)
                self.btn.setFont(QtGui.QFont("Arial", 20))
                self.btns.append(self.btn)
                self.grid.addWidget(self.btn, i, b)
                if self.numb == 9:
                    self.flag = True
                    break
                self.numb += 1
            if self.flag == True:

                self.grid.addWidget(self.insertAll, 3, 0)
                self.grid.addWidget(self.zero, 3, 1)
                self.grid.addWidget(self.clear, 3, 2)
                break

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self.insertAll.setFixedHeight(resizeFunc(event=event, constSize=self.constSize, sizeH=110)[1])
        self.zero.setFixedHeight(resizeFunc(event=event, constSize=self.constSize, sizeH=110)[1])
        self.clear.setFixedHeight(resizeFunc(event=event, constSize=self.constSize, sizeH=110)[1])
        for btn in self.btns:
            btn.setFixedHeight(resizeFunc(event=event, constSize=self.constSize, sizeH=90)[1])

        return super().resizeEvent(event)
    

