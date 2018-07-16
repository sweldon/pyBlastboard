import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPalette, QBrush, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        loadUi('ui/mainui.ui',self)
        self.close_button.clicked.connect(self.close_window)
        self.min_button.clicked.connect(self.min_window)
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor('#383939'))
        self.setPalette(palette)

    @pyqtSlot()
    def min_window(self):
        self.window().showMinimized()

    @pyqtSlot()
    def close_window(self):
        self.window().close()
