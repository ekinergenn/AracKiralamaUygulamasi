from datetime import date
from backend.uygulama import uygulama


class kiralama:
    def __init__(self,kullanici:int,araba:int,bas_tarih:date,bit_tarih:date,ucret:float,id:int,app:uygulama):
        self.kullanici = kullanici
        self.araba = araba
        self.bas_tarih = bas_tarih
        self.bit_tarih = bit_tarih
        self.ucret = ucret
        self.id = id

        if app.araba_id_arama(araba).durum == False:
            app.kullanici_id_arama(self.kullanici).aktif_kiralamalar.append(araba)
            app.araba_id_arama(araba).durum = True
        else:
            pass


    def __init__(self,veri:dict,app:uygulama):
        self.kullanici = veri["kullanici"]
        self.araba = veri["araba"]
        data_str = veri["bas_tarih"].split("-")
        self.bas_tarih = date(int(data_str[0]),int(data_str[1]),int(data_str[2]))
        data_str = veri["bit_tarih"].split("-")
        self.bit_tarih = date(int(data_str[0]),int(data_str[1]),int(data_str[2]))
        self.ucret = veri["ucret"]
        self.id = veri["id"]


        if app.araba_id_arama(self.araba).durum == False:
            app.kullanici_id_arama(self.kullanici).aktif_kiralamalar.append(self.araba)
            app.araba_id_arama(self.araba).durum = True
        else:
            pass


    def sozluk_veri(self) -> dict:
        veri = {
            "kullanici":0,
            "araba":0,
            "bas_tarih":"",
            "bit_tarih":"",
            "ucret":0,
            "id":0
        }
        
        veri["kullanici"] = self.kullanici
        veri["araba"] = self.araba
        veri["bas_tarih"] = str(self.bas_tarih)
        veri["bit_tarih"] = str(self.bit_tarih)
        veri["ucret"] = self.ucret
        veri["id"] = self.id
        return veri

