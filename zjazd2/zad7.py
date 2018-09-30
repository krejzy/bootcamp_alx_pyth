# Napisz program zliczający liczbę wystąpień samogłosek (a,e,i,o,u,y) w podanym napisie
ile_samoglosek = 0
SAMOGLOSKI = a,e,i,o,u,y
text = input("Podaj text: ")

for l in text:
    if l.lower() in SAMOGLOSKI:
      ile_samoglosek += l


print(f'ile samoglosek)

print "Nigdy nie czytalem 'Potopu'."   # Nigdy nie czytalem 'Potopu'.
print dna.count("samogloski")
