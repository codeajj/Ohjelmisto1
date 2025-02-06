def lasku(para):
    litrat = para * 3.785
    return litrat

while True:
    luku = int(input("Anna minulle gallonamäärä ja lopusi muutan ne litroiksi, negatiivinen luku lopettaa: "))
    if luku >= 0:
        tulos = lasku(luku)
        print(f"Antamasi gallonamäärä on {tulos:.3f} litraa")
    else:
        break