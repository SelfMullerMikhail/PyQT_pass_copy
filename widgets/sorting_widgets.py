from PyQt6.QtWidgets import QComboBox, QLineEdit



class QComboBoxSorting(QComboBox):
    def __init__(self, selfWidget, sort_list, quick_search):
        super().__init__()
        self.selfWidget = selfWidget
        self.quick_search = quick_search
        
        for i in sort_list:
            self.addItem(f"{i}")
        self.category_search = sort_list[0]
        self.quick_search.setPlaceholderText(f"Quick search: {self.category_search}")
        self.textActivated.connect(self.sorting_func)
    
    def sorting_func(self, e):
        self.category_search = e
        self.quick_search.setPlaceholderText(f"Quick search {self.category_search}")
        self.selfWidget.drow_func()


class QLineEditSorting(QLineEdit):
    def __init__(self, selfWidget):
        super().__init__()
        self.quick_search_line = ''
        self.func = selfWidget

        self.textChanged.connect(self.quick_search_func)

    def quick_search_func(self, e):
        self.quick_search_line = e
        self.func.drow_func()