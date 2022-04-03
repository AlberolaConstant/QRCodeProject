import QRFixedPatterns as FP
import Constante as C

info = [0.1, 0.1, 0.1, 0.1,0.1]

formatErrorCorrectionQ = [0.1,0.9]
formatEncodage = [0, 1, 0, 0]

errorCorrectionLevel = C.errorCorrectionL

formatEncodageM0 = [0.1,0.9,0.1,0.9,0.9,0.9,0.9,0.9]
# formatEncodageM3 = [0.9,0.9,0.9,0.9,0.1,0.1,0.1,0.9,0.1,0.1,0.9,0.9,0.9,0.1,0.9]


def zerogauche(format):
    if format[0] == 0:
        format.remove(0)

def xorBetween(format, poly):
    xor = []
    for i in range(len(format)):
        xor.append(format[i] ^ poly[i])
    return xor

def formatPoly(format,poly):
    while len(poly) < len(format):
        poly.append(0)

def polynomeformat(format=C.chaineforma):
    poly = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1]
    speL = [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
    startforma = C.errorCorrection + C.mask
    while len(format) < 14:
        format.append(0)
        zerogauche(format)

    while len(format) > 10:
        formatPoly(format, poly)
        format = xorBetween(format, poly)
        zerogauche(format)

    if len(format) < 10:
        while len(format) < 10:
            format.append(0)
            zerogauche(format)

    format = startforma + format
    format = xorBetween(format, speL)
    return format

formatCorrectionErreur = polynomeformat(format=C.chaineforma)
print(polynomeformat())

def FormatErrorCorrectionhorizontale(y = 8, d = 0, x =0):
    while d < 7:
        if FP.A[y, x] == 0.9:
            x = x + 1
        FP.A[y,x] = formatCorrectionErreur[d]
        # print('gauche', formatCorrectionErreur[d])
        x = x + 1
        d = d + 1
    x = C.VersionQR-8
    while d < 15:
        FP.A[y, x] = formatCorrectionErreur[d]
        # print('droite', formatCorrectionErreur[d])
        x = x + 1
        d = d + 1


def FormatErrorCorrectionVerticale(y = C.VersionQR-1, d = 0, x = 8):
    while d < 7:
        if FP.A[y, x] == 0.9:
            y = y - 1
            d +=1
        FP.A[y,x] = formatCorrectionErreur[d]
        # print('bas', formatCorrectionErreur[d])
        y = y - 1
        d = d + 1
    y = 8
    while d < 15:
        if FP.A[y, x] == 0.9:
            y = y - 1
        FP.A[y, x] = formatCorrectionErreur[d]
        # print('haut', formatCorrectionErreur[d])
        y = y - 1
        d = d + 1


def FormatErrorCorrectionhorizontaleVide(y = 8, d = 0, x =0): #C.VersionQR - 10
    while d < 7:
        if FP.A[y, x] == 0.9:
            x = x + 1
        FP.A[y,x] = 0.1
        # print('gauche', formatCorrectionErreur[d])
        x = x + 1
        d = d + 1
    x = C.VersionQR-8
    while d < 15:
        FP.A[y, x] = 0.1
        # print('droite', formatCorrectionErreur[d])
        x = x + 1
        d = d + 1


def FormatErrorCorrectionVerticaleVide(y = C.VersionQR-1, d = 0, x = 8):
    while d < 7:
        if FP.A[y, x] == 0.9:
            y = y - 1
            d +=1
        FP.A[y,x] = 0.1
        # print('bas', formatCorrectionErreur[d])
        y = y - 1
        d = d + 1
    y = 8
    while d < 15:
        if FP.A[y, x] == 0.9:
            y = y - 1
        FP.A[y, x] = 0.1
        # print('haut', formatCorrectionErreur[d])
        y = y - 1
        d = d + 1

def FormatEncodage(y = C.VersionQR - 1,x = C.VersionQR - 1,d = 0):

    while d < 4:
        FP.A[y, x] = formatEncodage[d]
        x = x - 1
        d = d + 1
        FP.A[y, x] = formatEncodage[d]
        x = x + 1
        y = y - 1
        d = d + 1


def InfoVide():
    FormatErrorCorrectionhorizontaleVide()
    FormatErrorCorrectionVerticaleVide()
    FormatEncodage()


def InfoPlein():
    FormatErrorCorrectionhorizontale()
    FormatErrorCorrectionVerticale()


