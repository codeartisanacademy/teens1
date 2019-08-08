print('i can\'t do this')
print("Goethe said \"hello\"")

email = ' john@gmail.com '.strip()

print(len(email))

length = len(email)

print(email)

name = 'john'

print('Hi my name is %s and my email is %s' % (name.title(), email))

print(name.upper())

print(email[length-1])

print(email[-1])

# slice 3 characters from 0
print(email[0:3])

# slice from 0 to last characters
print(email[0:])

# count how many characters
print(email.count('o'))

# find the first index of a character
first_o = email.find('o')
print(email.find('o'))

print(email.find('o', first_o+1))

numbers = '123'

print(numbers.isnumeric())

password = 'secret123'

print(password.isalnum())

greet = 'mrs.'
full_name = 'jane doe'

print("hello {0} {1}".format(greet.title(), full_name.title()))

print("hello {greeting} {fullname}".format(greeting=greet, fullname=full_name))

print(full_name.startswith('j'))


