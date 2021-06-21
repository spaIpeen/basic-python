def check(var):
    def _check(func):
        def wrapper(*args):
            if var(*args) == 0:
                raise ValueError("wrong val")
            return func(*args)
        return wrapper
    return _check


@check(lambda var: var > 0)
def calc(x):
    return x**3


print(calc(8))

