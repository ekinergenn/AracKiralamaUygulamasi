from backend.kullanici import kullanici
from backend.araba import araba

class admin(kullanici):
    def __init__(self,isim:str,sifre:str,eposta:str,telefon_num:str,id:int):
        super().__init__(isim,sifre,eposta,telefon_num,id)
        self.sahip_arabalar = []


    @classmethod
    def from_dict(cls, veri: dict):
        obj = cls(
            veri["isim"],
            veri["sifre"],
            veri["eposta"],
            veri["telefon_num"],
            veri["id"]
        )
        obj.aktif_kiralamalar = list(veri.get("aktif_kiralamalar", []))
        obj.sahip_arabalar = list(veri.get("sahip_arabalar", []))
        return obj

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

