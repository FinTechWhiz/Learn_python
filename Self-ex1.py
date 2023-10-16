"""
Create a username and password input interface
if correctly entered then print Login Successful
if incorrect input is given then print Invalid username or password. Try again with correct username or password
total no. of attempt = 4
if attempt exceeds 4 time then print Account blocked . please visit the nearest branch.
(Username = Ram & Password= 1234)
"""
cu = ("Ram")
cp = 1234
i = 1
while (i<=4):
    u = input("Username: ")
    p = input("Password :")

    if cu==u and cp==p:
        print("Login Successful")
        break
    else:
        print("invalid username or password","Please try again with correct username or password")
        print("Attempt left: ", 4-i)
    i=i+1

if (i>4):
    print("Account blocked. Please visit the nearest branch")