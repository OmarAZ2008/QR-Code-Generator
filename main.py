from qr.qrcode import QRCode

qr = QRCode("Hello World1234")

qr.encode_data()

def exp_to_int(exp):
    val = 1
    for _ in range(exp):
        val *= 2
        if val > 255:
            val = val^285
    return val
print(exp_to_int(254))
        

