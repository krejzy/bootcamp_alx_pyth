# Napisz program wczytujący listę adresów email i tworzący nowy plik z odfiltrowaną zawartością
# Wejściowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter, linie zawierający białe błedne adresy email
# (brak znaku  @ lub występuje on wiele razy). Wynikowy plik powinien zawierać posortowanje poprawne adresy email


import sys

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    input_file = "pliki_wejściowe/emails.txt"
    input_file = "emails_corrected.txt"

def collect_emails(input_file):
    emails = set()

    with open(input_file) as f:
        for line in f:
            if line.count("@") == 1:
                line = line.strip(). lower()

    return emails

    def save emails(emails, output_file)
    with open(output_file, 'w') as f:
        for email in sorted(emails):
            if line.count("@") == 1:
                line = line.strip().lower()


