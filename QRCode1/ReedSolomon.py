# import itertools
#
# import numpy as np
# import numpy.polynomial.polynomial as nppol
# import matplotlib.pyplot as plt
# import galois
import QRGenerBinaire as GB

#
# # def ReedSolomon (msg, k, t): #avec des NULL
# #     n = 2**k - 1
# #     m = n - 2*t
# #     g = BinaryToDecimal(toBinary(msg))
# #     for i in range(len(g), m):
# #         g.append(0)
# #     return g
#
# def toBinary(a):
#   l,m=[],[]
#   for i in a:
#     l.append(ord(i))
#   for i in l:
#     m.append(int(bin(i)[2:]))
#   return m
#
# def BinaryToDecimal(Tab2):
#     for y in range(len(Tab2)):
#         bnum = Tab2[y]
#
#         dnum = 0
#         i = 1
#         while bnum != 0:
#             rem = bnum % 10
#             dnum = dnum + (rem * i)
#             i = i * 2
#             bnum = int(bnum / 10)
#         Tab2[y] = dnum
#     return Tab2
#
# def ReedSolomon (msg, k, t):
#     n = 2**k - 1
#     m = n - 2*t
#     for j in range(len(msg), m):
#         msg = msg + " "
#     i = BinaryToDecimal(toBinary(msg))
#     k = []
#     for j in range(len(i)-1, -1, -1):
#         k.append(i[j])
#     i = nppol.Polynomial(k)
#     return i
#
#
#
# GF = galois.GF(2**8)
# print(GF)
# issubclass(GF, np.ndarray)
# x = GF([45, 36, 7, 74, 135])
# # print(x)
# y = np.array([103, 146, 186, 83, 112], dtype=int)
# y = y.view(GF)
# # print(y)
# isinstance(x, GF)
# isinstance(x, np.ndarray)
# GF.display("poly")
# # print(x + y)
# # x = np.arange(10)
# # msg = "trop"
# # print(ReedSolomon(msg, 4, 3))

