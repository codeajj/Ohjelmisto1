import math
suurin = -math.inf
pienin = math.inf

print("Hei! Kysyn sinulta lukuja ja kerron kaikkien niiden pienimmän ja suurimman!")
print("Lopettaaksesi prosessin anna tyhjä merkkijono")

luku_str = input("Anna minulle luku: ")
while luku_str != "":
    luku = float(luku_str)
    if luku < pienin:
        pienin = luku

    luku_str = input("Anna minulle taas luku: ")
    if luku > suurin:
        suurin = luku

if luku_str == "":
    print(f"Suurin antamasi luku on {suurin}, pienin on {pienin}.")