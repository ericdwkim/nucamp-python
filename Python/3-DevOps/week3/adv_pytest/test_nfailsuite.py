def test_first_failure():
    numerator = 25
    assert numerator % 3 == 0

def test_second_failure():
    numerator = 7
    assert numerator % 2 == 0

def test_third_failure():
    numerator = 10
    assert numerator % 23 == 0
