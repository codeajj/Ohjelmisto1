import math
def laskuri(pitsa, euro):
    pinta = math.pi * pitsa ** 2
    pintasentti = pinta * pinta
    pintametri = pintasentti * 0.0001
    arvo = euro / pintametri
    return arvo

print("Anna minulle kahden pitsan halkasijat ja hinnat niin lasken kumpi on parempi vastine neliömetreinä: ")

pitsa = int(input("Ekan pitsan halkasija: "))
euro = int(input("ja pitsan hinta: "))
pitsa1 = laskuri(pitsa, euro)

pitsa = int(input("Toisen pitsan halkasija: "))
euro = int(input("ja sen hinta: "))
pitsa2 = laskuri(pitsa, euro)

if pitsa1 < pitsa2:
    print("Ensimmäinen pitsa on arvokkaampi")
elif pitsa1 > pitsa2:
    print("Toinen pitsa on arvokkaampi")