import os

file = open("M:/PYTHON_EDUREKA/FILE_HANDLING/TestFile.txt", 'r')
for line in file:
    print(file.readlines())
file.close()