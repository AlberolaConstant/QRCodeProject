# qr code

import qrcode

#img = qrcode.make('http://ens.casali.me/')
#img.ERROR_CORRECT_H
#img.save('logoQRcode.png')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,#7 % error corrected
    box_size=100,
    border=3
)
qr.add_data('1')
qr.make()
img = qr.make_image(fill_color="black", back_color="white")
img.save('logoQRcode2.png')