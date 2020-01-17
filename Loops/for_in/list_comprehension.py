num_list = range(1, 11)
# cubed_nums = []

# Base way
# for num in num_list:
#     cubed_nums.append(num ** 3)

# even_numbers = []

# for num in num_list:
#     if num % 2 == 0:
#         even_numbers.append(num)

# List Comprehension
# cubed_nums = [num ** 3 for num in num_list]

even_numbers = [num ** 3 for num in num_list if num % 2 == 0]


# print(cubed_nums)
print(even_numbers)