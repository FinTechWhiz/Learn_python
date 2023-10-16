"""
i = 0
while (i<45):
    print(i+1, end=" ")
    i = i+1
"""
"""
i = 0
while (True):
    print(i+1, end=" ")
    i = i+1
# This loop will run to infinite  untill stopped.
"""
"""
# TO stop this loop we use break.\
i = 0
while (True):
    print(i+1, end=" ")
    if(i==44):
        break #To stop the loop
    i = i+1
"""
"""
##Continue function in loop
#To continue when condition is met, and ignore other remaining functions
i = 0
while (True):
    if i+1<5:
        i = i+1
        continue
    print(i+1, end=" ")
    if(i==44):
        break
    i = i+1
    #To stop the loop
"""
## Take input form users. If they entered
# number greater than 100 print congrats and
#if less than 100 print try again and ask for
# input again and again untill he entere >100.

while (True):
    i = int(input("Enter a number\n"))
    if i<=100:
        print("Try again!\n")
        continue
    if(i>100):
        print("Congratulation! You have crossed 100\n")
        break
"""
## (Alternatively)
while (True):
    i = int(input("Enter a number\n"))
    if i>100:
        print("Congratulation! You have crossed 100\n")
        break
    else:
        print("Try again!\n")
        continue
"""