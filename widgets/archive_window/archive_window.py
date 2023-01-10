import sys, os

from PyQt6.QtWidgets import  QVBoxLayout, QGridLayout

# sys.path.append(os.path.dirname( __file__ ).replace("widgets/main_window", ""))

class Archive_widget(QGridLayout):
    def __init__(self, *args):
        super().__init__()
        ...