import urlib.reqest

f = urlib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
print(f.status)
data = f.read()
data = json.loads(data)


kursy = data[0] ['rates']
for kurs in kursy:
    print(f"{kurs['currency']") - {kurs[code]} - {kurs['mid']}")
