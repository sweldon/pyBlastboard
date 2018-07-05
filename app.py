import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPalette, QBrush, QImage, QPixmap

class Login(QMainWindow):

    def __init__(self):
        super(Login, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        loadUi('ui/loginui.ui',self)
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("images/blast.png")))
        self.setPalette(palette)
        self.close_button.clicked.connect(self.close_window)
        self.min_button.clicked.connect(self.min_window)
        self.user_field.setPlaceholderText("Username")
        self.pass_field.setPlaceholderText("Password")

    @pyqtSlot()
    def min_window(self):
        self.window().showMinimized()

    @pyqtSlot()
    def close_window(self):
        self.window().close()

app = QApplication(sys.argv)
widget = Login()
widget.show()
sys.exit(app.exec_())