from matplotlib import pyplot as plt

# import perso
import QRFixedPatterns as FP
import QRFormatInfo as FI
import QRMessage as MS
import QRMask as MA
import Constante as C
import ReedSolomon as RS
import QRGenerBinaire as GB

x = RS.ReedSolomon()
x = x.RSEncode(GB.Information,13)
x = RS.DecimalToBinary(x)

def reedSolomonSTR():
    a = []
    d = 0
    for i in x:
        a.append(str(x[d]))
        d += 1
    return a

bits = reedSolomonSTR()
bits.insert(0,(format((len(GB.Information)), 'b')))

print(bits)

FP.calibragePattern()
FI.InfoVide()
# MS.messagePose(M=0, Y=C.VersionQR - 1, X=C.VersionQR - 1, D=0, liste=GB.liste)
MS.messagePose(M=0, Y=C.VersionQR - 3, X=C.VersionQR - 1, D=0, liste=bits)
FI.InfoPlein()
MA.testmask()

# dessinez le QR code
# print(FP.A)
plt.imshow(FP.A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
plt.show()
