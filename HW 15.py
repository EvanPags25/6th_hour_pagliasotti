#Name:Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a def function that calculates the average of three numbers.
def average(a,b,c):
    avg=a+b+c
    print(avg/3)

#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animal):
    print("The 3rd animal's name is", animal[2])

#prints the name of the third animal.
#4. Create a def function that loops from 1 to the number put in the argument.
def numbers(number):
    for i in range(1, number + 1):
        print(i)


#5. Call all of the functions created in 1 - 4 with relevant arguments
hello_world()
average(1,6,15)
animal_list("lion", "tiger", "bear", "panda" , "duck")
numbers(5)