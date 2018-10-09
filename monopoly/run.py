import sys

from PyQt5.QtWidgets import QApplication

from monopoly.model import MonopolyModel
from PyQt5 import QtGui
from monopoly.gui import MonopolyWidget

def main():
    app = QApplication(sys.argv)
    w = MonopolyWidget(None)
    i = MonopolyModel()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
