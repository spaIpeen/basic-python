class IncorrectObject(Exception):
    def __init__(self, warning):
        self.warning = warning


main_list = []
while True:
    user_obj = input("Для выхода из программы введите 'stop'. Для продолжения заполнения списка введите число:\n")
    try:
        if user_obj == "stop":
            break
        elif user_obj.isdigit():
            main_list.append(int(user_obj))
        else:
            raise IncorrectObject("Необходимо ввести число!")
    except IncorrectObject as e:
        print(e)
print(main_list)

