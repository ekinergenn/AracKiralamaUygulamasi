from datetime import date
class kiralama:
    def __init__(self,kullanici:int,araba:int,bas_tarih:date,bit_tarih:date,ucret:float,id:int,app):
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


    @classmethod
    def from_dict(cls, veri, app):
        y, m, d = map(int, veri["bas_tarih"].split("-"))
        bas = date(y, m, d)
        y, m, d = map(int, veri["bit_tarih"].split("-"))
        bit = date(y, m, d)

        return cls(
            veri["kullanici"],
            veri["araba"],
            bas,
            bit,
            veri["ucret"],
            veri["id"],
            app
        )


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

