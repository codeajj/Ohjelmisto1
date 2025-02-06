ajat = {"12" : "talvella",
        "1" : "talvella",
        "2" : "talvella",
        "3" : "keväällä",
        "4" : "keväällä",
        "5" : "keväällä",
        "6" : "kesällä",
        "7" : "kesällä",
        "8" : "kesällä",
        "9" : "syksyllä",
        "10" : "syksyllä",
        "11" : "syksyllä"}

while True:
    kuukausi = input("Anna minulle kuukauden numero (1-12) ja kerron millä vuodenajalla se on: ")
    if kuukausi in ajat:
        print(f"Antamasi kuukausi on {ajat[kuukausi]}")
        break
    else:
        print("Error 404, 'kuukausi' not found")