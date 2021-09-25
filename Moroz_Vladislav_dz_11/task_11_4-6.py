class Warehouse:
    technics, number, departament = "", "", ""

    def __init__(self, *args):
        for i in args:
        Warehouse.technics, Warehouse.number, Warehouse.departament = teh, count, dep
        Warehouse.valid_dig()

    @classmethod
    def taking(cls):
        dep = Warehouse.technics, Warehouse.number, Printer.size_calc
        return dep

    @staticmethod
    def transfer():
        transfer_teh = {Warehouse.departament: Warehouse.taking()}
        print(transfer_teh)

    @staticmethod
    def valid_dig():
        if not Warehouse.technics.isalpha():
            raise ValueError("Неверно введен тип техники")
        elif not Warehouse.number.isdigit():
            raise ValueError("Неверно введено кол-во техники")
        elif not Warehouse.departament.isalpha():
            raise ValueError("Неверно введен отдел")


class OfficeEquipment(Warehouse):
    def __init__(self, name, count):
        self.name, self.count = name, count


class Printer(OfficeEquipment):
    def __init__(self, name, count, type_print, speed_print):
        super().__init__(name, count)
        self.type_print, self.speed_print = type_print, speed_print

    def size_calc(self):
        return self.type_print, self.speed_print


class Scanner(OfficeEquipment):
    def __init__(self, name, count, type_scan, speed_scan):
        super().__init__(name, count)
        self.type_scan, self.speed_scan = type_scan, speed_scan


class Xerox(OfficeEquipment):
    def __init__(self, name, count, type_copy, speed_copy):
        super().__init__(name, count)
        self.type_copy, self.speed_copy = type_copy, speed_copy


a = Warehouse("Printer", "3", "bookkeeping")
a.transfer()
b = Printer("Kyocera", "3", "type", "speed")


