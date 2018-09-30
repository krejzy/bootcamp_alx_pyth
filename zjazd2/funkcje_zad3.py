# napisz funkcje obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami.
# Znaki pomiędzy którymi ma odbywać się zliczanie powinny być argumentami z waqrtościami domyslnymi - odpowiednio <i>.
# Nawiasy mogą być zagnieżdzone i mogą wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nbawiasami liczone
# są zgodnie z poziomem zagnieżdzenia.

def policz_liczbę_znaków(napis, liczba_wystapien):
    wynik = set()

    for litera in napis:
        if napis.count(litera) > liczba_wystapien:
            wynik.add(litera)

    return wynik


def test_policz_liczbę_znaków_dla_pustego_znaku():
    assert wiecej_niz("", 1) == set()


def test_policz_liczbę_znaków_dla_niepustego_znaku():
    assert wiecej_niz("", 1) == set()


# prowadzący

def policz_znaki(napis):
    if start == end:

    ile_znaków = 0
    poziom = 0
    for litera in napis:
        if litera


def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0


def test_policz_znaki_gdy_brak_nawiasów():
    assert policz_znaki("ala ma kota") == 0


def test_policz_znaki_z_nawiasami_jeden_poziom():
    assert policz_znaki("ala ma kota") == 2


def test_policz_znaki_z_podanymi_parametrami():
    assert policz_znaki('ala')


def test_policz_znaki_z_nawiasami_jeden_poziom():
    assert policz_znaki("Ala <ma> kota") == 2
    assert policz_znaki("Ala <ma ko>ta") == 5
    assert policz_znaki("Ala <ma> <ko>ta") == 4
    assert policz_znaki("Ala << ma >> kota") == 8


import pytest
def test_raises_error():

    with pytest.raises(ValueError):
        policz_znaki("AAA", ".", ".")
