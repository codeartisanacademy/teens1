# simple function
def greet():
    print('hello world')


greet()


# function that returns something
def add(x, y):
    return x + y


result = add(2, 5)
print(result)


# create a function that will print "Hello Mr. John" or "Hello Ms. Jane"
def say_hello(salutation, name):
    print('hello {0}. {1}'.format(salutation.title(), name.title()))


say_hello('Mr', 'Mike')