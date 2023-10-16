"""
list1 = ["Harry", "Larry", "Carry", "Marie"]
for item in list1:
    print(item)
"""
"""

list1 = [ ["Harry",1], ["Larry",2], ["Carry",6], ["Marie",250]]
for item, lollypop in list1:
    print(item, lollypop)
"""
"""
list1 = [ ["Harry",1], ["Larry",2], ["Carry",6], ["Marie",250]]
dict1 = dict(list1)
for item, lollypop in dict1.items():
    print(item, lollypop)
"""
##Quize- make a list and print numbers only that is greater than 6.
l1 = [float, int,"Ram", 5, "shyam",10, "Gita", 101.2, "sita", 0.5, 6, "Ramesh", 50, 100]
for item in l1:
    if str(item).isnumeric() and item>6:
        print(item)

