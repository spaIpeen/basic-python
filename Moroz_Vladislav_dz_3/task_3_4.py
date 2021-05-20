def thesaurus_adv(*args):
    lastname_key, people = [], {}
    for man in args:
        if man.split(" ")[1][:1] not in lastname_key:
            lastname_key.append(man.split(" ")[1][:1])
    for l_let in lastname_key:
        lastname_val, sort_man = {}, []
        for person in args:
            if person.split(" ")[1][:1] == l_let:
                sort_man.append(person)
        for name_val in sort_man:
            if name_val.split(" ")[0][:1] in lastname_val:
                lastname_val[name_val.split(" ")[0][:1]] += [name_val]
            else:
                lastname_val[name_val.split(" ")[0][:1]] = [name_val]
        if l_let not in people:
            people.setdefault(l_let, lastname_val)
    print(people)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
