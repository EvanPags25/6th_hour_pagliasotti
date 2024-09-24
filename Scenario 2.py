#name: Evan Pagliasoti
#hour: HR 6
#Assignment: Scenario 2

print('hello world')


partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

print(partyDictionary)

enemyDict={
   "harry" : {
    "Race" : "Human",
    "Class" : "Hunter",
    "Backround" : "anakolite",
    "Health" : 130000,
    "AC" : 4500,
    "Damage" : 8900,
}
}

y=partyDictionary["Gale"]["Damage"]
x= enemyDict["harry"]["Health"]
z=x-y
print(z)
