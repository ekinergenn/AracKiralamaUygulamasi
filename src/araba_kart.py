import sys
import os  #Fotoğraflara ulaşmak için
from PySide6.QtCore import (QCoreApplication, QSize, QRect, Qt, QMetaObject,Signal)
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
        
        self.kart_yatay_layout = QHBoxLayout(self)

        #Araba Resmi
        self.etiket_arac_resim = QLabel(self)
        self.etiket_arac_resim.setFixedSize(140, 140)
        self.etiket_arac_resim.setStyleSheet("background-color: #F7FAFC; border-radius: 10px; border: none;")

        #Araba Resmi Adresi
        car_path = os.path.join(BASE_DIR, "../icon/caricon.jpg")
        if os.path.exists(car_path):
            self.etiket_arac_resim.setPixmap(QPixmap(car_path))

        self.etiket_arac_resim.setScaledContents(True)
        self.kart_yatay_layout.addWidget(self.etiket_arac_resim)

        #Bilgiler
        self.bilgi_dikey_layout = QVBoxLayout()
        self.etiket_marka = QLabel(f"<b>{marka}</b>")
        self.etiket_marka.setStyleSheet("font-size: 16px; color: #2D3748; border:none;")
        self.etiket_model = QLabel(f"Model: {model}")
        self.etiket_model.setStyleSheet("color: #4A5568; border:none;")
        self.etiket_plaka = QLabel(f"Plaka: {plaka}")
        self.etiket_plaka.setStyleSheet("color: #4A5568; border:none;")
        self.etiket_fiyat = QLabel(f"<b>{fiyat} / Günlük</b>")
        self.etiket_fiyat.setStyleSheet("color: #2E3A59; font-size: 14px; border:none;")

        self.buton_goruntule = QPushButton("Görüntüle")
        self.buton_goruntule.setCursor(Qt.PointingHandCursor)
        self.buton_goruntule.setStyleSheet(
            "background-color: #2E3A59; color: white; border-radius: 8px; padding: 8px; font-weight: bold;")

        self.bilgi_dikey_layout.addWidget(self.etiket_marka)
        self.bilgi_dikey_layout.addWidget(self.etiket_model)
        self.bilgi_dikey_layout.addWidget(self.etiket_plaka)
        self.bilgi_dikey_layout.addWidget(self.etiket_fiyat)
        self.bilgi_dikey_layout.addStretch()
        self.bilgi_dikey_layout.addWidget(self.buton_goruntule)

        self.kart_yatay_layout.addLayout(self.bilgi_dikey_layout)
