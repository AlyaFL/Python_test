import pytest 
from hometask.calculator.calculator import Calculator


@pytest.fixture()
def calc() -> Calculator:
    return Calculator()

@pytest.mark.parametrize(
    'x, y, result',
    [
        (1, 2, True),
        (0, 0, True),
        (1.0, 0, False),
        (-2, "qwe", False),
        ([1, 2, 3], 1, False),
        ({"a":1}, 2, False),
    ]
)
def test_is_number(calc: Calculator, x: int, y: int, result: bool):
    assert calc.is_number(x, y) == result

invalid_value = [
    ('qwe', 3, TypeError),
    (1, 'qwe', TypeError),
    (1, 1.0, TypeError),
    (1.2, 1, TypeError),
    ([1, 2, 3], 4, TypeError),
    (3, {"b":2}, TypeError),
]

@pytest.mark.parametrize(
    'x, y, result',
    [
        (1, 2, 3),
        (0, 0, 0),
        (-2, 1, -1),
        (1, -3, -2),
    ]
)    
def test_add_valid(calc: Calculator, x: int, y: int, result: bool):
    assert calc.add(x, y) == result 

@pytest.mark.parametrize(
    'x, y, result',
    invalid_value
)
def test_add_invalid(calc: Calculator, x: int, y: int, result: bool):
    answer = calc.add(x, y)
    assert TypeError == result

@pytest.mark.parametrize(
    'x, y, result',
    [
        (2, 1, 1),
        (0, 0, 0),
        (-2, 1, -3),
        (1, -3, 4),
    ]
)    
def test_subtract_valid(calc: Calculator, x: int, y: int, result: bool):
    assert calc.subtract(x, y) == result 

@pytest.mark.parametrize(
    'x, y, result',
    invalid_value
)
def test_subtract_invalid(calc: Calculator, x: int, y: int, result: bool):
    answer = calc.subtract(x, y)
    assert TypeError == result

@pytest.mark.parametrize(
    'x, y, result',
    [
        (6, 3, 2),
        (-3, 1, -3),
        (8, -2, -4),
        (-10, -5, 2),
        (0, -5, 0),
    ]
)    
def test_divide_valid(calc: Calculator, x: int, y: int, result: bool):
    assert calc.divide(x, y) == result 

@pytest.mark.parametrize(
    'x, y, result',
    invalid_value +
    [(1, 0, TypeError)]
)
def test_divide_invalid(calc: Calculator, x: int, y: int, result: bool):
    answer = calc.divide(x, y)
    assert TypeError == result

@pytest.mark.parametrize(
    'x, y, result',
    [
        (2, 3, 6),
        (-3, 1, -3),
        (8, -2, -16),
        (-10, -5, 50),
    ]
)    
def test_multiply_valid(calc: Calculator, x: int, y: int, result: bool):
    assert calc.multiply(x, y) == result 

@pytest.mark.parametrize(
    'x, y, result',
    invalid_value
)
def test_multiply_invalid(calc: Calculator, x: int, y: int, result: bool):
    answer = calc.multiply(x, y)
    assert TypeError == result

@pytest.mark.parametrize(
    'x, y, result',
    [
        (6, 3, 0),
        (-3, 9, 6),
        (-2, 10, 8),
        (-10, -5, 0),
    ]
)    
def test_mod_valid(calc: Calculator, x: int, y: int, result: bool):
    assert calc.mod(x, y) == result 

@pytest.mark.parametrize(
    'x, y, result',
    invalid_value
)
def test_mod_invalid(calc: Calculator, x: int, y: int, result: bool):
    answer = calc.mod(x, y)
    assert TypeError == result

@pytest.mark.parametrize(
    'x, y, result',
    [
        (6, 3, 216),
        (2, -3, 0.125),
        (-5, 4, 625),
        (-10, 0, 1),
        (0, 5, 0),
    ]
)    
def test_power_valid(calc: Calculator, x: int, y: int, result: bool):
    assert calc.power(x, y) == result 

@pytest.mark.parametrize(
    'x, y, result',
    invalid_value
)
def test_power_invalid(calc: Calculator, x: int, y: int, result: bool):
    answer = calc.power(x, y)
    assert TypeError == result

@pytest.mark.parametrize(
    'x, result',
    [
        (9, 3),
        (16, 4),
        (0, 0)
    ]
)    
def test_root_valid(calc: Calculator, x: int, result: bool):
    assert calc.root(x) == result 

@pytest.mark.parametrize(
    'x, result',
    [
    (-5, TypeError),
    (-10, TypeError)
    ]
)
def test_root_invalid(calc: Calculator, x: int, result: bool):
    answer = calc.root(x)
    assert TypeError == result