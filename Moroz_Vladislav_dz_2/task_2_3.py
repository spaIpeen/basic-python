temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(temp), temp)
for item in temp[:]:
    if item.isdigit():
        temp.insert(temp.index(item), '"')
        temp.insert(temp.index(item) + 1, '"')
        temp[temp.index(item)] = f"{int(item):02d}"
    if item[:1] == "+":
        temp.insert(temp.index(item), '"')
        temp.insert(temp.index(item) + 1, '"')
        temp[temp.index(item)] = f"+{int(item):02d}"
print(id(temp), temp)
print(" ".join(temp))
