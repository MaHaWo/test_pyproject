from example_package_mahawo import add_one, subtract_one


def test_add_one():
    assert add_one(1) == 2


def test_subtract_one():
    assert subtract_one(1) == 0
