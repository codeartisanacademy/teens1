countries = {'name': 'Indonesia', 'capital_city': 'Jakarta', 'language': 'Bahasa Indonesia', 'country_code': 62}

#print(countries)

#print(countries['name'])

#print(countries.get('capital_city'))

#print(countries.keys())
#print(countries.values())

asian_countries = [
    {'name': 'Malaysia', 'capital': 'Kuala Lumpur'},
    {'name': 'Indonesia', 'capital': 'Jakarta'},
    {'name': 'Thailand', 'capital': 'Bangkok'}
]

for country in asian_countries:

    for k in country.keys():
        print(k + ": " + country[k])

    print('-' * 20)



countries.update({'capital': 'Balikpapan', 'president':'Joko Widodo'})

countries['capital_city'] = 'Samarinda'

countries.pop('capital_city')
for country in countries.values():
    print(country)

colleges = dict(city='NYC', name='NYU')

print(colleges)