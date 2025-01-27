luku = int(input("Anna tuuma luku ja muunnan sen senttimetreiksi: "))
cm = 2.54
while luku >= 0:
    senttimetrit = luku * cm
    print(f"{senttimetrit}cm")
    luku = int(input("Anna uusi luku: "))
if luku <= 0:
    print("Error")