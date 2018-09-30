import tkinter

from Zjazd4.praca_z_siecią_zad2_slack import get_location_weather

def pobierz pogode():
    lokalizacja = lokalizacja_entry.get()
    lok_id = get.location_weather(lok_id)
    pogoda = get_location_weather(lok_id)
    output = present_results (pogoda)
    pogoda_label_configure(test=output)



root = tkinter.Tk()
root.tittle("Pogoda")

lokalizacja_label = tkinter.Label(master)