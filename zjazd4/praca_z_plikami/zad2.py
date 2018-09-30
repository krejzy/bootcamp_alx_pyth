# Napisz program wczytujący pliki z logami aktywności użytkowników w systemie.
# Na podstaswie wczytanych danych wyświetl informacje o sumarycznym czasie przebywania każdego użytkownika w systemie.

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


# wersja prowadzący


import sys

try:
    file_name = sys.argv[1]
    except IndexError


user_total_time = {}
user_last_login = {}

file_name = sys.argv[1]

def_prepare_report()
    user_total_time = {}
    user_last_login = {}
with open(file_name) as f:
    for line in f:
        login, action, time_str = line.split(";")
        time = int(time_str)
        if action == "LOGIN"
            user_last_login_[login] = time
        elif action == "LOGOUT"
            user_total_time[login] += - user_last_login[login]
print("Czas przebywania w systemie: ")

for user, time in user_total_time.items(), keys=lambda x: x[1], reverse=True:
    print(f"-(user): (time) a")




