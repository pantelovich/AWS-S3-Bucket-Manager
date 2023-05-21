travelLog = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def addCitie(country, visits, cities):
    travelLog.append({"country": country, "visits": visits, "cities": cities})
    return country, visits, cities

addCitie("Russia", 2, ["Moscow", "Saint Petersburg"])


for i in travelLog:
    print(f"Country: {i['country']}")
    print(f"Visits: {i['visits']}")
    print("Cities: "+ ", ".join(i['cities'])) 