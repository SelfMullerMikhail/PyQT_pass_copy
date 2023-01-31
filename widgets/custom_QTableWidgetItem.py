from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt


class CustomQTableWidgetItem(QTableWidgetItem):

    def __init__(self, *args):
        super().__init__(*args)
        self.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)