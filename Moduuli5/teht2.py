luvut = []

while True:
    luku = input("Anna minulle lukuja: ")
    if luku == "":
        break
    luvut.append(luku)
luvut.sort(reverse=True)
print(f"Tässä viisi suurinta antamaasi lukua: {luvut[:5]}")