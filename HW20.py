#Name:
#Class: 6th Hour
#Assignment: HW20
from logging import raiseExceptions

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")

#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    y=int(input())
    print(100/y)
except ZeroDivisionError:
    print("divide by zero error")
except:
    print("something else went wrong")
#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.

try:
    z= int(input("enter a number"))
    print(z)
except ValueError:
    print("not a number")


#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
i=5
while i >= 0:
    print(i)
    i -= 1
    if i<0:
        raise Exception("i is less than 0")