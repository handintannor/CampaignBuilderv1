from dice import *
from verify import *
from copy import deepcopy
import math


class Stats:
    def __init__(self):
        self.Strength = Attribute("Strength", 10)
        self.Dexterity = Attribute("Dexterity", 10)
        self.Constitution = Attribute("Constitution", 10)
        self.Intelligence = Attribute("Intelligence", 10)
        self.Wisdom = Attribute("Wisdom", 10)
        self.Charisma = Attribute("Charisma", 10)
        self.attributes = [self.Strength, self.Dexterity, self.Constitution, self.Intelligence, self.Wisdom,
                           self.Charisma]
        self.rolls = []

    def assignStats(self):
        temp = deepcopy(self.rolls)
        for n in range(0, 6):
            attribute = self.attributes[n]
            print("Setting score for", attribute.name)
            for i in range(0, len(temp)):
                print(temp[i], end=' ')
            print()

            choice = getValue(1, 6)
            if choice == -1:
                for j in range(0, len(self.attributes)):
                    self.attributes[j].setVal(10)
                return

            else:
                self.setAttribute(attribute, temp, choice)

    def setAttribute(self, attribute, templist, choice):
        print(attribute.name)

        attribute.setVal(templist[choice])
        print("You selected", templist[choice], "for", attribute.name, '\n')

        del templist[choice]
        return templist

    def rollStats(self):
        self.resetRolls()
        for n in range(0, 6):
            x = rollstat()
            self.rolls.append(x)
        return

    def resetRolls(self):
        self.rolls.clear()


class Attribute:
    def __init__(self, iname, ival):
        self.name = iname
        self.value = ival

    def setVal(self, ival):
        self.value = ival

    def setName(self, iName):
        self.name = iName

    def calcMod(self):
        if self.value < 0:
            return -5
        if self.value < 10:
            return int(math.floor((self.value-10)/2))
        else:
            return int((self.value-10)/2)