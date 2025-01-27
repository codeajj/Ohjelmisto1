import random

arvaus = int(input("Hei, valitsen numeron 1-10 väliltä, sinun tehtävä on arvata se: "))

numero = random.randint(1,10)

while arvaus != numero:
    if arvaus <= numero:
        arvaus = int(input("Liian vähän! Arvaa uudelleen: "))
    elif arvaus >= numero:
        arvaus = int(input("Liian suuri! Arvaa uudelleen: "))
if arvaus == numero:
    print("Oikein!")