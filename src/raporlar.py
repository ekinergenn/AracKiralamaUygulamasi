import sys
import os
from datetime import date
os.environ["QT_API"] = "pyside6"

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import (Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QVBoxLayout, QFrame, QHBoxLayout, QDialog)

class GrafikWidget(FigureCanvas):
    def __init__(self, data, admin_mi, parent=None):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(12, 5), dpi=100)
        self.fig.patch.set_facecolor('#F8F9FA')
        super().__init__(self.fig)
        self.verileri_ciz(data, admin_mi)

    def verileri_ciz(self, data, admin_mi):
        # Renk ve başlık seçimi
        tema_rengi = '#2E3A59' if admin_mi else '#4C51BF'
        baslik1 = 'Aylık Toplam Kazanç (TL)' if admin_mi else 'Aylık Toplam Harcama (TL)'
        baslik2 = 'Filo Marka Dağılımı' if admin_mi else 'Tercih Ettiğim Markalar'

        # 1. Çubuk Grafik (Aylık Durum)
        aylar = list(data['aylik_liste'].keys())
        degerler = list(data['aylik_liste'].values())
        self.ax1.clear()
        if any(degerler):
            self.ax1.bar(aylar, degerler, color=tema_rengi, width=0.6)
        self.ax1.set_title(baslik1, fontsize=10, fontweight='bold', color='#2E3A59')
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)
        self.ax1.tick_params(axis='both', labelsize=8)

        # 2. Pasta Grafik (Marka Analizi)
        markalar = list(data['marka_analizi'].keys())
        paylar = list(data['marka_analizi'].values())
        renk_paleti = ['#2E3A59', '#4A5568', '#718096', '#A0AEC0'] if admin_mi else ['#4C51BF', '#667EEA', '#7F9CF5', '#A3BFFA']

        self.ax2.clear()
        if markalar:
            self.ax2.pie(paylar, labels=markalar, autopct='%1.1f%%', startangle=140,
                         colors=renk_paleti, textprops={'fontsize': 8})
        self.ax2.set_title(baslik2, fontsize=10, fontweight='bold', color='#2E3A59')

        self.fig.tight_layout()
        self.draw()

class RaporKarti(QFrame):
    def __init__(self, baslik, deger, renk, parent=None):
        super().__init__(parent)
        self.setFixedSize(280, 100)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border-radius: 12px;
                border: 1px solid #E2E8F0;
            }}
            QLabel {{ border: none; background: transparent; }}
        """)
        layout = QVBoxLayout(self)
        self.lbl_baslik = QLabel(baslik.upper())
        self.lbl_baslik.setStyleSheet("color: #718096; font-size: 10px; font-weight: bold;")
        self.lbl_deger = QLabel(str(deger))
        self.lbl_deger.setStyleSheet(f"color: {renk}; font-size: 18px; font-weight: bold;")
        layout.addWidget(self.lbl_baslik)
        layout.addWidget(self.lbl_deger)

class Ui_RaporlarDialog(object):
    def __init__(self, app):
        self.app = app 

    def setupUi(self, RaporlarDialog):
        RaporlarDialog.setObjectName(u"RaporlarDialog")
        RaporlarDialog.resize(1100, 700)
        RaporlarDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_dikey_layout = QVBoxLayout(RaporlarDialog)
        self.ana_dikey_layout.setContentsMargins(40, 40, 40, 40)
        self.ana_dikey_layout.setSpacing(30)

        # Veriyi admin_bool'a göre hazırla
        rapor_verisi = self.data_isleme_merkezi()
        admin_mi = self.app.admin_bool
        tema_rengi = '#2E3A59' if admin_mi else '#4C51BF'

        # Başlık Bölümü
        baslik_metni = "Yönetim Paneli Finansal Raporu" if admin_mi else f"Kullanıcı Özeti: {self.app.aktif_hesap.isim}"
        self.etiket_sayfa_baslik = QLabel(baslik_metni)
        self.etiket_sayfa_baslik.setFont(QFont("Segoe UI", 18, QFont.Bold))
        self.etiket_sayfa_baslik.setStyleSheet(f"color: {tema_rengi};")
        self.ana_dikey_layout.addWidget(self.etiket_sayfa_baslik)

        # Kartlar Bölümü
        self.kartlar_layout = QHBoxLayout()
        if admin_mi:
            self.kartlar_layout.addWidget(RaporKarti("Toplam Tahsilat", f"₺{rapor_verisi['ana_toplam']:,}", tema_rengi))
            self.kartlar_layout.addWidget(RaporKarti("Kiradaki Araçlarınız", f"{rapor_verisi['aktif_adet']} Adet", tema_rengi))
            self.kartlar_layout.addWidget(RaporKarti("Toplam Filo Gücü", f"{len(self.app.aktif_hesap.sahip_arabalar)} Araç", tema_rengi)) #
        else:
            self.kartlar_layout.addWidget(RaporKarti("Toplam Harcamam", f"₺{rapor_verisi['ana_toplam']:,}", tema_rengi))
            self.kartlar_layout.addWidget(RaporKarti("Toplam Kiralama", f"{rapor_verisi['aktif_adet']} Kez", tema_rengi))
            self.kartlar_layout.addWidget(RaporKarti("Aktif Kiralamalarım", f"{len(self.app.aktif_hesap.aktif_kiralamalar)} Adet", tema_rengi)) #
        
        self.ana_dikey_layout.addLayout(self.kartlar_layout)

        # Grafik Alanı
        self.cerceve_grafik = QFrame()
        self.cerceve_grafik.setStyleSheet("background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.grafik_layout = QVBoxLayout(self.cerceve_grafik)
        self.kanvas = GrafikWidget(rapor_verisi, admin_mi)
        self.grafik_layout.addWidget(self.kanvas)
        self.ana_dikey_layout.addWidget(self.cerceve_grafik)

    def data_isleme_merkezi(self):
        # Ortak başlangıç değerleri
        ana_toplam = 0
        aktif_adet = 0
        marka_analizi = {}
        aylik_liste = {"Oca":0, "Şub":0, "Mar":0, "Nis":0, "May":0, "Haz":0, 
                        "Tem":0, "Ağu":0, "Eyl":0, "Eki":0, "Kas":0, "Ara":0}
        ay_isimleri = list(aylik_liste.keys())

        admin_mi = self.app.admin_bool #
        aktif_id = self.app.aktif_hesap.id #

        # Kiralamaları Tara
        for k in self.app.kiralamalar:
            islem_dahil_mi = False
            
            if admin_mi:
                # Admin ise: Kiralama adminin sahip olduğu araçlardan birine mi ait?
                if k.araba in self.app.aktif_hesap.sahip_arabalar:
                    islem_dahil_mi = True
                    if not k.gecmis: aktif_adet += 1 #
            else:
                # Kullanıcı ise: Kiralama bu kullanıcıya mı ait?
                if k.kullanici == aktif_id:
                    islem_dahil_mi = True
                    aktif_adet += 1 # Toplam işlem sayısı olarak kullanıyoruz

            if islem_dahil_mi:
                ana_toplam += k.ucret #
                ay_adi = ay_isimleri[k.bas_tarih.month - 1] #
                aylik_liste[ay_adi] += k.ucret
                
                arac = self.app.araba_id_arama(k.araba) #
                if arac:
                    marka_analizi[arac.marka] = marka_analizi.get(arac.marka, 0) + 1

        return {
            "ana_toplam": ana_toplam,
            "aktif_adet": aktif_adet,
            "marka_analizi": marka_analizi,
            "aylik_liste": aylik_liste
        }