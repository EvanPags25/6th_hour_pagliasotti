#Name: Evan Pagliasotti
#Hour: HR6
#assignment: Scenario


print('hello world')

#dictnary
monsterDict ={

    "subjectA":{
       "name" : "JETSAM",
        "damage" : (60),
    },

   "subjectB":{
        "name": "KINGSTON",
        "damage": (20),
    } ,

    "subjectC":{
       "name" : "Tarriot",
        "damage" : (55),
    },

    "subjectD":{
       "name" : "Los Angelo",
        "damage" : (88),
    },

    "subjectE":{
        "name": "ATLAS",
        "damage": (60),
    }

}

print(monsterDict)

monsterDict["subjectA"]["damage"]=int(input("enter new damage"))
monsterDict["subjectB"]["damage"]=int(input("enter new damage"))
monsterDict["subjectC"]["damage"]=int(input("enter new damage"))
monsterDict["subjectD"]["damage"]=int(input("enter new damage"))
monsterDict["subjectE"]["damage"]=int(input("enter new damage"))

print(monsterDict)