#import PyQt5
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QTime, QTimer,Qt
from datetime import date

"""vt=sqlite3.connect("FirstDataBase.db")
    im=vt.cursor()
    im.execute(cümlecik)
    if donus istiyorsan:
        veriler=im.fetchall()
        return veriler
    vt.commit()"""

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('GirdapNote.ui', self)

        self.baslangic()
        self.buttonCikis.clicked.connect(self.Cikis)
        # self.buttonDersEkle.clicked.connect(self.dersEkle)
        self.lineEditSearch.textChanged[str].connect(self.Search)
        self.show()
    def baslangic(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #main window tittle gizleme
        self.buttonYeniNot.setIcon(QIcon('logo\yeniNoteLogo.png'))
        self.buttonAyarlar.setIcon(QIcon('logo\settings.png'))
        self.buttonCikis.setIcon(QIcon('logo\close.png'))
        self.lineEditSearch.addAction(QIcon('logo\search.png'),QLineEdit.LeadingPosition)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.lineEditSearch.setPlaceholderText('Search...')
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.centralWidget2 = QWidget(self)


    def Cikis(self):
        window.close()
    def showTime(self):
        self.labelSaat.setText(QTime.currentTime().toString('hh:mm:ss'))
        self.labelTarih.setText(str(date.today().strftime("%d/%m/%Y")))

    def metinAlYaz(self):
        #vtVeriler = veritabaniSorgu("""Select * from dersler""", 1)
        vtVeriler=[[1,2],[2,4],[3,6],[4,8],[5,10]]
        for i in vtVeriler:

    def metinYaz(self):
        yeniWidget=QWidget(self)
        yeniWidget.setGeometry(0,0,260,100)
        yeniButton=QPushButton(str(date.today().strftime("%d/%m")),yeniWidget)
        yeniWidget.setStyleSheet("background-color:rgb(234,182,118)")
        yeniLabel=QLabel("Yazi",yeniWidget)
        yeniLabel.resize(220,70)
        yeniLabel.move(0,30)
        yeniLabelKonu = QLabel("", yeniWidget)
        yeniLabelKonu.setStyleSheet("background-color:rgb(226,135,67)")
        yeniLabelKonu.resize(260, 10)
        yeniLabelKonu.move(0, 0)
        yeniButton.resize(40,15)
        yeniButton.move(220,10)
        yeniWidget.setGeometry(0, 0, 260, 100)
        yeniWidget.setFixedHeight(100)
        self.layout.addWidget(yeniWidget)
        self.centralWidget2.setLayout(self.layout)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.centralWidget2)

    def deneme(self):
        layout = QVBoxLayout(self)
        centralWidget = QWidget()
        for i in range(50):
            print(i)
            labelOlustur = QLabel(str(i))
            labelOlustur.setGeometry(0, 5, 300, 200)
            labelOlustur.setFixedHeight(200)
            layout.addWidget(labelOlustur)
        centralWidget.setLayout(layout)
        self.scrollArea.setWidget(centralWidget)

    def Search(self):
        print(self.lineEditSearch.text())
        self.metinYaz()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
"""
        layout = QVBoxLayout(self)
        centralWidget = QWidget()
        for i in range(50):
            print(i)
            labelOlustur=QLabel(str(i))
            labelOlustur.setGeometry(0,5,300,60)
            layout.addWidget(labelOlustur)
        centralWidget.setLayout(layout)
        self.scrollArea.setWidget(centralWidget)
"""
#button.clicked.connect(lambda ch,j=int(rowPosition): self.DersSil(j,vtVeriler))