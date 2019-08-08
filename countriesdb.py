# create a list of countries
countries = ['indonesia', 'malaysia', 'thailand']

# ask user to enter country
country = input('enter a country: ')

# check if the input is in the list already or not
if len(country) == 0:
    input('enter a country: ')
else:
    if country not in countries:
        countries.append(country)
    else:
        print(country + " already in the list")

print('------ countries ------')
for c in countries:
    print(c.title())


