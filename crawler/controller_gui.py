import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtWidgets


class ControllerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_gui()

    def init_gui(self):
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('Crawler')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControllerGUI()
    sys.exit(app.exec_())




