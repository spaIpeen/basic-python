from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, size=0, height=0):
        self.V, self.H = size, height

    def __add__(self, other):
        return round(self.V / 6.5 + 0.5, 2) + (2 * other.H + 0.3)


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def size_calc(self):
        return f"{round(self.V / 6.5 + 0.5, 2)}"


class Costume(Clothes):
    def __init__(self, height):
        super().__init__(0, height)

    @property
    def height_calc(self):
        return f"{2 * self.H + 0.3}"


coat, costume = Coat(55), Costume(23)
print(f"Расход ткани:\n- для пальто: {coat.size_calc}\n- для костюма: {costume.height_calc}"
      f"\n- общий расход: {coat + costume}")
