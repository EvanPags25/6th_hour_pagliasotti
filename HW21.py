#Name: Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sports={
    "sport1" :{
        "name" : "Basketbal",
        "players" : 5,
        "ball" : True,
    },

    "sport2" : {
        "name" : "Football",
        "players" : 11,
        "ball" : True,
    },

     "sport3" : {
         "name" : "volleyball",
         "players" : 6,
         "ball" : True

    }

}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def pull(x,y,z):
    print (x+y+z)

#3. Call the function with arguments here
pull(sports["sport1"]["players"],sports["sport2"]["players"],sports["sport3"]["players"],)