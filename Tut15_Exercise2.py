#Exercise2 - Falutly Calculator
"""
Design a calculator which will correctly
solve all the problems except the following
ones: 45*3=55, 56+9= 77, 56/6=4, 90-50=23
Your program should take operator and the
two numbers as input form the user and
then return the result.
"""
n1 = float(input("Enter 1st number"))
op = input("Enter operation")
n2 = float(input("Enter 2nd number"))
if n1==43 and op=="*" and n2 == 3:
    print("55")
elif n1==56 and op=="+" and n2 == 9:
    print("7")
elif n1 == 56 and op == "/" and n2 == 6:
        print("4")
elif n1 == 90 and op == "-" and n2 == 50:
        print("23")
elif op == "*":
    print(n1*n2)
elif op == "+":
    print(n1+n2)
elif op == "/":
    print(n1/n2)
elif op == "-":
    print(n1-n2)
else:
    print("Error, Invalid Character")



