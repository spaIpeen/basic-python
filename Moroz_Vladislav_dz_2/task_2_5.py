default_price = [228.93, 940.3, 201.66, 727.64, 192.6,
                 589, 271.88, 348.42, 309.73, 370.95,
                 183.02, 201.52, 723, 294.13, 629.86,
                 725.93, 152.41, 406.38, 796.99, 139]
# Task_2_5_A
nice_price = []
for price in default_price:
    if price % 1 == 0:
        price /= 1
    _price = str(price)
    ruble_str, penny_str = _price.split(".")
    penny_int = int(penny_str)
    view = f'{ruble_str} руб {penny_int:02d} коп'
    nice_price.append(view)
print(id(nice_price), nice_price)
# Task_2_5_B
nice_price.sort()
print(id(nice_price), nice_price)
# Task_2_5_C
rev_table = list(reversed(nice_price))
print(id(rev_table), rev_table)
# Task_2_5_D
print(id(rev_table), rev_table[4::-1])
