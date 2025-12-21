

class araba:
    def __init__(self,plaka:str,marka:str,model:str,ucret:float,durum:bool,id:int):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.ucret = ucret
        self.durum = durum
        self.id = id

    @classmethod
    def from_dict(cls, veri: dict):
        return cls(
            veri["plaka"],
            veri["marka"],
            veri["model"],
            veri["ucret"],
            veri["durum"],
            veri["id"]
        )

    def sozluk_veri(self) -> dict:
        veri = {
            "plaka":"",
            "marka":"",
            "model":"",
            "ucret":0,
            "durum":False,
            "id":0    
        }

        veri["plaka"] = self.plaka
        veri["marka"] = self.marka
        veri["model"] = self.model
        veri["ucret"] = self.ucret
        veri["durum"] = self.durum
        veri["id"] = self.id
        return veri
