import random

maksimi = int(input("Määritä d20 nopan maksimi luku: "))

def noppa():
    luku = random.randint(1, 20)
    return luku

joku = 0
while joku != maksimi:
    joku = noppa()
    print(joku)
    if joku == maksimi:
        print("Maksimi!")