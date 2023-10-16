# File IO Basics
"""
"r"- Open file for reading - default
"w"- Open a file for writing
"x"- Create file if not exists
"a"- Add more content to a file
"t"- text mode - default
"b"- binary mode
"+"- read and write

"""
#Question of the day.
#func1() how to read docstring of this function?
#ans

def function1 (a,b):
    """This is a function which will multiply 2 numbers"""
    multiply = (a*b)
    return multiply
print(function1.__doc__)
