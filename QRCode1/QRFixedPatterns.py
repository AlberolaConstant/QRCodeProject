import numpy as np
import matplotlib.pyplot as plt

V1 = 21

#creation taille matrice
A = np.zeros((V1, V1))

def carreG(Y = 0, X = 0, C = 0):
    while C < 6:
        A[Y,X] = 1
        A[Y, X+6] = 1
        Y = Y + 1
        C = C + 1
    C = 0

    while C < 7:
        A[Y, X] = 1
        A[Y-6, X] = 1
        X = X + 1
        C = C + 1

def carre_blanc(Y = 1, X = 1, C = 0):
    while C < 4:
        A[Y, X] = 0
        A[Y, X+4] = 0
        Y = Y + 1
        C = C + 1
    C = 0
    Y = Y - 4
    while C < 1:
        A[Y, X] = 0
        A[Y+3, X] = 0
        X = X + 1
        C = C + 1
def petit_carre(X = 2, Y = 2, C = 0):
    while C < 3:
        A[Y, X] = 1
        Y = Y + 1
        A[Y, X] = 1
        Y = Y + 1
        A[Y, X] = 1
        X = X + 1
        Y = Y - 2
        C = C + 1

def fixedP():
    y = 8
    while y < V1-8:
        A[y, 6] = 1
        y = y + 2

    x = 8
    while x < V1 - 8:
        A[6, x] = 1
        x = x + 2

    A[V1-8, 8] = 1

def carreBlancV(X=7, Y=0, C=0):
    while C < 7:
        A[Y, X] = 0
        Y = Y + 1
        C = C + 1


    while C < 1:
        print(X)
        print ('Y',Y)
        C = C + 1



def calibragePattern():
    carreG(Y=0, X=0)
    carre_blanc(Y=1, X=1)
    petit_carre(Y=2, X=2)
    carreBlancV(X=7, Y=0, C=0)

    carreG(Y=0, X=V1-7)
    carre_blanc(Y=1, X=V1-6)
    petit_carre(Y=2, X=V1-5)
    carreBlancV(X=7, Y=V1-7, C=0)

    carreG(Y=V1-7, X=0)
    carre_blanc(Y=V1-6, X=1)
    petit_carre(Y=V1-5, X=2)
    carreBlancV(X=V1-8, Y=0, C=0)

    fixedP()

# print(A)
# plt.imshow(A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
# plt.show()


