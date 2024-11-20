#Name: Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW12
#helkp from https://www.w3schools.com/python/python_howto_reverse_string.asp

import time

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
for k in range(5, 0, -1):
    time.sleep(0.4)
    print(k)
print("Hello World")
#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
i=2
for i in range(1,31):
    if ( i % 2==0):
        print (i,)
#3. Create a for loop that prints 5 different animals from a list.
animals = ["Tiger", "Panda", "Dog", "Cat", "Duck"]
for y in animals:
    print(y)
#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for z in input("Give me a word: ")[::-1]:
    print(z)
