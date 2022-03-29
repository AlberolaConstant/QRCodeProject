import QRFixedPatterns as FP
import Constante as C

def Mask0ApplicationPro(Y = 0, X = 0):
    # C.mask = C.mask0.copy()
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if (X + Y) % 2 == 0:
                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    X = X + 1
            else:
                X=X+1
        Y=Y+1
        X=0



def Mask1ApplicationPro(Y = 0, X = 0):
    while Y < C.VersionQR:
        if Y % 2 == 0:
            while X < C.VersionQR:

                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    break
            Y=Y+1
            X=0
        else:
            Y=Y+1
            X=0


def Mask2ApplicationPro(Y=0, X=0):
    while X < C.VersionQR:
        if X % 3 == 0:
            while Y < C.VersionQR:

                if FP.A[Y, X] == 1:
                    FP.A[Y, X] = 0
                    Y = Y + 1

                elif FP.A[Y, X] == 0:
                    FP.A[Y, X] = 1
                    Y = Y + 1

                else:
                    break
            X = X + 1
            Y = 0
        else:
            X = X + 1
            Y = 0

def Mask3ApplicationPro(Y = 0, X = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if (X + Y) % 3 == 0:
                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    X = X + 1
            else:
                X=X+1
        Y=Y+1
        X=0


def Mask4ApplicationPro(Y = 0, X = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if (Y//2 + X//3) % 2 == 0:
                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    X = X + 1
            else:
                X=X+1
        Y=Y+1
        X=0

def Mask5ApplicationPro(Y = 0, X = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if ((X*Y)%2+(X*Y)%3) == 0:
                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    X = X + 1
            else:
                X=X+1
        Y=Y+1
        X=0

def Mask6ApplicationPro(Y = 0, X = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if ((X*Y)%3+X*Y)%2 == 0:
                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    X = X + 1
            else:
                X=X+1
        Y=Y+1
        X=0

def Mask7ApplicationPro(Y = 0, X = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if ((X*Y)%3+X+Y)%2 == 0:
                if FP.A[Y,X] == 1:
                    FP.A[Y,X] = 0
                    X = X +1

                elif FP.A[Y,X] == 0:
                    FP.A[Y, X] = 1
                    X = X + 1

                else:
                    X = X + 1
            else:
                X=X+1
        Y=Y+1
        X=0


def bestMaskHX5(Y=0, X=0, cptZero=0, cptUn=0, cptPointHX5=0):
    while Y < C.VersionQR:
        while X < C.VersionQR:
            if FP.A[Y, X] == 0:
                cptUn = 0
                cptZero += 1
                if cptZero == 5:
                    cptPoint += 3
                if cptZero > 5:
                    while FP.A[Y, X] == 0:
                        cptPoint += 1
                        X += 1
                        if X == C.VersionQR:
                            break

            elif FP.A[Y, X] == 1:
                cptZero = 0
                cptUn += 1
                if cptUn == 5:
                    cptPoint += 3
                if cptUn > 5:
                    while FP.A[Y, X] == 1:
                        cptPoint += 1
                        X += 1
                        if X == C.VersionQR:
                            break

            elif FP.A[Y, X] != 1 and FP.A[Y, X] != 0:
                cptUn = 0
                cptZero = 0
            X += 1
        Y += 1
        X = 0
        cptZero = 0
        cptUn = 0
    print("nb point horizontale : ", cptPoint)

def bestMaskVX5(Y = 0, X = 0, cptZero = 0, cptUn = 0, cptPointVX5 = 0):
    while X < C.VersionQR:
        while Y < C.VersionQR:
            if FP.A[Y,X] == 0:
                cptUn = 0
                cptZero += 1
                if cptZero == 5:
                    cptPoint +=3
                if cptZero > 5:
                    while FP.A[Y,X] == 0:
                        cptPoint += 1
                        Y+= 1
                        if Y == C.VersionQR:
                            break

            elif FP.A[Y,X] == 1:
                cptZero = 0
                cptUn += 1
                if cptUn == 5:
                    cptPoint +=3
                if cptUn > 5:
                    while FP.A[Y,X] == 1:
                        cptPoint += 1
                        Y += 1
                        if Y == C.VersionQR:
                            break

            elif FP.A[Y,X] != 1 and FP.A[Y,X] != 0:
                cptUn = 0
                cptZero = 0
            Y += 1
        X +=1
        Y = 0
        cptZero = 0
        cptUn = 0
    print("nb point verticale : ", cptPoint)


def bestMaskNB (X = 0, Y = 0, cptZero = 0, cptUn = 0, cptPointNB = 0, cptDiff = 0) : #calcul la différence de pixels noirs et de pixels blancs
    while X < C.VersionQR:
        while Y < C.VersionQR:
            if FP.A[Y, X] == 0:
                cptZero = cptZero + 1
            else:
                cptUn = cptUn + 1
            Y = Y + 1
        X = X + 1
    cptDiff = cptZero - cptUn;
    if cptDiff < 0:
        cptDiff = cptDiff * -1
    if cptDiff != 0 :
        cptPointNB = cptPointNB + cptDiff

