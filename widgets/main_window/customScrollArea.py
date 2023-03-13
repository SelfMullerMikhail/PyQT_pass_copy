from PyQt6.QtWidgets import QScrollArea
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSizePolicy

class CustomScrollArea(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setSizeAdjustPolicy(QScrollArea.SizeAdjustPolicy.AdjustToContents)