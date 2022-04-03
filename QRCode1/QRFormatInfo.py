import QRFixedPatterns as FP
import Constante as C

info = [0.1, 0.1, 0.1, 0.1,0.1]

formatErrorCorrectionQ = [0.1,0.9]
formatEncodage = [0.1, 0.9, 0.1, 0.1]

errorCorrectionLevel = C.errorCorrectionL

formatEncodageM0 = [0.1,0.9,0.1,0.9,0.9,0.9,0.9,0.9]
# formatEncodageM3 = [0.9,0.9,0.9,0.9,0.1,0.1,0.1,0.9,0.1,0.1,0.9,0.9,0.9,0.1,0.9]




def FormatEncodage(y = C.VersionQR - 1,x = C.VersionQR - 1,d = 0):

    while d < 4:
        FP.A[y, x] = formatEncodage[d]
        x = x - 1
        d = d + 1
        FP.A[y, x] = formatEncodage[d]
        x = x + 1
        y = y - 1
        d = d + 1

def Maskspace(y = C.VersionQR - 5, d = 0, x = 5):

    while d < 3:
        FP.A[y, 8] = 0.1
        FP.A[8, x] = 0.1
        y = y + 1
        x = x - 1
        d = d + 1

def ErrorCorrectionLevel(y=1, x=0, d=0, errorCorrection=errorCorrectionLevel):
    while y < 3:
        FP.A[C.VersionQR - y, 8] = errorCorrection[d]
        FP.A[8,x] = errorCorrection[d]
        y = y + 1
        d = d + 1
        x = x + 1

def FormatErrorCorrection(y = 6, d = 0, x = 5, formatErrorCorrection=formatErrorCorrectionQ):

    while d < 2:
        FP.A[C.VersionQR - y, 8] = formatErrorCorrection[d]
        if FP.A[8,x] == 0.9:
            x=x+1
        FP.A[8, x] = formatErrorCorrection[d]
        y = y + 1
        x = x + 1
        d = d + 1

def FormatErrorCorrectionD(y = 8, d = 0, x =C.VersionQR - 10):
    while d < 8:
        FP.A[y,x] = formatEncodageM0[d]
        x = x + 1
        d = d + 1

def FormatErrorCorrectionH(y =C.VersionQR - 14, d = 0, x = 8):
    while d < 8:
        FP.A[y, x] = formatEncodageM0[d]
        if FP.A[y-1, x] == 0.9:
            y = y - 1
        y = y - 1
        d = d + 1

# def plynomeformat(format=C.chaineforma):





def InfoVide():
    Maskspace(y=C.VersionQR - 5, d=0, x=4)
    FormatEncodage(y=C.VersionQR - 1, x=C.VersionQR - 1, d=0)
    FormatErrorCorrectionD(y=8, d=0, x=C.VersionQR - 8)
    ErrorCorrectionLevel(y=1, x=0, d=0, errorCorrection=info)
    FormatErrorCorrection(y=6, d=0, x=5, formatErrorCorrection=info)
    FormatErrorCorrectionH(y=C.VersionQR - 13, d=0, x=8)

def InfoPlein():
    ErrorCorrectionLevel()
    FormatErrorCorrection()


