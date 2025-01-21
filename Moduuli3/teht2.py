luokka = input("Tervetuloa Merihelvetin risteilylle! Kerro hyttiluokkasi: LUX, A, B vai C ")
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virhe! Hyttiluokkaa ei löydy!")
