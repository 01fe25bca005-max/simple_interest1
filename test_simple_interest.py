from simple_interest import simple_interest

def test_simple_interest():
    assert simple_interest(1000, 5, 2) == 100.0

def test_simple_interest_zero():
    assert simple_interest(0, 5, 2) == 0.0

def test_simple_interest_negative():
    assert simple_interest(-500, 5, 2) == -50.0