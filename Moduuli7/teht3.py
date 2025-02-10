kentät = {"ABCD":"Vantaa"}
koodi = "ABCD"
kysymys = input("Haluatko 1. lisätä vai  2. etsiä lentokenttiä ja 3. nähdä listan. Tyhjä vastaus lopettaa: ")

while kysymys != "":
    if kysymys == "1":
        lisäys = input("Anna uuden lentokentän nimi: ")
        koodi = input("Lisää ICAO koodi: ")
        kentät[koodi] = lisäys
        print(kentät)

        kysymys = input("Haluatko 1. lisätä vai  2. etsiä lentokenttiä ja 3. nähdä listan. Tyhjä vastaus lopettaa: ")


    elif kysymys == "2":
        etsi = input("Lentokentän ICAO koodi: ")
        if etsi in kentät:
            print(f"Etsintä: {etsi} : {kentät[koodi]}")
        kysymys = input("Haluatko 1. lisätä vai  2. etsiä lentokenttiä ja 3. nähdä listan. Tyhjä vastaus lopettaa: ")
    elif kysymys == "3":
        print(kentät)
        kysymys = input("Haluatko 1. lisätä vai  2. etsiä lentokenttiä ja 3. nähdä listan. Tyhjä vastaus lopettaa: ")

    elif kysymys == "":
        break

print("Bye bye!")
