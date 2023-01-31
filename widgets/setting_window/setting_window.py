from PyQt6.QtWidgets import QTableWidget, QListWidget, QTabWidget, QGridLayout

class Setting_widget(QGridLayout):
    def __init__(self, *args):
        super().__init__()
        self.addWidget(QTableWidget(), 0, 0, 3, 1)
        self.addWidget(QListWidget(), 0, 2, 13, 8)