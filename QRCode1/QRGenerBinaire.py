from numpy import integer
from PIL import Image
import numpy

Information = 'projet ptut qr'
i = 0
k = 0
caraNum = []
liste = []
imgbin = []

# img = Image.open("img/smile.jpg")
# np_img = numpy.array(img)

# print (Information)
liste.append(format((len(Information)), 'b'))
while i < len(Information):
    caraNum = format(ord(Information[i]), 'b')
    liste.append(caraNum)
    i = i+1
print (liste)


# a = 0
# y=0
# def decimalToBinary(n):
#     return bin(n).replace("0b", "")

# for y in np_img:
#     for k in y:
#         for p in k:
#            conv = decimalToBinary(p)
#            if conv == "0":
#                conv = conv + "0000000"
#            elif conv == "1":
#                conv = "0000000" + conv
#         imgbin.append(conv)


# print (liste)
# print ("l'image:",imgbin)