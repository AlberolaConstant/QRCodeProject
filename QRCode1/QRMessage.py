import QRFixedPatterns as FP
import QRGenerBinaire as GB
import Constante as C

"""pose le message dans la matrix en esquivant les bloc qui on deja une valeur"""

def messagePose(M, Y, X, D):

    etat = 0
    while M < len(GB.liste):
    # while M < 7:
        tabCara = GB.liste[M]
        tabCara = list(tabCara.strip())
        while len(tabCara) < 8:
            tabCara.insert(0, 0)

        while D < 7:
            message = tabCara[D]
            if etat == 0:
                if FP.A[Y, X] == 0:
                    FP.A[Y, X] = message
                    D = D + 1
                    message = tabCara[D]
                X = X - 1


                if FP.A[Y, X] == 0:
                    FP.A[Y, X] = message
                    D = D + 1
                X = X + 1
                if Y == 0:
                    X = X - 2
                    etat = 1
                else:
                    Y = Y - 1

            #---------------------vers le bas------------------#
            elif etat == 1:
                if FP.A[Y, X] == 0:
                    FP.A[Y, X] = message
                    D = D + 1
                    message = tabCara[D]
                X = X - 1


                if FP.A[Y, X] == 0:
                    FP.A[Y, X] = message
                    D = D + 1
                X = X + 1
                if Y == C.VersionQR-1:
                    etat = 0
                    X = X - 2
                else:
                    Y = Y + 1
        D = 0
        M = M + 1









