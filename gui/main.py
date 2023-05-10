import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QColor, QGuiApplication, QIcon, QPalette, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStackedLayout,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

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

        tabs = QTabWidget()
        tabs.addTab(Color("red"), "Accounts")
        tabs.addTab(Color("blue"), "Macros")
        self.layout.addWidget(tabs)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        # Menu Bar
        menu = self.menuBar()
        help_menu = menu.addMenu("Help")
        help_menu.addAction("About")
        help_menu.addAction("Check for Updates")
        help_menu.addSeparator()
        help_menu.addAction("Report a Bug")
        help_menu.addAction("Request a Feature")
        help_menu.addAction("Donate")
        help_menu.addSeparator()
        help_menu.addAction("Quit", self.app.quit, "Ctrl+Q")

        # Status Bar
        statusBarLabel = QLabel("v" + __version__)
        statusBarLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.statusBar().addWidget(statusBarLabel, 1)
        self.statusBar().setSizeGripEnabled(False)
        # add padding to the right of the status bar
        self.statusBar().setStyleSheet("padding: 0 5px;")

    def log(self, message):
        print("MAIN_WINDOW :: " + message)

    def main(self):
        self.show()
        self.app.exec()
