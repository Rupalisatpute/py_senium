from src import arithmetic_functions as AF
import pytest
import platform

def my_function():
    print("Inside my_function")

@pytest.mark.One
@pytest.mark.Sanity
def test_addition():
    assert AF.addition(2, 3) == 5
    assert AF.addition(3, 3) == 6
    assert AF.addition(4, 6) == 10
    assert AF.addition(5, 6) == 11
    print("Pass")

@pytest.mark.One
@pytest.mark.Smoke
def test_multiplication():
    assert AF.multiplication(2, 3) == 6
    my_function()

@pytest.mark.Two
@pytest.mark.Smoke
def test_subtraction():
    assert AF.subtraction(3, 2) == 1

@pytest.mark.Two
@pytest.mark.Sanity
def test_division():
    assert AF.division(4, 2) == 2

@pytest.mark.skipif(platform.system().lower()=="windows", reason="Test not supported on Windows version")
# @pytest.mark.skip(reason="Skipping Testcase at will")
def test_skipif_example():
    print("This should not get printed on Mac os")
# skip
# skipif