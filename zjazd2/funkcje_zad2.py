def test_więcej_niż_dla_pustego_napisu():
    assert 'więcej_niż'("", 1) == set()

def test_więcej_niż_dla_niepustego_napisu():
    assert 'więcej_niż'("", 2) == {'a'}


def test_więcej_niż{napis, liczba_wystąpień}:
    assert 'więcej_niż'("", 1) == set()