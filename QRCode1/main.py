from matplotlib import pyplot as plt

# import perso
import QRFixedPatterns as FP
import QRFormatInfo as FI
import QRMessage as MS
import QRMask as MA
import Constante as C


FP.calibragePattern()
FI.InfoH()
# MS.messagePose(M=0, Y=C.VersionQR - 1, X=C.VersionQR - 1, D=7)
MA.Mask0ApplicationPro()

# dessinez le QR code
print(FP.A)
plt.imshow(FP.A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
plt.show()
