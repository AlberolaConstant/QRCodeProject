import QRFixedPatterns as FP
import QRGenerBinaire as GB
import Constante as C


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
    X = X - 2
    Y = Y + 1
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

    X = X - 2
    Y = Y - 2
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


def messagePose(M, Y, X, D):

    print( len(GB.liste)-1)
    # while M < len(GB.liste):
    while M < 4:
        print (M)
        tabCara = GB.liste[M]
        print(tabCara)
        tabCara = list(tabCara.strip())
        while len(tabCara) < 8:
            tabCara.insert(0, 0)

        while D > 0:
            message = tabCara[D]        #charge le cara
            if FP.A[Y, X] == 0:         #verifie que la case devant et vide
                FP.A[Y, X] = message    #si ok ecrit et decale a gauche et charge le prochain caractere
                D = D - 1
                message = tabCara[D]
            X = X - 1                   #si il y a queleque chose decalde a gauche


            if FP.A[Y, X] == 0:         #verifie que la case devant et vide
                FP.A[Y, X] = message    #si ok ecrit et decale en haut a droite et charge le prochain caractere
                D = D - 1
            X = X + 1
            Y = Y - 1
        D = 7
        M = M + 1








