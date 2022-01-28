from matplotlib import pyplot as plt

# import perso
import QRFixedPatterns as FP
import QRFormatInfo as FI
import QRMessage as MS
import QRGenerBinaire as GB
import QRMask as MA
import Constante as C

def GenerQRV1():
    MS.DGBH(M=0, Y=C.V1 - 7, X=C.V1 - 1, D=0)
    ############################
    MS.RVB(M=1, Y=C.V1 - 11, X=C.V1 - 1, D=0)
    ############################

    y = C.V1 - 10
    x = C.V1 - 3
    m = 2
    for i in range(2):
        MS.DGHB(M=m, Y=y, X=x, D=0)
        m = 3
        y = C.V1 - 6
        x = C.V1 - 3
    ############################
    MS.RVH(M=4, Y=C.V1 - 2, X=C.V1 - 3, D=0)
    ############################

    y = C.V1 - 3
    x = C.V1 - 5
    m = 5
    for i in range(2):
        MS.DGBH(M=m, Y=y, X=x, D=0)
        m = 6
        y = C.V1 - 7
        x = C.V1 - 5

    ############################
    MS.RVB(M=7, Y=C.V1 - 11, X=C.V1 - 5, D=0)
    ############################
    m = 8
    y = C.V1 - 10
    x = C.V1 - 6
    for i in range(2):
        MS.DGHB(M=m, Y=y, X=x, D=0)
        m = 9
        y = C.V1 - 7
        x = C.V1 - 7
    ############################
    MS.RVH(M=10, Y=C.V1 - 2, X=C.V1 - 7, D=0)
    ############################
    y = C.V1 - 3
    x = C.V1 - 9
    m = 11
    for i in range(3):
        MS.DGBH(M=m, Y=y, X=x, D=0)
        m = m + 1
        y = y - 4
        x = C.V1 - 9
    y = y - 1
    MS.DGBH(M=m, Y=y, X=x, D=0)

    ###########################
    MS.RVB(M=15, Y=1, X=C.V1 - 9, D=0)
    ############################
    m = 16
    y = 2
    x = C.V1 - 11
    MS.DGHB(M=m, Y=y, X=x, D=0)
    ###########################Fin message coder


# GenerQRV1()
# FI.FormatEncodage()
# MA.Mask1Application()
FP.calibragePattern()
MS.messagePose(M=0, Y=C.V1 - 1, X=C.V1 - 1, D=7)
# FI.InfoH()

# dessinez le QR code
print(FP.A)
plt.imshow(FP.A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
plt.show()