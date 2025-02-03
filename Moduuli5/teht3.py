alku = True

luku = int(input("Anna luku: "))

for jakaja in range(2, luku):
    if luku % jakaja == 0:
        alku = False
        break
if alku == True:
    print("Se on alkuluku!")
else:
    print("Antamasi luku ei ollut alkuluku.")