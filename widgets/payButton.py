from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QSize

from widgets.func_get_path_icon import get_path_icon


class PayButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Payment")
        self.setFixedHeight(40)
        self.setIcon(get_path_icon("credit-card.svg"))
        self.setIconSize(QSize(25,25))

        self.clicked.connect(self.anyFunction)

    def anyFunction(self, e):
        print(e)