import QRFixedPatterns as FP
import QRGenerBinaire as GB

# message = [0, 1, 1, 0, 0, 0, 1, 1]

# a optimiser
def DGBH():
    M = 0
    y = FP.V1 - 3
    x = FP.V1 - 1
    d = 0
    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    tabCara.insert(0,0)

    while d < 8:
        message = tabCara[d]
        FP.A[y,x] = message
        x = x - 1
        d = d + 1
        message = tabCara[d]
        FP.A[y, x] = message
        x = x + 1
        y = y - 1
        d = d + 1

    M = M + 1
    y = FP.V1 -7
    x = FP.V1 - 1
    d = 0
    tabCara = GB.liste[M]
    tabCara = list(tabCara.strip())
    tabCara.insert(0,0)

    while d < 8:
        message = tabCara[d]
        FP.A[y,x] = message
        x = x - 1
        d = d + 1
        message = tabCara[d]
        FP.A[y, x] = message
        x = x + 1
        y = y - 1
        d = d + 1