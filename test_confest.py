import pytest
from conftest import PreciseCalculator
from calculator import Calculator


@pytest.fixture
def precise_calculator():
    return PreciseCalculator(precision=2)


@pytest.mark.parametrize("a, b, expected", [
    (2.345, 1.111, 3.46),
    (1.555, 1.555, 3.11),
    (0.1234, 0.8766, 1.0),
])
def test_add_with_precision_fixture(precise_calculator, a, b, expected):
    assert precise_calculator.add(a, b) == expected


@pytest.fixture
def custome_precise_calculator():
    return PreciseCalculator(precision=3)

@pytest.mark.parametrize("a,b,expected", [
    (2.345, 1.111, 3.456),
    (1.555, 1.555, 3.11),
    (0.1234, 0.8766, 1.0),
    (0.3333, 0.3333, 0.667),
    (5.6789, 2.1234, 7.802),
    (0.9999, 0.0001, 1.0),
])
def test_add_rounding_at_different_precisions(custome_precise_calculator, a, b, expected):
    assert custome_precise_calculator.add(a, b) == expected