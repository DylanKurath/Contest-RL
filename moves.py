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

moveObjects = []

moveData = [
    ["cool", 4, 0, Effect.NO_EFFECT, ["Drill Peck", "Horn Attack", "Mega Kick", "Metal Claw", "Peck", "SolarBeam", "Struggle", "Thunderbolt", "ThunderPunch", "ThunderShock", "Triple Kick", "Vine Whip", "Zap Cannon"]],
    ["cool", 3, 0, Effect.FRONT, ["Aeroblast", "Cross Chop", "Leaf Blade", "Razor Leaf", "Razor Wind", "Sky Attack", "Slash"]],
    ["cool", , , Effect., ["Hi Jump Kick", "Jump Kick", "Submission", "Volt Tackle"]],
    ["cool", , , Effect., ["Bullet Seed", "Cut", "Guillotine", "Horn Drill", "Thunder Wave"]],
    ["cool", , , Effect., ["Brick Break", "Crush Claw", "Dizzy Punch", "Extrasensory", "Hyper Fang", "Iron Tail", "Spark"]],
    ["cool", , , Effect., ["DragonBreath", "False Swipe", "Focus Energy", "Hyper Voice", "Rolling Kick"]],
    ["cool", , , Effect., ["Detect", "Double Team", "Rapid Spin"]],
    ["cool", , , Effect., ["Barrier", "Teleport"]],
    ["cool", , , Effect., ["Fury Cutter", "Rage"]],
    ["cool", , , Effect., ["Frenzy Plant", "Hyper Beam", "Outrage"]],
    ["cool", , , Effect., ["Roar", "Twister"]],
    ["cool", , , Effect., ["Thunder"]],
    ["cool", , , Effect., ["Air Cutter", "Dragon Claw", "Sky Uppercut"]],
    ["cool", , , Effect., ["Twineedle"]],
    ["cool", , , Effect., ["DynamicPunch", "Fury Attack", "Pin Missile", "Spike Cannon"]],
    ["cool", , , Effect., ["Doom Desire", "Leer"]],
    ["cool", , , Effect., ["Dragon Rage"]],
    ["cool", , , Effect., ["Aerial Ace", "Shock Wave", "Swift"]],
    ["cool", , , Effect., ["Reversal"]],
    ["cool", , , Effect., ["Agility", "ExtremeSpeed", "Mach Punch", "Quick Attack"]],
    ["cool", , , Effect., ["Vital Throw"]],
    ["cool", , , Effect., ["Cosmic Power", "Dragon Dance", "Howl"]],
    ["cool", , , Effect., ["Double Kick", "Megahorn", "Meteor Mash", "SonicBoom", "Steel Wing", "Wing Attack"]],
    ["beauty", , , Effect., ["Blaze Kick", "Blizzard", "Ember", "Fire Blast", "Fire Punch", "Flame Wheel", "Flamethrower", "Heat Wave", "Hydro Pump", "Ice Punch", "Powder Snow", "Sacred Fire", "Softboiled"]],
    ["beauty", , , Effect., ["Surf"]],
    ["beauty", , , Effect., ["Overheat"]],
    ["beauty", , , Effect., ["Perish Song", "Sheer Cold"]],
    ["beauty", , , Effect., ["Will-O-Wisp"]],
    ["beauty", , , Effect., ["Hail", "Icy Wind", "Lovely Kiss", "Spore", "BubbleBeam"]],
    ["beauty", , , Effect., ["Dive", "Mirror Coat"]],
    ["beauty", , , Effect., ["Light Screen", "Magic Coat", "Mist", "Safeguard"]],
    ["beauty", , , Effect., ["Blast Burn", "Hydro Cannon", "Petal Dance"]],
    ["beauty", , , Effect., ["Explosion", "Selfdestruct"]],
    ["beauty", , , Effect., ["Mean Look"]],
    ["beauty", , , Effect., ["Psybeam", "Signal Beam", "Water Pulse"]],
    ["beauty", , , Effect., ["Flash"]],
    ["beauty", , , Effect., ["Tri Attack"]],
    ["beauty", , , Effect., ["Aurora Beam", "Ice Beam", "Icicle Spear"]],
    ["beauty", , , Effect., ["Cotton Spore"]],
    ["beauty", , , Effect., ["Fire Spin", "Ice Ball", "Whirlpool"]],
    ["beauty", , , Effect., ["Nature Power"]],
    ["beauty", , , Effect., ["Eruption", "Water Spout"]],
    ["beauty", , , Effect., ["Magical Leaf"]],
    ["beauty", , , Effect., ["FeatherDance", "Heal Bell"]],
    ["beauty", , , Effect., ["Sunny Day"]],
    ["beauty", , , Effect., ["Moonlight", "Morning Sun"]],
    ["beauty", , , Effect., ["Bulk Up", "Growth", "Meditate", "Silver Wind", "Swords Dance", "Tail Glow"]],
    ["beauty", , , Effect., ["Conversion", "Conversion 2"]],
    ["beauty", , , Effect., ["Haze"]],
    ["cute", , , Effect., ["Mud Sport", "Snore", "Water Gun", "Water Sport"]],
    ["cute", , , Effect., ["Frustration", "Return"]],
    ["cute", , , Effect., ["Sweet Scent"]],
    ["cute", , , Effect., ["Defense Curl", "Minimize", "Rest"]],
    ["cute", , , Effect., ["Bounce", "Protect", "Withdraw"]],
    ["cute", , , Effect., ["Metronome", "Present", "Sleep Talk"]],
    ["cute", , , Effect., ["Teeter Dance"]],
    ["cute", , , Effect., ["Attract", "Baton Pass", "Block", "Encore", "Sing", "Sweet Kiss", "Yawn"]],
    ["cute", , , Effect., ["Mimic"]],
    ["cute", , , Effect., ["Covet", "Role Play"]],
    ["cute", , , Effect., ["Uproar"]],
    ["cute", , , Effect., ["Bubble"]],
    ["cute", , , Effect., ["Charm", "Fake Out"]],
    ["cute", , , Effect., ["Mud-Slap", "Sand-Attack"]],
    ["cute", , , Effect., ["Follow Me", "Wish"]],
    ["cute", , , Effect., ["Flail", "Slack Off"]],
    ["cute", , , Effect., ["Swagger"]],
    ["cute", , , Effect., ["Facade", "Growl", "Splash", "Tail Whip"]],
    ["cute", , , Effect., ["Assist"]],
    ["cute", , , Effect., ["Amnesia", "Belly Drum", "Refresh", "Sharpen"]],
    ["cute", , , Effect., ["Milk Drink"]],
    ["cute", , , Effect., ["Tickle"]],
    ["smart", , , Effect., ["Weather Ball"]],
    ["smart", , , Effect., ["Camouflage"]],
    ["smart", , , Effect., ["Psycho Boost"]],
    ["smart", , , Effect., ["Beat Up", "Psywave", "Pursuit", "Snatch", "Stun Spore"]],
    ["smart", , , Effect., ["Acid", "Knock Off", "Mega Drain", "Mist Ball", "Needle Arm", "Pain Split"]],
    ["smart", , , Effect., ["GrassWhistle", "Hypnosis", "Metal Sound", "Nightmare", "Psychic", "Screech", "Sleep Powder"]],
    ["smart", , , Effect., ["Calm Mind", "Substitute"]],
    ["smart", , , Effect., ["Dig", "Fly", "Ingrain", "Reflect"]],
    ["smart", , , Effect., ["Hidden Power", "Recycle", "Transform"]],
    ["smart", , , Effect., ["Destiny Bond"]],
    ["smart", , , Effect., ["Disable", "Flatter", "Helping Hand", "Spider Web", "Spikes", "Taunt"]],
    ["smart", , , Effect., ["Mirror Move", "Sketch"]],
    ["smart", , , Effect., ["Skill Swap"]],
    ["smart", , , Effect., ["Confuse Ray", "Gust", "Supersonic", "Whirlwind"]],
    ["smart", , , Effect., ["Shadow Ball", "SmokeScreen"]],
    ["smart", , , Effect., ["Dream Eater", "Leech Seed"]],
    ["smart", , , Effect., ["Night Shade", "Recover"]],
    ["smart", , , Effect., ["Absorb", "Astonish", "Confusion", "Leech Life", "Luster Purge", "Poison Sting", "SmellingSalt", "String Shot"]],
    ["smart", , , Effect., ["Giga Drain"]],
    ["smart", , , Effect., ["Future Sight", "Kinesis", "Lock-On", "Mind Reader", "Rock Tomb", "Sand Tomb"]],
    ["smart", , , Effect., ["Pay Day"]],
    ["smart", , , Effect., ["Faint Attack", "Shadow Punch"]],
    ["smart", , , Effect., ["Aromatherapy", "Fake Tears"]],
    ["smart", , , Effect., ["Secret Power"]],
    ["smart", , , Effect., ["Synthesis"]],
    ["smart", , , Effect., ["Charge", "Psych Up", "Trick"]],
    ["smart", , , Effect., ["Foresight", "Imprison", "Odor Sleuth", "Poison Fang", "Poison Gas", "PoisonPowder", "Poison Tail", "Toxic"]],
    ["tough", , , Effect., ["Bone Rush", "Bonemerang", "Egg Bomb", "Mega Punch", "Pound", "Scratch", "Spit Up", "Tackle", "ViceGrip"]],
    ["tough", , , Effect., ["Crabhammer", "Karate Chop"]],
    ["tough", , , Effect., ["Double-Edge", "Superpower", "Take Down"]],
    ["tough", , , Effect., ["Fissure", "Super Fang"]],
    ["tough", , , Effect., ["Body Slam", "Crunch", "Lick", "Low Kick", "Skull Bash", "Sludge", "Stomp"]],
    ["tough", , , Effect., ["Bite", "Earthquake", "Glare", "Mud Shot", "Rock Slide", "Smog"]],
    ["tough", , , Effect., ["Counter", "Endure", "Harden", "Stockpile"]],
    ["tough", , , Effect., ["Bide", "Iron Defense"]],
    ["tough", , , Effect., ["Thrash"]],
    ["tough", , , Effect., ["Memento"]],
    ["tough", , , Effect., ["Torment"]],
    ["tough", , , Effect., ["Thief"]],
    ["tough", , , Effect., ["Sandstorm"]],
    ["tough", , , Effect., ["Seismic Toss", "Slam", "Strength"]],
    ["tough", , , Effect., ["Constrict", "Headbutt"]],
    ["tough", , , Effect., ["Arm Thrust", "Bone Club", "DoubleSlap", "Fury Swipes", "Muddy Water", "Octazooka", "Scary Face", "Sludge Bomb"]],
    ["tough", , , Effect., ["Bind", "Clamp", "Rollout", "Wrap"]],
    ["tough", , , Effect., ["Magnitude", "Rain Dance"]],
    ["tough", , , Effect., ["Grudge", "Spite"]],
    ["tough", , , Effect., ["Endeavor", "Waterfall"]],
    ["tough", , , Effect., ["Rock Smash"]],
    ["tough", , , Effect., ["Curse", "Focus Punch", "Revenge"]],
    ["tough", , , Effect., ["Acid Armor", "AncientPower", "Swallow"]],
    ["tough", , , Effect., ["Barrage", "Comet Punch", "Rock Blast", "Rock Throw"]]
]

def listMoves():


def findMove():
    return 0

def executeMove():
    return 0