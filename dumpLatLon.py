import requests
import pickle

regions = [
    "Aguascalientes",
    "Baja California Norte",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Coahuila",
    "Colima",
    "Ciudad de México",
    "Durango",
    "Estado de México",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "Michoacán",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz",
    "Yucatán",
    "Zacatecas"
]

def getRegionLatLon(regions):
    latlon = {}

    for region in regions:
        if not region in latlon:
            r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyAH3VYuagoPFD67-SNs0zMJqXq14ty3BcY&address={}'.format(region))
            data = r.json()
            latlon[region] = data['results'][0]['geometry']['location']

    return latlon

latlon = getRegionLatLon(regions)
print(latlon)

file = open('latlon.data', 'wb')
pickle.dump(latlon, file)
file.close()
