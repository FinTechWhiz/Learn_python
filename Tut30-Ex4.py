"""
#Pattern Printing
input1 (n) = integer (any number)
Input = interger (1 or 0)
if 1 then True
if 0 then false
Take boolen variable
Boolean = True or False

Say (Ture when n =4)#n is the no. of rows of stars

*
**
***
****

False, when n= 4
****
***
**
*
"""
"""
# Solution
i = 0
a = input(int("Enter a number:"))

while i==0:
    a = input(int("Enter a number: "))
    n = input(int("Enter 0 or 1"))
    if a==0:
        print("True")
        print("*")
    break
else:
    print("False")
    print("*")
"""
a = int(input("Enter a number (a): "))
b = int(input("Enter 0 or 1 (b): "))

if b == 1:
    print("True")
else:
    print("False")

if b == 1:
    for i in range(0, a ):
        print('*' * (i+1))
elif b==0:
    for i in range(a, 0, -1):
        print('*' * i)
else:
    print("Invalid Input")