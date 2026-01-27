import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QCloseEvent
from src.anasayfa import Ui_Dialog


class AnaEkran(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def closeEvent(self, event: QCloseEvent):
        print("Program kapatılıyor...")

        self.ui.app.database_guncelleme()

        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnaEkran()
    window.show()
    sys.exit(app.exec())