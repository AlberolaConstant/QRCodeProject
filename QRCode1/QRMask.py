import numpy as np

import QRFixedPatterns as FP
import Constante as C

def Mask(I = C.VersionQR - 5, d = 0, J = 5, mask = C.mask0):
    while d < 3:
        FP.A[I, 8] = mask[d]
        FP.A[8, J] = mask[d]
        I = I + 1
        J = J - 1
        d = d + 1


def Mask0ApplicationPro(Y = 0, X = 0):

    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask = C.mask0)

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
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask1)
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
                    X = X + 1
            Y=Y+1
            X=0
        else:
            Y=Y+1
            X=0


def Mask2ApplicationPro(Y=0, X=0):
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask2)
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
                    Y = Y + 1

            X = X + 1
            Y = 0
        else:
            X = X + 1
            Y = 0

def Mask3ApplicationPro(Y = 0, X = 0):
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask3)

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
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask4)
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
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask5)
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
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask6)
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
    Mask(I = C.VersionQR - 5, d = 0, J = 5, mask=C.mask7)
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
            if FP.A[Y, X] < 0.2:
                cptUn = 0
                cptZero += 1
                if cptZero == 5:
                    cptPointHX5 += 3
                if cptZero > 5:
                    while FP.A[Y, X] < 0.2:
                        cptPointHX5 += 1
                        X += 1
                        if X == C.VersionQR:
                            break

            elif FP.A[Y, X] > 0.8:
                cptZero = 0
                cptUn += 1
                if cptUn == 5:
                    cptPointHX5 += 3
                if cptUn > 5:
                    while FP.A[Y, X] > 0.8:
                        cptPointHX5 += 1
                        X += 1
                        if X == C.VersionQR:
                            break
            # elif FP.A[Y, X] != 1 and FP.A[Y, X] != 0:
            #     cptUn = 0
            #     cptZero = 0
            X += 1
        Y += 1
        X = 0
        cptZero = 0
        cptUn = 0
    print("nb point horizontale : ", cptPointHX5)
    return cptPointHX5

def bestMaskVX5(Y = 0, X = 0, cptZero = 0, cptUn = 0, cptPointVX5 = 0):
    while X < C.VersionQR:
        while Y < C.VersionQR:
            if FP.A[Y,X] < 0.2:
                cptUn = 0
                cptZero += 1
                if cptZero == 5:
                    cptPointVX5 +=3
                if cptZero > 5:
                    while FP.A[Y,X] < 0.2:
                        cptPointVX5 += 1
                        Y+= 1
                        if Y == C.VersionQR:
                            break

            elif FP.A[Y,X] > 0.8:
                cptZero = 0
                cptUn += 1
                if cptUn == 5:
                    cptPointVX5 +=3
                if cptUn > 5:
                    while FP.A[Y,X] > 0.8:
                        cptPointVX5 += 1
                        Y += 1
                        if Y == C.VersionQR:
                            break
            Y += 1
        X +=1
        Y = 0
        cptZero = 0
        cptUn = 0
    print("nb point verticale : ", cptPointVX5)
    return cptPointVX5

def bestMaskNB (X = 0, Y = 0, cptZero = 0, cptUn = 0, cptPointNB = 0, cptDiff = 0) : #calcul la différence de pixels noirs et de pixels blancs
    while X < C.VersionQR:
        while Y < C.VersionQR:
            if FP.A[Y, X] == 0:
                cptZero = cptZero + 1
            else:
                cptUn = cptUn + 1
            Y = Y + 1
        X = X + 1
    cptDiff = cptZero - cptUn
    if cptDiff < 0:
        cptDiff = cptDiff * -1
    if cptDiff != 0 :
        cptPointNB = cptPointNB + cptDiff
        print('point NB = ' ,cptPointNB)
        return cptPointNB


def chercheCarre(X = 0, Y = 0, cptPointCarre = 0) :
    while Y < C.VersionQR-1:
        while X < C.VersionQR-1:
            if FP.A[Y, X] < 0.2 and FP.A[Y, X+1] < 0.2 and FP.A[Y+1, X] < 0.2 and FP.A[Y+1, X+1] < 0.2:
                cptPointCarre += 3
                X += 1
            if FP.A[Y, X] > 0.8 and FP.A[Y, X+1] > 0.8 and FP.A[Y+1, X] > 0.8 and FP.A[Y+1, X+1] > 0.8:
                cptPointCarre += 3
                X += 1
            else:
                X += 1
        Y += 1
        X = 0
    print("nb point carre : ", cptPointCarre)
    return cptPointCarre

def chercheMotif(X = 0, Y = 0, cptPointMotif = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR-10:
            if FP.A[Y, X] == 1 and FP.A[Y, X + 1] == 0 and FP.A[Y, X + 2] == 1 and FP.A[Y, X + 3] == 1 and FP.A[Y, X + 4] == 1 and FP.A[Y, X + 5] == 0 and FP.A[Y, X + 6] == 1:
                if FP.A[Y, X+8] == 0 and FP.A[Y, X+9] == 0 and FP.A[Y, X+10] == 0:
                    cptPointMotif += 1

                if FP.A[Y, X+-1] == 0 and FP.A[Y, X-2] == 0 and FP.A[Y, X-3] == 0:
                    cptPointMotif += 1
                X += 1
            else:
                X += 1

        Y += 1
        X = 0
    print("nb point Motif : ", cptPointMotif)
    return cptPointMotif

def Alltestmask():
    point = bestMaskHX5()+bestMaskVX5()+chercheCarre()+bestMaskNB()+chercheMotif()
    return point

def testmask():
    pointMask = []
    copy = FP.A.copy()
    Mask0ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask1ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask2ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask3ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask4ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask5ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask6ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    Mask7ApplicationPro()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()

    print('le min est :',min(pointMask), 'en position : ', pointMask.index(min(pointMask)))
    minpoint = pointMask.index(min(pointMask))

    if minpoint == 0:
        Mask0ApplicationPro()
    elif minpoint == 1:
        Mask1ApplicationPro()
    elif minpoint == 2:
        Mask2ApplicationPro()
    elif minpoint == 3:
        Mask3ApplicationPro()
    elif minpoint == 4:
        Mask4ApplicationPro()
    elif minpoint == 5:
        Mask5ApplicationPro()
    elif minpoint == 6:
        Mask6ApplicationPro()
    elif minpoint == 7:
        Mask7ApplicationPro()


