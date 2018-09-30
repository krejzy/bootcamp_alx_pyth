import sys

print(sys.args)
wejście = "pliki_wejściowe/dane.txt"

with open(wejście) as f:
    print(f.read)


    try:
        wejście = sys.argv[1]
        with open(wejście) as f:
            dane = f.readf()
            dane = splitlines()
            for i, linia in enumerate(dane, start=1):
                print(f"(i): (linia")

except IndexError
    print("Podaj nazwe pliku")


with open(sys.args(1)) as