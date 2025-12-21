import sys
import os
from PySide6.QtCore import (QCoreApplication, QSize, Qt, QMetaObject, QEvent)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
                               QLabel, QPushButton, QScrollArea, QVBoxLayout,
                               QWidget, QFrame)

from araba_kart import araba_kart


class Ui_AracYonetim(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.resize(900, 700)
        Dialog.setMinimumSize(420, 500)
        Dialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_dikey_layout = QVBoxLayout(Dialog)
        self.ana_dikey_layout.setContentsMargins(20, 20, 20, 20)
        self.ana_dikey_layout.setSpacing(15)

        #arac ekle butonu
        self.ust_cerceve = QFrame(Dialog)
        self.ust_cerceve.setFixedHeight(60)
        self.ust_cerceve.setStyleSheet(u"background-color: #2E3A59; border-radius: 12px;")
        self.ust_layout = QHBoxLayout(self.ust_cerceve)

        self.buton_arac_ekle = QPushButton(" + Yeni Araç Ekle", self.ust_cerceve)
        self.buton_arac_ekle.setFixedSize(160, 35)
        self.buton_arac_ekle.setCursor(Qt.PointingHandCursor)
        self.buton_arac_ekle.setStyleSheet(
            u"background-color: white; color: #2E3A59; border-radius: 8px; font-weight: bold; border: none;")
        self.ust_layout.addWidget(self.buton_arac_ekle)
        self.ust_layout.addStretch()

        self.ana_dikey_layout.addWidget(self.ust_cerceve)

        #mevcut araclar
        self.kaydirma_alani = QScrollArea(Dialog)
        self.kaydirma_alani.setWidgetResizable(True)
        self.kaydirma_alani.setStyleSheet(u"border: none; background-color: transparent;")

        self.icerik_widget = QWidget()
        self.icerik_izgarasi = QGridLayout(self.icerik_widget)
        self.icerik_izgarasi.setSpacing(20)
        self.icerik_izgarasi.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Kartları sola ve üste yasla

        self.kaydirma_alani.setWidget(self.icerik_widget)
        self.ana_dikey_layout.addWidget(self.kaydirma_alani)

        #ornek
        self.kartlar = []
        self.ornek_araclari_olustur()

        Dialog.installEventFilter(Dialog)
        self.ana_pencere = Dialog

        self.retranslateUi(Dialog)

    def ornek_araclari_olustur(self):
        veriler = [
            ("Tesla", "Model 3", "34 ABC 123", "2500 TL"),
            ("BMW", "i4", "34 DEF 456", "3200 TL"),
            ("Audi", "A4", "34 GHI 789", "1800 TL"),
            ("Mercedes", "C200", "34 JKL 101", "2900 TL"),
            ("Tesla", "Model Y", "34 XYZ 99", "2700 TL")
        ]
        for v in veriler:
            self.kartlar.append(araba_kart(v[0], v[1], v[2], v[3]))

    def kartlari_duzenle(self):
        genislik = self.kaydirma_alani.width()
        kart_genisligi = 400

        sutun_sayisi = max(1, genislik // kart_genisligi)

        for i in reversed(range(self.icerik_izgarasi.count())):
            self.icerik_izgarasi.itemAt(i).widget().setParent(None)

        for sira, kart in enumerate(self.kartlar):
            satir = sira // sutun_sayisi
            sutun = sira % sutun_sayisi
            self.icerik_izgarasi.addWidget(kart, satir, sutun)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Araç Yönetimi")


#main (simdilik baglı olmadıgı icin var sonra silinecek
class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AracYonetim()
        self.ui.setupUi(self)

    def eventFilter(self, source, event):
        # Pencere boyutu değiştiğinde kartları tekrar düzenle
        if event.type() == QEvent.Resize:
            self.ui.kartlari_duzenle()
        return super().eventFilter(source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())