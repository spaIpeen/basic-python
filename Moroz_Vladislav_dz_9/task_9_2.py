class Road:
    _length, _width = 0, 0

    def __init__(self, length, width, weight_sq_mt, thickness):
        self._weight_sq_mt, self._thickness, self._length, self._width = weight_sq_mt / 1000, thickness, length, width

    def asphalt(self):
        return self._length * self._width * self._weight_sq_mt * self._thickness


calc = Road(20, 5000, 25, 5)
print(calc.asphalt())
