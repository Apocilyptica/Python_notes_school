# 3.21 to equal a pretty price like 3.95 or 3.99 anything you want
# pretty_price(3.20, 99) returns 3.99
# pretty_price(3.20, 0.99) returns 3.99

# My Solution
from math import floor as f


def pretty_price(price, pretty):
    base_price = f(price)

    if pretty > 1:
        new_price = pretty / 100
    else:
        new_price = pretty

    return base_price + new_price


print(f"Price: ${pretty_price(3.20, 99)}")
print(f"Price: ${pretty_price(3.20, 0.99)}")

# JH Solution
def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.50, 0.95))
print(pretty_price(3.50, 95))
