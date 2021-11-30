import QRFixedPatterns as FP

def Mask1ApplicationX(Y = 0, X = 0):

    while X < FP.V1:
        if FP.A[Y,X] == 1:
            FP.A[Y,X] = 0
            X = X +1
        else:
            FP.A[Y, X] = 1
            X = X + 1

def Mask1Application():
    y = 0
    for i in range (11):
        Mask1ApplicationX(Y=y, X=0)
        y = y + 2

