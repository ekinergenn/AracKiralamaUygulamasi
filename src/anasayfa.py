import sys
import os
from PySide6.QtCore import (QCoreApplication, QSize, QRect, Qt, QMetaObject)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QScrollArea, QVBoxLayout, QWidget, QFrame, QStackedWidget, QSizePolicy, QMessageBox)

from src.araba_kart import araba_kart
from src.arababilgi import AracDetayWidget
from src.flowlayout import FlowLayout
from src.giris import ModernLoginDialog
from src.kayitol import RegisterDialog
from src.profilsayfası import ProfilWidget

# Python dosyasının adresi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        self.ana_layout = QVBoxLayout(Dialog)
        self.ana_layout.setSpacing(0)
        self.ana_layout.setContentsMargins(0, 0, 0, 0)

        self.ana_stack = QStackedWidget()
        self.ana_ekran = QWidget()
        self.giris_ekran = ModernLoginDialog(parent=self.ana_stack)
        self.kayitol_ekran = RegisterDialog()

        Dialog.resize(900, 750)
        Dialog.setStyleSheet(u"background-color: #F8F9FA;")
        self.ana_dikey_layout = QVBoxLayout(self.ana_ekran)
        self.ana_dikey_layout.setSpacing(20)
        self.ana_dikey_layout.setContentsMargins(0, 0, 0, 0)

        # Üst Kısım
        self.ust_bar_cerceve = QFrame(self.ana_ekran)
        self.ust_bar_cerceve.setStyleSheet(u"background-color: #2E3A59;")
        self.ust_yatay_layout = QHBoxLayout(self.ust_bar_cerceve)
        self.ust_yatay_layout.setContentsMargins(15, 10, 15, 10)

        # PP
        self.etiket_profil_resim = QPushButton(self.ust_bar_cerceve)  # QPushButton olarak değiştir
        self.etiket_profil_resim.setFixedSize(50, 50)
        self.etiket_profil_resim.setStyleSheet(
            "border-radius: 25px; background-color: #4A5568; border: 2px solid white;")
        self.etiket_profil_resim.setCursor(Qt.PointingHandCursor)
        self.etiket_profil_resim.setFlat(True)  # Arka planı şeffaf yap

        # PP adresi
        profile_path = os.path.join(BASE_DIR, "..", "icon", "profilepp.png")
        if os.path.exists(profile_path):
            icon = QPixmap(profile_path)
            self.etiket_profil_resim.setIcon(icon)
            self.etiket_profil_resim.setIconSize(QSize(46, 46))

        self.ust_yatay_layout.addWidget(self.etiket_profil_resim)

        # Mail kısmı
        self.etiket_mail = QPushButton(self.ust_bar_cerceve)  # QPushButton olarak değiştir
        self.etiket_mail.setText("ornek@gmail.com")
        self.etiket_mail.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white; 
                font-weight: bold; 
                font-size: 14px; 
                padding-left: 10px;
                border: none;
                text-align: left;
            }
            QPushButton:hover {
                color: #CBD5E0;
            }
        """)
        self.etiket_mail.setCursor(Qt.PointingHandCursor)
        self.etiket_mail.setFlat(True)
        self.ust_yatay_layout.addWidget(self.etiket_mail)

        self.ust_yatay_layout.addStretch()

        # Arama
        self.arama_satiri = QLineEdit(self.ust_bar_cerceve)
        self.arama_satiri.setPlaceholderText("Araç ara...")
        self.arama_satiri.setFixedWidth(250)
        self.arama_satiri.setStyleSheet("border-radius: 10px; padding: 8px; background-color: white; color: #2E3A59;")
        self.ust_yatay_layout.addWidget(self.arama_satiri)

        # Filtrele ve Sırala
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

        self.stack = QStackedWidget()
        self.page1 = QWidget()
        self.page2 = QWidget()

        # Scroll Area
        self.kaydirma_alani = QScrollArea()
        self.kaydirma_alani.setWidgetResizable(True)
        self.kaydirma_alani.setStyleSheet("border: none; background-color: transparent;")

        self.kaydirma_icerik_widget = QWidget()
        self.izgara_layout_araclar = FlowLayout(self.kaydirma_icerik_widget)
        self.izgara_layout_araclar.setContentsMargins(10, 0, 10, 0)

        # Kartlar
        self.arac_karti_ekle(0, 0, "Tesla Model 3", "2023", "34 ABC 123", "2500 TL", 1)
        self.arac_karti_ekle(0, 1, "BMW i4", "2024", "34 DEF 456", "3200 TL", 2)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 3)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 4)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 5)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 6)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 7)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 8)
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL", 9)

        self.kaydirma_alani.setWidget(self.kaydirma_icerik_widget)

        page1_layout = QVBoxLayout(self.page1)
        page1_layout.setContentsMargins(10, 0, 0, 0)
        page1_layout.addWidget(self.kaydirma_alani)

        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        self.ana_dikey_layout.addWidget(self.stack)
        self.stack.setCurrentIndex(0)

        # Profil sayfasını oluştur
        self.profil_ekran_widget = ProfilWidget()
        self.profil_ui = self.profil_ekran_widget
        self.profil_ui.ana_sayfa_istem_sinyali.connect(lambda: self.ana_stack.setCurrentWidget(self.ana_ekran))

        self.ana_stack.addWidget(self.profil_ekran_widget)
        self.ana_stack.addWidget(self.ana_ekran)
        self.ana_stack.addWidget(self.giris_ekran)
        self.ana_stack.addWidget(self.kayitol_ekran)

        self.ana_stack.setCurrentWidget(self.giris_ekran)

        self.ana_layout.addWidget(self.ana_stack)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        # Tıklama bağlantıları
        self.giris_ekran.buton_giris_yap.clicked.connect(self.giris_yap_baglanti)
        self.giris_ekran.buton_kayit_ol.clicked.connect(lambda: self.ana_stack.setCurrentWidget(self.kayitol_ekran))

        # Kayıt ol sayfasından girişe dönüş
        self.kayitol_ekran.etiket_giris_link.mousePressEvent = lambda e: (
            self.ana_stack.setCurrentWidget(self.giris_ekran) if e.button() == Qt.LeftButton else None
        )

        # Kayıt ol butonu
        self.kayitol_ekran.buton_kayit_ol.clicked.connect(lambda: self.ana_stack.setCurrentWidget(self.ana_ekran))

        # Profil resmi ve mail tıklama olayları
        self.etiket_profil_resim.clicked.connect(self.profil_sayfasina_gec)
        self.etiket_mail.clicked.connect(self.profil_sayfasina_gec)

    def profil_sayfasina_gec(self):
        # Giriş yapan kullanıcının mailini profil sayfasına aktar
        guncel_mail = self.etiket_mail.text()
        self.profil_ui.etiket_kullanici_mail.setText(guncel_mail)

        # Ekranı değiştir
        self.ana_stack.setCurrentWidget(self.profil_ekran_widget)

    def arac_karti_ekle(self, satir, sutun, marka, model, plaka, fiyat, id):
        araba = araba_kart(marka=marka, model=model, plaka=plaka, fiyat=fiyat, id=id)
        araba.buton_goruntule.clicked.connect(self.arac_kart_tiklanma)
        self.izgara_layout_araclar.addWidget(araba)

    def arac_kart_tiklanma(self):
        self.stack.removeWidget(self.page2)
        self.page2.deleteLater()

        self.page2 = QWidget()
        page2_layout = QVBoxLayout(self.page2)
        page2_layout.setContentsMargins(0, 0, 0, 0)

        araba_bilgi = AracDetayWidget()
        araba_bilgi.arac_bilgilerini_guncelle(
            marka="Tesla",
            model="Model 3",
            plaka="34 ABC 123",
            ucret="2.500",
            durum=True
        )
        araba_bilgi.geri_don_sinyali.connect(self.anasayfaya_don)

        page2_layout.addWidget(araba_bilgi)
        self.stack.addWidget(self.page2)
        self.stack.setCurrentWidget(self.page2)

    def anasayfaya_don(self):
        self.stack.setCurrentWidget(self.page1)

    def giris_yap_baglanti(self):
        if not self.giris_ekran.mail_giris.text().strip():
            QMessageBox.warning(
                self.giris_ekran,
                "Giriş Hatası",
                "Lütfen e-posta alanını doldurunuz."
            )
        elif not self.giris_ekran.sifre_giris.text().strip():
            QMessageBox.warning(
                self.giris_ekran,
                "Giriş Hatası",
                "Lütfen şifre alanını doldurunuz."
            )
        else:
            self.ana_stack.setCurrentWidget(self.ana_ekran)
            self.etiket_mail.setText(self.giris_ekran.mail_giris.text())

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Araç Kiralama Paneli")