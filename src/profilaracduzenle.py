import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt,Signal)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QPushButton, QScrollArea, QVBoxLayout, QWidget, QFrame, QHBoxLayout, QMessageBox)


from src.aracekle import AracEkleDialog
from src.aracduzenle import AracDuzenleDialog
from backend.araba import araba


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class YonetimAracKarti(QFrame):
    def __init__(self, araba, parent=None):
        self.kart_silme_sinyal = Signal()
        self.kart_duzenle_sinyal = Signal()
        super().__init__(parent)
        marka = araba.marka
        model = araba.model
        plaka = araba.plaka
        fiyat = araba.ucret
        self.id = araba.id
        durum = "Müsait" if not araba.durum else "Kirada"
    
        self.setFixedHeight(110)
        self.setMinimumWidth(800)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                border: 1px solid #E2E8F0;
            }
            QLabel { border: none; }
        """)

        self.ana_layout = QHBoxLayout(self)
        self.ana_layout.setContentsMargins(15, 5, 15, 5)

        #araba resmi
        self.etiket_resim = QLabel()
        self.etiket_resim.setFixedSize(80, 80)
        self.etiket_resim.setStyleSheet("background-color: #F7FAFC; border-radius: 8px;")

        resim_yolu = os.path.join(BASE_DIR, "..", "icon", "caricon.jpg")
        if os.path.exists(resim_yolu):
            self.etiket_resim.setPixmap(QPixmap(resim_yolu))
        self.etiket_resim.setScaledContents(True)
        self.ana_layout.addWidget(self.etiket_resim)

        #ozellikler
        self.bilgi_layout = QVBoxLayout()
        self.lbl_baslik = QLabel(f"<b>{marka} {model}</b>")
        self.lbl_baslik.setStyleSheet("color: #2E3A59; font-size: 14px;")
        self.lbl_detay = QLabel(f"Plaka: {plaka} | Günlük: {fiyat} TL")
        self.lbl_detay.setStyleSheet("color: #718096; font-size: 12px;")

        self.bilgi_layout.addWidget(self.lbl_baslik)
        self.bilgi_layout.addWidget(self.lbl_detay)
        self.ana_layout.addLayout(self.bilgi_layout)

        self.ana_layout.addStretch()

        #butonlar
        if durum == "Müsait":
            self.buton_duzenle = QPushButton("Düzenle")
            self.buton_duzenle.setFixedSize(80, 32)
            self.buton_duzenle.setCursor(Qt.PointingHandCursor)
            self.buton_duzenle.setStyleSheet(
                "background-color: #2E3A59; color: white; border-radius: 6px; font-weight: bold;")
            
            self.buton_sil = QPushButton("Sil")
            self.buton_sil.setFixedSize(70, 32)
            self.buton_sil.setCursor(Qt.PointingHandCursor)
            self.buton_sil.setStyleSheet(
                "background-color: #E53E3E; color: white; border-radius: 6px; font-weight: bold;")
            self.ana_layout.addWidget(self.buton_duzenle)
            self.ana_layout.addWidget(self.buton_sil)
        else:
            self.lbl_durum = QLabel("● KİRADAKİ ARAÇ")
            self.lbl_durum.setStyleSheet("color: #3182CE; font-weight: bold; font-size: 11px;")
            self.ana_layout.addWidget(self.lbl_durum)


class Ui_ProfilAracDuzenleDialog(object):
    def __init__(self,app):
        self.app = app
    def setupUi(self, Dialog):
        Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 800)
        Dialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_layout = QVBoxLayout(Dialog)
        self.ana_layout.setContentsMargins(25, 25, 25, 25)
        self.ana_layout.setSpacing(10)

        #ust kısım
        self.ust_yatay_layout = QHBoxLayout()

        baslik_font = QFont("Segoe UI", 13, QFont.Bold)
        self.lbl_kullanilabilir = QLabel("Kullanılabilir Araçlarım")
        self.lbl_kullanilabilir.setFont(baslik_font)
        self.lbl_kullanilabilir.setStyleSheet("color: #2E3A59; border-bottom: 2px solid #2E3A59; padding-bottom: 5px;")

        self.buton_yeni_arac_ekle = QPushButton("+ Yeni Araç Ekle")
        self.buton_yeni_arac_ekle.setFixedSize(140, 35)
        self.buton_yeni_arac_ekle.setCursor(Qt.PointingHandCursor)
        self.buton_yeni_arac_ekle.setStyleSheet("""
            QPushButton {
                background-color: #2E3A59;
                color: white;
                border-radius: 8px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #4A5568;
            }
        """)

        self.ust_yatay_layout.addWidget(self.lbl_kullanilabilir)
        self.ust_yatay_layout.addStretch()
        self.ust_yatay_layout.addWidget(self.buton_yeni_arac_ekle)

        self.ana_layout.addLayout(self.ust_yatay_layout)

        #kullanılabilir araclar
        self.scroll_müsait = QScrollArea(Dialog)
        self.scroll_müsait.setWidgetResizable(True)
        self.scroll_müsait.setStyleSheet("border: none; background-color: transparent;")

        self.icerik_müsait = QWidget()
        self.layout_müsait = QVBoxLayout(self.icerik_müsait)
        self.layout_müsait.setSpacing(10)
        self.layout_müsait.setAlignment(Qt.AlignTop)

        self.scroll_müsait.setWidget(self.icerik_müsait)
        self.ana_layout.addWidget(self.scroll_müsait)

        self.ana_layout.addSpacing(20)

        #kirada olan araclar
        self.lbl_kirada = QLabel("Kirada Olan Araçlarım")
        self.lbl_kirada.setFont(baslik_font)
        self.lbl_kirada.setStyleSheet("color: #2E3A59; border-bottom: 2px solid #2E3A59; padding-bottom: 5px;")
        self.ana_layout.addWidget(self.lbl_kirada)

        self.scroll_kirada = QScrollArea(Dialog)
        self.scroll_kirada.setWidgetResizable(True)
        self.scroll_kirada.setStyleSheet("border: none; background-color: transparent;")

        self.icerik_kirada = QWidget()
        self.layout_kirada = QVBoxLayout(self.icerik_kirada)
        self.layout_kirada.setSpacing(10)
        self.layout_kirada.setAlignment(Qt.AlignTop)

        self.buton_yeni_arac_ekle.clicked.connect(self.yani_araba_ekle_ekran_ac)

        self.refresh()
        self.scroll_kirada.setWidget(self.icerik_kirada)
        self.ana_layout.addWidget(self.scroll_kirada)
        Dialog.setWindowTitle("Araç Yönetimi")

    def refresh(self):
        self.clear_layout(self.layout_müsait)
        self.clear_layout(self.layout_kirada)

        for araba_id in self.app.aktif_hesap.sahip_arabalar:
            araba = self.app.araba_id_arama(araba_id)

            if not araba.durum:
                kart = YonetimAracKarti(araba, self.icerik_müsait)
                kart.buton_sil.clicked.connect(lambda:{self.app.araba_sil(kart.id),
                                                       self.refresh(),
                                                       QMessageBox.warning(self.icerik_müsait, "Araç Silime", "Araç başarıyla silindi.")})
                kart.buton_duzenle.clicked.connect(lambda: self.araba_bilgi_guncelle_ekran_ac(kart.id))
                
                self.layout_müsait.addWidget(kart)
            else:
                self.layout_kirada.addWidget(
                    YonetimAracKarti(araba, self.icerik_kirada)
                )

        self.icerik_müsait.adjustSize()
        self.icerik_kirada.adjustSize()

    def yani_araba_ekle_ekran_ac(self):
        self.dialog = AracEkleDialog()
        self.dialog.veri_gonder.connect(self.yeni_araba_ekle_func)
        self.dialog.exec()

    def yeni_araba_ekle_func(self,arac:araba):
        arac.id = self.app.arabalar[-1].id +1
        self.app.araba_ekle(arac)
        self.refresh()

    def araba_bilgi_guncelle_ekran_ac(self,id):
        self.dialog = AracDuzenleDialog(self.app.araba_id_arama(id))
        self.dialog.veri_gonder.connect(self.araba_bilgi_guncelle_func)
        self.dialog.sil_.connect(self.araba_bilgi_gucelle_silme)
        self.dialog.exec()

    def araba_bilgi_gucelle_silme(self,id):
        self.app.araba_sil(id)
        self.dialog.close()
        self.refresh()


    def araba_bilgi_guncelle_func(self,veri):
        arac = self.app.araba_id_arama(veri[5])
        arac.marka = veri[0]
        arac.model = veri[1]
        arac.plaka = veri[2]
        arac.ucret = veri[3]
        arac.durum = veri[4]

        self.refresh()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
