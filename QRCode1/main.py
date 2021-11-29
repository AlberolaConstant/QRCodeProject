from matplotlib import pyplot as plt

# import perso
import QRFixedPatterns as FP
import QRFormatInfo as FI
import QRMessage as MS

FP.calibragePattern()
FI.InfoH()
MS.DGBH()
MS.RB()

print(FP.A)
plt.imshow(FP.A, cmap = 'binary', vmin = 0, vmax = 1, interpolation = 'none')
plt.show()