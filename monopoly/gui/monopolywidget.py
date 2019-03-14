from PyQt5 import QtCore, QtGui, QtWidgets
from monopoly.gui.locations import locations


class MonopolyMarkerWidget(QtWidgets.QWidget):
    def __init__(self, parent, name):
        QtWidgets.QWidget.__init__(self, parent)
        self.setFixedSize(30, 30)

        self.label = QtWidgets.QLabel(name, self)  # test, if it's really backgroundimage
        self.label.setGeometry(0, 0, 30, 30)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")

    def set_text(self, text):
        self.label.setText(text)

    def set_value(self, i, max):
        i = 100+int(i/max*155)
        self.label.setStyleSheet("background-color: rgb({}, 100, 100);".format(i))



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

        self.markers = {}

        for f in flags:
            self.markers[f] = MonopolyMarkerWidget(self, f.name)
            self.markers[f].setGeometry(locations[f][0] - 15, locations[f][1] - 15, 30, 30)

    def set_values(self, values):
        m = max(values.values())
        for f in values:
            self.markers[f].set_text(str(values[f]))
            self.markers[f].set_value(values[f], m)
