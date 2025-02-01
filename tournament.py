from player import Player
import math

class Tournament:
    def __init__(self):
        self.playerList = []
    
    def addPlayer(self,player):
        self.playerList.append(player)
    
    def generateBrackets(self):
        bracket = []
        
        playerListLength = len(self.playerList)
        halfOfPlayerLength = playerListLength / 2 

        print(math.floor(halfOfPlayerLength))
        if int(math.floor(halfOfPlayerLength)) % 2 ==0:
            self.playerList.remove(self.playerList[-1])
            playerListLength = len(self.playerList)
            halfOfPlayerLength = int(playerListLength /2)
        elif int(math.ceil(halfOfPlayerLength)) % 2 ==0:
            self.addPlayer(Player())
            playerListLength = len(self.playerList)
            halfOfPlayerLength = int(playerListLength /2)
        

        print(halfOfPlayerLength)
        
        sortedPlayerList = sorted(self.playerList,key=lambda x: x.skillModifier, reverse=True)

        # Populate bracket
        for i in range(halfOfPlayerLength):
            game = [sortedPlayerList[i], sortedPlayerList[-(i+1)]]
            bracket.append(game)
        
        print(bracket)

        pass