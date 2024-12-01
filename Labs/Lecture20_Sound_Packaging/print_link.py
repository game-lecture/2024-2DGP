# file = 'C:\\Users\\dustinlee\\Documents\\pyinstaller\\dist\\main\\_internal'
file = 'W:/WorkCoding/2023-2DGP-Master/Labs/2023_Lecture19_Sound_Packaging\\print_link.py'
line = 14
# string = f'File "{file}"'.replace("\\", "/")
# string = f'File "{file}", line'
string = f'File "{file}", line {line}'
# string = f'File "{file}", line {line}'.replace("\\", "/")
# string = f'File "{file}, line {max(line, 1)}"'.replace("\\", "/")

print(f'File "{file}", line {line}')
print(f'File "{file}", line {0}')

import inspect

def print_link(file=None, line=None):
    """ Print a link in PyCharm to a line in file.
        Defaults to line where this function was called. """
    if file is None:
        file = inspect.stack()[1].filename
    if line is None:
        line = inspect.stack()[1].lineno
    string = f'File "{file}", line {max(line, 1)}'.replace("\\", "/")
    print(string)
    return string

# Default to this line and file (randomtesting.py in generallibrary, line 14)
print_link()

# Link relatively to another repository through parent's directory
print_link("../generalvector/generalvector/vector.py", 23)

# Link relatively to README which is in same directory as randomtesting.py
print_link("README.md", 1)

# Link absolutely to any file
print_link("A:/hello.txt", 1)

