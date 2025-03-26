#Name:Evan Pagliasotti
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class People:
    def __init__(self, health, damage, speed, max_health):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health= max_health

    def damage_over_time(self):
        for i in range(1,11):
            self.health -=random.randint(1,6)
            print(self.health)
            time.sleep(1)
    def healer_health(self):
        self.health +=(30)
        if self.health>100:
            self.health=100
#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior=People(100,20,30,100)
healer=People(60,10,30,60)
thief=People(50,30,40,50)
mage=People(45,35,25,45)

#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
random_choice= random.randint(1,4)
if random_choice ==1:
    warrior.damage_over_time()
elif random_choice ==2:
    healer.damage_over_time()
elif random_choice ==3:
    thief.damage_over_time()
elif random_choice ==4:
    mage.damage_over_time()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
if warrior.health<warrior.max_health:
   warrior.healer_health()
elif healer.health< healer.max_health:
    healer.healer_health()
elif thief.health< thief.max_health:
    thief.healer_health()
elif mage.health<mage.max_health:
    mage.healer_health()