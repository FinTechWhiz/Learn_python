"""
Create a username and password input interface
if correctly entered then print Login Successful
if incorrect input is given then print Invalid username or password. Try again with correct username or password
total no. of attempt = 4
if attempt exceeds 4 time then print Account blocked . please visit the nearest branch.
(Username = Ram & Password= 1234)
"""
ccu = ("Ram")
cp = ("Ram@11")
cpin = ("1212")
cOTP = ("1234")  # assume we recieve this OTP
i = 1
j = 1
k = 1
while (i <= 3):
    u = input("Username: ", )
    p = input("Password: ", )
    if cu == u and cp == p:
        print("Login Successful")
        break
    else:
        print("invalid username or password", "Please try again with correct username or password \n")
        print("Attempt left: ", 3 - i)
    i = i + 1
if (i>3):
    print("Account blocked. Please visit the nearest branch")


#When logged in successfully
if "Login Successful":
    balance = input("Enter Amount: ")
    while (j <= 3):
        pin = input("Enter your pin: ")
        if cpin == pin:
            print("Amount transferred successfully")
            break

        else:
            print("Invalid Pin \n")
            print("Attempt left: ", 3 - j)
        j = j + 1
    if (j > 3):
        print("Please reset your pin ")
        while (k <= 3):
            newpin = input("Enter new pin: ")
            OTP = input("Enter OTP")

            if cOTP == OTP:
                print("Pin reset successfully")
                break
            else:
                print("You entered wrong OPT. Please, try again with correct OTP")
                k = k + 1
        if (k > 3):
            print("Too many attempts. Try again after 30 minutes")


