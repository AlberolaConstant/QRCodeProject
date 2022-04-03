import numpy as np
import matplotlib.pyplot as plt
import Constante as C

#creation taille matrice
A = np.zeros((C.VersionQR, C.VersionQR))

def GrandCarreNoir(Y = 0, X = 0, C = 0):
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

def PetitCarreNoir(X = 2, Y = 2, C = 0):
    while C < 3:
        A[Y, X] = 0.9
        Y = Y + 1
        A[Y, X] = 0.9
        Y = Y + 1
        A[Y, X] = 0.9
        X = X + 1
        Y = Y - 2
        C = C + 1

def ModelesSynchronisation():
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

def EspacementBlanc(X=7, Y=0, C=0):
    while C < 8:
        A[Y, X] = 0.1
        A[X, Y] = 0.1
        Y = Y + 1
        C = C + 1

def CarreCalibrage(X=C.VersionQR-5, Y=C.VersionQR-5, C=0):
    while C < 4:
        A[Y, X] = 0.9
        Y = Y - 1
        C = C + 1
    while C < 8:
        A[Y, X] = 0.9
        X = X - 1
        C = C + 1
    while C < 12:
        A[Y, X] = 0.9
        Y = Y + 1
        C = C + 1
    while C < 16:
        A[Y, X] = 0.9
        X = X + 1
        C = C + 1

    Y = Y-1
    X = X-1
    while C < 18:
        A[Y, X] = 0.1
        Y = Y - 1
        C = C + 1
    while C < 20:
        A[Y, X] = 0.1
        X = X - 1
        C = C + 1
    while C < 22:
        A[Y, X] = 0.1
        Y = Y + 1
        C = C + 1
    while C < 24:
        A[Y, X] = 0.1
        X = X + 1
        C = C + 1
    A[Y-1, X-1] = 0.9

def Version10():
    CarreCalibrage(X=C.VersionQR-5, Y=C.VersionQR-5, C=0)
    CarreCalibrage(X=C.VersionQR - 27, Y=C.VersionQR - 5, C=0)
    CarreCalibrage(X=C.VersionQR - 5, Y=C.VersionQR - 27, C=0)
    CarreCalibrage(X=C.VersionQR - 27, Y=C.VersionQR - 27, C=0)
    CarreCalibrage(X=C.VersionQR - 49, Y=C.VersionQR - 27, C=0)
    CarreCalibrage(X=C.VersionQR - 27, Y=C.VersionQR - 49, C=0)

def VersionQuarente():
    x = C.VersionQR - 5
    y = C.VersionQR - 5
    while y > 3:
        while x > 3:
            if y == 4:
                y = 8
                if x == C.VersionQR - 5:
                    x = x - 28
            if x > 5:
                CarreCalibrage(X=x, Y=y, C=0)
            else :
                if A[y-1, 7] != 0.1:
                    x = 8
                    CarreCalibrage(X=x, Y=y, C=0)
                else:
                    break
            x = x - 28
        y = y - 28
        x = C.VersionQR - 5

def calibragePattern():
    # carre gauche
    GrandCarreNoir(Y=0, X=0)
    carre_blanc(Y=1, X=1)
    PetitCarreNoir(Y=2, X=2)
    EspacementBlanc(X=7, Y=0, C=0)
    # carre droit
    GrandCarreNoir(Y=0, X=C.VersionQR - 7)
    carre_blanc(Y=1, X=C.VersionQR-6)
    PetitCarreNoir(Y=2, X=C.VersionQR - 5)
    EspacementBlanc(X=7, Y=C.VersionQR - 8, C=0)
    # carre bas
    GrandCarreNoir(Y=C.VersionQR - 7, X=0)
    carre_blanc(Y=C.VersionQR-6, X=1)
    PetitCarreNoir(Y=C.VersionQR - 5, X=2)
    EspacementBlanc(X=C.VersionQR - 8, Y=0, C=0)

    if C.VersionQR > 24 and C.VersionQR < 56:
        CarreCalibrage(X=C.VersionQR - 5, Y=C.VersionQR - 5, C=0)
    if C.VersionQR == 57:
        Version10()
    if C.VersionQR == 177:
        VersionQuarente()

    ModelesSynchronisation()
