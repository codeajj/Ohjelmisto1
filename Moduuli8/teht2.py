import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port = 3306,
    database="flight_game",
    user="root",
    passwd="13522",
    autocommit = True
    )

def hae_lentokentät(tyyppi):
    sql = f"select type, count(*) from airport where iso_country = '{tyyppi}' group by type desc;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    print(tulos)

tyyppi = input("Anna maakoodi ja tulostan sinulle sen lentokenttien tyypit ja määrät: ")
hae_lentokentät(tyyppi)