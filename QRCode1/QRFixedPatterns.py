import numpy as np
import matplotlib.pyplot as plt

V1 = 21

#creation taille matrice
A = np.zeros((V1, V1))

def carreG(Y = 0, X = 0):
    while Y < 7:
        A[Y,0] = 1
        A[Y, 6] = 1
        Y = Y + 1

    while X < 7:
        A[0, X] = 1
        A[6, X] = 1
        X = X + 1

def carre_blanc(Y = 1, X = 1):
    while Y < 5:
        A[Y, 1] = 0
        A[Y, 5] = 0
        Y = Y + 1

    while X < 5:
        A[1, X] = 0
        A[5, X] = 0
        X = X + 1
def petit_carre(x = 2, y = 2):
    while x < 5:
        A[y, x] = 1
        y = y + 1
        A[y, x] = 1
        y = y + 1
        A[y, x] = 1
        x = x + 1
        y = y - 2



# def carreGB(y = V1 - 7, x = 0):
#     while y < V1:
#         A[y,0] = 1
#         A[y, 6] = 1
#         y = y + 1
#
#     while x < 7:
#         A[V1-7, x] = 1
#         A[V1-1, x] = 1
#         x = x + 1
#
#      #petit carre
#
#     x2 = 2
#     while x2 < 5:
#         A[V1-5, x2] = 1
#         A[V1-4, x2] = 1
#         A[V1-3, x2] = 1
#         x2 = x2 + 1
#
# def carreD(y = 0, x = V1 - 6):
#     while y < 7:
#         A[y, V1-7] = 1
#         A[y, V1-1] = 1
#         y = y + 1
#
#     while x < V1:
#         A[0, x] = 1
#         A[6, x] = 1
#         x = x + 1
#
#     # petit carre
#
#     x2 = V1 - 5
#     while x2 < V1 - 2:
#         A[2, x2] = 1
#         A[3, x2] = 1
#         A[4, x2] = 1
#         x2 = x2 + 1
#
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

def calibragePattern():
    for i in range(3):
        carreG(Y=0, X=0)
    carre_blanc()
    petit_carre()

    # carreD()
    # carreGB()
    fixedP()

# carreG()
# carreD()
# carreGB()
# fixedP()

# print(A)
# plt.imshow(A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
# plt.show()


