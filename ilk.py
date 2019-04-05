import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from ilkDB import ilkDB
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()     
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.text1 = QLineEdit(self)
        self.text1.move(50,50)
        self.text2 = QLineEdit(self)
        self.text2.move(50,80)
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(180,70) 
        button.clicked.connect(self.on_click)
        self.show()        
    @pyqtSlot()
    def on_click(self):
        AYDB = ilkDB()
        AYDB.VeriEkle(self.text1.text(),self.text2.text())
        print(self.text1.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 
