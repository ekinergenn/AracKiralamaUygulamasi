import sys
import os

# matplotlib'e pyside6 kullandırma
os.environ["QT_API"] = "pyside6"

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QVBoxLayout, QWidget, QFrame, QHBoxLayout)

#grafik
class GrafikWidget(FigureCanvas):
    def __init__(self, parent=None):
        # Figür oluşturma
        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.fig.patch.set_facecolor('#F8F9FA')
        super().__init__(self.fig)
        self.verileri_ciz()

    def verileri_ciz(self):
        aylar = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz']
        gelirler = [12000, 15000, 11000, 18000, 22000, 25000]

        self.ax.clear()
        self.ax.bar(aylar, gelirler, color='#2E3A59', width=0.6)

        self.ax.set_title('Aylık Toplam Gelir (TL)', fontsize=10, fontweight='bold', color='#2E3A59')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.tick_params(axis='both', which='major', labelsize=8, colors='#718096')
        self.draw()

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


#ana kısım
class Ui_RaporlarDialog(object):
    def setupUi(self, RaporlarDialog):
        RaporlarDialog.setObjectName(u"RaporlarDialog")
        RaporlarDialog.resize(950, 750)
        RaporlarDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_dikey_layout = QVBoxLayout(RaporlarDialog)
        self.ana_dikey_layout.setContentsMargins(30, 30, 30, 30)
        self.ana_dikey_layout.setSpacing(20)

        self.etiket_sayfa_baslik = QLabel("Performans Analizi")
        self.etiket_sayfa_baslik.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.etiket_sayfa_baslik.setStyleSheet("color: #2E3A59; border-bottom: 2px solid #2E3A59; padding-bottom: 5px;")
        self.ana_dikey_layout.addWidget(self.etiket_sayfa_baslik)

        # ust kısım
        self.kartlar_layout = QHBoxLayout()
        self.kartlar_layout.addWidget(RaporKarti("TOPLAM GELİR", "₺45.250"))
        self.kartlar_layout.addWidget(RaporKarti("AKTİF KİRA", "12 Araç"))
        self.kartlar_layout.addWidget(RaporKarti("POPÜLER", "Tesla M3"))
        self.ana_dikey_layout.addLayout(self.kartlar_layout)

        #grafik kısmı
        self.cerceve_grafik = QFrame(RaporlarDialog)
        self.cerceve_grafik.setStyleSheet("background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.grafik_layout = QVBoxLayout(self.cerceve_grafik)
        self.grafik_layout.setContentsMargins(15, 15, 15, 15)

        self.kanvas = GrafikWidget()
        self.grafik_layout.addWidget(self.kanvas)
        self.ana_dikey_layout.addWidget(self.cerceve_grafik)

#main simdilik var baglı degil
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = QDialog()
    ui = Ui_RaporlarDialog()
    ui.setupUi(pencere)
    pencere.show()
    sys.exit(app.exec())