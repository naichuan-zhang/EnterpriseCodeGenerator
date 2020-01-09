import qrcode

encoder = qrcode.make("667767789912")
encoder.save("667767789912.png")

img = qrcode.make("https://github.com/naichuan-zhang")
img.save("naichuan.png")

qr = qrcode.QRCode(version=2, error_correction=qrcode.ERROR_CORRECT_L,
                   box_size=8, border=10)
qr.add_data("https://www.mingrisoft.com")
qr.make(fit=True)
img = qr.make_image()
img.show()
img.save("naichuan2.png")
