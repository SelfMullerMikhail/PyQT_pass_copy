import os

from PyQt6.QtGui import QIcon


def get_path_icon(name):
    return QIcon(os.path.join( os.path.dirname( __file__ ), '' ) + f"feather/{name}")  