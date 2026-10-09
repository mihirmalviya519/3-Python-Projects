import qrcode
import os
import secrets

url = input("Enter your url : ")
image = qrcode.make(url)

filename = f"{secrets.token_hex(4)}"
path = os.path.join(os.getcwd(), filename)
image.save(path)