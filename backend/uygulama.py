from backend.database import database
from backend.kullanici import kullanici
from backend.araba import araba
from backend.kiralama import kiralama
from backend.admin import admin

class uygulama:
    def __init__(self,dosya):
        self.kullanicilar = []
        self.kiralamalar = []
        self.adminler = []
        self.arabalar = []
        self.my_database = database(dosya)
        self.aktif_hesap = None
        
        data = self.my_database.verileri_oku()
        
        for x in data["kullanicilar"]:
            self.kullanicilar.append(kullanici.from_dict(x))

        for x in data["arabalar"]:
            self.arabalar.append(araba.from_dict(x))

        for x in data["adminler"]:
            self.adminler.append(admin.from_dict(x))

        for x in data["kiralamalar"]:
            self.kiralamalar.append(kiralama.from_dict(x,self))


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


