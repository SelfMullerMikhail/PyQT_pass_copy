from PyQt6.QtWidgets import QGridLayout, QDialog


class DialogInfo(QDialog):
    def __inti__(self, widget):
        super().__init__()
        self.loy = QGridLayout()
        self.widget = widget
        self.setLayout(self.loy)
        self.loy.addWidget(self.widget)