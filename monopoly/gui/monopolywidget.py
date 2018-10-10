from PyQt5 import QtCore, QtGui, QtWidgets

class MonopolyMarkerWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFixedSize(30, 30)

        self.label = QtWidgets.QLabel('Test', self)  # test, if it's really backgroundimage
        self.label.setGeometry(0, 0, 30, 30)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")


class MonopolyWidget(QtWidgets.QWidget):
    def __init__(self, parent, flags):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(100, 100, 600, 600)
        self.setFixedSize(600, 600)

        oImage = QtGui.QImage("./gui/board3.jpg")
        sImage = oImage.scaled(QtCore.QSize(600, 600))  # resize Image to widgets size
        palette = QtGui.QPalette()
        palette.setBrush(10, QtGui.QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        markers = {}

        for f in flags:
            markers[f] = MonopolyMarkerWidget(self)
            markers[f].setGeometry(f.x, f.y,30,30)

