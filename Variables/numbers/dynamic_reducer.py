import operator
from functools import reduce

"""
dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '-') # -4
dynamic_reducer([1, 2, 3], '*') # 6
dynamic_reducer([1, 2, 3], '/') # .16667
"""
"""
list_add = [1, 2, 3]
list_subtract = [1, 2, 3]
list_multiply = [1, 2, 3]
list_divide = [1, 2, 3]

print(reduce(operator.add,list_add))
print(reduce(operator.sub,list_subtract))
print(reduce(operator.mul,list_multiply))
print(reduce(operator.truediv,list_divide))
"""

def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], '+'))
print(dynamic_reducer([1, 2, 3], '-'))
print(dynamic_reducer([1, 2, 3], '*'))
print(dynamic_reducer([1, 2, 3], '/'))