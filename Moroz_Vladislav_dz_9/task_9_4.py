class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.color} {self.name} повернула на{self.direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")

    def check_police(self):
        print(f"Полицейская: {self.is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 60 else print("Превышена допустимая скорость")

    def check_police(self):
        print(self.is_police)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 40 else print("Превышена допустимая скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def check_police(self):
        print(f"Полицейская: {self.is_police}")


c, t, s, w, p = Car(40, "Белая", "Audi"), TownCar(40, "Черная", "BMW"), SportCar(40, "Красная", "Ferrari"),\
                WorkCar(40, "Вишневая", "Lada"), PoliceCar(40, "Серая", "Skoda")

c.go(), c.turn("право"), c.stop()
c.show_speed(), c.check_police()
print(f"Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n")
#
# t.go(), t.turn("право"), t.stop()
# t.show_speed(), t.check_police()
# print(f"Марка: {t.name}, Цвет: {t.color}, Скорость: {t.speed}, Полицейская: {t.is_police} \n")
#
# s.go(), s.turn("право"), s.stop()
# s.show_speed(), s.check_police()
# print(f"Марка: {s.name}, Цвет: {s.color}, Скорость: {s.speed}, Полицейская: {s.is_police} \n")
#
# w.go(), w.turn("право"), w.stop()
# w.show_speed(), w.check_police()
# print(f"Марка: {w.name}, Цвет: {w.color}, Скорость: {w.speed}, Полицейская: {w.is_police} \n")
#
# p.go(), p.turn("право"), p.stop()
# p.show_speed(), p.check_police()
# print(f"Марка: {p.name}, Цвет: {p.color}, Скорость: {p.speed}, Полицейская: {p.is_police} \n")

