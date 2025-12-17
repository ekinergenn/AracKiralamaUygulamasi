import sys
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QColor)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget,
                               QSpacerItem, QLayout, QGraphicsDropShadowEffect)


class ModernLoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kullanıcı Girişi")
        self.resize(700, 450)

        self.setStyleSheet("background-color: #EFEFEF;")

        self.ana_yatay_layout = QHBoxLayout(self)
        self.ana_yatay_layout.setContentsMargins(0, 0, 0, 0)
        self.ana_yatay_layout.setSpacing(0)

        #Giriş Kısmı
        self.sol_cerceve = QFrame(self)
        self.sol_cerceve.setFixedWidth(400)
        self.sol_cerceve.setStyleSheet(self.form_stil_sayfasi_getir())

        self.sol_cerceve.setGraphicsEffect(self.golge_efekti_getir())

        self.form_dikey_layout = QVBoxLayout(self.sol_cerceve)
        self.form_dikey_layout.setContentsMargins(40, 40, 40, 40)
        self.form_dikey_layout.setSpacing(20)

        # Başlık
        self.etiket_baslik = QLabel("Giriş Yap")
        self.etiket_baslik.setFont(self.font_getir(22, True))
        self.etiket_baslik.setStyleSheet("color: #333333;")
        self.form_dikey_layout.addWidget(self.etiket_baslik)

        # Mail Girişi
        self.mail_giris = QLineEdit()
        self.mail_giris.setPlaceholderText("E-posta")
        self.form_dikey_layout.addWidget(self.mail_giris)

        # Şifre Girişi
        self.sifre_giris = QLineEdit()
        self.sifre_giris.setPlaceholderText("Parola")
        self.sifre_giris.setEchoMode(QLineEdit.EchoMode.Password)
        self.form_dikey_layout.addWidget(self.sifre_giris)

        # Giriş Butonu
        self.buton_giris_yap = QPushButton("GİRİŞ YAP")
        self.form_dikey_layout.addWidget(self.buton_giris_yap)

        self.form_dikey_layout.addStretch()

        # Kayıt Kısmı
        self.sag_cerceve = QFrame(self)
        self.sag_cerceve.setStyleSheet(self.bilgi_stil_sayfasi_getir())

        self.bilgi_dikey_layout = QVBoxLayout(self.sag_cerceve)
        self.bilgi_dikey_layout.setContentsMargins(30, 80, 30, 80)
        self.bilgi_dikey_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Başlık
        self.etiket_bilgi_baslik = QLabel("Hesabın Yok Mu?")
        self.etiket_bilgi_baslik.setFont(self.font_getir(20, True))
        self.etiket_bilgi_baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiket_bilgi_baslik.setWordWrap(True)
        self.etiket_bilgi_baslik.setStyleSheet("color: white;")
        self.bilgi_dikey_layout.addWidget(self.etiket_bilgi_baslik)

        # Metin
        self.etiket_bilgi_metni = QLabel("Hemen aracını kirala.")
        self.etiket_bilgi_metni.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiket_bilgi_metni.setWordWrap(True)
        self.etiket_bilgi_metni.setStyleSheet("color: #EFEFEF; font-size: 14px;")
        self.bilgi_dikey_layout.addWidget(self.etiket_bilgi_metni)

        self.bilgi_dikey_layout.addSpacing(30)

        # Kayıt Ol Butonu
        self.buton_kayit_ol = QPushButton("KAYIT OL")
        self.buton_kayit_ol.setObjectName("KayitButonu")
        self.buton_kayit_ol.setCursor(Qt.PointingHandCursor)
        self.buton_kayit_ol.setStyleSheet(self.kayit_butonu_stil_sayfasi_getir())
        self.bilgi_dikey_layout.addWidget(self.buton_kayit_ol)

        # Ekleme
        self.ana_yatay_layout.addWidget(self.sol_cerceve)
        self.ana_yatay_layout.addWidget(self.sag_cerceve)

    def font_getir(self, boyut, kalin=False):
        font = QFont("Arial")
        font.setPointSize(boyut)
        font.setBold(kalin)
        return font

    def golge_efekti_getir(self):
        golge = QGraphicsDropShadowEffect()
        golge.setBlurRadius(20)
        golge.setColor(QColor(0, 0, 0, 80))
        golge.setOffset(0, 0)
        return golge

    def form_stil_sayfasi_getir(self):
        return """
        QFrame {
            background-color: white; 
            border-top-left-radius: 12px;
            border-bottom-left-radius: 12px;
            border-top-right-radius: 0px;
            border-bottom-right-radius: 0px;
        }

        QLineEdit {
            background-color: #F8F9FA; 
            border: 1px solid #D2D6DC; 
            border-radius: 6px;
            padding: 10px 15px; 
            font-size: 14px;
            color: #333333;
        }
        QLineEdit:focus {
            border: 1px solid #4C8BF5;
        }

        QPushButton {
            background-color: #2E3A59; 
            color: white;
            border: none;
            border-radius: 6px;
            padding: 12px 20px;
            font-size: 15px;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #3567D6;
        }
        """

    def bilgi_stil_sayfasi_getir(self):
        return """
        QFrame {
            background-color: #2E3A59; 
            border-top-left-radius: 0px;
            border-bottom-left-radius: 0px;
            border-top-right-radius: 12px;
            border-bottom-right-radius: 12px;
        }
        """

    def kayit_butonu_stil_sayfasi_getir(self):
        return """
        QPushButton#KayitButonu {
            background-color: transparent; 
            color: white;                 
            border: 2px solid white;       
            border-radius: 6px;
            padding: 10px 20px;
            font-size: 14px;
            font-weight: bold;
        }
        QPushButton#KayitButonu:hover {
            background-color: rgba(255, 255, 255, 50); 
        }
        """
