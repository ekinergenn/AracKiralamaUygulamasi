import sys
import os  # Fotoğraflara ulaşmak için
from PySide6.QtCore import (QCoreApplication, QSize, QRect, Qt, QMetaObject, QDate, Signal)
from PySide6.QtGui import (QColor, QFont, QPixmap)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QScrollArea, QVBoxLayout, QWidget, QFrame, QStackedWidget, QSizePolicy, QMessageBox)

from backend.admin import admin
from src.araba_kart import araba_kart
from src.arababilgi import AracDetayWidget
from src.flowlayout import FlowLayout, ClickableLabel
from src.giris import ModernLoginDialog
from src.kayitol import RegisterDialog
from src.profilsayfası import ProfilWidget

from backend.uygulama import uygulama, kullanici, kiralama
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.normpath(
    os.path.join(BASE_DIR, "..", "database", "database.json")
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")

        self.app = uygulama(db_path)
  
        self.arabalar = self.app.arabalar

        self.ana_layout = QVBoxLayout(Dialog)
        self.ana_layout.setSpacing(0)
        self.ana_layout.setContentsMargins(0, 0, 0, 0)

        self.ana_stack = QStackedWidget()
        self.ana_ekran = QWidget()
        self.giris_ekran = ModernLoginDialog()
        self.kayitol_ekran = RegisterDialog()
        self.profil_sayfasi_ekran = ProfilWidget(self.app)

        Dialog.resize(900, 750)
        Dialog.setStyleSheet(u"background-color: #F8F9FA;")
        self.ana_dikey_layout = QVBoxLayout(self.ana_ekran)
        self.ana_dikey_layout.setSpacing(20)
        self.ana_dikey_layout.setContentsMargins(0, 0, 0, 0)

        self.ust_bar_cerceve = QFrame(self.ana_ekran)
        self.ust_bar_cerceve.setStyleSheet(u"background-color: #2E3A59;")
        self.ust_yatay_layout = QHBoxLayout(self.ust_bar_cerceve)
        self.ust_yatay_layout.setContentsMargins(15, 10, 15, 10)


        self.etiket_profil_resim = ClickableLabel(self.ust_bar_cerceve)
        self.etiket_profil_resim.setFixedSize(50, 50)
        self.etiket_profil_resim.setStyleSheet(
            "border-radius: 25px; background-color: #4A5568; border: 2px solid white;")

        profile_path = os.path.join(BASE_DIR, "../icon/profilepp.png")
        if os.path.exists(profile_path):
            self.etiket_profil_resim.setPixmap(QPixmap(profile_path))

        self.etiket_profil_resim.setScaledContents(True)
        self.ust_yatay_layout.addWidget(self.etiket_profil_resim)


        self.etiket_mail = QLabel(self.ust_bar_cerceve)
        self.etiket_mail.setText("ornek@gmail.com")
        self.etiket_mail.setStyleSheet("color: white; font-weight: bold; font-size: 14px; padding-left: 10px;")
        self.ust_yatay_layout.addWidget(self.etiket_mail)

        self.ust_yatay_layout.addStretch()


        self.arama_satiri = QLineEdit(self.ust_bar_cerceve)
        self.arama_satiri.setPlaceholderText("Araç ara...")
        self.arama_satiri.setFixedWidth(400)
        self.arama_satiri.setStyleSheet("border-radius: 10px; padding: 8px; background-color: white; color: #2E3A59;")
        self.ust_yatay_layout.addStretch()
        self.ust_yatay_layout.addWidget(self.arama_satiri)
        self.ust_yatay_layout.addStretch()


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


        self.kaydirma_alani = QScrollArea()
        self.kaydirma_alani.setWidgetResizable(True)
        self.kaydirma_alani.setStyleSheet("border: none; background-color: transparent;")

        self.kaydirma_icerik_widget = QWidget()
        self.izgara_layout_araclar = FlowLayout(self.kaydirma_icerik_widget)
        self.izgara_layout_araclar.setContentsMargins(10, 0, 10, 0)

        
        
        self.araclari_guncelle(self.app.arabalar)

        self.kaydirma_alani.setWidget(self.kaydirma_icerik_widget)

        page1_layout = QVBoxLayout(self.page1)
        page1_layout.setContentsMargins(10, 0, 0, 0)
        page1_layout.addWidget(self.kaydirma_alani)

       
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        
        self.ana_dikey_layout.addWidget(self.stack)
       
        self.stack.setCurrentIndex(0)

        
        self.ana_stack.addWidget(self.ana_ekran)
        self.ana_stack.addWidget(self.giris_ekran)
        self.ana_stack.addWidget(self.kayitol_ekran)
        self.ana_stack.addWidget(self.profil_sayfasi_ekran)

        
        self.ana_stack.setCurrentWidget(self.giris_ekran)

        
        self.ana_layout.addWidget(self.ana_stack)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

        self.giris_ekran.buton_giris_yap.clicked.connect(self.giris_yap_baglanti)
        self.giris_ekran.buton_kayit_ol.clicked.connect(self.kayit_ol_page_baglanti)
        self.kayitol_ekran.buton_kayit_ol.clicked.connect(self.kayit_ol_baglanti)
        self.etiket_profil_resim.clicked.connect(self.profil_page_baglanti)
        self.arama_satiri.returnPressed.connect(self.arama)
        self.combo_sirala.currentTextChanged.connect(self.sirala)
        self.combo_filtrele.currentTextChanged.connect(self.filtrele)
        self.profil_sayfasi_ekran.cikis_yap_sinyali.connect(self.cikis_yap_baglanti)
        self.kayitol_ekran.giris_sayfasi_isteniyor.connect(
            lambda: self.ana_stack.setCurrentWidget(self.giris_ekran)
        )

    def cikis_yap_baglanti(self):
        if self.profil_sayfasi_ekran:
            self.ana_stack.removeWidget(self.profil_sayfasi_ekran)
            self.profil_sayfasi_ekran.deleteLater()
            self.profil_sayfasi_ekran = None

        self.app.aktif_hesap = None
        self.app.admin_bool = False

        self.etiket_mail.setText("E-Posta")

        self.ana_stack.setCurrentWidget(self.giris_ekran)

    
    def arac_kart_tiklanma(self, _araba):
       
        self.stack.removeWidget(self.page2)
        self.page2.deleteLater()

        self.page2 = QWidget()
        page2_layout = QVBoxLayout(self.page2)
        page2_layout.setContentsMargins(0, 0, 0, 0)

        self.araba_bilgi = AracDetayWidget(_araba,self.app)
        self.araba_bilgi.ui.tarih_bitis.dateChanged.connect(self.araba_kiralama_gun_secimi)
        self.araba_bilgi.ui.buton_kirala.clicked.connect(self.araba_kirala)
        self.araba_bilgi.ui.buton_geri_don.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))
        self.araba_bilgi.ui.buton_iade.clicked.connect(lambda: self.iade_et(_araba))
        page2_layout.addWidget(self.araba_bilgi)
        self.stack.addWidget(self.page2)
        self.stack.setCurrentWidget(self.page2)

    def kayit_ol_page_baglanti(self):
        self.ana_stack.setCurrentWidget(self.kayitol_ekran)

    def profil_page_baglanti(self):
        self.profil_sayfasi_ekran = ProfilWidget(self.app)
        self.ana_stack.addWidget(self.profil_sayfasi_ekran)
        self.profil_sayfasi_ekran.etiket_kullanici_mail.setText(self.app.aktif_hesap.eposta)
        self.profil_sayfasi_ekran.buton_ana_sayfa.clicked.connect(
            lambda: {self.ana_stack.setCurrentWidget(self.ana_ekran), self.araclari_guncelle(self.app.arabalar)})
        self.profil_sayfasi_ekran.cikis_yap_sinyali.connect(self.cikis_yap_baglanti)
        self.ana_stack.setCurrentWidget(self.profil_sayfasi_ekran)

    def araba_kiralama_gun_secimi(self, qdate):
        date1 = self.araba_bilgi.ui.tarih_baslangic.date().toPython()
        date2 = qdate.toPython()
        gun = (date2 - date1).days

        if (gun > 0):
            self.araba_bilgi.ui.etiket_toplam_ucret.setText(
                "Toplam: " + str(self.araba_bilgi.ui.araba.ucret * gun) + " TL")
        else:
            QMessageBox.warning(
                self.page2,
                "Giris Hatası",
                "başlangıç günü ile bitiş günü arasında en az 1 gün olmalı"

            )
            self.araba_bilgi.ui.tarih_bitis.setDate(QDate.currentDate().addDays(1))
            self.araba_bilgi.ui.etiket_toplam_ucret.setText("Toplam: 0 TL")


    def araba_kirala(self):
            date1 = self.araba_bilgi.ui.tarih_baslangic.date().toPython()
            date2 = self.araba_bilgi.ui.tarih_bitis.date().toPython()

            bugun = date.today()

            if date1 < bugun:
                QMessageBox.warning(
                    self.page2,
                    "Giris Hatası",
                    "Geçersiz tarih girdiniz."
                )

            elif date2 < bugun:
                QMessageBox.warning(
                    self.page2,
                    "Giris Hatası",
                    "Geçersiz tarih girdiniz."
                )

            elif date1 > date2:
                QMessageBox.warning(
                    self.page2,
                    "Giris Hatası",
                    "Geçersiz tarih girdiniz."

                )
            elif (not self.araba_bilgi.ui.araba.durum):
                QMessageBox.information(
                    self.page2,
                    "araba kiralama",
                    "arabayi kiraladınız"
                )
                self.app.kiralamalar.append(kiralama(self.app.aktif_hesap.id, self.araba_bilgi.ui.araba.id, date1, date2,
                                                    ((date2 - date1).days) * self.araba_bilgi.ui.araba.ucret,
                                                    len(self.app.kiralamalar), self.app))
                self.app.database_guncelleme()
            else:
                QMessageBox.warning(
                    self.page2,
                    "araba kiralama",
                    "bu araba kirada kiralanamaz"
                )

    
    def giris_yap_baglanti(self):

        eposta = self.giris_ekran.mail_giris.text()
        sifre = self.giris_ekran.sifre_giris.text()
        if not eposta.split():
            QMessageBox.warning(
                self.giris_ekran,
                "Giris Hatası",
                "Lütfen gerekli alani doldurunuz."
            )
        elif not sifre.split():
            QMessageBox.warning(
                self.giris_ekran,
                "Giris Hatası",
                "Lütfen gerekli alani doldurunuz."
            )
        else:
            kisi = self.app.kullanici_eposta_arama(eposta)
            admin = self.app.admin_eposta_arama(eposta)
            if (kisi and kisi.sifre == sifre):
                self.app.aktif_hesap = kisi
                self.etiket_mail.setText(kisi.eposta)
                self.ana_stack.setCurrentWidget(self.ana_ekran)
            elif (admin and admin.sifre == sifre):
                self.app.aktif_hesap = admin
                self.etiket_mail.setText(admin.eposta)
                self.app.admin_bool = True
                self.ana_stack.setCurrentWidget(self.ana_ekran)
            else:
                QMessageBox.warning(
                    self.giris_ekran,
                    "Giris Hatası",
                    "boyle bir hesap bulunamadi"
                )

    def kayit_ol_baglanti(self):
        
        isim = self.kayitol_ekran.isim_giris.text().strip()
        eposta = self.kayitol_ekran.mail_giris.text().strip()
        sifre = self.kayitol_ekran.sifre_giris.text()
        sifre_tekrar = self.kayitol_ekran.sifre_tekrar_giris.text()
        telefon = self.kayitol_ekran.tel_giris.text().strip()
        if not telefon.isdigit():
            QMessageBox.warning(self.kayitol_ekran, "Kayıt Hatası", "Telefon numarası sadece sayılardan oluşabilir.")
            return
        if not len(telefon)==10:
            QMessageBox.warning(self.kayitol_ekran, "Kayıt Hatası", "Telefon numarası sadece 10 rakam olmalı.")
            return

        
        if not all([isim, eposta, sifre, sifre_tekrar, telefon]):
            QMessageBox.warning(self.kayitol_ekran, "Kayıt Hatası", "Lütfen tüm alanları doldurunuz.")
            return

        
        if sifre != sifre_tekrar:
            QMessageBox.warning(self.kayitol_ekran, "Kayıt Hatası", "Girdiğiniz şifreler birbiriyle eşleşmiyor.")
            return

    
        if self.app.kullanici_eposta_arama(eposta) or self.app.admin_eposta_arama(eposta):
            QMessageBox.warning(self.kayitol_ekran, "Kayıt Hatası", "Bu e-posta adresi zaten sisteme kayıtlı.")
            return

        
        eposta_tur = ("@gmail.com", "@hotmail.com", "@yahoo.com", "@outlook.com")
        if not eposta.endswith(eposta_tur):
            QMessageBox.warning(self.kayitol_ekran, "Geçersiz E-posta", "Lütfen geçerli bir e-posta türü giriniz.")
            return

        
        for k in self.app.kullanicilar + self.app.adminler:
            if k.telefon_num == telefon:
                QMessageBox.warning(self.kayitol_ekran, "Kayıt Hatası", "Bu telefon numarası zaten sisteme kayıtlı.")
                return

        
        yeni_id = 0
        tum_liste = self.app.kullanicilar + self.app.adminler

        is_admin = self.kayitol_ekran.check_admin.isChecked()

        if is_admin:
            yeni_admin = admin(
                isim=isim,
                sifre=sifre,
                eposta=eposta,
                telefon_num=telefon,
                id=yeni_id
            )

            
            self.app.adminler.append(yeni_admin)
            self.app.database_guncelleme() 

            QMessageBox.information(self.kayitol_ekran, "Başarılı",
                                    "Hesabınız başarıyla oluşturuldu. Giriş yapabilirsiniz.")
        else:
            yeni_kullanici = kullanici(
                isim=isim,
                sifre=sifre,
                eposta=eposta,
                telefon_num=telefon,
                id=yeni_id
            )

            
            self.app.kullanicilar.append(yeni_kullanici)
            self.app.database_guncelleme() 

            QMessageBox.information(self.kayitol_ekran, "Başarılı",
                                    "Hesabınız başarıyla oluşturuldu. Giriş yapabilirsiniz.")

        
        self.ana_stack.setCurrentWidget(self.giris_ekran)

    def araclari_guncelle(self, _arabalar):
        self.clear_layout(self.izgara_layout_araclar)
        self.arabalar = []
        for i in _arabalar:
            araba = araba_kart(marka=i.marka, model=i.model, plaka=i.plaka, fiyat=i.ucret, id=i.id)
            araba.buton_goruntule.clicked.connect(lambda checked=False, i_id=i.id: self.arac_kart_tiklanma(self.app.araba_id_arama(i_id)))
            self.izgara_layout_araclar.addWidget(araba)
            self.arabalar.append(i)

    def iade_et(self, secili_araba):
            bugun = date.today()
            aktif_kullanici_id = self.app.aktif_hesap.id #

            # 1. Kontrol: Araç kirada mı?
            if not secili_araba.durum:
                QMessageBox.warning(self.page2, "İade Hatası", "Bu araç zaten kirada değil.")
                return

            # 2. İlgili kiralama kaydını bul
            hedef_kiralama = None
            for k in self.app.kiralamalar:
                # Araç ID'si eşleşen ve aktif olan kiralama
                if k.araba == secili_araba.id and not k.gecmis:
                    # Sahiplik kontrolü: Bizim mi yoksa admin miyiz?
                    if k.kullanici == aktif_kullanici_id or self.app.admin_bool:
                        hedef_kiralama = k
                        break

            if hedef_kiralama:
                onay = QMessageBox.question(self.page2, "İade ve Kayıt Silme", 
                                            f"{secili_araba.marka} aracının kiralama kaydını tamamen silmek istediğinize emin misiniz?",
                                            QMessageBox.Yes | QMessageBox.No)
                
                if onay == QMessageBox.Yes:
                    # 3. Kiralama nesnesini ana listeden sil (Database'den silinmesi için şart)
                    self.app.kiralamalar.remove(hedef_kiralama)
                    
                    # 4. Aracın durumunu boşa çıkar
                    secili_araba.durum = False
                    
                    # 5. Kullanıcının aktif kiralamalar listesinden ID'yi kaldır
                    sahibi = self.app.kullanici_id_arama(hedef_kiralama.kullanici)
                    if not sahibi:
                        sahibi = self.app.admin_id_arama(hedef_kiralama.kullanici)
                    
                    if sahibi and hedef_kiralama.id in sahibi.aktif_kiralamalar:
                        sahibi.aktif_kiralamalar.remove(hedef_kiralama.id)

                    # 6. Veritabanını kalıcı olarak güncelle
                    self.app.database_guncelleme()
                    
                    QMessageBox.information(self.page2, "Başarılı", "Kiralama kaydı silindi ve araç iade alındı.")
                    
                    # Arayüzü güncelle
                    self.araba_bilgi.arac_bilgilerini_guncelle(
                        secili_araba.marka, secili_araba.model, secili_araba.plaka, 
                        secili_araba.ucret, secili_araba.durum
                    )
                    self.stack.setCurrentWidget(self.page1)
                    self.araclari_guncelle(self.app.arabalar)
            else:
                QMessageBox.warning(self.page2, "İade Hatası", "Bu aracı siz kiralamadığınız için iade edemezsiniz.")
    def arama(self):
        icerik = self.arama_satiri.text()
        aranmıs = []
        print("icerik: ",icerik)
        if icerik == "":
            self.araclari_guncelle(self.app.arabalar)
            return
        for a in self.app.arabalar:
            if icerik.lower() in a.marka.lower():
                aranmıs.append(a)
        self.araclari_guncelle(aranmıs)

    def sirala(self, secim):
        siralanmis = sorted(self.arabalar, key=lambda x: x.ucret)

        if secim == "Fiyat: Artan":
            self.araclari_guncelle(siralanmis)
        else:
            siralanmis.reverse()
            self.araclari_guncelle(siralanmis)

    def filtrele(self,secim):
        filtreli = []
        if secim == "Hepsi":
            self.araclari_guncelle(self.app.arabalar)
        elif secim == "Müsait":
            for a in self.app.arabalar:
                if a.durum == False:
                    filtreli.append(a)
            self.araclari_guncelle(filtreli)
        else:
            for a in self.app.arabalar:
                if a.durum == True:
                    filtreli.append(a)
            self.araclari_guncelle(filtreli)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("Araç Kiralama Paneli")