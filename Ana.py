import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
from ilkDB import ilkDB
class Ana(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.veriTaban = ilkDB()
        self.Ay = "Seçiniz"
        self.secilenAy = ""
        self.secilenKalem = ""
        self.win = uic.loadUi(r"Ana.ui")

        self.win.cmbAy.currentIndexChanged.connect(self.cmbAyClick)
        self.win.cmbKalem.currentIndexChanged.connect(self.cmbKalemClick)

        self.win.btKaydet.clicked.connect(self.btKaydeyClick)
        self.win.cmbKalem.addItem("Seçiniz",-1)
        self.win.cmbAy.addItem("Seçiniz",-1)
        for a,b in self.veriTaban.sozlukGetir(1):
            self.win.cmbKalem.addItem(b,a)
        for a,b in self.veriTaban.sozlukGetir(2):
            self.win.cmbAy.addItem(b,a)
        self.listeDoldur()
            

    def btKaydeyClick(self):
        tutar =  self.win.txtTutar.text()
        sonuc = self.veriTaban.VeriEkle(self.secilenKalem,self.secilenAy,tutar)
        if sonuc == 1:
            QMessageBox.information(self,"Sonuç","Kaydedildi")
            self.listeDoldur()
        

    def listeDoldur(self):
        satir = 0
        self.win.listDinamik.clear()
        self.win.listDinamik.setColumnCount(4)
        liste = self.veriTaban.listeGetir(self.Ay)
        self.win.listDinamik.setRowCount(20)
        for a,b,c,d in liste:
            self.win.listDinamik.setItem(satir, 0, QTableWidgetItem(str(a)))
            self.win.listDinamik.setItem(satir, 1, QTableWidgetItem(str(b)))
            self.win.listDinamik.setItem(satir, 2, QTableWidgetItem(str(c)))
            self.win.listDinamik.setItem(satir, 3, QTableWidgetItem(str(d)))
            satir+=1

    def cmbAyClick(self,i):
        self.secilenAy = self.win.cmbAy.itemData(i)
        self.Ay = self.win.cmbAy.itemText(i)
        print(self.Ay)
        self.listeDoldur()
    def cmbKalemClick(self,i):
        self.secilenKalem = self.win.cmbKalem.itemData(i)


        
        self.win.show()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ana()
    sys.exit(app.exec_())