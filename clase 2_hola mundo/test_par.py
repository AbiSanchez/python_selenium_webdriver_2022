def es_par(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    else:
        return False


def test_positive():
    result = es_par(2, 4)
    assert result


def test_negative():
    result = es_par(3, 9)
    assert not result

def test_difente():
    result = es_par(3, 4)
    assert not result

