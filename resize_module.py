


class ResizeModule():
    def __init__(self, *args, **kwargs):
        self.upMenu = args[0]
        self.Main_widget = args[1]
        self.managment_window = args[2]
        self.archive_widget = args[3]
        self.dayOf_widget = args[4]
        self.authorization_window = args[5]
        self.login_window = args[6]

    def upMenu_resize(self):
        # self.upMenu.resize(self.upMenu.width(), self.upMenu.height())
        ...

    def managment_window_resize(self):
        ...

    # def Main_widget_resize(self):
    #     .resizeEvent.connect(self.resizePrint)

    def resizePrint(self, event):
        print(event)