class ReedSolomon:
    # Galois fields
    # -- exponents (anti-logarithms)
    __GFEXP = [0] * 512

    # -- logarithms
    __GFLOG = [0] * 256

    # INITIALISATION CONSTRUCTOR
    def __init__(self):
        # prepare the exponential and logarithmic fields
        self.__GFEXP[0] = 1
        byteValu = 1
        for bytePos in range(1, 255):
            byteValu <<= 1
            if (byteValu & 0x100):
                byteValu ^= 0x11d

            # update the field elements
            self.__GFEXP[bytePos] = byteValu
            self.__GFLOG[byteValu] = bytePos

        # finalise the exponential field
        for bytePos in range(255, 512):
            self.__GFEXP[bytePos] = self.__GFEXP[bytePos - 255]

    ## GALOIS PRIMITIVE OPERATIONS
    # -----
    # Galois multiplication
    # argX, argY: multiplicand, multiplier
    # byteValu: product
    def __gfMult(self, argX, argY):
        # parametre checks
        if ((argX == 0) or (argY == 0)):
            byteValu = 0
        else:
            # perform the operation
            byteValu = self.__GFLOG[argX]
            byteValu += self.__GFLOG[argY]
            byteValu = self.__GFEXP[byteValu]

        # return the product result
        return (byteValu)

    # Galois division
    # argX, argY: dividend, divisor
    # byteValu: quotient
    def __gfDivi(self, argX, argY):
        # validate the divisor
        if (argY == 0):
            raise ZeroDivisionError()

        # validate the dividend
        if (argX == 0):
            byteValu = 0
        else:
            # perform the division
            byteValu = self.__GFLOG[argX] - self.__GFLOG[argY]
            byteValu += 255
            byteValu = self.__GFEXP[byteValu]

        # return the division result
        return (byteValu)

    ## GALOIS POLYNOMIAL OPERATIONS
    # -----
    # Polynomial addition
    # polyA, polyB: polynomial addends
    # polySum: polynomial sum
    def _gfPolyAdd(self, polyA, polyB):
        # initialise the polynomial sum
        polySum = [0] * max(len(polyA), len(polyB))

        # process the first addend
        for polyPos in range(0, len(polyA)):
            polySum[polyPos + len(polySum) - len(polyA)] = polyA[polyPos]

        # add the second addend
        for polyPos in range(0, len(polyB)):
            polySum[polyPos + len(polySum) - len(polyB)] ^= polyB[polyPos]

        # return the sum
        return (polySum)

    # Polynomial multiplication
    # polyA, polyB: polynomial factors
    # polyProd: polynomial product
    def _gfPolyMult(self, polyA, polyB):
        # initialise the product
        polyProd = len(polyA) + len(polyB) - 1
        polyProd = [0] * polyProd

        # start multiplying
        for posB in range(0, len(polyB)):
            for posA in range(0, len(polyA)):
                polyProd[posA + posB] ^= self.__gfMult(polyA[posA], polyB[posB])

        # return the product result
        return (polyProd)

    # Polynomial scaling
    # argPoly: polynomial argument
    # argX: scaling factor
    # polyVal: scaled polynomial
    def _gfPolyScale(self, argPoly, argX):
        # initialise the scaled polynomial
        polyVal = [0] * len(argPoly)

        # start scaling
        for polyPos in range(0, len(argPoly)):
            polyVal[polyPos] = self.__gfMult(argPoly[polyPos], argX)

        # return the scaled polynomial
        return (polyVal)

    # Polynomial evaluation
    # argPoly: polynomial argument
    # argX: independent variable
    # byteValu: dependent variable
    def _gfPolyEval(self, argPoly, argX):
        # initialise the polynomial result
        byteValu = argPoly[0]

        # evaluate the polynomial argument
        for polyPos in range(1, len(argPoly)):
            tempValu = self.__gfMult(byteValu, argX)
            tempValu = tempValu ^ argPoly[polyPos]
            byteValu = tempValu

        # return the evaluated result
        return (byteValu)

    ## REED-SOLOMON SUPPORT ROUTINES
    # -----
    # Prepare the generator polynomial
    # errSize: number of error symbols
    # polyValu: generator polynomial
    def _rsGenPoly(self, errSize):
        polyValu = [1]

        for polyPos in range(0, errSize):
            tempVal = [1, self.__GFEXP[polyPos]]
            polyValu = self._gfPolyMult(polyValu, tempVal)

        # return the polynomial result
        return (polyValu)

    ## REED-SOLOMON ENCODING
    # ------
    # argMesg: the message block
    # errSize: number of error symbols
    # outBuffer: the encoded output buffer
    def RSEncode(self, argMesg, errSize):

        # prepare the generator polynomial
        polyGen = self._rsGenPoly(errSize)

        # prepare the output buffer
        outBuffer = (len(argMesg) + errSize)
        outBuffer = [0] * outBuffer

        # initialise the output buffer
        for mesgPos in range(0, len(argMesg)):
            mesgChar = argMesg[mesgPos]
            outBuffer[mesgPos] = ord(mesgChar)

        # begin encoding
        for mesgPos in range(0, len(argMesg)):
            mesgChar = outBuffer[mesgPos]
            if (mesgChar != 0):
                for polyPos in range(0, len(polyGen)):
                    tempValu = self.__gfMult(polyGen[polyPos], mesgChar)
                    outBuffer[mesgPos + polyPos] ^= tempValu

        # finalise the output buffer
        for mesgPos in range(0, len(argMesg)):
            mesgChar = argMesg[mesgPos]
            outBuffer[mesgPos] = ord(mesgChar)

        # return the output buffer
        return (outBuffer)


#tranforme un tableau de décimal en tableau de binaire
def DecimalToBinary(Tab):
    for pos in range(len(Tab)):
        bnum = Tab[pos]
        dnum = 0
        val = 1
        while bnum != 0:
            rem = bnum % 2
            dnum = dnum + (rem * val)
            val = val * 10
            bnum = int(bnum / 2)
        Tab[pos] = dnum
    return Tab

def CorrecErreur(mes, level):
    if (level == "L"):
        level = round(len(mes) * 0.071) * 2
    if (level == "M"):
        level = round(len(mes) * 0.151) * 2
    if (level == "Q"):
        level = round(len(mes) * 0.251) * 2
    if (level == "H"):
        level = round(len(mes) * 0.301) * 2
    return level

x = ReedSolomon()
x = x.RSEncode(GB.Information,CorrecErreur(GB.Information,'L'))
x = DecimalToBinary(x)


def reedSolomonSTR():
    a = []
    d = 0
    for i in x:
        a.append(str(x[d]))
        d += 1
    return a

bits = reedSolomonSTR()
bits.insert(0,(format((len(GB.Information)), 'b')))