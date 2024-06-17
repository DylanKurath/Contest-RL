from enum import Enum

class Effect(Enum):
    NO_EFFECT = "This move has no additonal effect"
    FRONT = "??? / Affected by how well the appeal in front goes."
    TYPELESS = "Always increases applause regardless of contest type."
    RECKLESS = "The user loses twice as many hearts from jamming attempts against it this round."
    JAM_GOOD = "??? / Badly startles all POKéMON that made good appeals."
    JAM_FRONT = "Attempts to jam the player who went first this round."
    JAM_ALL = "Attempts to jam all players who took turns before the user this round."
    ONE_SHIELD = "The user is protected from the first jamming attempt against it this round."
    ALL_SHIELD = "The user is protected from all jamming attempts against it this round."
    REPEATABLE = "This move can be used any number of times in a row without losing hearts for repeating the same move."
    JAM_SKIP = "Attempts to jam all players who took turns before the user this round and the user can't take their turn or be affected by enemy moves next round."
    DEAD = "The user can't take their turn or be affected by enemy moves for all remaining rounds."
    UNNERVE = "Attempts to make players who haven't taken their turn skip their turn."
    SCRAMBLE = "The turn order will be randomized next round."
    LOSE_ATTENTION = "If an enemy is using a move that is part of a combo, that combo won't give double hearts next round."
    JAM_SAME = "Attempts to jam all players who used a move of the same type as this move."
    JAM_STAR = "Attempts to jam a player that used a move that is part of a combo."
    PAUSE_APPLAUSE = "The applause level won't go up for the rest of this round."
    BETTER_APPLAUSE = "The move gains more hearts depending on the applause level."
    BETTER_LATE = "??? / The appeal works better the later it is performed."
    BETTER_FIRST = "??? / The appeal works great if performed first."
    BETTER_LAST = "??? / The appeal works great if performed last."
    RANDOM = "??? / The appeal's quality varies depending on its timing."
    GO_FIRST = "The user will go first next round."
    GO_LAST = "The user will go last next round."
    CONDITION = "The user increases their condition by 1 for the rest of the game. Future moves gain 1 appeal heart per condition. ??? / Helps prevent nervousness."
    COPY_HEARTS_PREVIOUS = "??? / Makes the appeal as good as the one before it."
    COPY_HEARTS_ALL = "??? / Makes the appeal as good as those before it."
    COPY_TYPE = "??? / Works well if it's the same type as the one before."
    LOWER_CONDITION = "Lowers the condition of all players who have taken their turn by 1 if its greater than 0. Future moves gain 1 appeal heart per condition."
    BETTER_CONDITION = "??? / Ups the user's condition. Helps prevent nervousness."
    
    

class Move():
    def __init__(self, id, type, name, appeal, jam, effect, combos=[]):
        self.id = id
        self.name = name
        self.type = type
        self.appeal = appeal
        self.jam = jam
        self.effect = effect
        self.combos = combos

def listMoves():


def findMove():
    return 0

def executeMove():
    return 0