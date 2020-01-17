"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
# last_item = sale_prices[-1]
# index_of_last_item = sale_prices.index(last_item)
# median_index = index_of_last_item / 2
median_index = int(sorted_list.index(sorted_list[-1]) / 2)

print(sorted_list[median_index])

# JH Slicing option
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice +1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)