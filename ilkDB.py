from DB import VeriTabani
import sqlite3 as sql
class ilkDB():
    def __init__(self):
        self.adres = r"D:\İbrahim EDİZ\HesapTakip_5\IEDB.db"

        

    def VeriEkle(self,kalem,ay,tutar):
        import sqlite3
        db = sqlite3.connect(self.adres)
        cursor = db.cursor()
        cursor.execute("""
                INSERT INTO HSP_BILGI (HSP_KALEM,HSP_TUTAR,HSP_AY)
                VALUES (
                {},
                {},
                {}
                )
                """.format(kalem,tutar,ay)
         )
        db.commit()

    

    def sozlukGetir(self,tabloid):
        db = sql.connect(self.adres)
        cursor = db.cursor()
        cursor.execute("""
        SELECT sozluk_id,SOZLUK_ADI FROM HSP_SOZLUK WHERE TABLO_ID = {}""".format(tabloid)
        )
        return cursor.fetchall()


        # print(text1,text2)
        # self.insert(TABLO=self.TabloAdi,SUTUN=self.Sutun,
        # DEGER=[text1,text2])