# # # # # Подзадание "a"
def count_sum():
    sum_cube_num = 0
    # Перебираем каждое число списка
    for cube_number in not_even_cube:
        count = 0
        # Перебираем каждую цифру числа и складываем их
        for symbol in cube_number:
            count += int(symbol)
        # Проверяем делится ли нацело сумма цифр числа на 7
        if count % 7 == 0:
            sum_cube_num += int(cube_number)
    print(sum_cube_num)


# Создаем список из кубов нечетных чисел
not_even_cube = []
for num in range(1, 1001):
    if num % 2 == 1:
        not_even_cube.append(str(num ** 3))
print(not_even_cube)
# Вызываем ранее созданную функцию
count_sum()

# # # # # Подзадание "b" со звездочкой "c"
count_change = 0
# Меняем все элементы последовательности, прибавляя 7 к каждому
for cube_num in not_even_cube:
    mediator = int(not_even_cube[count_change]) + 17
    not_even_cube[count_change] = str(mediator)
    count_change += 1
print(not_even_cube)
# Вызываем ранее созданную функцию
count_sum()
# here homework