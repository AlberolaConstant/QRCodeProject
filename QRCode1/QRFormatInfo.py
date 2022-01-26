import QRFixedPatterns as FP

errorCorrectionL = [1, 1]
mask1 = [0, 0, 1]
formatErrorCorrection = [1, 0]
formatEncodage = [0, 0, 1, 0]


def ErrorCorrection():      #correction d'erreur (à terminer quand on sera plus intelligents XD)
    y = 1
    x = 0
    d = 0
    while y < 3:
        FP.A[FP.V1 - y, 8] = errorCorrectionL[d]
        FP.A[8,x] = errorCorrectionL[d]
        y = y + 1
        d = d + 1
        x = x + 1



def Mask1():    #Affiche la version du masque
    y = 3
    d = 0
    x = 2
    while y < 6:
        FP.A[FP.V1 - y, 8] = mask1[d]
        FP.A[8, x] = mask1[d]
        y = y + 1
        x = x + 1
        d = d + 1

def FormatErrorCorrection():
    y = 6
    d = 0
    x = 5
    while y < 8:
        FP.A[FP.V1 - y, 8] = formatErrorCorrection[d]
        FP.A[8, x] = formatErrorCorrection[d]
        y = y + 1
        x = x + 2
        d = d + 1

def FormatEncodage():       #Affiche l'encodage du QR code
    y = FP.V1 - 1
    x = FP.V1 - 1
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
    FormatEncodage()