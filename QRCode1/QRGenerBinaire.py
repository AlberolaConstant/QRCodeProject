Information = 'projet qr code'
i = 0
cara = ''
caraNum = ''
liste = []
newListe = []

while i < len(Information):
    cara = Information[i]
    caraNum = format(ord(cara), 'b')
    liste.append(caraNum)
    i = i+1
print(liste)
a = 0
print(format(14, 'b'))
#vut sur le site : http://tpe-codebarre2d.e-monsite.com/pages/page.html

# while a < len(liste):
#     newListe.append(bin(liste[a]*45+liste[a+1]))
#     a = a+2
# print(newListe)

print('fin programme')