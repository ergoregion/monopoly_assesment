import sys

from PyQt5.QtWidgets import QApplication

from monopoly.model import MonopolyModel
from PyQt5 import QtGui
from monopoly.gui import MonopolyWidget
from monopoly.gui.heatmap import heatmap_matrix

def main():
    app = QApplication(sys.argv)
    i = MonopolyModel()
    print(len(i.sites))
    print(len(i.states))
    heatmap_matrix(i)
    w = MonopolyWidget(None, i.sites)
    w.set_values({i.sites[1]: 10.0})
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
