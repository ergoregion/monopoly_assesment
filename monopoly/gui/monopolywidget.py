from PyQt5 import QtCore, QtGui, QtWidgets

class MonopolyWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QHBoxLayout(self)

        self._button = QtWidgets.QPushButton('Error Check', self)
        self._button.clicked.connect(self._check_button_pushed)
        self.layout.addWidget(self._button)


    @QtCore.pyqtSlot()
    def _check_button_pushed(self):
        self._refresh()