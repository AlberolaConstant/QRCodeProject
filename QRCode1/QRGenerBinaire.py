from numpy import integer

Information = 'projet qr code ptut qui me soule grave quelle projet/cool(QRCODE)sdfd'
i = 0
caraNum = []
liste = []

print (Information)
while i < len(Information):
    caraNum = format(ord(Information[i]), 'b')
    liste.append(caraNum)
    i = i+1
a = 0
print (liste)

