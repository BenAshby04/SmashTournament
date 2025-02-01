from player import Player
from tournament import Tournament

def main():
    tournament = Tournament()

    for i in range(16):
        tournament.addPlayer(Player())
    
    tournament.generateBrackets()

if __name__ == "__main__":
    main()