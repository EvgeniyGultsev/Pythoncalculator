import Pytest
from Calculator import Calculate
def pytest():
    assert Calculate.add(1, 3, 5)==8
    assert Calculate.multiply(1, 3, 5) == 15
    assert Calculate.divide(1, 6, 2) == 3
    assert Calculate.substract(1, 3, 5) == -2
if __name__ == '__main__':
    pytest()