from numpy import integer

Information = 'projet qr code ptut'
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

#vut sur le site : http://tpe-codebarre2d.e-monsite.com/pages/page.html

# while a < len(liste):
#     newListe.append(bin(liste[a]*45+liste[a+1]))
#     a = a+2
# print(newListe)
