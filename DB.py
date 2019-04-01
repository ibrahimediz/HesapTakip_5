class VeriTabani():
    def __init__(self,adres):
        self.adres = adres
    
    def select(self,**kwargs):
        import sqlite3
        try:
            adim = "1"
            liste = []
            baglanti = sqlite3.connect(self.adres)
            adim = "1A"
            cur = baglanti.cursor()
            sorgu = "SELECT * FROM "
            for key,value in kwargs.items():
                if key=="Tablo":
                    sorgu += value
            adim = "2A"
            cur.execute(sorgu)
            liste = cur.fetchall()
            adim = "3A"
        except:
            liste.insert(0,"Hata :"+adim)
        finally:
            baglanti.close()
            return liste

    def TabloIsmiBul(self):
        sonuc = ""
        for key,value in self.sozluk.items():
            if key.upper() == "TABLO":
                sonuc = value
        return sonuc
    
    def IDBul(self):
        sonuc = ""
        for key,value in self.sozluk.items():
            if key.upper() == "ID":
                sonuc = value
        return sonuc
    
    def SutunBul(self):
        liste = []
        for key,value in self.sozluk.items():
            if key.upper() == "SUTUN":
                liste = value
        return liste

    def DegerBul(self):
        liste = []
        for key,value in self.sozluk.items():
            if key.upper() == "DEGER":
                liste = value
        return liste
    def strGonder(self,metin):
        return "'" + metin + "'"
    def insert(self,**kwargs):
        import sqlite3
        adim = 0
        self.sozluk = kwargs
        try:
            adim = "-1"
            baglanti = sqlite3.connect(self.adres)
            adim = "1A"
            cur = baglanti.cursor()
            sorgu = "INSERT INTO "
            if self.TabloIsmiBul():
                sorgu += self.TabloIsmiBul() + " ( "
                liste = self.SutunBul()
                for item in liste:
                    sorgu += item + ","
                sorgu = sorgu[0:len(sorgu)-1]
                sorgu += " ) VALUES ("
                liste = self.DegerBul()
                for item in liste:
                    sorgu += str(item) + ","
                sorgu = sorgu[0:len(sorgu)-1]
                sorgu += ")"
            adim = "2A"
            cur.execute(sorgu)
            adim = "1"
        except:
            adim = "Hata:"+adim+"Sorgu:"+sorgu
        finally:
            baglanti.commit()
            baglanti.close()
            return adim    
    def UpdateWithID(self,**kwargs):
            import sqlite3
            adim = 0
            self.sozluk = kwargs
            try:
                adim = "-1"
                baglanti = sqlite3.connect(self.adres)
                adim = "1A"
                cur = baglanti.cursor()
                sorgu = "UPDATE  "
                if self.TabloIsmiBul():
                    sorgu += self.TabloIsmiBul() + " SET "
                    liste1 = self.SutunBul()
                    liste2 = self.DegerBul()
                    for i in range(0,len(liste1)):
                        sorgu += liste1[i] + "=" + str(liste2[i]) + ","
                    sorgu = sorgu[0:len(sorgu)-1]
                    sorgu += " WHERE ID = " + str(self.IDBul())
                adim = "2A"
                cur.execute(sorgu)
                adim = "1"
                
            except:
                adim = "Hata:"+adim+"Sorgu:"+sorgu
            finally:
                baglanti.commit()
                baglanti.close()
                return adim    
    def DeleteWithID(self,**kwargs):
            import sqlite3
            adim = 0
            self.sozluk = kwargs
            try:
                adim = "-1"
                baglanti = sqlite3.connect(self.adres)
                adim = "1A"
                cur = baglanti.cursor()
                sorgu = "DELETE FROM " +self.TabloIsmiBul() + " WHERE ID = " +str(self.IDBul())
               
                adim = "2A"
                cur.execute(sorgu)
                adim = "1"
            except:
                adim = "Hata:"+adim+"Sorgu:"+sorgu
            finally:
                baglanti.commit()
                baglanti.close()
                return adim 
    


