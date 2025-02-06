nimet = set()

nimi = input("Anna minulle nimiä ja lisään ne listaan, tyhjä vastaus lopettaa: ")
nimet.add(nimi)
print("Uusi nimi")

while nimi != "":
    nimi = input("Seuraava: ")
    if nimi in nimet:
        print("Aiemmin annettu nimi")
    if nimi == "":
        break
    else:
        nimet.add(nimi)
        print("Uusi nimi")

print(nimet)