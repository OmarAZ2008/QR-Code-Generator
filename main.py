from qr.qrcode import QRCode

qr = QRCode("https://omaraz2008.itch.io/box")
print(qr.data_length)
print(qr.version)
print(len(qr.matrix), len(qr.matrix[0]))