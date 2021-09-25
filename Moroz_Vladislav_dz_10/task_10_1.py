class Matrix:
    def __init__(self, nums):
        self.nums_mtx = nums

    def __str__(self):
        a = ""
        for i in range(len(self.nums_mtx)):
            a += f"{self.nums_mtx[i]} \n".replace(']', ' |').replace('[', '| ').replace(",", "")
        return a

    def __add__(self, other):
        sum_result = ""
        for i in range(len(self.nums_mtx)):
            sum_result += "| "
            for k in range(len(self.nums_mtx[i])):
                sum_result += f"{self.nums_mtx[i][k] + other.nums_mtx[i][k]} ".replace(']', '|').replace('[', '|')
            sum_result += "|\n"
        return sum_result


first_list, second_list = [[4, 6, 3], [2, 5, 1]], [[3, 1, 4], [5, 2, 6]]
mtx1, mtx2 = Matrix(first_list), Matrix(second_list)
print(mtx1)
print(mtx2)
print(mtx1 + mtx2)
