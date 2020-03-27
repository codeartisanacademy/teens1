# open the file with a: open existing or create a new one
with open('news_2.txt', 'a') as my_file:
    my_file.write('\nThis is a new line from Python')

with open('newfile.txt', 'w') as new_file:
    new_file.write("Hello this is a new file")
    