x = int(input(f'podaj pozycję gracza X: '))
y = int(input(f'podaj pozycję gracza Y: '))
if 10 <= x <= 90 and 10 <= y <= 90:
   print (środek planszy ')
elif 0 <= x < 10 and 10 <= y <= 90:  
   print (lewa krawędź ')
elif 90 < x <= 100 and 10 <= y <= 90:
   print (prawa krawędź ')
   
   

   
   
if x < 0 or x > 100 or y > 100:
   print ( 'poza planszą')
elif x < 10 and y > 90:
   print (lewy górny róg ') 
 
 