#Name: Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW10
#help from: stackoverflow.com and programiz.com

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i=0
while i <= 30:
    print(i)
    i += 1
print("hello world")
#2. Create a while loop that prints only even numbers
#between 1 and 30.
i=2
while i <= 30:
    if ( i % 2==0):
        print (i,)
    i+=1
#3. Create a while loop that repeats until the user
#inputs the number 0.


number = int(input('Enter a number: '))

while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))
