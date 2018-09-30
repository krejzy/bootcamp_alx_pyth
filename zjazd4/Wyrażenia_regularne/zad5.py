import re

post_code_pattern = re.compile('\d(2)-\d(3)')
email_pattern = re.compile ('[\w\-\.]+8[\w\-.]+\.\w+')
date_pattern


with open("input.txt") as f:
    text = f.read()
    kody = post_code_pattern.findall(text)
    print(kody)

    import re

    tekst =

    sciezka = r'\d\d\d\d'
    dopasowanie = re.search(sciezka, tekst)

    if dopasowanie:  # Sprawdzamy czy udalo sie cos znalezc
        numer = dopasowanie.group()
        print numer