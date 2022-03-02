import QRFixedPatterns as FP
import Constante as C

def Mask0ApplicationPro(Y = 0, X = 0):
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
                    X = X + 1
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
                    Y = Y + 1
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