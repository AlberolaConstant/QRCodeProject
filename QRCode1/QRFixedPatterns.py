import numpy as np
import matplotlib.pyplot as plt
import Constante as C

#creation taille matrice
A = np.zeros((C.VersionQR, C.VersionQR))

def carreG(Y = 0, X = 0, C = 0):
    while C < 6:
        A[Y,X] = 0.9
        A[Y, X+6] = 0.9
        Y = Y + 1
        C = C + 1
    C = 0

    while C < 7:
        A[Y, X] = 0.9
        A[Y-6, X] = 0.9
        X = X + 1
        C = C + 1

def carre_blanc(Y = 1, X = 1, C = 0):
    while C < 5:
        A[Y, X] = 0.1
        A[Y, X+4] = 0.1
        Y = Y + 1
        C = C + 1
    C = 0
    Y = Y - 5
    while C < 5:
        A[Y, X] = 0.1
        A[Y+4, X] = 0.1
        X = X + 1
        C = C + 1

def petit_carre(X = 2, Y = 2, C = 0):
    while C < 3:
        A[Y, X] = 0.9
        Y = Y + 1
        A[Y, X] = 0.9
        Y = Y + 1
        A[Y, X] = 0.9
        X = X + 1
        Y = Y - 2
        C = C + 1

def fixedP():
    y = 8
    while y < C.VersionQR - 8:
        A[y, 6] = 0.9
        y = y + 1
        A[y, 6] = 0.1
        y = y + 1

    x = 8
    while x < C.VersionQR - 8:
        A[6, x] = 0.9
        x = x + 1
        A[6, x] = 0.1
        x = x + 1

    A[C.VersionQR-8, 8] = 0.9

def carreBlancV(X=7, Y=0, C=0):
    while C < 8:
        A[Y, X] = 0.1
        A[X, Y] = 0.1
        Y = Y + 1
        C = C + 1

def calibrageV2(X=C.VersionQR, Y=C.VersionQR, C=0):
    while C < 4:
        A[Y, X] = 0.9
        A[X, Y] = 0.9
        Y = Y - 1
        C = C + 1
    while C < 9:
        A[Y, X] = 0.9
        A[X, Y] = 0.9
        X = X - 1
        C = C + 1

def calibrageV3(X=C.VersionQR, Y=C.VersionQR, C=0):
    while C < 2:
        A[Y, X] = 0.1
        A[X, Y] = 0.1
        Y = Y - 1
        C = C + 1
    while C < 5:
        A[Y, X] = 0.1
        A[X, Y] = 0.1
        X = X - 1
        C = C + 1
    A[Y+1, X+2] = 0.9

def calibragePattern():
    carreG(Y=0, X=0)
    carre_blanc(Y=1, X=1)
    petit_carre(Y=2, X=2)
    carreBlancV(X=7, Y=0, C=0)

    carreG(Y=0, X=C.VersionQR-7)
    carre_blanc(Y=1, X=C.VersionQR-6)
    petit_carre(Y=2, X=C.VersionQR-5)
    carreBlancV(X=7, Y=C.VersionQR-8, C=0)

    carreG(Y=C.VersionQR-7, X=0)
    carre_blanc(Y=C.VersionQR-6, X=1)
    petit_carre(Y=C.VersionQR-5, X=2)
    carreBlancV(X=C.VersionQR-8, Y=0, C=0)

    fixedP()

    if C.VersionQR > 25:
        calibrageV2(X=C.VersionQR - 5 , Y=C.VersionQR - 5, C=0)
        calibrageV3(X=C.VersionQR - 6, Y=C.VersionQR - 6, C=0)


