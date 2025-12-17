import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget, QFrame)

# Dosya yolları için
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Ui_ProfilSekmesi(object):
    def setupUi(self, ProfilSekmesi):
        if not ProfilSekmesi.objectName():
            ProfilSekmesi.setObjectName(u"ProfilSekmesi")

        ProfilSekmesi.resize(1000, 750)
        ProfilSekmesi.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_izgara_layout = QGridLayout(ProfilSekmesi)
        self.ana_izgara_layout.setSpacing(0)
        self.ana_izgara_layout.setContentsMargins(0, 0, 0, 0)

        # Menü Paneli
        self.sol_menu_cerceve = QFrame(ProfilSekmesi)
        self.sol_menu_cerceve.setFixedWidth(250)
        self.sol_menu_cerceve.setStyleSheet(u"background-color: #2E3A59; border: none;")

        self.menu_dikey_layout = QVBoxLayout(self.sol_menu_cerceve)
        self.menu_dikey_layout.setContentsMargins(20, 40, 20, 20)
        self.menu_dikey_layout.setSpacing(15)

        # PP
        self.etiket_profil_resim = QLabel(self.sol_menu_cerceve)
        self.etiket_profil_resim.setFixedSize(100, 100)
        self.etiket_profil_resim.setAlignment(Qt.AlignCenter)
        self.etiket_profil_resim.setStyleSheet(
            u"border-radius: 50px; border: 3px solid white; background-color: #4A5568;")

        profil_yolu = os.path.join(BASE_DIR, "profilepp.png")
        if os.path.exists(profil_yolu):
            self.etiket_profil_resim.setPixmap(QPixmap(profil_yolu))
        self.etiket_profil_resim.setScaledContents(True)

        self.menu_dikey_layout.addWidget(self.etiket_profil_resim, 0, Qt.AlignCenter)

        # Kullanıcı Bilgisi
        self.etiket_kullanici_mail = QLabel(self.sol_menu_cerceve)
        self.etiket_kullanici_mail.setText("ornek@gmail.com")
        self.etiket_kullanici_mail.setStyleSheet(u"color: white; font-weight: bold; font-size: 13px;")
        self.etiket_kullanici_mail.setAlignment(Qt.AlignCenter)
        self.menu_dikey_layout.addWidget(self.etiket_kullanici_mail)

        self.menu_dikey_layout.addSpacing(30)

        # Profil Menü Butonları
        buton_stili = u"""
            QPushButton {
                background-color: transparent;
                color: #E2E8F0;
                border-radius: 8px;
                padding: 12px;
                text-align: left;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #4A5568;
                color: white;
            }
            QPushButton:pressed {
                background-color: #1A202C;
            }
        """

        self.buton_ana_sayfa = QPushButton("Ana Sayfa", self.sol_menu_cerceve)
        self.buton_arac_ekle = QPushButton("Araç Düzenle/Ekle", self.sol_menu_cerceve)
        self.buton_aktif_kiralar = QPushButton("Aktif Kiralar", self.sol_menu_cerceve)
        self.buton_gecmis_kiralar = QPushButton("Geçmiş Kiralar", self.sol_menu_cerceve)
        self.buton_raporlar = QPushButton("Raporlar", self.sol_menu_cerceve)

        self.menu_butonlari = [
            self.buton_ana_sayfa, self.buton_arac_ekle,
            self.buton_aktif_kiralar, self.buton_gecmis_kiralar, self.buton_raporlar
        ]

        for buton in self.menu_butonlari:
            buton.setStyleSheet(buton_stili)
            buton.setCursor(Qt.PointingHandCursor)
            self.menu_dikey_layout.addWidget(buton)

        self.menu_dikey_layout.addStretch()

        self.ana_izgara_layout.addWidget(self.sol_menu_cerceve, 0, 0, 1, 1)

        # Sağ taraf
        self.profil_sayfa_yigini = QStackedWidget(ProfilSekmesi)
        self.profil_sayfa_yigini.setStyleSheet(u"background-color: white; border-top-left-radius: 20px;")

        # Sayfaların Oluşturma
        self.sayfa_ana_ekran = QWidget()
        self.sayfa_arac_yonetimi = QWidget()
        self.sayfa_aktif_kiralar = QWidget()

        # Örnek içerik
        self.sayfa_ana_ekran_layout = QVBoxLayout(self.sayfa_ana_ekran)
        self.sayfa_ana_ekran_layout.addWidget(QLabel("Profil Ana Sayfasına Hoş Geldiniz", alignment=Qt.AlignCenter))

        self.profil_sayfa_yigini.addWidget(self.sayfa_ana_ekran)
        self.profil_sayfa_yigini.addWidget(self.sayfa_arac_yonetimi)
        self.profil_sayfa_yigini.addWidget(self.sayfa_aktif_kiralar)

        self.ana_izgara_layout.addWidget(self.profil_sayfa_yigini, 0, 1, 1, 1)

        self.retranslateUi(ProfilSekmesi)
        QMetaObject.connectSlotsByName(ProfilSekmesi)

    def retranslateUi(self, ProfilSekmesi):
        ProfilSekmesi.setWindowTitle(QCoreApplication.translate("ProfilSekmesi", u"Profilim", None))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setFont(QFont("Segoe UI", 10))

    dialog = QDialog()
    ui = Ui_ProfilSekmesi()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec())