import sys
import os
os.environ["QT_API"] = "pyside6"

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QVBoxLayout, QWidget, QFrame, QHBoxLayout)

#grafikler
class GrafikWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4), dpi=100)
        self.fig.patch.set_facecolor('#F8F9FA')
        super().__init__(self.fig)
        self.verileri_ciz()

    def verileri_ciz(self):
        #cubuk grafik
        aylar = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz']
        gelirler = [12000, 15000, 11000, 18000, 22000, 25000]

        self.ax1.clear()
        self.ax1.bar(aylar, gelirler, color='#2E3A59', width=0.6)
        self.ax1.set_title('Aylık Toplam Gelir (TL)', fontsize=10, fontweight='bold', color='#2E3A59')
        self.ax1.spines['top'].set_visible(False)
        self.ax1.spines['right'].set_visible(False)
        self.ax1.tick_params(axis='both', which='major', labelsize=8, colors='#718096')

        #pasta grafik
        markalar = ['Tesla', 'BMW', 'Audi', 'Mercedes', 'Diğer']
        paylar = [35, 25, 15, 15, 10]
        renkler = ['#2E3A59', '#4A5568', '#718096', '#A0AEC0', '#CBD5E0']  # Lacivert tonları

        self.ax2.clear()
        #dilimler
        self.ax2.pie(paylar, labels=markalar, autopct='%1.1f%%', startangle=140,
                     colors=renkler, textprops={'fontsize': 8, 'color': '#2E3A59'})
        self.ax2.set_title('Araç Kullanım Dağılımı', fontsize=10, fontweight='bold', color='#2E3A59')

        self.fig.tight_layout()  # Grafikler arası boşluğu ayarla
        self.draw()

#rapor karti
class RaporKarti(QFrame):
    def __init__(self, baslik, deger, parent=None):
        super().__init__(parent)
        self.setFixedSize(260, 120)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: 1px solid #E2E8F0;
            }
            QLabel { border: none; }
        """)
        layout = QVBoxLayout(self)
        self.lbl_baslik = QLabel(baslik)
        self.lbl_baslik.setStyleSheet("color: #718096; font-size: 11px; font-weight: bold;")
        self.lbl_deger = QLabel(deger)
        self.lbl_deger.setStyleSheet("color: #2E3A59; font-size: 20px; font-weight: bold;")
        layout.addWidget(self.lbl_baslik)
        layout.addStretch()
        layout.addWidget(self.lbl_deger)

class Ui_RaporlarDialog(object):
    def setupUi(self, RaporlarDialog):
        RaporlarDialog.setObjectName(u"RaporlarDialog")
        RaporlarDialog.resize(1000, 750)  # Pasta grafiği için genişliği biraz artırdık
        RaporlarDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_dikey_layout = QVBoxLayout(RaporlarDialog)
        self.ana_dikey_layout.setContentsMargins(30, 30, 30, 30)
        self.ana_dikey_layout.setSpacing(25)

        #baslık
        self.etiket_sayfa_baslik = QLabel("Raporlar")
        self.etiket_sayfa_baslik.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.etiket_sayfa_baslik.setStyleSheet("color: #2E3A59; border-bottom: 2px solid #2E3A59; padding-bottom: 5px;")
        self.ana_dikey_layout.addWidget(self.etiket_sayfa_baslik)

        #ust kısım
        self.kartlar_layout = QHBoxLayout()
        self.kartlar_layout.setSpacing(20)
        self.kartlar_layout.addWidget(RaporKarti("TOPLAM GELİR", "₺45.250"))
        self.kartlar_layout.addWidget(RaporKarti("KİRADAKİ ARAÇLAR", "12 Araç"))
        self.kartlar_layout.addWidget(RaporKarti("EN ÇOK KİRALANAN", "Tesla M3"))
        self.ana_dikey_layout.addLayout(self.kartlar_layout)

        #grafik
        self.cerceve_grafik = QFrame(RaporlarDialog)
        self.cerceve_grafik.setStyleSheet("background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.grafik_layout = QVBoxLayout(self.cerceve_grafik)
        self.grafik_layout.setContentsMargins(15, 15, 15, 15)

        self.kanvas = GrafikWidget()
        self.grafik_layout.addWidget(self.kanvas)
        self.ana_dikey_layout.addWidget(self.cerceve_grafik)

        self.ana_dikey_layout.addStretch()