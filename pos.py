beverages = {'coke':1.5, 'orange juice':1.0, 'iced tea': 1.0}

orders = []

orders.append(beverages['coke'])
orders.append(beverages['iced tea'])

total = 0.0

for order in orders:
    total += order

print(total)