ile_podzielnych = 0

for i in range(101):
    if i%3 == 0 or i%5 ==0:
        ile_podzielnych += 1
        print(i)

print(f"W przedziale 0-100 jest (ile_podzielnych) liczb podzielnych przez 3 lub 5")

for element in range(1, 100):
  if element % 3 == 0:
    print(element)
