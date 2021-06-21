class ComplexNum:
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        var = ""
        self.exp = self.exp.split(" ")
        for i in range(len(self.exp)):
            if self.exp[i].isdigit() or self.exp[i][-1] == "i":
                var += f"{self.exp[i]} + "
        return var[:-3]

    def __add__(self, other):
        sum_result = ""
        for i in range(len(self.exp)):
            if self.exp[i].isdigit():
                sum_result += f"{int(self.exp[i]) + int(other.exp[i])} + "
            elif self.exp[i][-1] == "i":
                sum_result += f"{int(self.exp[i][:-1]) + int(other.exp[i][:-1])}i"
        return sum_result

    def __mul__(self, other):
        aaa, bbb = [], []
        for i in range(len(other.exp)):
            if self.exp[i].isdigit():
                aaa.append(int(self.exp[i]))
            elif self.exp[i][-1] == "i":
                aaa.append(int(self.exp[i][:-1]))
            if other.exp[i].isdigit():
                bbb.append(int(other.exp[i]))
            elif other.exp[i][-1] == "i":
                bbb.append(int(other.exp[i][:-1]))
        mul_res = f"{aaa[0] * bbb[0] - aaa[1] * bbb[1]} + {aaa[1] * bbb[0] + aaa[0] * bbb[1]}i"
        return mul_res


first_cpx, second_cpx = "52 + 7i", "3 + 44i"
cpx1, cpx2 = ComplexNum(first_cpx), ComplexNum(second_cpx)
print(cpx1), print(cpx2)
print(cpx1 + cpx2), print(cpx1 * cpx2)

