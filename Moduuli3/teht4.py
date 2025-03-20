vuosi = int(input("Anna minulle vuosi luku ja kerron onko se karkaus vuosi "))

if vuosi % 4 == 0:
    if vuosi % 4 == 0 and vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Tämä on karkausvuosi!")

        else: print("Tämä ei ole karkausvuosi!")

    else: print("Tämä on karkausvuosi!")

else: print("Tämä ei ole karkausvuosi!")
#moii