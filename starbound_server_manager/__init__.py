import os.path
import sys

from PySide2 import QtWidgets as QtW
from PySide2 import QtGui as QtG


class MainWindow(QtW.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Starbound Server Manager")
        self.setWindowIcon(QtG.QIcon(os.path.join("resources", "ssm-logo.png")))

        self.top_menu = self.menuBar()
        file_menu = self.top_menu.addMenu("&File")
        exit_menu_item = file_menu.addAction("E&xit")
        exit_menu_item.triggered.connect(self.exit_menu_item_clicked)
        help_menu = self.top_menu.addMenu("&Help")
        about_menu_item = help_menu.addAction("&About")
        about_menu_item.triggered.connect(self.about_menu_item_clicked)

        self.status = self.statusBar()

        # Main Layout
        main_widget = QtW.QTabWidget()
        self.setCentralWidget(main_widget)

        # General Tab
        general_grid = QtW.QGridLayout()
        main_widget.addTab(general_grid, "General")
        players_label = QtW.QLabel("Players")

        server_log_label = QtW.QLabel("Server Log")

        players_list = QtW.QListView()

        self.show()

    def exit_menu_item_clicked(self, s):
        self.close()

    def about_menu_item_clicked(self, s):
        return


if __name__ == '__main__':
    app = QtW.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()
