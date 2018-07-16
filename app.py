import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QSplashScreen
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPalette, QBrush, QImage, QPixmap
from main import MainWindow
import requests
import json
import configparser

class Login(QMainWindow):

    def __init__(self, servers_up):
        super(Login, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.servers_up = servers_up
        loadUi('ui/loginui.ui',self)
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("images/blast.png")))
        self.setPalette(palette)
        self.close_button.clicked.connect(self.close_window)
        self.min_button.clicked.connect(self.min_window)
        self.user_field.setPlaceholderText("Username")
        self.pass_field.setPlaceholderText("Password")
        self.pass_field.setEchoMode(QLineEdit.Password)
        self.pass_field.returnPressed.connect(self.login)
        self.submit_login.clicked.connect(self.login)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.error_label.hide()
        config = configparser.ConfigParser()
        config.read('config.ini')
        api_endpoint = config["API_SERVER"]["address"]
        
        # Check servers
        if not self.servers_up:
            self.error_label.setText('Can\'t connect to the Blastboard servers.')
            self.error_label.show()  
            self.user_field.setDisabled(True)
            self.pass_field.setDisabled(True)
            self.submit_login.setDisabled(True)

    @pyqtSlot()
    def min_window(self):
        self.window().showMinimized()

    @pyqtSlot()
    def close_window(self):
        self.window().close()

    @pyqtSlot()
    def login(self):
        username = self.user_field.text()
        password = self.pass_field.text()
        login_endpoint = self.api_endpoint + "/Login"
        login_request = requests.post(login_endpoint, 
            data={'username': username, 'password': password})
        login_response = json.loads(login_request.text)

        if login_response:
            login_status = login_response["status"]
            login_message = login_response["message"]
            
            if login_status == 200:
                self.close()
                self.main_window = MainWindow()
                self.main_window.show()
            elif login_status == 100:
                self.error_label.setText('Incorrect username or password')
                self.error_label.show()
            else:
                self.error_label.show()
        else:
            self.error_label.setText('Please try again.')
            self.error_label.show()

app = QApplication(sys.argv)
splash_pix = QPixmap("images/blast_splash.png")
splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
splash.setMask(splash_pix.mask())
splash.show()
app.processEvents()

servers_up = True

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_endpoint = config["API_SERVER"]["address"]
    print(type(api_endpoint))
    api_request = requests.head(api_endpoint, timeout=10)
except:
    servers_up = False

login = Login(servers_up)
splash.finish(login)
login.show()
sys.exit(app.exec_())