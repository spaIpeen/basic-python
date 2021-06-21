class DivisionByZero(Exception):
    def __init__(self, warning):
        self.warning = warning


user_num = int(input("Делим 100 на ваше число, введите свой делитель: "))

try:
    if user_num == 0:
        raise DivisionByZero("На ноль делить нельзя")
except DivisionByZero as e:
    print(e)
else:
    print(100 / user_num)
finally:
    print("Конец программы")

