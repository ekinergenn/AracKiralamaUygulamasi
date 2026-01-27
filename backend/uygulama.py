from backend.database import database
from backend.kullanici import kullanici
from backend.araba import araba
from backend.kiralama import kiralama
from backend.admin import admin

class uygulama:
    def __init__(self, dosya):
        self.kullanicilar = []
        self.kiralamalar = []
        self.adminler = []
        self.arabalar = []
        self.my_database = database(dosya)
        self.aktif_hesap = admin("","","","",-1) 
        self.admin_bool = False
        
        data = self.my_database.verileri_oku()
        
        for x in data["arabalar"]:
            obj_araba = araba.from_dict(x)
            obj_araba.durum = False 
            self.arabalar.append(obj_araba)

        
        for x in data["kullanicilar"]:
            self.kullanicilar.append(kullanici.from_dict(x))
        for x in data["adminler"]:
            self.adminler.append(admin.from_dict(x))

        for x in data["kiralamalar"]:
            self.kiralamalar.append(kiralama.from_dict(x, self))

    def database_guncelleme(self):
        data = {
                "kullanicilar":[
                ],
                "adminler":[
                ],
                "arabalar":[
                ],
                "kiralamalar":[
                ]
            }
        for x in self.kullanicilar:
            data["kullanicilar"].append(x.sozluk_veri())

        for x in self.adminler:
            data["adminler"].append(x.sozluk_veri())

        for x in self.arabalar:
            data["arabalar"].append(x.sozluk_veri())

        for x in self.kiralamalar:
            data["kiralamalar"].append(x.sozluk_veri())

        self.my_database.verileri_yazdir(data)


    def kullanici_id_arama(self,id:int)-> kullanici:
        for x in self.kullanicilar:
            if (x.id == id):
                return x
        return None
            
    def kullanici_eposta_arama(self,eposta:str)-> kullanici:
        for x in self.kullanicilar:
            if (x.eposta == eposta):
                return x
        return None
    
    def admin_eposta_arama(self,eposta:str)-> admin:
        for x in self.adminler:
            if (x.eposta == eposta):
                return x
        return None



    def admin_id_arama(self,id:int)-> admin:
        for x in self.adminler:
            if (x.id == id):
                return x
        return None

    def kiralamalar_id_arama(self,id:int)-> kiralama:
        for x in self.kiralamalar:
            if (x.id == id):
                return x
        return None
            
    def araba_id_arama(self,id:int)-> araba:
        for x in self.arabalar:
            if (x.id == id):
                return x
        return None
    
    def araba_sahip_arama(self,id:int)-> admin:
        for x in self.adminler:
            for arac in x.sahip_arabalar:
                if arac == id:
                    return x
        return None

    def araba_sil(self,id):
        silinecek = self.araba_id_arama(id)
        self.aktif_hesap.sahip_arabalar.remove(id)
        self.arabalar.remove(silinecek)

    def araba_ekle(self,arac):
        self.aktif_hesap.sahip_arabalar.append(arac.id)
        self.arabalar.append(arac)