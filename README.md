# QRCodeProject
Alberola Constant

Enzo Vargas

Thomas Celeschi

Oussama Talbi

Adrien Lacroix

Projet de Ptut pour l'IUT 

## QRFixedPattern.py

- Génération de la Matrix et ça taille

- Génération des pattern pour la lecture du QR Code

![myplot](https://user-images.githubusercontent.com/73159320/145255519-19321df3-4204-4eb0-b21b-5a6f18d4f196.png)

- [ ] Génération des autre taille de matrix 

## QRFormatInfo.py

- Initialisation des info pour le % de correction d'erreur, sont format, le mask et le format d'encodage

- [ ] implementer les autre % de correction d'erreur 

![image](https://user-images.githubusercontent.com/73159320/145255714-559686c9-d0be-47d6-8bb9-a895e488972c.png)

## QRGenerBinaire.py

- Transformation de la string en une liste de charactere puis les charactere en binaire
![image](https://user-images.githubusercontent.com/73159320/145256780-ab408765-420c-47a1-8608-19eb945e7bbe.png)
![image](https://user-images.githubusercontent.com/73159320/145256952-735a672d-53ca-4cd4-b78f-9a1fa657d759.png)



## QRMessage

- Initialisation des different carré d'information pour une matrix de taille 1 (21 x 21)

![image](https://user-images.githubusercontent.com/73159320/145256083-8631738a-9f76-4cbd-9cb4-cf09c70a3d28.png)

## QRMask.py

- Applique le mask de Niveau 1 a toute la matrix
![image](https://user-images.githubusercontent.com/73159320/145256290-45b3c3fc-f532-4d6d-99cd-4abe58b45fd2.png)

- [ ] Appliquer les autre mask 


##QRCorrectionError

- [ ] Remplir la partie pour la correction d'error du QRCode 

![code sens V1](https://user-images.githubusercontent.com/73159320/145255466-0accf21d-a3a9-46c9-95a8-2b676197128e.png)
