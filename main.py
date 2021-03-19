import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

htmlprice = ""
date = 0
coinname = ""
coinprice = ""


root = Tk()

icon = PhotoImage(file = 'logo.png')

root.iconphoto(False, icon)
#Tkinter window settings
w = 800
h = 650
root.title("TheCoinProject")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
canvas1 = tk.Canvas(root, width = 700, height = 600)
canvas1.pack()

#Month Selector
month = StringVar(root)
month.set("January")
monthchooser = OptionMenu(root, month, "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
canvas1.create_window(350, 200, window=monthchooser)

#Year selector
year = StringVar(root)
year.set("2013")
yearchooser = OptionMenu(root, year, "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021")
canvas1.create_window(550, 200, window=yearchooser)

#day selector
day = StringVar(root)
day.set("5")
daychooser = OptionMenu(root, day, "09", "12")
canvas1.create_window(150, 200, window=daychooser)

#Coin Selector
crypto = StringVar(root)
crypto.set("bitcoin")
cryptochooser = OptionMenu(root, crypto, "ethereum", "xrp", "bitcoincash", "eos", "stellar", "litecoin", "tether", "cardano", "monero", "dash", "iota")
canvas1.create_window(350, 400, window=cryptochooser)

#Tkinter text inputs
#date = tk.Entry(root)
#canvas1.create_window(350, 140, window=date)

#coinname = tk.Entry(root)
#canvas1.create_window(350, 200, window=coinname)


def getSquareRoot():
    x1 = coinprice

    label1 = tk.Label(root, text=x1)
    canvas1.create_window(350, 450, window=label1)


def getPrice():
    global coinprice

    URL = "https://coinmarketcap.com/historical/" + year.get() + m + day.get() + "/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find(class_='cmc-main-section')

    prices = table.find_all('td', 'cmc-table__cell--sort-by__price')

    #The price of the coin in html format (before.get_text)
    htmlprice = table.find(href=re.compile("currencies/" + crypto.get() + "/markets/"))

    coinprice = htmlprice.get_text()
    getSquareRoot()

    print(year.get() + day.get(), month.get())
    print(coinprice)

def convertMonth():
    global m

    if month.get() == "January":
        m = "01"

    if month.get() == "Febuary":
        m = "02"

    if month.get() == "March":
        m = "03"

    if month.get() == "April":
        m = "04"

    if month.get() == "May":
        m = "05"

    if month.get() == "June":
        m = "06"

    if month.get() == "July":
        m = "07"

    if month.get() == "August":
        m = "08"

    if month.get() == "September":
        m = "09"

    if month.get() == "October":
        m = "10"

    if month.get() == "November":
        m = "11"

    if month.get() == "December":
        m = "12"


#Tkinter buttons
button1 = tk.Button(text='Coin Price', command=lambda: [convertMonth(), getPrice()])
canvas1.create_window(350, 500, window=button1)



root.mainloop()