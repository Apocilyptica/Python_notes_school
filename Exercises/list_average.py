# My Solution
from functools import reduce as r


num_list = [1, 2, 3, 4, 5, 6]
num_total = r(lambda a, b: a + b, num_list)
num_count = len(num_list)
num_average = num_total / num_count

print(num_average)

# JH Solution
def get_average(num_list):
    total = r(lambda total, element: total + element, num_list)

    return total / len(num_list)


print(get_average(num_list))
