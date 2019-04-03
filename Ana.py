import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic

class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.win = uic.loadUi(r"D:\İbrahim EDİZ\HesapTakip_5\Ana.ui")
        self.win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())