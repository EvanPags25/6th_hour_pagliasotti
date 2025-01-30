#Name: Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random

def hello_world():
    print("hello world")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanbag= ["red","orange","green","blue","yellow"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def beanbagpull():
    if not beanbag:
        print("list is empty")
    else :
        bean_choice= random.choice(beanbag)
        print(bean_choice)
        beanbag.remove(bean_choice)
        repeat()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat():
    replayInput = input("Would like to play again? Y/N")
    if replayInput == "y":
        beanbagpull()
    else:
        exit()

#5. Call the #3 function at the bottom
hello_world()
beanbagpull()