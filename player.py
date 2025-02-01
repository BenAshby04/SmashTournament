import random as rnd

class Player:
    def __init__(self):
        self.playerName = ""
        self.wins = 0
        self.skillModifier = 0.0
        self.points = 0
        self.generateName()
        self.generateSkillModifier()
        
    # Picks a random name from the playerDictionary and adds a random number on the end
    def generateName(self):
        with open("playerDictionary.txt", "r") as file:
            nameList = []
            for line in file:
                nameList.append(line.strip("\n"))
            
            name = nameList[rnd.randint(0,len(nameList) - 1)]
            nameNum = str(rnd.randint(1,1000))
            self.playerName = name + nameNum
            
            
    def generateSkillModifier(self):
        skillMod = rnd.uniform(0.75,2)
        self.skillModifier = round(skillMod, 2)
    
    def generateGameSkill(self,baseUpper):
        base = rnd.uniform(0,baseUpper)
        base = (base * self.skillModifier) + self.skillModifier
        return base
        