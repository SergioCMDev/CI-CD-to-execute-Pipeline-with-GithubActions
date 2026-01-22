from Operations import add, product, division, subs

def test_add():
    assert add(1, 2) == 3, "Should be 3"
    assert add(1, 3) == 4, "Should be 4"

def test_prod():
    assert product(1, 2) == 2, "Should be 2"
    assert product(14, 2) == 28, "Should be 28"

def test_sub():
    assert subs(1, 2) == 0, "Should be 0"
    assert subs(2, 1) == 1, "Should be 1"

def test_div():
    assert division(1, 2) == 0.5, "Should be 0.5"
    assert division(2, 1) == 2, "Should be 2"
    assert division(2, 0) == 0, "Should be 0"
    assert division(0, 1) == 0, "Should be 0"

if __name__ == "__main__":
    test_add()
    test_prod()
    test_sub()
    test_div()
    print("Everything passed")