countries = ['indonesia', 'singapore']
fruits = []
# add an item to a list
countries.append('malaysia')

# accessing an item in the list
print(countries[-1])

countries.insert(1, 'vietnam')

print(countries)

for country in countries:
    print(country)

# membership of an item in a list
print('thailand' not in countries)

print(max(countries))
print(min(countries))

print(countries.count('vietnam'))

#countries.remove('singapore')

print(countries[0:3])

print(len(countries))

for x in range(1,11):
    print("hello %d" % x)