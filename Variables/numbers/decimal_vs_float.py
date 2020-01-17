from decimal import Decimal

# product_cost = 88.40
# commission_rate = 0.08
# qty = 450

# product_cost += (commission_rate * product_cost)
# print(product_cost * qty) # 42962.4 floating point total

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451 Decimal total (High percision)