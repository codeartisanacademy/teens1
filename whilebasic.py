x = 1

while x < 6:
    print(x)
    x+=1


names = []

stop = False

while not stop:
    print('enter a name or press q to quit')
    name = input('enter a name: ')
    if name == 'q':
        stop = True
    else:
        names.append(name)

for name in names:
    print(name)


x = 2
y = 5

if x > 2 or x < 5:
    print('x is less greater than 2 and less than 5')