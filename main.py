from player import Player
from tournament import Tournament

def main():
    tournament = Tournament()
    print("How many players do you want to compete in the tournament?")
    players = int(input())
    for i in range(players):
        tournament.addPlayer(Player())
    
    while len(tournament.playerList) > 1:
        tournament.generateBrackets()
        tournament.playerList = tournament.playBracket(tournament.playerList)
    print("The winner is: {}".format(tournament.playerList[0].playerName))

if __name__ == "__main__":
    main()