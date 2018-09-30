# Napisz program z graficznym interfejsem użytkownika - GUI, do obliczania kosztów przejazdu na zadanym dystansie
#  na podstawie spalania samochodu oraz ceny paliwa.

import tkinter

def oblicz koszty():
   a = a_entry.get()
   b = b_entry.get()
   wynik_label.configure(text=f"Wynik: {a*b}")

a = input("podaj [Dystans]: ")
b = input("podaj ilość zużytego paliwa: ")

print
"Dystans: ", a, " [km]\n"
print
"Zużyto paliwa: ", b, " [litrów]\n"

root = tkinter.Tk()
root.columnconfigure(1, weight=1)
root.title("Kalkulator_kosztów")

# wersja prowadzący

import tkinter

def policz spalanie():
    try:
        dystans = int(dystans_e.get())
        spalanie = int(spalanie_e.get())
        cena = int(cena_e.get())
        koszt = (dystans/100) * spalanie * cena
        wynik_l.configure(text=koszt)
    except ValueError:
        tkinter.messagebox.showerror("Błędnje poprawić dane")



root = tkinter.Tk()
root.tittle("Kalkulator spalania")

dystans_1 = tkinter.Label(master-root, text="Dystans")
