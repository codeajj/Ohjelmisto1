import math

kanta_str =input("Anna suorakulmion kanta: ")
korkeus_str =input("Anna suorakulmion korkeus: ")

korkeus = int(korkeus_str)
kanta = int(kanta_str)

piiri = (kanta + kanta + korkeus + korkeus)
pintaala = (kanta * korkeus)
print(f"Suorakulmion kanta on: " + str(piiri))
print(f"ja sen pinta-ala on: " + str(pintaala))