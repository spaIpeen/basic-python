top_border = int(input("Введите n: "))
odd_nums = (el for el in range(1, top_border + 1, 2))

if top_border % 2 == 1:
    for i in range(top_border // 2 + 1):
        print(next(odd_nums))
else:
    for i in range(top_border // 2):
        print(next(odd_nums))
