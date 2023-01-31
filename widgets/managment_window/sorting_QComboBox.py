from PyQt6.QtWidgets import QComboBox

class Sorting_QComboBox(QComboBox):
    def addItemCycle(self, names):
        for i in names:
            self.addItem(i)

    def __init__(self):
        super().__init__()
