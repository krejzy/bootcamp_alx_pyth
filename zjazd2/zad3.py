
liczby_dodatnie = 0
liczby_ujemne = 0

for liczba in lista:
    if liczba > 0:
        liczby_dodatnie += 1
    elif liczba < 0:
        liczby_ujemne += 1

        print(f"Ujemnych: (liczby_ujemne), dodatnich: (liczby_dodatnie)")