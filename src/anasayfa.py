import sys
import os  #Fotoğraflara ulaşmak için
from PySide6.QtCore import (QCoreApplication, QSize, QRect, Qt, QMetaObject)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QScrollArea, QVBoxLayout, QWidget, QFrame)

#Python dosyasının adresi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        Dialog.resize(900, 750)
        Dialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_dikey_layout = QVBoxLayout(Dialog)
        self.ana_dikey_layout.setSpacing(20)
        self.ana_dikey_layout.setContentsMargins(20, 20, 20, 20)

        #Üst Kısım
        self.ust_bar_cerceve = QFrame(Dialog)
        self.ust_bar_cerceve.setStyleSheet(u"background-color: #2E3A59; border-radius: 15px;")
        self.ust_yatay_layout = QHBoxLayout(self.ust_bar_cerceve)
        self.ust_yatay_layout.setContentsMargins(15, 10, 15, 10)

        #PP
        self.etiket_profil_resim = QLabel(self.ust_bar_cerceve)
        self.etiket_profil_resim.setFixedSize(50, 50)
        self.etiket_profil_resim.setStyleSheet("border-radius: 25px; background-color: #4A5568; border: 2px solid white;")

        #PP adresi
        profile_path = os.path.join(BASE_DIR, "profilepp.png")
        if os.path.exists(profile_path):
            self.etiket_profil_resim.setPixmap(QPixmap(profile_path))

        self.etiket_profil_resim.setScaledContents(True)
        self.ust_yatay_layout.addWidget(self.etiket_profil_resim)

        #Mail kısmı
        self.etiket_mail = QLabel(self.ust_bar_cerceve)
        self.etiket_mail.setText("ornek@gmail.com")
        self.etiket_mail.setStyleSheet("color: white; font-weight: bold; font-size: 14px; padding-left: 10px;")
        self.ust_yatay_layout.addWidget(self.etiket_mail)

        self.ust_yatay_layout.addStretch()

        #Arama
        self.arama_satiri = QLineEdit(self.ust_bar_cerceve)
        self.arama_satiri.setPlaceholderText("Araç ara...")
        self.arama_satiri.setFixedWidth(250)
        self.arama_satiri.setStyleSheet("border-radius: 10px; padding: 8px; background-color: white; color: #2E3A59;")
        self.ust_yatay_layout.addWidget(self.arama_satiri)

        #Filtrele ve Sırala
        combo_stil = "background-color: #4A5568; color: white; border-radius: 8px; padding: 5px; min-width: 110px;"
        self.combo_sirala = QComboBox(self.ust_bar_cerceve)
        self.combo_sirala.addItems(["Fiyat: Artan", "Fiyat: Azalan"])
        self.combo_sirala.setStyleSheet(combo_stil)
        self.combo_filtrele = QComboBox(self.ust_bar_cerceve)
        self.combo_filtrele.addItems(["Hepsi", "Müsait", "Kirada"])
        self.combo_filtrele.setStyleSheet(combo_stil)

        self.ust_yatay_layout.addWidget(self.combo_sirala)
        self.ust_yatay_layout.addWidget(self.combo_filtrele)

        self.ana_dikey_layout.addWidget(self.ust_bar_cerceve)

        #Ana Kısım
        self.kaydirma_alani = QScrollArea(Dialog)
        self.kaydirma_alani.setWidgetResizable(True)
        self.kaydirma_alani.setStyleSheet("border: None; background-color: transparent;")

        self.kaydirma_icerik_widget = QWidget()
        self.izgara_layout_araclar = QGridLayout(self.kaydirma_icerik_widget)
        self.izgara_layout_araclar.setSpacing(20)

        #Örnek Araçlar
        self.arac_karti_ekle(0, 0, "Tesla Model 3", "2023", "34 ABC 123", "2500 TL")
        self.arac_karti_ekle(0, 1, "BMW i4", "2024", "34 DEF 456", "3200 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")

        self.kaydirma_alani.setWidget(self.kaydirma_icerik_widget)
        self.ana_dikey_layout.addWidget(self.kaydirma_alani)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def arac_karti_ekle(self, satir, sutun, marka, model, plaka, fiyat):
        kart_cerceve = QFrame()
        kart_cerceve.setFixedSize(380, 200)
        kart_cerceve.setStyleSheet("background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")

        kart_yatay_layout = QHBoxLayout(kart_cerceve)

        #Araba Resmi
        etiket_arac_resim = QLabel(kart_cerceve)
        etiket_arac_resim.setFixedSize(140, 140)
        etiket_arac_resim.setStyleSheet("background-color: #F7FAFC; border-radius: 10px; border: none;")

        #Araba Resmi Adresi
        car_path = os.path.join(BASE_DIR, "caricon.jpg")
        if os.path.exists(car_path):
            etiket_arac_resim.setPixmap(QPixmap(car_path))

        etiket_arac_resim.setScaledContents(True)
        kart_yatay_layout.addWidget(etiket_arac_resim)

        #Bilgiler
        bilgi_dikey_layout = QVBoxLayout()
        etiket_marka = QLabel(f"<b>{marka}</b>")
        etiket_marka.setStyleSheet("font-size: 16px; color: #2D3748; border:none;")
        etiket_model = QLabel(f"Model: {model}")
        etiket_model.setStyleSheet("color: #4A5568; border:none;")
        etiket_plaka = QLabel(f"Plaka: {plaka}")
        etiket_plaka.setStyleSheet("color: #4A5568; border:none;")
        etiket_fiyat = QLabel(f"<b>{fiyat} / Günlük</b>")
        etiket_fiyat.setStyleSheet("color: #2E3A59; font-size: 14px; border:none;")

        buton_goruntule = QPushButton("Görüntüle")
        buton_goruntule.setCursor(Qt.PointingHandCursor)
        buton_goruntule.setStyleSheet(
            "background-color: #2E3A59; color: white; border-radius: 8px; padding: 8px; font-weight: bold;")

        bilgi_dikey_layout.addWidget(etiket_marka)
        bilgi_dikey_layout.addWidget(etiket_model)
        bilgi_dikey_layout.addWidget(etiket_plaka)
        bilgi_dikey_layout.addWidget(etiket_fiyat)
        bilgi_dikey_layout.addStretch()
        bilgi_dikey_layout.addWidget(buton_goruntule)

        kart_yatay_layout.addLayout(bilgi_dikey_layout)
        self.izgara_layout_araclar.addWidget(kart_cerceve, satir, sutun)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Araç Kiralama Paneli")

#Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())