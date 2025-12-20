from backend.kullanici import kullanici
from backend.araba import araba

class admin(kullanici):
    def __init__(self,isim:str,sifre:str,eposta:str,telefon_num:str,id:int):
        super().__init__(isim,sifre,eposta,telefon_num,id)
        self.sahip_arabalar = []


    def __init__(self,veri:dict):
        self.isim = veri["isim"]
        self.sifre = veri["sifre"]
        self.eposta = veri["eposta"]
        self.telefon_num = veri["telefon_num"]
        self.id = veri["id"]
        self.aktif_kiralamalar = veri["aktif_kiralamalar"]
        self.sahip_arabalar = veri["sahip_arabalar"]

    def sozluk_veri(self) -> dict:
        veri = {"isim":"",
            "sifre":"",
            "eposta":"",
            "telefon_num":"",
            "id":0,
            "aktif_kiralamalar":[]}
        
        veri["isim"] = self.isim
        veri["sifre"] = self.sifre
        veri["eposta"] = self.eposta
        veri["telefon_num"] = self.telefon_num
        veri["id"] = self.id
        veri["aktif_kiralamalar"] = self.aktif_kiralamalar
        veri["sahip_arabalar"] = self.sahip_arabalar
        
        return veri

    def araba_ekle(_araba:araba):
        pass

    def araba_sil(_araba:araba):
        pass

