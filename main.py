from qr.qrcode import QRCode
from qr.EC import get_EC_codewords

qr = QRCode("Hello")

qr.encode_data()

qr.structure_data()

qr.generate_EC_codewords()

qr.structure_data_EC()

#print(qr.version)
#print(qr.data_codewords)
#print(qr.group1_data)
#print(qr.group2_data)
#print(qr.group1_EC)
#print(qr.group2_EC)
#print(qr.codewords)
