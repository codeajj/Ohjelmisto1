def lasku(määrä):
    gallon = 3.785
    litrat = määrä * gallon
    return litrat

gallonat = []

while True:
    gallon = int(input("Anna minulle gallonamäärä ja lopusi muutan ne litroiksi, negatiivinen luku lopettaa: "))
    if gallon >= 0:
        gallonat.append(gallon)
    else:
        break
määrä = sum(gallonat)
print(f"Antamasi gallonamäärä on {lasku(määrä):.3f} litraa")