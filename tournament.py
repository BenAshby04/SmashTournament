from player import Player
from game import Game
import math

class Tournament:
    def __init__(self):
        self.playerList = []
    
    def addPlayer(self,player):
        self.playerList.append(player)
    
    def generateBrackets(self):
        self.bracket = []
        
        playerListLength = len(self.playerList)
        halfOfPlayerLength = int(playerListLength / 2) 

        if int(math.floor(halfOfPlayerLength)) % 2 ==0:
            self.playerList.remove(self.playerList[-1])
            playerListLength = len(self.playerList)
            halfOfPlayerLength = int(playerListLength /2)
        elif int(math.ceil(halfOfPlayerLength)) % 2 ==0:
            self.addPlayer(Player())
            playerListLength = len(self.playerList)
            halfOfPlayerLength = int(playerListLength /2)
        
        sortedPlayerList = sorted(self.playerList,key=lambda x: x.skillModifier, reverse=True)

        # Populate bracket
        for i in range(halfOfPlayerLength):
            game = [sortedPlayerList[i], sortedPlayerList[-(i+1)]]
            self.bracket.append(game)
        
    
    def playBracket(self, bracket):
        winners = []
        for match in self.bracket:
            game = Game(match)
            winners.append(game.simGame())
        return winners
