# ask user to enter the city
city = input('enter the city: ')
# ask user to enter the college name
college = input('enter the college name: ')

college_info = dict(city=city, college=college)
# print out in the format of
# City: XYZ
# College: ABC

print(college_info['city'])
print(college_info['college'])