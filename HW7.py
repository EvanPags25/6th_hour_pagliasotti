#Name:Evan Pagliasotti
#Hour: HR6
#assignment: HW7
from itertools import filterfalse

#1. Print Hello World!
print('hello world')
#2. Create three different boolean variables named wifi, login, and admin.
wifi=True
login=True
admin=False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminlogin=23
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".

if wifi==True:
    if login==True:
        if admin==True:
            adminlogin +=1
            print("welcome")
        else:
            print("no admin info")
    else:
        print("no login info")
else:
    print("no wifi")
