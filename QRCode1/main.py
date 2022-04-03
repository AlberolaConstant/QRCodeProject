from matplotlib import pyplot as plt

# import perso
import QRFixedPatterns as FP
import QRFormatInfo as FI
import QRMessage as MS
import QRMask as MA
import Constante as C
import ReedSolomon as RS
import QRGenerBinaire as GB

GB.genereBinaire()
FP.calibragePattern()
# FI.InfoVide()
# MS.messagePose(M=0, Y=C.VersionQR - 3, X=C.VersionQR - 1, D=0, liste=RS.bits)
# FI.InfoPlein()
# MA.testmask()





plt.imshow(FP.A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
plt.show()
