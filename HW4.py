#name:Evan Pagliasotti
#class: HR6
#assignment: HW4

print('hello world')

carDict = {
    "make" : "Chevy",
    "model"  : "EL Camino",
    "years of production": "1969-2023",
}
print(carDict)
print(carDict["model"])
print(carDict["years of production"])

carDict["color"] = "blue"
print(carDict)

carDict.update({"wheels" : 4})
print(carDict)

carDictKeys = carDict.keys()
print(carDictKeys)

carDictValues = carDict.values()
print(carDictValues)

carDict.pop("wheels")
print(carDict)

carDict.clear()
print(carDict)

HourFive ={
    "student1":{
        "Name" : "Evan",
        "Grade" : "09",
        "esports": "no",

    },
    "student2": {
        "name": "dave",
        "grade" : "99",
        "esports": "perchance",
    }
}
print(HourFive["student1"])

print(HourFive["student2"]["esports"])

print(HourFive["student1"]["Name"],[])