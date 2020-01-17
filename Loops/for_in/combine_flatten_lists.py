legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

# raw_db = [legacy_customers, new_customers]
# [['Alice', 'Bob'], ['Tiffany', 'Kristine']]

for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer)

print(new_customers)