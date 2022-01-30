import QRFixedPatterns as FP
import QRGenerBinaire as GB
import Constante as C

def messagePose(M, Y, X, D):

    print( len(GB.liste)-1)
    etat = 0
    while M < len(GB.liste):
    # while M < 7:
        tabCara = GB.liste[M]
        tabCara = list(tabCara.strip())
        while len(tabCara) < 8:
            tabCara.insert(0, 0)

        while D > 0:
            message = tabCara[D]        #charge le cara
            if etat == 0:
                if FP.A[Y, X] == 0:         #verifie que la case devant et vide
                    FP.A[Y, X] = message    #si ok ecrit et decale a gauche et charge le prochain caractere
                    D = D - 1
                    message = tabCara[D]
                X = X - 1


                if FP.A[Y, X] == 0:         #verifie que la case devant et vide
                    FP.A[Y, X] = message    #si ok ecrit et decale en haut a droite et charge le prochain caractere
                    D = D - 1
                X = X + 1
                if Y == 0:
                    X = X - 2
                    etat = 1
                else:
                    Y = Y - 1

            #---------------------vers le bas------------------#
            elif etat == 1:
                if FP.A[Y, X] == 0:         #verifie que la case devant et vide
                    FP.A[Y, X] = message    #si ok ecrit et decale a gauche et charge le prochain caractere
                    D = D - 1
                    message = tabCara[D]
                X = X - 1                   #si il y a queleque chose decalde a gauche


                if FP.A[Y, X] == 0:         #verifie que la case devant et vide
                    FP.A[Y, X] = message    #si ok ecrit et decale en haut a droite et charge le prochain caractere
                    D = D - 1
                X = X + 1
                if Y == C.V1-1:
                    etat = 0
                    X = X - 2
                else:
                    Y = Y + 1
        D = 7
        M = M + 1









