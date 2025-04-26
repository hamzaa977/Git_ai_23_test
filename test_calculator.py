import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected




@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2),
    (0, 0, 0)
])
def test_sub_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected



@pytest.mark.parametrize("a, b, expected", [
    (2, 5, 10),
    (-3, 4, -12),
    (1.5, 2, 3.0),
    (2.0, 2.5, 5.0),
    (0, 10, 0)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == pytest.approx(expected)



@pytest.mark.parametrize("a, b, expected", [
    (50, 5, 10),
    (33, 16, 2.0625),
])
def test_div_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.divide(a, b)==expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (3, 3, 27),
    (1, 1, 1)
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (4, 4, 256),
    (2, -1, 0.5),
])
def test_pow_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.power(a, b) == expected



@pytest.mark.parametrize("n, expected", [
    (0,1), 
    (1,1), 
    (2,2), 
    (10,3628800),  
])
def test_factorial_parameterized(n, expected):
    calc = Calculator()
    assert calc.factorial(n) == expected

def test_factorial():
    calc = Calculator() 
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        calc.factorial(-22)




@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (10, 55)
])
def test_fibonacci_parameterized(n, expected):
    calc = Calculator()
    assert calc.fibonacci(n) == expected

def test_fibonacci():
    calc = Calculator() 
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative numbers"):
        calc.fibonacci(-2)


# def test_add():
#     calc = Calculator()
#     assert calc.add(3, 5) == 8
#     assert calc.add(-1, 1) == 0
#     assert calc.add(-1, -1) == -2

# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2

# def test_multiply():
#     calc = Calculator()
#     assert calc.multiply(2,5)==10
#     assert calc.multiply(3.0,3.0)==9.0

# # def test_div(calculator):
# #     assert calculator.divide(10, 2) == 5
# #     assert calculator.divide(5, 2) == 2.5
# #     assert calculator.divide(2, 0) == "Invalid"

# def test_divide():
#     calc = Calculator()
#     assert calc.divide(10,2)==5
#     assert calc.divide(5, 2)==2.5

#     with pytest.raises(ValueError):
#         calc.divide(5,0)