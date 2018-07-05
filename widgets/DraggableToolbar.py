import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class DraggableToolbar(QtWidgets.QWidget):

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self,event):
        self.window().move(event.globalPos()-self.offset)