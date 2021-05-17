default_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                'директор аэлита']

for position_name in default_list:
    name = position_name.split()[-1]
    print(f"Привет, {name.title()}")
