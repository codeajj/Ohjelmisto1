import random
summa = 0
heitot = int(input("Kuinka monta kertaa heitän noppaa: "))
for i in range(heitot):
    noppa = random.randint(1, 6)
    summa = summa + noppa
    if (i -1) == noppa:
        break
print(f"Heittojen summa: {summa}")