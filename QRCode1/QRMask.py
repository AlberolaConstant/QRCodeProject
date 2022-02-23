import QRFixedPatterns as FP

def Mask000Application(Y = 0, X = 0):    #Masque 000
    for i in range(11):
        while X < FP.V1:
            if FP.A[Y,X] == 1:
                FP.A[Y,X] = 0
                X = X +1
                if FP.A[Y, X] == 1:
                    FP.A[Y, X] = 1
                    X = X + 1
                else :
                    FP.A[Y, X] = 0
                    X = X + 1
            else:
                FP.A[Y, X] = 1
                X = X + 1
                if FP.A[Y, X] == 1:
                    FP.A[Y, X] = 1
                    X = X + 1
                else:
                    FP.A[Y, X] = 0
                    X = X + 1
        Y = Y + 1

def Mask001Application(Y = 0, X = 0):    #Masque 001
    for i in range(11):
        while X < FP.V1:
            if FP.A[Y,X] == 1:
                FP.A[Y,X] = 0
                X = X +1
            else:
                FP.A[Y, X] = 1
                X = X + 1
        Y = Y + 2

def Mask010Application(Y = 0, X = 0):    #Masque 010
    for i in range(11):
        while Y < FP.V1:
            if FP.A[Y,X] == 1:
                FP.A[Y,X] = 0
                Y = Y +1
            else:
                FP.A[Y, X] = 1
                Y = Y + 1
        X = X + 3


