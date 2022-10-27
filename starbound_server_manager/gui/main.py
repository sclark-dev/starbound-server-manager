import os
import sys

from PySide2 import QtWidgets as QtW
from PySide2 import QtGui as QtG


MonospaceFont = QtG.QFont("Consolas")


class Widgets:
    pass


class MainWindow(QtW.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Starbound Server Manager")
        self.setWindowIcon(QtG.QIcon(os.path.join("resources", "images", "ssm-logo.png")))
        self.setMinimumSize(800, 500)
        self.setFont(MonospaceFont)
        self.widgets = Widgets()

        # Menu and Status
        self.top_menu = self.menuBar()
        self.widgets.file_menu = self.top_menu.addMenu("&File")
        self.widgets.exit_action = self.widgets.file_menu.addAction("E&xit")
        self.widgets.exit_action.triggered.connect(self.__exit_action__)
        self.widgets.help_menu = self.top_menu.addMenu("&Help")
        self.widgets.about_action = self.widgets.help_menu.addAction("&About")
        self.widgets.about_action.triggered.connect(self.__about_action__)

        self.widgets.status = self.statusBar()

        # Main Layout
        self.widgets.central_widget = QtW.QWidget()
        self.widgets.layout = QtW.QVBoxLayout()
        self.widgets.central_widget.setLayout(self.widgets.layout)
        self.setCentralWidget(self.widgets.central_widget)
        self.widgets.tab_widget = QtW.QTabWidget()
        self.widgets.layout.addWidget(self.widgets.tab_widget)

        # General Tab
        self.widgets.general = Widgets()
        self.widgets.general.widget = QtW.QWidget()
        self.widgets.general.layout = QtW.QGridLayout()
        self.widgets.general.widget.setLayout(self.widgets.general.layout)
        self.widgets.tab_widget.addTab(self.widgets.general.widget, "General")

        self.widgets.general.player_label = QtW.QLabel("Players")
        self.widgets.general.layout.addWidget(self.widgets.general.player_label, 0, 0)
        self.widgets.general.log_label = QtW.QLabel("Server Log")
        self.widgets.general.layout.addWidget(self.widgets.general.log_label, 0, 1)

        self.widgets.general.player_list = QtW.QListWidget()
        self.widgets.general.player_list.setSizePolicy(QtW.QSizePolicy(QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Preferred))
        self.widgets.general.player_list.addItem(QtW.QListWidgetItem(QtG.QIcon(os.path.join("resources", "images", "ssm-logo.png")), "Test Item"))
        self.widgets.general.layout.addWidget(self.widgets.general.player_list, 1, 0, 4, 1)

        self.widgets.general.log_list = QtW.QListWidget()
        self.widgets.general.log_list.addItem("[01:09:35] Server stopped")
        self.widgets.general.layout.addWidget(self.widgets.general.log_list, 1, 1)

        self.widgets.general.command_layout = QtW.QHBoxLayout()
        self.widgets.general.layout.addLayout(self.widgets.general.command_layout, 2, 1)
        self.widgets.general.command_edit = QtW.QLineEdit()
        self.widgets.general.command_layout.addWidget(self.widgets.general.command_edit)
        self.widgets.general.command_send = QtW.QPushButton("Send")
        self.widgets.general.command_send.clicked.connect(self.__general_command_send_clicked__)
        self.widgets.general.command_layout.addWidget(self.widgets.general.command_send)

        self.widgets.general.chat_label = QtW.QLabel("Chat Log")
        self.widgets.general.layout.addWidget(self.widgets.general.chat_label, 3, 1)
        self.widgets.general.chat_list = QtW.QListWidget()
        self.widgets.general.layout.addWidget(self.widgets.general.chat_list, 4, 1)

        self.widgets.general.controls_group = QtW.QGroupBox("Server Controls")
        self.widgets.general.controls_group.setSizePolicy(QtW.QSizePolicy(QtW.QSizePolicy.Minimum, QtW.QSizePolicy.Preferred))
        self.widgets.general.layout.addWidget(self.widgets.general.controls_group, 5, 0)
        self.widgets.general.controls_layout = QtW.QVBoxLayout()
        self.widgets.general.controls_group.setLayout(self.widgets.general.controls_layout)
        self.widgets.general.controls_start = QtW.QPushButton("Start")
        self.widgets.general.controls_start.clicked.connect(self.__general_controls_start_clicked__)
        self.widgets.general.controls_layout.addWidget(self.widgets.general.controls_start)
        self.widgets.general.controls_restart = QtW.QPushButton("Restart")
        self.widgets.general.controls_start.clicked.connect(self.__general_controls_restart_clicked__)
        self.widgets.general.controls_layout.addWidget(self.widgets.general.controls_restart)
        self.widgets.general.controls_stop = QtW.QPushButton("Stop")
        self.widgets.general.controls_start.clicked.connect(self.__general_controls_stop_clicked__)
        self.widgets.general.controls_layout.addWidget(self.widgets.general.controls_stop)

        self.widgets.general.info_group = QtW.QGroupBox("Information")
        self.widgets.general.layout.addWidget(self.widgets.general.info_group, 5, 1)
        self.widgets.general.info_layout = QtW.QGridLayout()
        self.widgets.general.info_group.setLayout(self.widgets.general.info_layout)
        self.widgets.general.info_status_label = QtW.QLabel("Status:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_status_label, 0, 0)
        self.widgets.general.info_status_data = QtW.QLabel("Offline")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_status_data, 0, 1, 1, 3)
        self.widgets.general.info_uptime_label = QtW.QLabel("Uptime:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_uptime_label, 1, 0)
        self.widgets.general.info_uptime_data = QtW.QLabel("0d 0h 0m 0s")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_uptime_data, 1, 1, 1, 3)
        self.widgets.general.info_version_label = QtW.QLabel("Version:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_version_label, 2, 0)
        self.widgets.general.info_version_data = QtW.QLabel("Unknown")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_version_data, 2, 1, 1, 3)
        self.widgets.general.info_ip_label = QtW.QLabel("IP:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_ip_label, 3, 0)
        self.widgets.general.info_ip_data = QtW.QLabel("0.0.0.0")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_ip_data, 3, 1)
        self.widgets.general.info_port_label = QtW.QLabel("Port:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_port_label, 3, 2)
        self.widgets.general.info_port_data = QtW.QLabel("21025")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_port_data, 3, 3)
        self.widgets.general.info_connected_label = QtW.QLabel("Players Connected:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_connected_label, 0, 4)
        self.widgets.general.info_connected_data = QtW.QLabel("0")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_connected_data, 0, 5)
        self.widgets.general.info_planets_label = QtW.QLabel("Loaded Planets:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_planets_label, 1, 4)
        self.widgets.general.info_planets_data = QtW.QLabel("0")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_planets_data, 1, 5)
        self.widgets.general.info_ships_label = QtW.QLabel("Loaded Ships:")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_ships_label, 2, 4)
        self.widgets.general.info_ships_data = QtW.QLabel("0")
        self.widgets.general.info_layout.addWidget(self.widgets.general.info_ships_data, 2, 5)

        # Players Tab
        self.widgets.players = Widgets()
        self.widgets.players.widget = QtW.QWidget()
        self.widgets.players.layout = QtW.QVBoxLayout()
        self.widgets.players.widget.setLayout(self.widgets.players.layout)
        self.widgets.tab_widget.addTab(self.widgets.players.widget, "Players")

        self.widgets.players.current_players_label = QtW.QLabel("Current Connected Players: 0")
        self.widgets.players.layout.addWidget(self.widgets.players.current_players_label)
        self.widgets.players.current_players_table = QtW.QTableWidget()
        self.widgets.players.current_players_table.setColumnCount(6)
        self.widgets.players.current_players_table.setHorizontalHeaderItem(0, QtW.QTableWidgetItem("ID"))
        self.widgets.players.current_players_table.horizontalHeader().setSectionResizeMode(0, QtW.QHeaderView.ResizeToContents)
        self.widgets.players.current_players_table.setHorizontalHeaderItem(1, QtW.QTableWidgetItem("Name"))
        self.widgets.players.current_players_table.horizontalHeader().setSectionResizeMode(1, QtW.QHeaderView.Stretch)
        self.widgets.players.current_players_table.setHorizontalHeaderItem(2, QtW.QTableWidgetItem("Account"))
        self.widgets.players.current_players_table.horizontalHeader().setSectionResizeMode(2, QtW.QHeaderView.Stretch)
        self.widgets.players.current_players_table.setHorizontalHeaderItem(3, QtW.QTableWidgetItem("UUID"))
        self.widgets.players.current_players_table.horizontalHeader().setSectionResizeMode(3, QtW.QHeaderView.Stretch)
        self.widgets.players.current_players_table.setHorizontalHeaderItem(4, QtW.QTableWidgetItem("IP"))
        self.widgets.players.current_players_table.horizontalHeader().setSectionResizeMode(4, QtW.QHeaderView.Stretch)
        self.widgets.players.current_players_table.setHorizontalHeaderItem(5, QtW.QTableWidgetItem("Connection Time"))
        self.widgets.players.current_players_table.horizontalHeader().setSectionResizeMode(5, QtW.QHeaderView.Stretch)
        self.widgets.players.layout.addWidget(self.widgets.players.current_players_table)

    def __exit_action__(self):
        pass

    def __about_action__(self):
        pass

    def __general_command_send_clicked__(self):
        pass

    def __general_controls_start_clicked__(self):
        pass

    def __general_controls_restart_clicked__(self):
        pass

    def __general_controls_stop_clicked__(self):
        pass


def main():
    app = QtW.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
