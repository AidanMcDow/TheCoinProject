from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QComboBox, QGroupBox, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys
from bs4 import BeautifulSoup
import requests
import re


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'The Coin Project'
        self.left = 650
        self.top = 250
        self.width = 800
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("./venv/include/logo.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.horizontalLayout()
        self.verticalLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.verticalGroupBox)
        self.setLayout(windowLayout)



        self.show()
        sys.exit(app.exec_())

    def verticalLayout(self):
        self.verticalGroupBox = QGroupBox()
        vlay = QVBoxLayout()

        #Button
        insert = QPushButton("Check", self)
        insert.move(400, 400)
        insert.clicked.connect(self.getPrice)

        vlay.addWidget(insert)
        insert.resize(100, 40)

        self.verticalGroupBox.setLayout(vlay)

    def horizontalLayout(self):

        global mselect
        global dselect
        global yselect
        global cselect
        global hlay

        coinprice = ""

        self.horizontalGroupBox = QGroupBox("Crypto Time Period")
        hlay = QHBoxLayout()

        #Combobox
        cselect = QComboBox(self)
        cselect.addItem("bitcoin")
        cselect.addItem("Ethereum")
        cselect.addItem("EOS")
        cselect.addItem("Doge")
        cselect.addItem("Litecoin")

        hlay.addWidget(cselect)
        cselect.resize(100, 40)


        dselect = QComboBox(self)
        dselect.addItem("1")
        dselect.addItem("02")
        dselect.addItem("3")
        dselect.addItem("4")
        dselect.addItem("5")
        dselect.addItem("6")
        dselect.addItem("7")
        dselect.addItem("8")
        dselect.addItem("9")
        dselect.addItem("10")
        dselect.addItem("11")

        dselect.resize(100, 40)
        hlay.addWidget(dselect)

        mselect = QComboBox(self)
        mselect.addItem("1")
        mselect.addItem("2")
        mselect.addItem("3")
        mselect.addItem("4")
        mselect.addItem("5")
        mselect.addItem("6")
        mselect.addItem("07")
        mselect.addItem("8")
        mselect.addItem("9")
        mselect.addItem("10")
        mselect.addItem("11")

        mselect.resize(100, 40)
        hlay.addWidget(mselect)

        yselect = QComboBox(self)
        yselect.addItem("2021")
        yselect.addItem("2020")
        yselect.addItem("2019")
        yselect.addItem("2018")
        yselect.addItem("2017")
        yselect.addItem("2016")
        yselect.addItem("2015")
        yselect.addItem("2014")
        yselect.addItem("2013")

        yselect.resize(100, 40)
        hlay.addWidget(yselect)

        if (coinprice != ""):
            pricelabel = QLabel(self)
            pricelabel.setText(coinprice)
            hlay.addWidget(pricelabel)

        self.horizontalGroupBox.setLayout(hlay)
        print(yselect.currentText() + dselect.currentText(), mselect.currentText())

    @pyqtSlot()
    def getPrice(self):
        global coinprice

        print(yselect.currentText() + dselect.currentText() + mselect.currentText())

        URL = "https://coinmarketcap.com/historical/" + yselect.currentText() + dselect.currentText() + mselect.currentText() + "/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        table = soup.find(class_='cmc-main-section')

        prices = table.find_all('td', 'cmc-table__cell--sort-by__price')

        # The price of the coin in html format (before.get_text)
        htmlprice = table.find(href=re.compile("currencies/" + cselect.currentText() + "/markets/"))

        coinprice = htmlprice.get_text()

        pricelabel = QLabel(self)
        pricelabel.setText(coinprice)
        hlay.addWidget(pricelabel)

        print(coinprice)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
