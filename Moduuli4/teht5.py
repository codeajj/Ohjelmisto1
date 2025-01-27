print("Tervotuloa Python clubin kirjautumis sivulle!")
tunnus = input("Anna käyttäjätunnus: ")
sana = input("Anna salasana: ")

yritykset = 1

while tunnus != "python" and sana != "rules":
    tunnus = input("Virheellinen käyttäjä! Anna käyttäjätunnus: ")
    sana = input("Virheellinen salasana! Anna salasana: ")
    yritykset = yritykset + 1
    if yritykset == 5:
        print("Pääsy kielletty!")
        break
if tunnus == "python" and sana == "rules":
    print("Tervetuloa!")
