import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QScrollArea, QVBoxLayout, QWidget, QFrame, QHBoxLayout, QPushButton)

from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class ArabaKartGecmis(QFrame):
    def __init__(self, marka, model, plaka, fiyat, baslangic, bitis, parent=None):
        super().__init__(parent)
        self.setFixedSize(380, 200)  # Tarihler için alanı biraz genişlettik
        self.setStyleSheet("background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")

        self.kart_yatay_layout = QHBoxLayout(self)


        #araba resmi
        self.etiket_arac_resim = QLabel(self)
        self.etiket_arac_resim.setFixedSize(120, 120)
        self.etiket_arac_resim.setStyleSheet("background-color: #F7FAFC; border-radius: 10px; border: none;")

        car_path = os.path.join(BASE_DIR, "..", "icon", "caricon.jpg")
        if os.path.exists(car_path):
            self.etiket_arac_resim.setPixmap(QPixmap(car_path))
        self.etiket_arac_resim.setScaledContents(True)
        self.kart_yatay_layout.addWidget(self.etiket_arac_resim)

        #ozellikler
        self.bilgi_dikey_layout = QVBoxLayout()
        self.etiket_marka = QLabel(f"<b>{marka} {model}</b>")
        self.etiket_marka.setStyleSheet("font-size: 15px; color: #2D3748; border:none;")

        self.etiket_plaka = QLabel(f"Plaka: {plaka}")
        self.etiket_plaka.setStyleSheet("color: #4A5568; border:none; font-size: 13px;")

        #tarihler
        self.etiket_tarih_basla = QLabel(f"Başlangıç: {baslangic}")
        self.etiket_tarih_basla.setStyleSheet("color: #718096; font-size: 12px; border:none;")

        self.etiket_tarih_bitis = QLabel(f"Bitiş: {bitis}")
        self.etiket_tarih_bitis.setStyleSheet("color: #2E3A59; font-weight: bold; font-size: 12px; border:none;")

        self.etiket_fiyat = QLabel(f"Toplam: {fiyat} TL")
        self.etiket_fiyat.setStyleSheet("color: #2E3A59; font-size: 14px; border:none; font-weight: bold;")

        self.bilgi_dikey_layout.addWidget(self.etiket_marka)
        self.bilgi_dikey_layout.addWidget(self.etiket_plaka)
        self.bilgi_dikey_layout.addWidget(self.etiket_tarih_basla)
        self.bilgi_dikey_layout.addWidget(self.etiket_tarih_bitis)
        self.bilgi_dikey_layout.addStretch()
        self.bilgi_dikey_layout.addWidget(self.etiket_fiyat)

        self.kart_yatay_layout.addLayout(self.bilgi_dikey_layout)


#ana kısım
class Ui_KiraGecmisiDialog(object):
    def __init__(self,app):
        self.app = app
    def setupUi(self, KiraGecmisiDialog):
        KiraGecmisiDialog.setObjectName(u"KiraGecmisiDialog")
        KiraGecmisiDialog.resize(900, 750)
        KiraGecmisiDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_izgara_layout = QGridLayout(KiraGecmisiDialog)
        self.ana_izgara_layout.setContentsMargins(20, 20, 20, 20)
        self.ana_izgara_layout.setSpacing(20)

        baslik_font = QFont("Segoe UI", 14, QFont.Bold)
        

        #kiraladıklarım gecmisi (sol)
        self.etiket_sol_baslik = QLabel("Geçmişte Kiraladıklarım")
        self.etiket_sol_baslik.setFont(baslik_font)
        self.etiket_sol_baslik.setStyleSheet("color: #2E3A59; border-bottom: 2px solid #2E3A59; padding-bottom: 5px;")
        self.ana_izgara_layout.addWidget(self.etiket_sol_baslik, 0, 0)

        self.kaydirma_sol = QScrollArea(KiraGecmisiDialog)
        self.kaydirma_sol.setWidgetResizable(True)
        self.kaydirma_sol.setStyleSheet("border: none; background-color: transparent;")

        self.icerik_sol = QWidget()
        self.layout_sol = QVBoxLayout(self.icerik_sol)
        self.layout_sol.setSpacing(15)
        self.layout_sol.setAlignment(Qt.AlignTop)

      
        self.kaydirma_sol.setWidget(self.icerik_sol)
        self.ana_izgara_layout.addWidget(self.kaydirma_sol, 1, 0)

        #kiraya verdiklerim gecmisi(sag)
        self.etiket_sag_baslik = QLabel("Geçmişte Kiraya Verdiklerim")
        self.etiket_sag_baslik.setFont(baslik_font)
        self.etiket_sag_baslik.setStyleSheet("color: #2E3A59; border-bottom: 2px solid #2E3A59; padding-bottom: 5px;")
        self.ana_izgara_layout.addWidget(self.etiket_sag_baslik, 0, 1)

        self.kaydirma_sag = QScrollArea(KiraGecmisiDialog)
        self.kaydirma_sag.setWidgetResizable(True)
        self.kaydirma_sag.setStyleSheet("border: none; background-color: transparent;")

        self.icerik_sag = QWidget()
        self.layout_sag = QVBoxLayout(self.icerik_sag)
        self.layout_sag.setSpacing(15)
        self.layout_sag.setAlignment(Qt.AlignTop)

        #ornek
        #self.refresh()

        self.kaydirma_sag.setWidget(self.icerik_sag)
        self.ana_izgara_layout.addWidget(self.kaydirma_sag, 1, 1)

    def refresh(self):
        self.clear_layout(self.layout_sol)
        self.clear_layout(self.layout_sag)
        for a in self.app.kiralamalar:
            if a.gecmis and a.kullanici == self.app.aktif_hesap.id:
                arac = self.app.araba_id_arama(a.araba)
                self.layout_sol.addWidget(ArabaKartGecmis(arac.marka, arac.model,arac.plaka,a.ucret,str(a.bas_tarih),str(a.bit_tarih)))
            elif a.gecmis and self.app.araba_sahip_arama(a.araba) == self.app.aktif_hesap:
                arac = self.app.araba_id_arama(a.araba)
                self.layout_sag.addWidget(ArabaKartGecmis(arac.marka, arac.model,arac.plaka,a.ucret,str(a.bas_tarih),str(a.bit_tarih)))


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
