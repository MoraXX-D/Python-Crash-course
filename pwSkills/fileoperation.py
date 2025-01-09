import os

# open file in write mode
f = open("text.txt",'w')
f.write("This is my first file.\n")
f.close()
f = open("text.txt",'w')
f.write("this is my file.\n")
f.close()

# write without truncating
f = open("text.txt",'a')
f.write("I like Data Science")
f.close()

# Read
f = open("text.txt",'r')
print(f.read())

f.seek(0) # take the reading pointer to the beginning of the file
f = open("text.txt",'r')
print(f.readline()) # read the first line
f.close()

size = os.path.getsize('text.txt')
print(size) # print the size of the file in bytes