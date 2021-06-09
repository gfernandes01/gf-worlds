import pyqrcode
from pyqrcode import QRCode

s = 'https://www.linkedin.com/in/gabriel-fernandes-ferreira-1244b319a/'
url = pyqrcode.create(s)

url.svg('qrcode.svg', scale=8)