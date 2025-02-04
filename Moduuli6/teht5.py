def luvut(lista):
    print("Karsittu lista:")
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            karsittu.append(lista[i])
    return karsittu

karsittu = []

lista = [1,2,3,4,5,6]
print(lista)
print(luvut(lista))