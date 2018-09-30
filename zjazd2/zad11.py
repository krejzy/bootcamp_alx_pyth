# Zrobić zmienną licznik i za każdym razem jak się pojawi liczba parzysta dodać jeden do tego licznika.
Sprawdzenie czy liczba jest parzysta polega na sprawdzeniu, czy jej reszta po podziale przez dwa jest równa 0.

liczby = set()

liczby_parzyste = set()

for i in range (0-100):

    if i % 2 == 0:
            ile_podzielnych += 1
            print(i)

    print(f"W przedziale 0-100 jest (ile_podzielnych) liczb podzielnych przez 2")

    for element in range(1, 100):
        if element % 2 == 0:
            print(element)

# wersja prowadzącego
 liczby = set()

 while True
     komenda = input("podaj liczbę lub wpisz x by zakończyć")
     if komenda == 'x':
         break
         else
         liczba = int(komenda)
         liczby.add(liczba)
         