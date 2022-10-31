import PySide6.QtWidgets as QtW


class AboutWindow(QtW.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Starbound Server Manager")

