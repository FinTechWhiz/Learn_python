grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56]
#print(grocery)
#print(grocery[2])
#print(grocery[5])
numbers = [2,7,9,11,3]
#print(numbers)
#print(numbers[2])
#print(numbers.sort())#This will not work
#numbers.sort()
#numbers.reverse()
#print(numbers)
#Now lets learn about slicing
"""
print(grocery[0:5])
print(numbers[0:5])#it is just like strings as learnt before
print(numbers[1:4])
"""
#the above function doesnot change the original list
# it will only print the required items
#But if we reverse list as mentioned above
#Then such functions will change the original list
"""
numbers.sort()
numbers.reverse()
print(numbers[4])
"""
#print(numbers[::1])
#print(numbers[::2])
# now lets move to extented slicing
#print(numbers[::-1])
#print(numbers[::-2])
# but if you define the range then it wont work for other than -1
#print(numbers[0:5:-2])# it wont show any item
# some other fuctions
#print(len(numbers))
#print(max(numbers))
#print(min(numbers))
"""
numbers.append(8)
numbers.append(9)
numbers.append(10)
numbers.append(12)
print(numbers)
#Some other functions#
sort(): Sorts the list in ascending order.
type(list): It returns the class type of an object.
append(): Adds one element to a list.
extend(): Adds multiple elements to a list.
index(): Returns the first appearance of a particular value.
max(list): It returns an item from the list with a max value.
min(list): It returns an item from the list with a min value.
len(list): It gives the overall length of the list.
clear(): Removes all the elements from the list.
insert(): Adds a component at the required position.
count(): Returns the number of elements with the required value.
pop(): Removes the element at the required position.
remove(): Removes the primary item with the desired value.
reverse(): Reverses the order of the list.
copy():  Returns a duplicate of the list
"""
#numbers.insert(1,13)
#print(numbers)
#numbers.remove(9)
#print(numbers)
#numbers.pop()
#numbers.pop(2)
#print(numbers)
#numbers[1] = 5
#print(numbers)
#mutuable-can change
#immutable-cannot change
#tp = [1, 2, 3]
#tp[1] = 8
#print(tp)
a= 1
b= 3
a, b = b,a
print(a, b)