import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QColor, QGuiApplication, QIcon, QPalette, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QStackedLayout, QWidget

from lib.shared import __program_name__, __version__


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    app = QApplication(sys.argv)
    width = 400
    height = 600

    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle(__program_name__)
        self.setFixedSize(QSize(self.width, self.height))
        # Set app icon from assets/logo.png
        icon_pixmap = QPixmap("assets/logo.png")
        icon = QIcon(icon_pixmap)
        self.setWindowIcon(icon)

        # Layout
        self.layout = QStackedLayout()

        self.layout.addWidget(Color("red"))
        self.layout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # Menu Bar
        self.accounts_button_action = QAction("&Accounts", self)
        self.accounts_button_action.triggered.connect(self.showAccountsView)
        self.accounts_button_action.setCheckable(True)
        self.accounts_button_action.setChecked(True)  # Default View
        self.accounts_button_action.setDisabled(True)  # Default View

        self.macros_button_action = QAction("&Macros", self)
        self.macros_button_action.triggered.connect(self.showMacrosView)
        self.macros_button_action.setCheckable(True)

        menu = self.menuBar()
        view_menu = menu.addMenu("&View")
        view_menu.addAction(self.accounts_button_action)
        view_menu.addAction(self.macros_button_action)

        # Status Bar
        statusBarLabel = QLabel("v" + __version__)
        statusBarLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.statusBar().addWidget(statusBarLabel, 1)
        self.statusBar().setSizeGripEnabled(False)
        # add padding to the right of the status bar
        self.statusBar().setStyleSheet("padding: 0 5px;")

    def showAccountsView(self, checked):
        self.accounts_button_action.setDisabled(True)
        self.macros_button_action.setDisabled(False)
        self.macros_button_action.setChecked(False)
        self.layout.setCurrentIndex(0)
        self.log("Switched to Accounts View")

    def showMacrosView(self, checked):
        self.macros_button_action.setDisabled(True)
        self.accounts_button_action.setDisabled(False)
        self.accounts_button_action.setChecked(False)
        self.layout.setCurrentIndex(1)
        self.log("Switched to Macros View")

    def log(self, message):
        print("MAIN_WINDOW :: " + message)

    def main(self):
        self.show()
        self.app.exec()
