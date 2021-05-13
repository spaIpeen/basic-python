percent = []


# Функция для создания списка
def create_list():
    for i in range(1, 21):
        percent.append(i)
    print(percent)


create_list()
# Вычисление соответствующего склонения
for element in percent:
    if element == 1:
        print(f"{element} процент")
    elif 1 < element <= 4:
        print(f"{element} процента")
    elif 4 < element <= 20:
        print(f"{element} процентов")
# here homework