portal = []


def write_data(sale):
    with open("bakery.csv", "a", encoding="utf-8") as f:
        count = f.tell()
        f.write(f"{sale}\n")
    with open("tell.txt", "a", encoding="utf-8") as file:
        file.write(f"{count}\n")


def tell_read():
    with open("tell.txt", "r", encoding="utf-8") as f:
        while True:
            aa = f.readline()
            if not aa:
                break
            portal.append(int(aa.strip()))


def read_data(a=None, b=None):
    tell_read()
    with open("bakery.csv", "r", encoding="utf-8") as file:
        if a is not None and b is None:
            file.seek(portal[a - 1])
            while True:
                aa = file.readline()
                if not aa:
                    break
                print(aa.strip())
        elif a is not None and b is not None:
            file.seek(portal[a - 1])
            while file.tell() <= portal[b - 1]:
                aa = file.readline()
                if not aa:
                    break
                print(aa.strip())
        else:
            while True:
                aa = file.readline()
                if not aa:
                    break
                print(aa.strip())


def change_data(c, d):
    with open("bakery.csv", "r+", encoding="utf-8") as f:
        f.seek(portal[c - 1])
        f.write(f"{d}")


if __name__ == "__main__":
    write_data(55)
    write_data(98)
    read_data(1)
    bb = float(input("Enter Enter"))
    change_data(2, bb)
