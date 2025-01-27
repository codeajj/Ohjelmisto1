import random

N = int(input("Anna pisteiden määrä: "))

A = 0 #ympyrä
B = N #neliö

while N > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(1, -1)
    N = N - 1
    if x**2 + y**2 < 1:
        A = A + 1
    if N == 0:
        break
print(f"Piin likiarvo: {(4 * A) / B}")