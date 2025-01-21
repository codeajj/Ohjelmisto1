suku = input("Oletko mies vai nainen? ")
if suku == "Mies":
    mies = int(input("Mikä on sinun hemoglobiini arvosi? "))
    if mies >=135<=195:
        print("Hemoglobiini arvosi on normaali.")
    elif mies <= 135:
        print("Hemoglobiini arvosi on alhainen.")
    elif mies >= 195:
        print("Hemoglobiini arvosi on korkea:")
elif suku == "Nainen":
    nainen = int(input("Mikä on sinun hemoglobiini arvosi? "))
    if nainen >= 117<=175:
        print("Hemoglobiini arvosi on normaali.")
    elif nainen <= 117:
        print("Hemoglobiini arvosi on alhainen.")
    elif nainen >= 175:
        print("Hemoglobiini arvosi on korkea.")
else: print("Virhe!")