from numpy import integer

Information = 'coucou'
i = 0
caraNum = []
liste = []
nombre = [1, 3, 4]

while i < len(Information):
    caraNum = format(ord(Information[i]), 'b')
    liste.append(caraNum)
    i = i+1
a = 0
print (liste)

M = 1
cool = liste[M]
cool = list(cool.strip())
print (cool)
message = int(cool[2])
print (message)

#vut sur le site : http://tpe-codebarre2d.e-monsite.com/pages/page.html

# while a < len(liste):
#     newListe.append(bin(liste[a]*45+liste[a+1]))
#     a = a+2
# print(newListe)
