import os

if os.path.exists('M:/PYTHON_EDUREKA/FILE_HANDLING/DELETION/test.txt'):
    os.remove("M:/PYTHON_EDUREKA/FILE_HANDLING/DELETION/test.txt")
else:
    print("File doesnt exits in the file location")