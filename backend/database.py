
import json

class database:
    def __init__(self,dosya:str):
        self.dosya = dosya

    def verileri_yazdir(self,veriler:dict)->int:
        with open(self.dosya, "w", encoding="utf-8") as f:
            json.dump(veriler, f, ensure_ascii=False, indent=4)
        return 1
    
    def verileri_oku(self) -> dict:
        with open(self.dosya, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data