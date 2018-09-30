import csv

with open ("pliki_wejściowe/WA_Sales_products_2012-14.csv") as f:
    dane = csv.DictReader(f)
    for row in dane:
        print(row["Year"])

