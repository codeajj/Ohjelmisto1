import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port = 3306,
    database="flight_game",
    user="root",
    passwd="13522",
    autocommit = True
    )

def hae_icao(ICAO):
    sql = f"select airport.name as 'airport' from airport where gps_code = '{ICAO}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    print(tulos)

ICAO = input("Kysy minulta ICAO koodi ja printaa sinulle sen lentokentän ja maan: ")
hae_icao(ICAO)