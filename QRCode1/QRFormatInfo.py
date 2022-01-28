import QRFixedPatterns as FP
import Constante as C


formatErrorCorrection = [1, 0]
formatEncodage = [0, 1, 0, 0]


def ErrorCorrection():
    y = 1
    x = 0
    d = 0
    while y < 3:
        FP.A[C.V1 - y, 8] = C.errorCorrectionL[d]
        FP.A[8,x] = C.errorCorrectionL[d]
        y = y + 1
        d = d + 1
        x = x + 1



def Mask1():
    y = 3
    d = 0
    x = 2
    while y < 6:
        FP.A[C.V1 - y, 8] = C.mask[d]
        FP.A[8, x] = C.mask[d]
        y = y + 1
        x = x + 1
        d = d + 1

def FormatErrorCorrection():
    y = 6
    d = 0
    x = 5
    while y < 8:
        FP.A[C.V1 - y, 8] = formatErrorCorrection[d]
        FP.A[8, x] = formatErrorCorrection[d]
        y = y + 1
        x = x + 2
        d = d + 1

def FormatEncodage():
    y = C.V1 - 1
    x = C.V1 - 1
    d = 0
    while d < 3:
        FP.A[y, x] = formatEncodage[d]
        x = x - 1
        d = d + 1
        FP.A[y, x] = formatEncodage[d]
        x = x + 1
        y = y - 1
        d = d + 1


def InfoH():
    ErrorCorrection()
    Mask1()
    FormatErrorCorrection()