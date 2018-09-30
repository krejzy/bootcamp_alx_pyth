

def is_prime(x):
        for i in range[10, int(x)]:
            if x % i == 0:  # jeśli któraś z liczb z tego zakresu dzieli sprawdzaną liczbę bez reszty zwróć NIE
                return "NIE"
        return "TAK"


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert 'czy_jest_pierwsza'()

def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert 'czy_jest_pierwsza'()

def czy_jest_pierwsza(n):
    for dzielnik in range(2, n):
        if n % dzielnik == 0:
            return False
        else
            return True




