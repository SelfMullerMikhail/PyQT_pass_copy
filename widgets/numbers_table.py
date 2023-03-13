from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6 import QtGui




class Numbers_table(QWidget):
    def __init__(self, selfWidget, tipe_of_button, main_wdinow = ...):
        super().__init__()
        self.selfWidget = selfWidget
        self.main_wdinow = main_wdinow
        self.loy = QGridLayout() 
        self.setLayout(self.loy) 
        self.clear = QPushButton()
        self.clear.setFont(QtGui.QFont("Arial", 20))
        self.clear.setMinimumHeight(90)
        self.zero = tipe_of_button(text="0", selfWidget=self.selfWidget, main_wdinow = self.main_wdinow)
        self.zero.setFont(QtGui.QFont("Arial", 20))
        self.zero.setMinimumHeight(90)
        self.close_button = QPushButton()
        self.close_button.setMinimumHeight(90)
        self.close_button.setFont(QtGui.QFont("Arial", 20))
        self.flag = False
        self.numb = 1
        for i in range(4):
            for b in range(3):
                btn = tipe_of_button(text = f"{self.numb}", selfWidget=self.selfWidget, main_wdinow = self.main_wdinow)
                btn.setFont(QtGui.QFont("Arial", 20))
                btn.setMinimumHeight(90)
                self.loy.addWidget(btn, i, b)
                if self.numb == 9:
                    self.flag = True
                    break
                self.numb += 1
            if self.flag == True:
                self.loy.addWidget(self.close_button, 3, 0)
                self.loy.addWidget(self.zero, 3, 1)
                self.loy.addWidget(self.clear, 3, 2)
                break
        