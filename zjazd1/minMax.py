while True 
txt = int(input('Podaj kolejną liczbę: ')
if txt == 'koniec':
break
liczba = int(txt)
if liczba > max|
max = liczba
if liczba < min:
min = liczba 


while True 
txt = int(input('Podaj kolejną liczbę: ')
if txt == 'koniec':
break
liczba = int(txt)
if 'pierwszy raz':
min = max = liczba 






liczba = int(input(' ile liczb: '))
pierwsza = {}
for i in range (liczba): 
liczba = int(input('wprowadź liczbę ')
max = 0
print (f'Maximum: {max}')

print ' Maximum number ', int(max)
print ' Minmum number ', int(min)























def max(tab):
m=tab[0]
for i in tab: #pętla for w Pythonie to bardziej "foreach"
if i>m:   #i przyjmuje wartości kolejnych komórek tablicy tab
m=i
return m
 
def min(tab):
m=tab[0]
for i in tab:
if i<m:
m=i
return m
 
tab=[]; #utworzenie tablicy
for i in range(10):
tab.append(random.randint(0,20)) #wylosowanie wartośći
print "tablica: "+str(tab) #wypisanie całej tablicy
print "min: "+str(min(tab))
print "max: "+str(max(tab))