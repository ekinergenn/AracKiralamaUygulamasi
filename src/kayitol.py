import sys
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class RegisterDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Yeni Hesap Oluştur")
        self.resize(500, 450)

        # Ana Pencere
        self.setStyleSheet(self.ana_stil_sayfasi_getir())
        self.izgara_layout = QGridLayout(self)
        self.izgara_layout.setObjectName(u"izgara_layout")

        # Kayıt Formu
        self.kayit_cercevesi = QFrame(self)
        self.kayit_cercevesi.setObjectName(u"kayit_cercevesi")
        self.kayit_cercevesi.setMinimumSize(QSize(350, 400))
        self.kayit_cercevesi.setMaximumSize(QSize(400, 450))

        # Frame
        self.kayit_cercevesi.setStyleSheet(u"QFrame {\n"
                                           "    background-color: #2E3A59; /* Koyu Lacivert Arka Plan */\n"
                                           "    border: none; \n"
                                           "    border-radius: 12px;        \n"
                                           "}")

        self.kayit_cercevesi.setFrameShape(QFrame.Shape.StyledPanel)
        self.kayit_cercevesi.setFrameShadow(QFrame.Shadow.Raised)
        self.dikey_yerlesim = QVBoxLayout(self.kayit_cercevesi)
        self.dikey_yerlesim.setObjectName(u"dikey_yerlesim")
        self.dikey_yerlesim.setContentsMargins(40, 40, 40, 40)
        self.dikey_yerlesim.setSpacing(15)

        # Başlık
        self.etiket_baslik = QLabel(self.kayit_cercevesi)
        self.etiket_baslik.setText("YENİ HESAP OLUŞTUR")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.etiket_baslik.setFont(font)
        self.etiket_baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiket_baslik.setStyleSheet("color: #FFFFFF;")
        self.dikey_yerlesim.addWidget(self.etiket_baslik)

        self.dikey_yerlesim.addSpacing(20)

        # Mail
        self.mail_giris = QLineEdit(self.kayit_cercevesi)
        self.mail_giris.setPlaceholderText("Mail Adresi")
        self.dikey_yerlesim.addWidget(self.mail_giris)

        # Şifre
        self.sifre_giris = QLineEdit(self.kayit_cercevesi)
        self.sifre_giris.setPlaceholderText("Şifre")
        self.sifre_giris.setEchoMode(QLineEdit.EchoMode.Password)
        self.dikey_yerlesim.addWidget(self.sifre_giris)

        # Şifre Tekrar
        self.sifre_tekrar_giris = QLineEdit(self.kayit_cercevesi)
        self.sifre_tekrar_giris.setPlaceholderText("Şifre Tekrarı")
        self.sifre_tekrar_giris.setEchoMode(QLineEdit.EchoMode.Password)
        self.dikey_yerlesim.addWidget(self.sifre_tekrar_giris)

        # Buton
        self.buton_kayit_ol = QPushButton(self.kayit_cercevesi)
        self.buton_kayit_ol.setText("KAYIT OL")
        self.dikey_yerlesim.addWidget(self.buton_kayit_ol)

        self.dikey_yerlesim.addSpacing(10)

        # Giriş Yap Metini
        self.etiket_giris_link = QLabel(self.kayit_cercevesi)
        self.etiket_giris_link.setText("Zaten hesabın var mı? Giriş Yap")
        self.etiket_giris_link.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiket_giris_link.setStyleSheet("color: #A0B9F7; font-size: 11px;")
        self.dikey_yerlesim.addWidget(self.etiket_giris_link)

        self.izgara_layout.addWidget(self.kayit_cercevesi, 0, 0, 1, 1)

    def ana_stil_sayfasi_getir(self):
        return u"""

        QDialog {
            background-color: #EFEFEF; 
        }

        QLineEdit {
            background-color: #FFFFFF;
            border: 1px solid #4C8BF5;
            border-radius: 6px;
            padding: 12px 15px;
            font-size: 14px;
            color: #333333;
        }

        QLineEdit:focus {
            border: 2px solid #3A74D4;
        }

        QPushButton {
            background-color: #4C8BF5;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 12px 20px;
            font-size: 15px;
            font-weight: bold;
            letter-spacing: 1px;
        }
        QPushButton:hover {
            background-color: #357AE8;
        }
        QPushButton:pressed {
            background-color: #265BAE; 
            padding-top: 13px;
            padding-bottom: 11px;
        }
        """


# # Main
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle("Fusion")

#     pencere = RegisterDialog()
#     pencere.show()
#     sys.exit(app.exec())