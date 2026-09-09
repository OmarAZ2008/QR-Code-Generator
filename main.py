from qr.qrcode import QRCode

qr = QRCode("Hello World1234110851666ssc")

qr.encode_data()

qr.structure_data()

print(qr.version)
print(qr.data_codewords)
print(qr.group1_data)
print(qr.group2_data)