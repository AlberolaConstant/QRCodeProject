from numpy import integer
from PIL import Image
import numpy

Information = 'HELLO WORLD'
k = 0
liste = []
imgbin = []


# img = Image.open("img/smile.jpg")
# np_img = numpy.array(img)
def genereBinaire(message = Information):
    i = 0
    caraNum = []
    while i < len(message):
        caraNum = format(ord(message[i]), 'b')
        liste.append(caraNum)
        i = i+1

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