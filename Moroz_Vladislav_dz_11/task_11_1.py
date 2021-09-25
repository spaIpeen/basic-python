class Data:
    data = ""

    def __init__(self, user_data):
        Data.data = user_data

    @classmethod
    def make_dig(cls):
        int_data = Data.data.split("-")
        for i in range(len(int_data)):
            int_data[i] = int(int_data[i])
        return int_data

    @staticmethod
    def valid_dig():
        check_data = Data.make_dig()
        if 0 < check_data[0] < 32:
            print("ok")
        else:
            raise ValueError("Неверно введено число даты")
        if 0 < check_data[1] < 13:
            print("ok")
        else:
            raise ValueError("Неверно введен месяц даты")
        if 0 < check_data[2] < 2022:
            print("ok")
        else:
            raise ValueError("Неверно введен год даты")


data_checker = Data("08-04-1998")
print(type(data_checker.make_dig()[0]), type(data_checker.make_dig()[1]), type(data_checker.make_dig()[2]))
data_checker.valid_dig()

