from functools import wraps


def ticket(func):
    @wraps(func)
    def sub_ticket(*args):
        line = [f"{func.__name__}({args[i]}:{type(args[i])})" for i in range(len(args))]
        return line
    return sub_ticket


@ticket
def calc(x):
    return x**3


print(", ".join(calc(5, 8, 9, 23)))

