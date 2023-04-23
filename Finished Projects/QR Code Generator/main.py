import os

import qrcode

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


def Generate_QRCode():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"https://www.{url}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{FILE_PATH}/{name}.png")


url = input("URL https://www.")
name = input("Name: ")
Generate_QRCode()
