#Name: Evan Pagliasotti
#Class: 6th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code

#Party Dictionary Goes Here

partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "Armor" : 17,
        "Damage" : random.randint(1,6)+random.randint(1,6)+3,
        "atk MOD" : 4,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "Armor" : 14,
        "Damage" : random.randint(1,6)+2,
        "atk MOD" : 7,

    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "Armor" : 14,
        "Damage" : random.randint(1,10),
        "atk MOD" : 5,

    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "Armor" : 8,
        "Damage" : random.randint(1,6)+4,
        "atk MOD" : 6,

    }
}



#Enemy Dictionary Goes Here
monsterDict ={

    "subjectA":{
       "name" : "JETSAM",
        "damage" : random.randint(1,5),
        "health" : 13,
        "Armor"  : 10,
        "atk MOD" : 4

    },

   "subjectB":{
        "name": "KINGSTON",
        "damage": random.randint(1,6),
        "health": 8,
        "Armor" : 13,
       "atk MOD" : 6

   } ,

    "subjectC":{
        "name" : "Tarriot",
        "damage": random.randint(2,6)+3,
        "health": 5,
        "Armor" : 12,
        "atk MOD":  3

    },

    "subjectD":{
       "name" : "Los Angelo",
        "damage" : random.randint(1,10)+2,
        "health": 9,
        "Armor" : 15,
        "atk MOD" : 4

    },

    "subjectE":{
        "name": "ATLAS",
        "damage": random.randint(1,8),
        "health" : 1,
        "Armor" : 10,
        "atk MOD" : 4

    }

}



#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#Step 7: Roll the attack roll for party member (d20 + Attack Modifier)

#Step 8: Check to see if the party member hits the enemy
if random.randint(1,20)+partyDictionary["Gale"]["atk MOD"] >= monsterDict["subjectE"]["Armor"]:
    monsterDict["subjectE"]["health"] -= partyDictionary["Gale"]["Damage"]
    print(f"gale hits, he rolled {partyDictionary["Gale"]["Damage"]}")
    if monsterDict["subjectE"]["health"] <= 0:
        print("subjectE is dead")
        exit()
    else:
        print("subjectE is still alive")
else:
    print("gale misses")
#Step 9: Roll damage if it hits and subtract from enemy health

#Step 10: Check to see if the enemy is still alive

#Step 11: If the enemy is alive, repeat steps 7 through 10 but with the enemy attacking

if random.randint(1,20) + monsterDict["subjectE"]["atk MOD"] >= partyDictionary["Gale"]["Armor"]:
    print("subjectE hits")
    monsterDict["subjectE"]["health"] -= partyDictionary["Gale"]["Damage"]
    if  monsterDict["subjectE"]["health"]<=0:
        print("Gale is dead")
        exit()
    else:
        print("Gale is still alive")
else:
    print("SubjectE misses")



#Combat Code Goes Here

class Frendly_team:
    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

class opposing_team:
    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod

    def __init__(self, health, damage, name, atk_mod):
        self.name = name
        self.damage = damage
        self.health = health
        self.atk_mod = atk_mod


