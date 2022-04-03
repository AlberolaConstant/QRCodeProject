import numpy as np

import QRFixedPatterns as FP
import Constante as C

def truncate(n, decimals = 0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def Mask(I = C.VersionQR - 5, d = 0, J = 4, mask = C.mask0):
    while d < 3:
        FP.A[I, 8] = mask[d]
        FP.A[8, J] = mask[d]
        I = I + 1
        J = J - 1
        d = d + 1


def MaskApplication0(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask = C.mask0)
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



def MaskApplication1(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask1)
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


def MaskApplication2(Y=0, X=0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask2)
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

def MaskApplication3(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask3)
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


def MaskApplication4(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask4)
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

def MaskApplication5(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask5)
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

def MaskApplication6(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask6)
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

def MaskApplication7(Y = 0, X = 0):
    # Mask(I = C.VersionQR - 5, d = 0, J = 4, mask=C.mask7)
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


def ChercheCinqBitsH(Y=0, X=0, cptZero=0, cptUn=0, cptPointHX5=0):
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
            X += 1
        Y += 1
        X = 0
        cptZero = 0
        cptUn = 0
    return cptPointHX5

def ChercheCinqBitsV(Y = 0, X = 0, cptZero = 0, cptUn = 0, cptPointVX5 = 0):
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
    return cptPointVX5

def PenaliteDiffBits (X=0, Y=0, cptZero=0, cptUn=0,cptPointNB=0) : #calcul la différence de pixels noirs et de pixels blancs
    while X < C.VersionQR:
        while X < C.VersionQR:
            Y = 0
            while Y < C.VersionQR:
                if FP.A[Y, X] == 0:
                    cptZero = cptZero + 1
                else:
                    cptUn = cptUn + 1
                Y = Y + 1
            X = X + 1

            cptPointNB = (((cptUn / (cptUn + cptZero)) * 100) - 50)
            cptPointNB = truncate(cptPointNB, 0)
            if cptPointNB < 0:
                cptPointNB = cptPointNB * -1
            cptPointNB = cptPointNB * 2
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
    return cptPointCarre

def chercheMotifH(X = 0, Y = 0, cptPointMotif = 0):
    while Y < C.VersionQR:
        while X < C.VersionQR-10:
            if FP.A[Y, X] == 1 and FP.A[Y, X + 1] == 0 and FP.A[Y, X + 2] == 1 and FP.A[Y, X + 3] == 1 and FP.A[Y, X + 4] == 1 and FP.A[Y, X + 5] == 0 and FP.A[Y, X + 6] == 1:
                if FP.A[Y, X+8] == 0 and FP.A[Y, X+9] == 0 and FP.A[Y, X+10] == 0:
                    cptPointMotif += 1

                if FP.A[Y, X-1] == 0 and FP.A[Y, X-2] == 0 and FP.A[Y, X-3] == 0:
                    cptPointMotif += 1
                X += 1
            else:
                X += 1

        Y += 1
        X = 0
    return cptPointMotif

def chercheMotifV(X = 0, Y = 0, cptPointMotif = 0):
    while X < C.VersionQR:
        while Y < C.VersionQR-10:
            if FP.A[Y, X] == 1 and FP.A[Y+1, X] == 0 and FP.A[Y+2, X] == 1 and FP.A[Y+3, X] == 1 and FP.A[Y+4, X] == 1 and FP.A[Y+5, X] == 0 and FP.A[Y+6, X] == 1:
                if FP.A[Y+8, X] == 0 and FP.A[Y+9, X] == 0 and FP.A[Y+10, X] == 0:
                    cptPointMotif += 1

                if FP.A[Y-1, X] == 0 and FP.A[Y-2, X] == 0 and FP.A[Y-3, X] == 0:
                    cptPointMotif += 1
                Y += 1
            else:
                Y += 1

        X += 1
        Y = 0
    return cptPointMotif

def Alltestmask():
    point = ChercheCinqBitsH() + ChercheCinqBitsV() + chercheCarre() + PenaliteDiffBits() + chercheMotifV() + chercheMotifH()
    return point

def testmask():
    pointMask = []
    copy = FP.A.copy()
    MaskApplication0()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication1()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication2()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication3()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication4()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication5()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication6()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()
    MaskApplication7()
    pointMask.append(Alltestmask())

    FP.A = copy.copy()

    print('le min est :',min(pointMask), 'en position : ', pointMask.index(min(pointMask)))
    minpoint = pointMask.index(min(pointMask))

    if minpoint == 0:
        MaskApplication0()
    elif minpoint == 1:
        MaskApplication1()
    elif minpoint == 2:
        MaskApplication2()
    elif minpoint == 3:
        MaskApplication3()
    elif minpoint == 4:
        MaskApplication4()
    elif minpoint == 5:
        MaskApplication5()
    elif minpoint == 6:
        MaskApplication6()
    elif minpoint == 7:
        MaskApplication7()


