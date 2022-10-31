import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
sc = input("Enter the link")
qr = sc
  
# Generate QR code 
url = pyqrcode.create(qr) 
  
