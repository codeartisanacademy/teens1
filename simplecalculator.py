# prompt user to enter numbers
x = input('enter the first number: ')
y = input('enter the second number: ')
operation = input('type a for addition, type s for subtraction: ')

# convert the inputs to string
x_int = int(x)
y_int = int(y)

if operation == 'a':
    print('the result is: ', x_int + y_int)
elif operation == 's':
    print('the result is: ', x_int - y_int)
else:
    print("i don't know what you want")

