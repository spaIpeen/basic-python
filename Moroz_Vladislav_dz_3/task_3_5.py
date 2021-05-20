from random import choice, shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=3, repeat="yes"):
    """Returns 'n' random jokes from strings words"""
    count, jokes = 0, []
    if repeat == "yes":
        while count < n:
            jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
            count += 1
    elif repeat == "no":
        shuffle(nouns), shuffle(adverbs), shuffle(adjectives)
        while count < n:
            jokes.append(f"{nouns[count]} {adverbs[count]} {adjectives[count]}")
            count += 1
    return jokes


print(get_jokes(5, repeat="yes"))
