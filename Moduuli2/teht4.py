import math

lukuA = float(input("Anna leiviskät "))
lukuB = float(input("Anna naulat "))
lukuC = float(input("Anna luodit "))

luodit = lukuC * 13.3
naulat = lukuB * 32 * 13.3
leiviska = lukuA * 20 * 32 * 13.3

kilo = int((luodit + naulat + leiviska) / 1000)
gramma = (luodit + naulat + leiviska)%1000

print(f"Yhteispaino on {kilo}kg ja {gramma:.2f}g")








