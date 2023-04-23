import os
from datetime import datetime
from tkinter import Canvas, PhotoImage, Tk

import requests

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def getPrice():
    url = "http://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")
    canvas.delete("text")
    canvas.create_text((250, 50), text=f"{price}$", fill="orange", tags=("text"))
    canvas.create_text(
        (250, 100), text=f"Updated At: {time}", fill="orange", tags=("text")
    )
    window.after(1000, getPrice)


window = Tk()
crypto = PhotoImage(file=f"{FILE_PATH}/Crypto.ppm")
background = PhotoImage(file=f"{FILE_PATH}/Background.ppm")
canvas = Canvas(window, width=500, height=500)
window.title("Bitcoin Price")
canvas.pack()
window.geometry("500x500")
canvas.create_image(100, 100, image=background)
canvas.create_image(250, 250, anchor="center", image=crypto)
getPrice()
window.mainloop()
