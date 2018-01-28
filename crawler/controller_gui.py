import sys
import logging
from time import sleep

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QDesktopWidget, QSlider, QLineEdit, QLabel, QPushButton
from PyQt5.QtCore import Qt

from crawler.controller import CrawlerController


logger = logging.getLogger("ipx_logget")


class ControllerGUI(QWidget):
    """ControllerGUI
        Class used to handle Crawler's Controller in a GUI.
    """
    def __init__(self):
        """Constructor
        """
        super().__init__()

        self.init_gui()

        self.control = None

    def init_gui(self):
        """init_gui
            Define aspect of the GUI.
        :return: None
        """
        self.setWindowTitle('Crawler')
        self.resize(800, 500)
        self.center()
        self.__create_widgets__()

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __create_widgets__(self):
        """create_widgets
            Create app's widgets
        """
        self.__create_drive_slider__()
        self.__create_steer_slider__()
        self.__create_crawler_ip_line_edit__()
        self.__create_crawler_port_line_edit__()
        self.__create_connect_button__()

    def __create_connect_button__(self):
        """__create_connect_button__
            Create the connect button used to establish connection between Crawler and controller.
        :return: None
        """
        self.connect_button = QPushButton(self)
        self.connect_button.move(10, 115)
        self.connect_button.setText("Connect")
        self.connect_button.clicked.connect(self.connect_to_crawler)
        self.connect_button.show()

    def __create_crawler_ip_line_edit__(self):
        """__create_crawler_ip_line_edit__
            Creates the widget which store Crawler's IP address.
        :return: None
        """
        ip_label = QLabel(self)
        ip_label.setText("Crawler's IP")
        ip_label.move(10, 20)
        ip_label.show()
        self.crawler_ip_line_edit = QLineEdit(self)
        self.crawler_ip_line_edit.move(10, 40)
        self.crawler_ip_line_edit.setText('192.168.0.101')
        self.crawler_ip_line_edit.show()

    def __create_crawler_port_line_edit__(self):
        """__create_crawler_port_line_edit__
            Creates the widget which store Crawler's port.
        :return: None
        """
        port_label = QLabel(self)
        port_label.setText("Crawler's port")
        port_label.move(10, 70)
        port_label.show()
        self.crawler_port_line_edit = QLineEdit(self)
        self.crawler_port_line_edit.move(10, 90)
        self.crawler_port_line_edit.setText('1369')
        self.crawler_port_line_edit.show()

    def __create_drive_slider__(self):
        """__create_drive_slider__
            Slider used to control driving of the Crawler.
        :return: None
        """
        self.drive_slider = QSlider(Qt.Vertical, self)
        self.drive_slider.move(750, 50)
        self.drive_slider.setMaximum(100)
        self.drive_slider.setMinimum(-100)
        self.drive_slider.resize(30, 200)
        self.drive_slider.valueChanged.connect(self.drive)

    def __create_steer_slider__(self):
        """__create_steer_slider__
            Slider used to control steering of the Crawler.
        :return: None
        """
        self.steer_slider = QSlider(Qt.Horizontal, self)
        self.steer_slider.move(550, 250)
        self.steer_slider.setMaximum(100)
        self.steer_slider.setMinimum(-100)
        self.steer_slider.resize(200, 30)
        self.steer_slider.valueChanged.connect(self.steer)

    def connect_to_crawler(self):
        """connect_to_crawler
            Connect to crawler using provided credentials (IP and port).
        :return: None
        """
        ip = self.crawler_ip_line_edit.text()
        port = self.crawler_port_line_edit.text()
        try:
            port = int(port)
        except Exception as err:
            logger.warning("Invalid port: {}".format(port))
        self.control = CrawlerController(ip, port)
        self.control.connect_to_crawler()

        sleep(1)
        self.control.send_command(self.control.commands.enable_motor_control)

    def drive(self):
        """drive
            Drive Crawler.
        :return: None
        """
        speed = int(self.drive_slider.value())
        self.control.drive(speed)

    def steer(self):
        """steer
            Steer Crawler.
        :return: None
        """
        steering = int(self.steer_slider.value())
        self.control.steer(steering)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControllerGUI()
    sys.exit(app.exec_())




