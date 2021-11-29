import QRFixedPatterns as FP
import QRGenerBinaire as GB

# message = [0, 1, 1, 0, 0, 0, 1, 1]




def DGBH():
    M = 0
    y = FP.V1 - 7
    x = FP.V1 - 1
    d = 0
    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    tabCara.insert(0,0)

    while d < 7:
        message = tabCara[d]
        FP.A[y, x] = message
        x = x - 1
        d = d + 1
        message = tabCara[d]
        FP.A[y, x] = message
        x = x + 1
        y = y - 1
        d = d + 1

def RB ():
    M = 1
    y = 10
    x = FP.V1 - 1
    d = 0
    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    tabCara.insert(0,0)

    while d < 3:
        message = tabCara[d]
        print (message)
        FP.A[y,x] = message
        x = x - 1
        d = d + 1
        message = tabCara[d]
        FP.A[y, x] = message
        x = x + 1
        y = y - 1
        d = d + 1

    y = 9
    x = FP.V1 - 3
    d = 4
    while d < 7:
        message = tabCara[d]
        FP.A[y,x] = message
        x = x - 1
        d = d + 1
        message = tabCara[d]
        FP.A[y, x] = message
        x = x + 1
        y = y + 1
        d = d + 1
