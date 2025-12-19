import sys
import os  #Fotoğraflara ulaşmak için
from PySide6.QtCore import (QCoreApplication, QSize, QRect, Qt, QMetaObject)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QScrollArea, QVBoxLayout, QWidget, QFrame,QStackedWidget,QSizePolicy,QMessageBox)

from src.araba_kart import araba_kart
from src.arababilgi import AracDetayWidget
from src.flowlayout import FlowLayout
from src.giris import ModernLoginDialog
from src.kayitol import RegisterDialog

#Python dosyasının adresi
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        self.ana_layout = QVBoxLayout(Dialog)
        self.ana_layout.setSpacing(0)
        self.ana_layout.setContentsMargins(0, 0, 0, 0)

        self.ana_stack = QStackedWidget()
        self.ana_ekran = QWidget()
        self.giris_ekran = ModernLoginDialog(parent=self.ana_stack)
        self.kayitol_ekran = RegisterDialog()


        Dialog.resize(900, 750)
        Dialog.setStyleSheet(u"background-color: #F8F9FA;")
        self.ana_dikey_layout = QVBoxLayout(self.ana_ekran)
        self.ana_dikey_layout.setSpacing(20)
        self.ana_dikey_layout.setContentsMargins(0, 0, 0, 0)

        #Üst Kısım
        self.ust_bar_cerceve = QFrame(self.ana_ekran)
        self.ust_bar_cerceve.setStyleSheet(u"background-color: #2E3A59;")
        self.ust_yatay_layout = QHBoxLayout(self.ust_bar_cerceve)
        self.ust_yatay_layout.setContentsMargins(15, 10, 15, 10)

        #PP
        self.etiket_profil_resim = QLabel(self.ust_bar_cerceve)
        self.etiket_profil_resim.setFixedSize(50, 50)
        self.etiket_profil_resim.setStyleSheet("border-radius: 25px; background-color: #4A5568; border: 2px solid white;")

        #PP adresi
        profile_path = os.path.join(BASE_DIR, "../icon/profilepp.png")
        if os.path.exists(profile_path):
            self.etiket_profil_resim.setPixmap(QPixmap(profile_path))

        self.etiket_profil_resim.setScaledContents(True)
        self.ust_yatay_layout.addWidget(self.etiket_profil_resim)

        #Mail kısmı
        self.etiket_mail = QLabel(self.ust_bar_cerceve)
        self.etiket_mail.setText("ornek@gmail.com")
        self.etiket_mail.setStyleSheet("color: white; font-weight: bold; font-size: 14px; padding-left: 10px;")
        self.ust_yatay_layout.addWidget(self.etiket_mail)

        self.ust_yatay_layout.addStretch()

        #Arama
        self.arama_satiri = QLineEdit(self.ust_bar_cerceve)
        self.arama_satiri.setPlaceholderText("Araç ara...")
        self.arama_satiri.setFixedWidth(250)
        self.arama_satiri.setStyleSheet("border-radius: 10px; padding: 8px; background-color: white; color: #2E3A59;")
        self.ust_yatay_layout.addWidget(self.arama_satiri)

        #Filtrele ve Sırala
        combo_stil = "background-color: #4A5568; color: white; border-radius: 8px; padding: 5px; min-width: 110px;"
        self.combo_sirala = QComboBox(self.ust_bar_cerceve)
        self.combo_sirala.addItems(["Fiyat: Artan", "Fiyat: Azalan"])
        self.combo_sirala.setStyleSheet(combo_stil)
        self.combo_filtrele = QComboBox(self.ust_bar_cerceve)
        self.combo_filtrele.addItems(["Hepsi", "Müsait", "Kirada"])
        self.combo_filtrele.setStyleSheet(combo_stil)

        self.ust_yatay_layout.addWidget(self.combo_sirala)
        self.ust_yatay_layout.addWidget(self.combo_filtrele)

        self.ana_dikey_layout.addWidget(self.ust_bar_cerceve)

        self.stack = QStackedWidget()
        self.page1 = QWidget()
        self.page2 = QWidget()

        # Scroll Area
        self.kaydirma_alani = QScrollArea()
        self.kaydirma_alani.setWidgetResizable(True)
        self.kaydirma_alani.setStyleSheet("border: none; background-color: transparent;")

        self.kaydirma_icerik_widget = QWidget()
        self.izgara_layout_araclar = FlowLayout(self.kaydirma_icerik_widget)
        #self.izgara_layout_araclar.setSpacing(5)
        self.izgara_layout_araclar.setContentsMargins(10, 0, 10, 0)
        # self.izgara_layout_araclar.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # self.kaydirma_icerik_widget.setSizePolicy(
        #     QSizePolicy.Policy.Preferred,
        #     QSizePolicy.Policy.Minimum
        # )

        # Kartlar
        self.arac_karti_ekle(0, 0, "Tesla Model 3", "2023", "34 ABC 123", "2500 TL")
        self.arac_karti_ekle(0, 1, "BMW i4", "2024", "34 DEF 456", "3200 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")
        self.arac_karti_ekle(1, 0, "Audi A4", "2022", "34 GHI 789", "1800 TL")

        self.kaydirma_alani.setWidget(self.kaydirma_icerik_widget)

        # 🔴 EN KRİTİK SATIRLAR
        page1_layout = QVBoxLayout(self.page1)
        page1_layout.setContentsMargins(10, 0, 0, 0)
        page1_layout.addWidget(self.kaydirma_alani)

        # bu Stack ana ekran içerisindeki bir araba ya batığımızda ekranın değişmesini sağlayan QStackWidgetın sayfalarını ekliyor
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        # ana_ekran daki stack in bütün ekranı kaplayabilemsi için bir layout içerisinde olası lazım
        self.ana_dikey_layout.addWidget(self.stack)
        # ana_ekran içerisindeki stack widget ın sayfasını değiştiriyor
        self.stack.setCurrentIndex(0)

        # bu stack widget da 4 temel sayfa (login,register,main,profile) ekranları arasında geçişyapılmasını sağlıyor bu sayede sayfalar arasında geçiş yaparken hiç baştan yükleme veya nesne oluşturulmuyor var olan sayfalar arasında geçiş yapılıyor
        self.ana_stack.addWidget(self.ana_ekran)
        self.ana_stack.addWidget(self.giris_ekran)
        self.ana_stack.addWidget(self.kayitol_ekran)

        # bu ana_stack in sayfaları arasında geçiş yapmasını sağlıyor uygulama ilk açıldığında giris_ekranını yüklenmesi ayarlanmış
        self.ana_stack.setCurrentWidget(self.giris_ekran)

        # gene ana_stack widgetı bütün ekranı kaplasın diye bir layout un içerisine koyuyuruz
        self.ana_layout.addWidget(self.ana_stack)
        
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        # bu kısımda click eventler var
        self.giris_ekran.buton_giris_yap.clicked.connect(self.giris_yap_baglanti)


    # araba_karların eklenmesi sağlanıyor aslında bunu burda yapmak yerine direkt nesne oluşturma ile yapıcam ve backend den alınan veriler ile oluşturulması sağlanacak
    def arac_karti_ekle(self, satir, sutun, marka, model, plaka, fiyat):
        araba = araba_kart(marka=marka,model=model,plaka=plaka,fiyat=fiyat)
        araba.buton_goruntule.clicked.connect(self.arac_kart_tiklanma)
        self.izgara_layout_araclar.addWidget(araba)

    # herhangi bir arac_kart nesnesinde görüntüleme butonuna basıldığında bu foksiyon ile o arabanın araba_sayfasına bilgilerini göndererek daha detaylı bir ekrana geçilmesini sağlaaycak.
    def arac_kart_tiklanma(self):
        # önce page2 deki bütün nesneleri aslında direkt kendisini siliyoruz ve sonrasında tekrar yeni bilgiler ile oluşturuyoruz
        self.stack.removeWidget(self.page2)
        self.page2.deleteLater()

        self.page2 = QWidget()
        page2_layout = QVBoxLayout(self.page2)
        page2_layout.setContentsMargins(0, 0, 0, 0)

        araba_bilgi = AracDetayWidget()
        page2_layout.addWidget(araba_bilgi)
        self.stack.addWidget(self.page2)
        self.stack.setCurrentWidget(self.page2)
        

    # giris yap butonuna basıldığında login alanlarının boş olup olmadığını kontrol ediyor
    def giris_yap_baglanti(self):
        if not self.giris_ekran.mail_giris.text().split():
            QMessageBox.warning(
                self.giris_ekran,
                "Giris Hatası",
                "Lütfen gerekli alani doldurunuz."
            )
        elif not self.giris_ekran.sifre_giris.text().split():
            QMessageBox.warning(
                self.giris_ekran,
                "Giris Hatası",
                "Lütfen gerekli alani doldurunuz."
            )
        else:
            # burda uygulama classındaki kullanicileri kontrol ederek bir eşleşmeye bakar eğer varsa diğer ekrana geçirir
            self.ana_stack.setCurrentWidget(self.ana_ekran)
            
            # eğer eşleleşme olmazsa tekrar bir mesaj bloğu ile şifre veya mail hatalı uyarısı atacağız 

 


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Araç Kiralama Paneli")