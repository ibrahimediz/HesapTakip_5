from DB import VeriTabani
import sqlite3 as sql
class ilkDB():
    def __init__(self):
        self.adres = r"IEDB.db"

        

    def VeriEkle(self,kalem,ay,tutar):
        try:
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
            return 1
        except:
            return 0
        finally:
            db.close()


    # select * from v_hesap 
    def listeGetir(self,ay="Seçiniz"):
        db = sql.connect(self.adres)
        cursor = db.cursor()
        sorgu = """
        select * from v_hesap """
        if ay != "Seçiniz":
                sorgu += " where  AY = '" + ay + "'"
        cursor.execute(sorgu)
        return cursor.fetchall()


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