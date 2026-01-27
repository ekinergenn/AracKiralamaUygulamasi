import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt, Signal)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
                               QWidget, QFrame)

try:
    from src.profilaracduzenle import Ui_ProfilAracDuzenleDialog
    from src.gecmiskiralar import Ui_KiraGecmisiDialog
    from src.raporlar import Ui_RaporlarDialog
except ImportError:
    from profilaracduzenle import Ui_ProfilAracDuzenleDialog
    from gecmiskiralar import Ui_KiraGecmisiDialog
    from raporlar import Ui_RaporlarDialog

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from backend.uygulama import kullanici, admin

class ProfilWidget(QWidget):
    ana_sayfa_istem_sinyali = Signal()
    cikis_yap_sinyali = Signal()  # YENİ: Çıkış yap sinyali

    def __init__(self, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.setupUi(self)

    def setupUi(self, ProfilSekmesi):
        if not ProfilSekmesi.objectName():
            ProfilSekmesi.setObjectName(u"ProfilSekmesi")

        ProfilSekmesi.resize(1200, 750)
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

        profil_yolu = os.path.join(BASE_DIR, "../icon/profilepp.png")
        if os.path.exists(profil_yolu):
            pixmap = QPixmap(profil_yolu).scaled(90, 90, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.etiket_profil_resim.setPixmap(pixmap)

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
        if self.app.admin_bool:
            self.buton_arac_ekle = QPushButton("Araç Düzenle/Ekle", self.sol_menu_cerceve)
        else:
            self.buton_arac_ekle = QPushButton("Araç Düzenle/Ekle")
        self.buton_gecmis_kiralar = QPushButton("Geçmiş Kiralar", self.sol_menu_cerceve)
        self.buton_raporlar = QPushButton("Raporlar", self.sol_menu_cerceve)

        #çkıkış butonu
        self.buton_cikis_yap = QPushButton("Çıkış Yap", self.sol_menu_cerceve)
        self.buton_cikis_yap.setStyleSheet(u"""
            QPushButton {
                background-color: #DC2626;
                color: white;
                border-radius: 8px;
                padding: 12px;
                text-align: left;
                font-size: 14px;
                font-weight: 500;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #B91C1C;
                color: white;
            }
            QPushButton:pressed {
                background-color: #991B1B;
            }
        """)

        if self.app.admin_bool:
            self.menu_butonlari = [
                self.buton_ana_sayfa, self.buton_arac_ekle,
                self.buton_gecmis_kiralar, self.buton_raporlar
            ]
        else:
            self.menu_butonlari = [
                self.buton_ana_sayfa,
                self.buton_gecmis_kiralar, self.buton_raporlar
            ]
        for buton in self.menu_butonlari:
            buton.setStyleSheet(buton_stili)
            buton.setCursor(Qt.PointingHandCursor)
            self.menu_dikey_layout.addWidget(buton)

        # Çıkış butonunu ekle
        self.buton_cikis_yap.setCursor(Qt.PointingHandCursor)
        self.menu_dikey_layout.addWidget(self.buton_cikis_yap)

        self.menu_dikey_layout.addStretch()

        self.ana_izgara_layout.addWidget(self.sol_menu_cerceve, 0, 0, 1, 1)

        # Sağ taraf - QStackedWidget
        self.profil_sayfa_yigini = QStackedWidget(ProfilSekmesi)
        self.profil_sayfa_yigini.setStyleSheet(u"background-color: white; border-top-left-radius: 20px;")

        # Sayfa 0: Ana Sayfa
        self.sayfa_ana_ekran = QWidget()
        self.ana_sayfa_layout = QVBoxLayout(self.sayfa_ana_ekran)
        self.label_ana = QLabel("Profil Sayfasına Hoş Geldiniz", self.sayfa_ana_ekran)
        self.label_ana.setAlignment(Qt.AlignCenter)
        self.label_ana.setStyleSheet("font-size: 18px; font-weight: bold; color: #2E3A59;")
        self.ana_sayfa_layout.addWidget(self.label_ana)
        self.profil_sayfa_yigini.addWidget(self.sayfa_ana_ekran)

        # Sayfa 1: Araç Yönetimi
        if self.app.admin_bool:
            self.sayfa_arac_yonetimi = QWidget()
            self.ui_arac_yonetim = Ui_ProfilAracDuzenleDialog(self.app)
            self.ui_arac_yonetim.setupUi(self.sayfa_arac_yonetimi)
            self.profil_sayfa_yigini.addWidget(self.sayfa_arac_yonetimi)

        # Sayfa 2: Geçmiş Kiralar
        self.sayfa_gecmis = QWidget()
        self.ui_gecmis = Ui_KiraGecmisiDialog(self.app)
        self.ui_gecmis.setupUi(self.sayfa_gecmis)
        self.profil_sayfa_yigini.addWidget(self.sayfa_gecmis)

        # Sayfa 3: Raporlar
        self.sayfa_raporlar = QWidget()
        self.ui_raporlar = Ui_RaporlarDialog(self.app)
        self.ui_raporlar.setupUi(self.sayfa_raporlar)
        self.profil_sayfa_yigini.addWidget(self.sayfa_raporlar)

        self.ana_izgara_layout.addWidget(self.profil_sayfa_yigini, 0, 1, 1, 1)

        # Buton tıklama bağlantıları
        self.buton_ana_sayfa.clicked.connect(self.ana_sayfa_butonu_tiklandi)
        self.buton_arac_ekle.clicked.connect(self.arac_ekle_goster)
        self.buton_gecmis_kiralar.clicked.connect(self.gecmis_goster)
        self.buton_raporlar.clicked.connect(self.raporlar_goster)
        self.buton_cikis_yap.clicked.connect(self.cikis_yap_butonu_tiklandi)  # YENİ: Çıkış yap butonu bağlantısı

        self.retranslateUi(ProfilSekmesi)
        QMetaObject.connectSlotsByName(ProfilSekmesi)

    def ana_sayfa_butonu_tiklandi(self):
        self.ana_sayfa_istem_sinyali.emit()

    # YENİ: Çıkış yap butonu tıklanınca
    def cikis_yap_butonu_tiklandi(self):
        self.cikis_yap_sinyali.emit()

    def arac_ekle_goster(self):
        if hasattr(self, 'ui_arac_yonetim'):
            self.ui_arac_yonetim.refresh()
            self.profil_sayfa_yigini.setCurrentWidget(self.sayfa_arac_yonetimi)

    def gecmis_goster(self):
        if hasattr(self, 'ui_gecmis'):
            self.ui_gecmis.refresh()
            self.profil_sayfa_yigini.setCurrentWidget(self.sayfa_gecmis)

    def raporlar_goster(self):
        self.profil_sayfa_yigini.setCurrentWidget(self.sayfa_raporlar)

    def retranslateUi(self, ProfilSekmesi):
        ProfilSekmesi.setWindowTitle(QCoreApplication.translate("ProfilSekmesi", u"Profilim", None))