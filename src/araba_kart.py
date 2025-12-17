import sys
import os  #Fotoğraflara ulaşmak için
from PySide6.QtCore import (QCoreApplication, QSize, QRect, Qt, QMetaObject)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QScrollArea, QVBoxLayout, QWidget, QFrame)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class araba_kart(QFrame):
    def __init__(self, marka, model, plaka, fiyat, parent=None):
        super().__init__(parent)
        self.setFixedSize(380, 200)
        self.setStyleSheet("background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")

        kart_yatay_layout = QHBoxLayout(self)

        #Araba Resmi
        etiket_arac_resim = QLabel(self)
        etiket_arac_resim.setFixedSize(140, 140)
        etiket_arac_resim.setStyleSheet("background-color: #F7FAFC; border-radius: 10px; border: none;")

        #Araba Resmi Adresi
        car_path = os.path.join(BASE_DIR, "../icon/caricon.jpg")
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