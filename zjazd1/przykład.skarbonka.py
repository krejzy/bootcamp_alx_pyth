skarbonka = 20
#program ma wyświetlać aktualną wartośc skarbonki 
# i pytać o kolejną wpłatę 
# tak długo aż w skarbonce zbierze się odpowiednia kwota np.100

while skarbonka < 100:
wpłata = int(input('Ile wpłacasz'))
skarbonka += wpłata
print(f' Po wpłaceniu {wpłata} w skarbonce jest {skarbonka}')
print ('Osiągnąłeś swój cel :)')
