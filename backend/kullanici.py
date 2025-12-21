class kullanici:
    def __init__(self,isim:str,sifre:str,eposta:str,telefon_num:str,id:int):
        self.isim = isim
        self.sifre = sifre
        self.eposta = eposta
        self.telefon_num = telefon_num
        self.id = id

        self.aktif_kiralamalar = []

    @classmethod
    def from_dict(cls, veri: dict):
        obj = cls(
            veri["isim"],
            veri["sifre"],
            veri["eposta"],
            veri["telefon_num"],
            veri["id"]
        )
        obj.aktif_kiralamalar = veri.get("aktif_kiralamalar", [])
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
        
        return veri


