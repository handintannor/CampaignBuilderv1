from random import *

class Race:

    def __init__(self,name,asi,baseage,ageroll,age,size,speed,darkvision,traits,languages,subraces,description):
        self.name = name
        self.asi = asi
        self.baseage = baseage
        self.ageroll =  ageroll
        self.size = size
        self.speed = speed
        self.darkvision = darkvision
        self.traits = traits
        self.languages = languages
        self.subraces = subraces
        self.description = description
        self.age = Age(baseage, ageroll, age)
        
    def setAsi(self,stat,bonus):
        self.asi['{}'.format(stat)] = bonus
        
    def resetAsi(self):
        self.asi = {}
        
    def getAsi(self):
        return self.asi
    
    def getSize(self):
        return self.size

    def getSpeed(self):
        return self.speed

    def getDarkvision(self):
        return self.darkvision

    def getTraits(self):
        return self.traits

    def getLanguages(self):
        return self.languages

    def getSubraces(self):
        return self.subraces

    def getDescription(self):
        return self.description

class Age:
    def __init__(self,baseAge,rollAge,age):
        self.baseAge = baseAge
        self.rollAge = rollAge
        self.age = age

    def rand(self):
        x = self.rollAge.split("d")
        self.age = dice(int(x[0]),int(x[1]),self.baseAge)

    def set(self,age):
        self.age = age

    def get(self):
        return self.age

class Trait:
    def __init__(self, name, description, traittype):
        self.name = name
        self.description = description
        self.traittype = traittype


def dice(number, faces, bonus):
	#Faces = int(input("How many faces does each die have? "))
	#Number = int(input("How many dice do you want to roll? "))
	#Bonus = int(input("What is the bonus on the roll? "))
	Faces = faces
	Number = number
	Bonus = bonus
	xtotal = 0
	rolls = []
	for i in range(0,Number):
		rolls.append(randint(1,Faces))
		xtotal += rolls[i]
	xtotal = sum(rolls, Bonus)
	return xtotal



