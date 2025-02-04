import random

print("Noppa heittää kunnes saa luvun kuusi.")

def noppa():
    luku = random.randint(1, 6)
    return luku
joku = 0
while joku != 6:
    joku = noppa()
    print(joku)
    if joku == 6:
        print("Kuusi!")