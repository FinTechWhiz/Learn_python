"""
a = 9
b = 8
c = sum((a, b)) #built in function
print (c)
"""
"""
def function1():
    print("Hello you are in fuction 1")
#print(function1())
function1()
"""
"""
def function1(a, b):
    print("Hello you are in fuction 1", a+b)
function1(5, 7)
"""

"""
def function2(a,b):
    average = (a+b)/2
    print(average)
function2(5, 7)

"""
def function2(a,b):
    """This is a function which will calculate average of two numbers"""
    average = (a+b)/2
    #print(average)
    return(average)

print(function2.__doc__)