import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic
from ilkDB import ilkDB
class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.veriTaban = ilkDB()
        self.secilenAy = ""
        self.secilenKalem = ""
        self.win = uic.loadUi(r"Ana.ui")

        self.win.cmbAy.currentIndexChanged.connect(self.cmbAyClick)
        self.win.cmbKalem.currentIndexChanged.connect(self.cmbKalemClick)

        self.win.btKaydet.clicked.connect(self.btKaydeyClick)

        for a,b in self.veriTaban.sozlukGetir(1):
            self.win.cmbKalem.addItem(b,a)
        for a,b in self.veriTaban.sozlukGetir(2):
            self.win.cmbAy.addItem(b,a)
        

    def btKaydeyClick(self):
        tutar =  self.win.txtTutar.text()
        self.veriTaban.VeriEkle(self.secilenKalem,self.secilenAy,tutar)


    def cmbAyClick(self,i):
        self.secilenAy = self.win.cmbAy.itemData(i)
    def cmbKalemClick(self,i):
        self.secilenKalem = self.win.cmbKalem.itemData(i)


        
        self.win.show()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())