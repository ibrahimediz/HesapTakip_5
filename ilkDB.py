from DB import VeriTabani
class ilkDB():
    def __init__(self):
        self.adres = r"D:\İbrahim EDİZ\HesapTakip_5\IEDB.db"

        

    def VeriEkle(self,text1,text2):
        import sqlite3
        db = sqlite3.connect(self.adres)
        cursor = db.cursor()
        cursor.execute("""INSERT INTO ARAYUZ_DENEME 
        (TEXT1,TEXT2) VALUES 
        ('{}','{}')""".format(text1,text2))
        db.commit()


        # print(text1,text2)
        # self.insert(TABLO=self.TabloAdi,SUTUN=self.Sutun,
        # DEGER=[text1,text2])