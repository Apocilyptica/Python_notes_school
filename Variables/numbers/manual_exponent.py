from functools import reduce

"""
manual_exponent(2, 3)
#> 8

manual_exponent(10, 2)
#>100
"""

# My solutions

manual_exponent = reduce((lambda a, b: a ** b), (2, 3))

print(manual_exponent)

def manual_exponent(number, exponent):
    return reduce((lambda a, b: a ** b), (number, exponent))

print(manual_exponent(10, 2))

# iterdiv approach

def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

#functional solution

def manual_exponent(num, exp):
    computed_list = [num] * exp
    return (reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))