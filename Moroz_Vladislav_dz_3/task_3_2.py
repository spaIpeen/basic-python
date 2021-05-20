def num_translate(str_num):
    if str_num in words_translate:
        print(words_translate[str_num])
    elif str_num.lower() in words_translate:
        print(words_translate[str_num.lower()].capitalize())
    else:
        print("None")


words_translate = {"one": "один", "two": "два", "three": "три","four": "четыре", "five": "пять",
                   "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

num_translate("Three")
