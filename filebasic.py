import os

# current directory
print("My current directory: " + os.getcwd())

files = os.listdir()

# os.mkdir("new_directory")

files = os.listdir()

#s.rename('new_directory', 'old_directory')

# os.remove('junk.txt')
# os.removedirs('old_directory')

# to open a file open()
# open mode: r, w, x, a
with open('news.txt', 'r') as my_file:
    # text = my_file.read(6)
    # print(my_file.tell())
    # my_file.seek(0)
    # first_line = my_file.readline()
    # second_line = my_file.readline()
    # print(first_line)
    # print(second_line)
    for line in my_file.readlines():
        print(line, end='')


'''
for item in files:
    print(item)
'''

