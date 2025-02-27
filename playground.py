#Name: Evan Pagliasotti
#Hour: Hour 6
#Assignment: Playground
import random
#hello print
print('hello')

#calculater and name user inputs
input('what is your name?')
x=int(input("enter a interger"))
y=int(input("enter another interger"))
z=x+y
print('answer')
print(z)

#print moving on
print('moving on')

#numbers
numbers=[230849,893042,10,842]
print(numbers)

#try except
i=5
while i >= 0:
    print(i)
    i -= 1
    if i<0:
        raise Exception("i is less than 0")