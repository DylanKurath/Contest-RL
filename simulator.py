from moves import executeMove, findMove
from bot import Brain

contestTypes = ['cool', 'beauty', 'cute', 'smart', 'tough']

class Player():
    def __init__(self, userControlled=False):
        self.moves = []
        self.knownEnemyMoves = [[],[],[]]  
        
        self.hearts = 0
        self.chosenMove = None
        self.awaitingComboMove = None
        self.enemyLastMoves = []
        self.status = None
        self.userControlled = userControlled
        self.brain = Brain()

    def setMoves(self, moves):
        self.moves = moves

    def pickMove(self):
        self.chosenMove = self.brain.pickMove(self)
        return self.chosenMove

    def selectMoveset(self):
        self.moves = self.brain.selectMoveset(self)
        return self.moves

def simulateRound(players, voltage):
    turnNumber = 1
    for player in players:
        executeMove(player.chosenMove, turnNumber)
        turnNumber += 1
    return voltage

def simulationWindow():
    return 0

# Simulate a game with inputted players
if __name__ == '__main__':
    print("Gen 3 Hoenn Contest Simulation")

    selectedType = False
    contestType = None
    while not selectedType:
        contestType = input('Enter the contest type (cool, beauty, cute, smart, tough): ').lower
        try:
            contestType = contestTypes.index(contestType)
            selectedType = True
        except:
            print("Invalid contest type")

    print("Create player movesets:")
    players = []
    for playerNum in range(4):
        print("Player " + str(playerNum + 1))
        userControlled = input("Do you want to control this player? (y/n): ").lower
        userControlled = (userControlled == 'y')
        player = Player(userControlled=userControlled)
        moves = []
        aiMoves = input('Should the ai select the moveset? (y/n): ').lower
        if aiMoves == 'y':
            aiMoves = player.selectMoveset(contestType)
            print("Moveset: " + aiMoves[0]["Name"] + ", " + aiMoves[1]["Name"] + ", " + aiMoves[2]["Name"] + ", " + aiMoves[3]["Name"])
        else:
            for movesNum in range(4):
                moveSelected = False
                while not moveSelected:
                    moveName = input("Enter move " + str(movesNum) + " name: ")
                    move, suggestion = findMove(moveName)
                    if move:
                        moves.append(move)
                        moveSelected = True
                    else:
                        useSuggestion = input("Move not found. Did you mean " + suggestion['Name'] + "? (y/n): ").lower
                        if useSuggestion == 'y':
                            moves.append(suggestion['ID'])
                            moveSelected = True
            player.setMoves(moves)
        players.append(player)


    for roundNum in range(5):
        print("Round " + str(roundNum + 1))

        