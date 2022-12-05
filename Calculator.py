class Calculate:
    def __init__(self):
        pass
    def add(self, x1, x2):
        return int(x1)+int(x2)
    def multiply(self, x1, x2):
        return int(x1)*int(x2)
    def substract(self, x1, x2):
        return int(x1)-int(x2)
    def divide(self, x1, x2):
        if int(x2) == 0:
            return "ERROR"
        else:
            return int(x1)/int(x2)