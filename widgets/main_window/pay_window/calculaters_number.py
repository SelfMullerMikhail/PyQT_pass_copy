from PyQt6.QtWidgets import QPushButton



class Calculaters_number(QPushButton):
    def __init__(self, text, active_line):
        super().__init__(text=text)
        self.active_line = active_line
        self.numb = text
        self.clicked.connect(self.func)

    def func(self):
        self.active_line.active_line.insert(self.numb)

