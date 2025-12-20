class kullanici:
    def __init__(self,isim:str,sifre:str,eposta:str,telefon_num:str,id:int):
        self.isim = isim
        self.sifre = sifre
        self.eposte = eposta
        self.telefon_num = telefon_num
        self.id = id

        self.aktif_kiralamalar = []

    def __init__(self,veri:dict):
        self.isim = veri["isim"]
        self.sifre = veri["sifre"]
        self.eposta = veri["eposta"]
        self.telefon_num = veri["telefon_num"]
        self.id = veri["id"]
        self.aktif_kiralamalar = veri["aktif_kiralamalar"]


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


