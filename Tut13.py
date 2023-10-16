"""
var1 = 6
var2 = 56
var3 = int(input())

if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")
"""
"""
list1 = [5, 7, 3]
print(7 in list1)
if 7 in list1:
    print("Yes its in the list")
else:
    print("No its not in the list")
"""
"""
print("What is your age?")
age = int(input())
if age>18:
    print("Yes. You can drive")
elif age==18:
    print("Not sure. you need to visit our office physically")
else:
    print("No. Your cannot drive")
"""
age = int(input("Enter your age: "))

if 18 < age <= 100:
    print("You can drive.")
elif 5 <= age < 18:
    print("NO, you cannot drive.")
elif age == 18:
    print("Not sure, please visit our office.")
else:
    print("Error: Invalid age input.")