import json

ob1 = ["AAA", 2, 3, ["Rafał\u142", "Napis"]]

print(type(json,dumps(ob1)))

# zapis do pliku
with open("example.json", 'w') as f:
    json.dump(ob1. f)

# otwarcie pliku
with open("example.json", 'w') as f:
   data = json.load(f)
   print(data)
   print (type(data))
   data.append("coś tam")

print(data)

with open("example.json", 'w') as f:
    json.dump(data. f)



