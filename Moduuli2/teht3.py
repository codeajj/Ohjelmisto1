eka_str =input("Hei anna minulle luku: ")
toka_str =input("Okei, anna toinen luku: ")
kolmas_str  =input("Nyt anna minulle vielä yksi luku: ")

eka = int(eka_str)
toka = int(toka_str)
kolmas = int(kolmas_str)

summa = eka + toka + kolmas
tulo = eka * toka * kolmas
keskiarvo = str(summa / 3)

print(f"Lukujesi summa on " + str(summa) + " tulo on " + str(tulo) + " ja niiden keskiarvo on: " + str(keskiarvo))