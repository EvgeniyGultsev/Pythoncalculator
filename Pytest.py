from Calculator import Calculate

def pytestadd():
    assert Calculate.add(1, 3, 5)==8
def pytestmultiply():
    assert Calculate.multiply(1, 3, 5) == 15
def pytestdivide():
    assert Calculate.divide(1, 6, 2) == 3
def pytestsubstract():
    assert Calculate.substract(1, 3, 5) == -2
