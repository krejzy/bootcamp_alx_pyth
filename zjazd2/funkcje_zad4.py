def test_formatuj_napis_bez_znaczników():
    assert formatuj ("hello world") == "hello world"

def test_formatuj_wiele_napisów_bez_znaczników():
    assert formatuj ("hello world") == "hello world"

def test_formatuj_napis_ze_znacznikiem():
    assert formatuj ("subway is ok") == "subway is ok"

def formatuj (
        'koszt $cena PLN','kwota $cens brutto', cena = 10,
        )

def test_formatuj_napis_ze_znacznikiem():
    assert formatuj (
        'koszt $cena PLN',
        'kwota $cens brutto'.
        cena = 10,
        )