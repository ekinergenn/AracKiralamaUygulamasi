import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QPushButton, QVBoxLayout, QWidget, QFrame,
                               QHBoxLayout, QLineEdit, QComboBox)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Ui_AracEkleDialog(object):
    def setupUi(self, AracEkleDialog):
        if not AracEkleDialog.objectName():
            AracEkleDialog.setObjectName(u"AracEkleDialog")

        AracEkleDialog.resize(850, 600)
        AracEkleDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_izgara_layout = QGridLayout(AracEkleDialog)
        self.ana_izgara_layout.setContentsMargins(25, 25, 25, 25)
        self.ana_izgara_layout.setSpacing(20)

        #arac resmi
        self.cerceve_resim = QFrame(AracEkleDialog)
        self.cerceve_resim.setStyleSheet(u"background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.resim_layout = QVBoxLayout(self.cerceve_resim)

        self.etiket_arac_resim = QLabel(self.cerceve_resim)
        self.etiket_arac_resim.setFixedSize(400, 300)
        self.etiket_arac_resim.setStyleSheet(u"border: none;")

        resim_yolu = os.path.join(BASE_DIR, "..", "icon", "caricon.jpg")

        if os.path.exists(resim_yolu):
            self.etiket_arac_resim.setPixmap(QPixmap(resim_yolu))

        self.etiket_arac_resim.setScaledContents(True)
        self.resim_layout.addWidget(self.etiket_arac_resim)

        self.buton_resim_sec = QPushButton("Araç Fotoğrafı Seç")
        self.buton_resim_sec.setCursor(Qt.PointingHandCursor)
        self.buton_resim_sec.setStyleSheet("""
            QPushButton { background-color: #EDF2F7; color: #2E3A59; border-radius: 8px; padding: 10px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #E2E8F0; }
        """)
        self.resim_layout.addWidget(self.buton_resim_sec)

        self.ana_izgara_layout.addWidget(self.cerceve_resim, 0, 0)

        # arac ozellikleri (sag)
        self.cerceve_form = QFrame(AracEkleDialog)
        self.cerceve_form.setStyleSheet(u"background-color: #2E3A59; border-radius: 15px; color: white;")
        self.form_layout = QVBoxLayout(self.cerceve_form)
        self.form_layout.setContentsMargins(25, 25, 25, 25)
        self.form_layout.setSpacing(10)

        #stil
        bilesen_stili = """
            QLineEdit, QComboBox {
                background-color: white;
                color: #2E3A59;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                border: none;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: #2E3A59;
                selection-background-color: #2E3A59;
                selection-color: white;
            }
        """

        self.form_layout.addWidget(QLabel("Marka:"))
        self.input_marka = QLineEdit()
        self.input_marka.setPlaceholderText("Örn: Tesla, BMW...")
        self.form_layout.addWidget(self.input_marka)

        self.form_layout.addWidget(QLabel("Model:"))
        self.input_model = QLineEdit()
        self.input_model.setPlaceholderText("Örn: Model 3, i4...")
        self.form_layout.addWidget(self.input_model)

        self.form_layout.addWidget(QLabel("Plaka:"))
        self.input_plaka = QLineEdit()
        self.input_plaka.setPlaceholderText("Örn: 34 ABC 123")
        self.form_layout.addWidget(self.input_plaka)

        self.form_layout.addWidget(QLabel("Günlük Ücret (TL):"))
        self.input_ucret = QLineEdit()
        self.input_ucret.setPlaceholderText("Örn: 2500")
        self.form_layout.addWidget(self.input_ucret)

        self.form_layout.addWidget(QLabel("Başlangıç Durumu:"))
        self.combo_durum = QComboBox()
        self.combo_durum.addItems(["Müsait", "Bakımda"])
        self.form_layout.addWidget(self.combo_durum)

        self.input_marka.setStyleSheet(bilesen_stili)
        self.input_model.setStyleSheet(bilesen_stili)
        self.input_plaka.setStyleSheet(bilesen_stili)
        self.input_ucret.setStyleSheet(bilesen_stili)
        self.combo_durum.setStyleSheet(bilesen_stili)

        self.ana_izgara_layout.addWidget(self.cerceve_form, 0, 1)

        #butonlar (alt kısım)
        self.cerceve_aksiyon = QFrame(AracEkleDialog)
        self.cerceve_aksiyon.setStyleSheet(u"background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.aksiyon_layout = QHBoxLayout(self.cerceve_aksiyon)
        self.aksiyon_layout.setContentsMargins(20, 15, 20, 15)

        self.buton_iptal = QPushButton("İptal Et")
        self.buton_iptal.setCursor(Qt.PointingHandCursor)
        self.buton_iptal.setStyleSheet("""
            QPushButton { background-color: #718096; color: white; border-radius: 8px; padding: 12px 20px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #4A5568; }
        """)

        self.buton_kaydet = QPushButton("Aracı Kaydet")
        self.buton_kaydet.setCursor(Qt.PointingHandCursor)
        self.buton_kaydet.setStyleSheet("""
            QPushButton { background-color: #2E3A59; color: white; border-radius: 8px; padding: 12px 40px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #4A5568; }
        """)

        self.aksiyon_layout.addWidget(self.buton_iptal)
        self.aksiyon_layout.addStretch()
        self.aksiyon_layout.addWidget(self.buton_kaydet)

        self.ana_izgara_layout.addWidget(self.cerceve_aksiyon, 1, 0, 1, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = QDialog()
    ui = Ui_AracEkleDialog()
    ui.setupUi(pencere)
    pencere.setWindowTitle("Yeni Araç Kaydı")
    pencere.show()
    sys.exit(app.exec())