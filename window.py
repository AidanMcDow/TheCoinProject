from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QComboBox, QGroupBox, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import sys

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
        self.createHorizontalLayout()
        self.verticalLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(self.verticalGroupBox)
        self.setLayout(windowLayout)



        self.show()
        sys.exit(app.exec_())

    def verticalLayout(self):
        self.verticalGroupBox = QGroupBox("Vertical Layout")
        vlay = QVBoxLayout()

        mselect = QComboBox(self)
        mselect.addItem("Bitcoin")
        mselect.addItem("Ethereum")
        mselect.addItem("EOS")
        mselect.addItem("Doge")
        mselect.addItem("Litecoin")

        vlay.addWidget(mselect)
        mselect.resize(100, 40)

        self.verticalGroupBox.setLayout(vlay)

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("Crypto Time Period")
        layout = QHBoxLayout()

        #Button
        insert = QPushButton("Check", self)
        insert.move(400, 400)
        insert.clicked.connect(self.onClick)

        #Combobox
        mselect = QComboBox(self)
        mselect.addItem("Bitcoin")
        mselect.addItem("Ethereum")
        mselect.addItem("EOS")
        mselect.addItem("Doge")
        mselect.addItem("Litecoin")

        layout.addWidget(mselect)
        mselect.resize(100, 40)


        dselect = QComboBox(self)
        dselect.addItem("1")
        dselect.addItem("2")
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
        layout.addWidget(dselect)

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
        layout.addWidget(yselect)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def onClick(self):
        print('Button click!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
