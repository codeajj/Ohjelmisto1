kuha = int(input("Kerro kuhan pituus: "))
if kuha < 37:
    puute = 37 - kuha
    print(f"Kuha on {puute}cm liian lyhtyt, laske se takaisin.")
if kuha >= 37:
    print("Kuha on tarpeeksi pitkä")
