class Cell:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return self.count - other.count if self.count - other.count > 0 else print("Разность меньше или равна нулю")

    def __mul__(self, other):
        return self.count * other.count

    def __floordiv__(self, other):
        return self.count // other.count

    def __truediv__(self, other):
        return self.count / other.count

    def make_order(self, column):
        for i in range(self.count // column):
            print("*"*column)
        print("*" * (self.count % column))


first, second, third = Cell(10), Cell(3), Cell(15)
print(first + second), print(first - second), print(first * second), print(first // second), print(first / second)
third.make_order(4)
