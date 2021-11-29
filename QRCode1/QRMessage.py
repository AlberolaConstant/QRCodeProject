import QRFixedPatterns as FP
import QRGenerBinaire as GB


def DGBH(M, Y, X, D):

    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    while len(tabCara) < 8:
        tabCara.insert(0,0)

    while D < 7:
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X - 1
        D = D + 1
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X + 1
        Y = Y - 1
        D = D + 1



def DGHB(M, Y, X, D):

    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    while len(tabCara) < 8:
        tabCara.insert(0,0)

    while D < 7:
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X - 1
        D = D + 1
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X + 1
        Y = Y + 1
        D = D + 1

def RVB (M, Y, X, D):

    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    while len(tabCara) < 8:
        tabCara.insert(0,0)

    while D < 3:
        message = tabCara[D]
        FP.A[Y,X] = message
        X = X - 1
        D = D + 1
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X + 1
        Y = Y - 1
        D = D + 1

    Y = 9
    X = FP.V1 - 3
    D = 4
    while D < 7:
        message = tabCara[D]
        FP.A[Y,X] = message
        X = X - 1
        D = D + 1
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X + 1
        Y = Y + 1
        D = D + 1

def RVH (M, Y, X, D):

    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    while len(tabCara) < 8:
        tabCara.insert(0,0)

    while D < 3:
        message = tabCara[D]
        FP.A[Y,X] = message
        X = X - 1
        D = D + 1
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X + 1
        Y = Y + 1
        D = D + 1

    Y = FP.V1 - 1
    X = FP.V1 - 5
    D = 4
    while D < 7:
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X - 1
        D = D + 1
        message = tabCara[D]
        FP.A[Y, X] = message
        X = X + 1
        Y = Y - 1
        D = D + 1