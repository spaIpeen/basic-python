tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Николай'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def journal(name, rank):
    for i in range(len(name)):
        if i > len(rank) - 1:
            yield name[i], None
        else:
            yield name[i], rank[i]


sort_journal = journal(tutors, classes)
print(type(sort_journal), *sort_journal, sep="\n")
