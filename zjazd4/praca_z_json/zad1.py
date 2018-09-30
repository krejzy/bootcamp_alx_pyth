# Napisz program obsługujący bazę danych pracowników
# W bazie danych przechowuj imię, nazwisko, email, rok urodzenia, pensję.
# Skorzystaj z modułu json

$ python employees.py
Co chcesz zrobić? [d - dodaj, w - wypisz] data
Imie: Karol

import json

print(type(json,dumps(date_base)))

# zapis do pliku
with open("example.json", 'w') as f:
    json.dump(date_base. f)

# otwarcie pliku
with open("example.json", 'w') as f:
   data = json.load(f)
   print(data)
   print (type(data))
   data.append("name", "last name", "email","year of birth", "salary")

print(data)

with open("example.json", 'w') as f:
    json.dump(data. f)

# wersja prowadzący

import json

def zapisz(dane):
    pass

def wypisz(pracownicy):
    for nr, pracownik in enumerate (pracownicy, start=1):
        print{
            f""


        }
def odczytaj():
    pass

def dane_do_zapisu():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia"))
    pensja = float(input("Pensja"))

    dane = {
        "imie": imie
        "nazwisko": nazwisko
        "rok_urodzenia": rok_urodzenia
        "pensja": pensja
    }



while True:
    action = input("Co chcess zrobić? [d-dodaj, w-wypisz")

    if action == 'd':
        dane = dane_do_zapisu():
        zapisz(dane)

    elif action == 'w':
        wypisz()




