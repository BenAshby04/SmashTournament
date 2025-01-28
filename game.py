import random as rnd
from player import Player

class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = ""
    
    def simGame(self):
        baseProb = rnd.uniform(0,0.5)
        player1Skill = self.player1.generateGameSkill(baseProb)
        player2Skill = self.player2.generateGameSkill(baseProb)
        
        if player1Skill > player2Skill:
            self.winner = "player1"
        elif player1Skill < player2Skill:
            self.winner = "player2"
        else:
            self.simGame()
            
        
        