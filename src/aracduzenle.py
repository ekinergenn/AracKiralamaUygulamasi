import sys
import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, Signal)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
                               QPushButton, QVBoxLayout, QWidget, QFrame,
                               QHBoxLayout, QLineEdit, QComboBox)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Ui_AracDuzenleDialog(object):
    def setupUi(self, AracDuzenleDialog):
        if not AracDuzenleDialog.objectName():
            AracDuzenleDialog.setObjectName(u"AracDuzenleDialog")

        AracDuzenleDialog.resize(850, 600)
        AracDuzenleDialog.setStyleSheet(u"background-color: #F8F9FA;")

        self.ana_izgara_layout = QGridLayout(AracDuzenleDialog)
        self.ana_izgara_layout.setContentsMargins(25, 25, 25, 25)
        self.ana_izgara_layout.setSpacing(20)

        #araba resmi
        self.cerceve_resim = QFrame(AracDuzenleDialog)
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

        self.buton_resim_degistir = QPushButton("Fotoğrafı Değiştir")
        self.buton_resim_degistir.setCursor(Qt.PointingHandCursor)
        self.buton_resim_degistir.setStyleSheet("""
            QPushButton { background-color: #EDF2F7; color: #2E3A59; border-radius: 8px; padding: 10px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #E2E8F0; }
        """)
        self.resim_layout.addWidget(self.buton_resim_degistir)

        self.ana_izgara_layout.addWidget(self.cerceve_resim, 0, 0)

        #düzenleme kısmı (sol taraf)
        self.cerceve_form = QFrame(AracDuzenleDialog)
        self.cerceve_form.setStyleSheet(u"background-color: #2E3A59; border-radius: 15px; color: white;")
        self.form_layout = QVBoxLayout(self.cerceve_form)
        self.form_layout.setContentsMargins(25, 25, 25, 25)
        self.form_layout.setSpacing(10)

        #input kısmı
        bileşen_stili = """
            QLineEdit, QComboBox {
                background-color: white;
                color: #2E3A59;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
                border: none;
            }
            /* Açılır menüdeki liste öğelerinin görünürlüğü */
            QComboBox QAbstractItemView {
                background-color: white;
                color: #2E3A59;
                selection-background-color: #2E3A59;
                selection-color: white;
                border: 1px solid #CBD5E0;
            }
        """

        #marka (simdilik ornek, veri okuyup mevcut verileri yazacak.)
        self.form_layout.addWidget(QLabel("Marka:"))
        self.input_marka = QLineEdit()
        self.input_marka.setText("Tesla")  # Mevcut marka
        self.form_layout.addWidget(self.input_marka)

        #model
        self.form_layout.addWidget(QLabel("Model:"))
        self.input_model = QLineEdit()
        self.input_model.setText("Model 3")  # Mevcut model
        self.form_layout.addWidget(self.input_model)

        #plaka
        self.form_layout.addWidget(QLabel("Plaka:"))
        self.input_plaka = QLineEdit()
        self.input_plaka.setText("34 ABC 123")  # Mevcut plaka
        self.form_layout.addWidget(self.input_plaka)

        #ücret
        self.form_layout.addWidget(QLabel("Günlük Ücret (TL):"))
        self.input_ucret = QLineEdit()
        self.input_ucret.setText("2500")  # Mevcut ücret
        self.form_layout.addWidget(self.input_ucret)

        #durum
        self.form_layout.addWidget(QLabel("Araç Durumu:"))
        self.combo_durum = QComboBox()
        self.combo_durum.addItems(["Müsait", "Kirada", "Bakımda"])
        #musaitlik
        self.combo_durum.setStyleSheet(bileşen_stili)
        self.form_layout.addWidget(self.combo_durum)

        self.input_marka.setStyleSheet(bileşen_stili)
        self.input_model.setStyleSheet(bileşen_stili)
        self.input_plaka.setStyleSheet(bileşen_stili)
        self.input_ucret.setStyleSheet(bileşen_stili)

        self.ana_izgara_layout.addWidget(self.cerceve_form, 0, 1)

        #alt kısım
        self.cerceve_aksiyon = QFrame(AracDuzenleDialog)
        self.cerceve_aksiyon.setStyleSheet(u"background-color: white; border-radius: 15px; border: 1px solid #E2E8F0;")
        self.aksiyon_layout = QHBoxLayout(self.cerceve_aksiyon)
        self.aksiyon_layout.setContentsMargins(20, 15, 20, 15)

        #geri don
        self.buton_geri = QPushButton("← Geri Dön")
        self.buton_geri.setCursor(Qt.PointingHandCursor)
        self.buton_geri.setStyleSheet("""
            QPushButton { background-color: #718096; color: white; border-radius: 8px; padding: 12px 20px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #4A5568; }
        """)

        #sil
        self.buton_sil = QPushButton("Aracı Sil")
        self.buton_sil.setCursor(Qt.PointingHandCursor)
        self.buton_sil.setStyleSheet("""
            QPushButton { background-color: #E53E3E; color: white; border-radius: 8px; padding: 12px 20px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #C53030; }
        """)

        #kaydet
        self.buton_kaydet = QPushButton("Değişiklikleri Kaydet")
        self.buton_kaydet.setCursor(Qt.PointingHandCursor)
        self.buton_kaydet.setStyleSheet("""
            QPushButton { background-color: #2E3A59; color: white; border-radius: 8px; padding: 12px 30px; font-weight: bold; border: none; }
            QPushButton:hover { background-color: #4A5568; }
        """)

        self.aksiyon_layout.addWidget(self.buton_geri)
        self.aksiyon_layout.addStretch()
        self.aksiyon_layout.addWidget(self.buton_sil)
        self.aksiyon_layout.addWidget(self.buton_kaydet)

        self.ana_izgara_layout.addWidget(self.cerceve_aksiyon, 1, 0, 1, 2)


#main simdilik var bagli olmadıgı icin
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = QDialog()
    ui = Ui_AracDuzenleDialog()
    ui.setupUi(pencere)
    pencere.show()
    sys.exit(app.exec())