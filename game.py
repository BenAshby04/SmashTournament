import random as rnd
from player import Player

class Game:
    def __init__(self,playerGame):
        self.player1 = playerGame[0]
        self.player2 = playerGame[1]
        self.winner = ""
    
    def simGame(self):
        baseProb = rnd.uniform(0,0.5)
        player1Skill = self.player1.generateGameSkill(baseProb)
        player2Skill = self.player2.generateGameSkill(baseProb)
        
        if player1Skill > player2Skill:
            self.winner = self.player1.playerName
            return self.player1
        elif player1Skill < player2Skill:
            self.winner = self.player2.playerName
            return self.player2
        else:
            self.simGame()
            
        
        