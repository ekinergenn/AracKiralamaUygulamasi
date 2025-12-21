import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QDate, Signal)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QPushButton, QDateEdit, QVBoxLayout, QWidget, QFrame, QHBoxLayout)

# Dosya yolları için
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Ui_AracDetayDialog(object):
    def setupUi(self, AracDetayDialog):
        if not AracDetayDialog.objectName():
            AracDetayDialog.setObjectName(u"AracDetayDialog")

        AracDetayDialog.resize(850, 650)
        AracDetayDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_izgara_layout = QGridLayout(AracDetayDialog)
        self.ana_izgara_layout.setContentsMargins(25, 25, 25, 25)
        self.ana_izgara_layout.setSpacing(20)

        # Araç Görseli
        self.cerceve_resim = QFrame(AracDetayDialog)
        self.cerceve_resim.setStyleSheet(u"background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.resim_layout = QVBoxLayout(self.cerceve_resim)

        self.etiket_arac_resim = QLabel(self.cerceve_resim)
        self.etiket_arac_resim.setFixedSize(400, 300)
        self.etiket_arac_resim.setStyleSheet(u"border: none;")

        resim_yolu = os.path.join(BASE_DIR, "icon", "caricon.jpg")
        if os.path.exists(resim_yolu):
            self.etiket_arac_resim.setPixmap(QPixmap(resim_yolu))

        self.etiket_arac_resim.setScaledContents(True)
        self.resim_layout.addWidget(self.etiket_arac_resim)
        self.ana_izgara_layout.addWidget(self.cerceve_resim, 0, 0, 1, 1)

        # Araç Bilgileri
        self.cerceve_bilgi = QFrame(AracDetayDialog)
        self.cerceve_bilgi.setStyleSheet(u"background-color: #2E3A59; border-radius: 15px; color: white;")
        self.bilgi_dikey_layout = QVBoxLayout(self.cerceve_bilgi)
        self.bilgi_dikey_layout.setContentsMargins(25, 25, 25, 25)
        self.bilgi_dikey_layout.setSpacing(12)

        baslik_font = QFont("Segoe UI", 11, QFont.Bold)

        self.etiket_marka = QLabel("Marka: Tesla")
        self.etiket_model = QLabel("Model: Model 3")
        self.etiket_plaka = QLabel("Plaka: 34 ABC 123")
        self.etiket_ucret = QLabel("Günlük Ücret: 2.500 TL")
        self.etiket_durum = QLabel("Durum: Müsait")
        self.etiket_kiralayan = QLabel("Kiralayan: -")

        bilgi_etiketleri = [self.etiket_marka, self.etiket_model, self.etiket_plaka,
                            self.etiket_ucret, self.etiket_durum, self.etiket_kiralayan]

        for etiket in bilgi_etiketleri:
            etiket.setFont(baslik_font)
            etiket.setStyleSheet("border: none; color: white;")
            self.bilgi_dikey_layout.addWidget(etiket)

        self.ana_izgara_layout.addWidget(self.cerceve_bilgi, 0, 1, 1, 2)

        # Tarih ve kiralama işlemi
        self.cerceve_islem = QFrame(AracDetayDialog)
        self.cerceve_islem.setStyleSheet(u"background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.islem_yatay_layout = QHBoxLayout(self.cerceve_islem)
        self.islem_yatay_layout.setContentsMargins(20, 15, 20, 15)

        # takvim stil
        tarih_stil = u"""
            QDateEdit { 
                padding: 8px; 
                border: 1px solid #CBD5E0; 
                border-radius: 6px; 
                color: #2E3A59; 
                font-weight: bold; 
            }
            /* Takvim Genel Arka Planı */
            QCalendarWidget QWidget { 
                background-color: white; 
            }
            /* Üst Navigasyon Çubuğu */
            QCalendarWidget QWidget#qt_calendar_navigationbar { 
                background-color: #2E3A59; 
            }
            /* Ay ve Yıl Seçme Butonları */
            QCalendarWidget QToolButton {
                color: white;
                background-color: #2E3A59;
                font-weight: bold;
                border: none;
                padding: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #4A5568;
            }
            /* Ay Seçimi Açılır Menüsü (Önemli: Yazı rengini koyulaştırır) */
            QCalendarWidget QMenu {
                background-color: white;
                color: #2E3A59;
                selection-background-color: #2E3A59;
                selection-color: white;
            }
            /* Yıl Seçimi Sayı Kutusu */
            QCalendarWidget QSpinBox {
                color: white;
                background-color: #2E3A59;
                selection-background-color: #4A5568;
                selection-color: white;
            }
            /* Günlerin Olduğu Ana Tablo */
            QCalendarWidget QAbstractItemView:enabled {
                color: #2E3A59; 
                selection-background-color: #2E3A59;
                selection-color: white;
                background-color: white;
            }
            /* Gün İsimleri (Pzt, Sal...) */
            QCalendarWidget QWidget#qt_calendar_calendarview {
                background-color: white;
            }
        """

        # Başlangıç Tarihi
        self.v_layout_baslangic = QVBoxLayout()
        self.v_layout_baslangic.addWidget(
            QLabel("Başlangıç Tarihi", styleSheet="color: #4A5568; font-weight: bold; border: none;"))
        self.tarih_baslangic = QDateEdit()
        self.tarih_baslangic.setCalendarPopup(True)
        self.tarih_baslangic.setDate(QDate.currentDate())
        self.tarih_baslangic.setStyleSheet(tarih_stil)
        self.v_layout_baslangic.addWidget(self.tarih_baslangic)

        # Bitiş Tarihi
        self.v_layout_bitis = QVBoxLayout()
        self.v_layout_bitis.addWidget(
            QLabel("Bitiş Tarihi", styleSheet="color: #4A5568; font-weight: bold; border: none;"))
        self.tarih_bitis = QDateEdit()
        self.tarih_bitis.setCalendarPopup(True)
        self.tarih_bitis.setDate(QDate.currentDate().addDays(1))
        self.tarih_bitis.setStyleSheet(tarih_stil)
        self.v_layout_bitis.addWidget(self.tarih_bitis)

        # Ücret ve Buton Alanı
        self.v_layout_onay = QVBoxLayout()
        self.v_layout_onay.setSpacing(10)

        self.etiket_toplam_ucret = QLabel("Toplam: 2.500 TL")
        self.etiket_toplam_ucret.setStyleSheet("font-size: 16px; color: #2E3A59; font-weight: bold; border: none;")

        self.buton_geri_don = QPushButton("← Geri Dön")
        self.buton_geri_don.setCursor(Qt.PointingHandCursor)
        self.buton_geri_don.setStyleSheet("""
            QPushButton {
                background-color: #718096;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { 
                background-color: #4A5568; 
            }
        """)

        self.buton_kirala = QPushButton("Hemen Kirala")
        self.buton_kirala.setCursor(Qt.PointingHandCursor)
        self.buton_kirala.setStyleSheet(u"""
            QPushButton {
                background-color: #2E3A59;
                color: white;
                border-radius: 8px;
                padding: 12px 25px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { 
                background-color: #4A5568; 
            }
        """)

        self.v_layout_onay.addWidget(self.buton_geri_don)
        self.v_layout_onay.addWidget(self.etiket_toplam_ucret)
        self.v_layout_onay.addWidget(self.buton_kirala)
        self.v_layout_onay.addStretch()

        self.islem_yatay_layout.addLayout(self.v_layout_baslangic)
        self.islem_yatay_layout.addLayout(self.v_layout_bitis)
        self.islem_yatay_layout.addStretch()
        self.islem_yatay_layout.addLayout(self.v_layout_onay)

        self.ana_izgara_layout.addWidget(self.cerceve_islem, 1, 0, 1, 3)

        self.retranslateUi(AracDetayDialog)

    def retranslateUi(self, AracDetayDialog):
        AracDetayDialog.setWindowTitle("Araç Detayı ve Kiralama")


class AracDetayWidget(QWidget):
    geri_don_sinyali = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AracDetayDialog()
        self.ui.setupUi(self)

        # geri don butonu islevsel
        self.ui.buton_geri_don.clicked.connect(self.geri_don)

    def geri_don(self):
        # sinyal gonder (anasayfa.py bu sinyali dinleyecek)
        self.geri_don_sinyali.emit()

    def arac_bilgilerini_guncelle(self, marka, model, plaka, ucret, durum=True):
        self.ui.etiket_marka.setText(f"Marka: {marka}")
        self.ui.etiket_model.setText(f"Model: {model}")
        self.ui.etiket_plaka.setText(f"Plaka: {plaka}")
        self.ui.etiket_ucret.setText(f"Günlük Ücret: {ucret} TL")

        durum_metni = "Müsait" if durum else "Kirada"
        self.ui.etiket_durum.setText(f"Durum: {durum_metni}")
        self.ui.etiket_toplam_ucret.setText(f"Toplam: {ucret} TL")