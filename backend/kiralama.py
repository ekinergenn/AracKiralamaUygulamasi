from datetime import date

class kiralama:
    def __init__(self, kullanici: int, araba_id: int, bas_tarih: date, bit_tarih: date, ucret: float, id: int, app):
        self.kullanici = kullanici
        self.araba = araba_id
        self.bas_tarih = bas_tarih
        self.bit_tarih = bit_tarih
        self.ucret = ucret
        self.id = id
        
        today = date.today()
        
        if self.bit_tarih < today:
            self.gecmis = True
        else:
            self.gecmis = False

       
        arac = app.araba_id_arama(araba_id)
        
        if arac:
            
            if self.bas_tarih <= today <= self.bit_tarih:
                arac.durum = True
                
                
                if not self.gecmis:
                    if app.admin_bool:
                        admin_obj = app.admin_id_arama(self.kullanici)
                        if admin_obj and id not in admin_obj.aktif_kiralamalar:
                            admin_obj.aktif_kiralamalar.append(id)
                    else:
                        kullanici_obj = app.kullanici_id_arama(self.kullanici)
                        if kullanici_obj and id not in kullanici_obj.aktif_kiralamalar:
                            kullanici_obj.aktif_kiralamalar.append(id)
            
            
            elif self.gecmis:
                arac.durum = False

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
        return {
            "kullanici": self.kullanici,
            "araba": self.araba,
            "bas_tarih": str(self.bas_tarih),
            "bit_tarih": str(self.bit_tarih),
            "ucret": self.ucret,
            "id": self.id
        }