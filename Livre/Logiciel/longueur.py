""" Détermination de la longueur entre 2 points dans l'espace """

from math import sqrt

x1, y1 = int(input(" x pour 1 = ")), int(input(" y pour 1 "))
x2, y2 = int(input(" x pour 2 = ")), int(input(" y pour 2 "))

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("la distance séparant les 2 points est de : ", distance)


