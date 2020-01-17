"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""
# My Solution
sales = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12
}

print(list(sales.values())[0])
print('g ' + list(sales.values())[0] * '$')
print('f ' + list(sales.values())[1] * '$')
print('t ' + list(sales.values())[2] * '$')
print('o ' + list(sales.values())[3] * '$')

# JH Solution
sales_JH = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12
}

print('g ' + sales_JH['google'] * '$')
print('f ' + sales_JH['facebook'] * '$')
print('t ' + sales_JH['twitter'] * '$')
print('o ' + sales_JH['offline'] * '$')