# Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji.

$ python ex_02.py warsaw
Pogoda w Warsaw:
- temperatura: 18.43°C
- ciśnienie: 1019.725 hPa
- wilgotność: 62%

import urlib.reqest


def zapisz(dane):
   with open("pogoda.json", 'w') as f:
       json.dump(dane, f)


def wypisz(pogoda):
   for pogoda, pogoda in enumerate(pogoda, start=1):
       print(
           f"temperatura [{'stopnie'}] "
           f"ciśnienie: {['']}, "
           f"wilgotność: {['']}"
       )

f = urlib.request.urlopen("https://www.metaweather.com/api/#locationsearch")
print(f.status)
data = f.read()
data = json.loads(data)


pogoda = data[0] ['pogoda']
for pogoda in pogoda:
    print(f"{pogoda['temperatura']") - {pogoda[ciśnienie]} - {pogoda['wilgotność']}")


# wersja prowadzący

def get_location_id(location_name)
    urlib.request.urlopen(/api/location/search/?query={location_name}) as f:
    with requests.get(f"")
    data = f.read()
    data =
pass

def get_location_weather(location_name)
pass

def present_results


