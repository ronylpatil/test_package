# test each component individually

import pytest
from dummypackage12624 import addition, subtraction, division
from dummypackage12624 import InvalidUserInput

good_input_data = [(2, 1), (6, 2), (9, 7)]

bad_input_sub = [(1, 2), (4, 5)]

bad_input_div = [(3, 0), (0, 0)]

@pytest.mark.parametrize("a, b", good_input_data)
def test_addition(a, b):
     assert addition(a, b) == (a + b)


@pytest.mark.parametrize("a, b", good_input_data)
def test_subtraction(a, b):
     assert subtraction(a, b) == (a - b)
     

@pytest.mark.parametrize("a, b", good_input_data)
def test_division(a, b):
     assert division(a, b) == (a / b)


@pytest.mark.parametrize("a, b", bad_input_sub)
def test_subtraction_failed(a, b):
    with pytest.raises((InvalidUserInput)):
        subtraction(a, b)

@pytest.mark.parametrize("a, b", bad_input_div)
def test_division_failed(a, b) :
     with pytest.raises((InvalidUserInput)) :
          division(a, b)

# cmd: pytest -v or pytest ./src/tests/test_unit.py