from matplotlib import pyplot as plt

# import perso
import QRFixedPatterns as FP
import QRFormatInfo as FI
import QRMessage as MS
import QRGenerBinaire as GB

FP.calibragePattern()
FI.InfoH()
m = 0
MS.DGBH(M = 0, Y = FP.V1 - 7, X = FP.V1 - 1, D = 0)
############################
MS.RVB(    M = 1, Y = FP.V1 - 11, X = FP.V1 - 1, D = 0)
############################

y = FP.V1 - 10
x = FP.V1 - 3
for i in range(2):
    MS.DGHB(M = 2, Y = y, X = x, D = 0)
    m = 3
    y = FP.V1 - 6
    x = FP.V1 - 3
############################
MS.RVH(    M = 4, Y = FP.V1 - 2, X = FP.V1 - 3, D = 0)
############################

y = FP.V1 - 3
x = FP.V1 - 5
for i in range(2):
    MS.DGBH(M = 5, Y = y, X = x, D = 0)
    m = 6
    y = FP.V1 - 7
    x = FP.V1 - 5

############################
MS.RVB(M = 7, Y = FP.V1 - 11, X = FP.V1 - 7, D = 0)
############################


# dessinez le QR code
print(FP.A)
plt.imshow(FP.A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
plt.show()