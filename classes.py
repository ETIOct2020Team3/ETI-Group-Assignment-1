class World:
    def __init__(self):
        self.world_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                     [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
                     [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
                     [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                     [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
        self.day = 1

class Player:  
    def __init__(self):   
        self.name = 'The Hero'
        self.minDamage = 2
        self.maxDamage = 4
        self.damage = str(self.minDamage)+'-'+str(self.maxDamage)
        self.defence = 1
        self.hp = 20
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.hasOrb = False

    def is_alive(self): 
        return self.hp > 0
    
    def minusOneDay(self):
        Player.day -= 1

class SavedPlayer: 
    def __init__(self):   
        self.name = 'SavedData' 
        self.damage = 'SavedData' 
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 'SavedData'
        self.hp = 'SavedData' 
        self.day = 'SavedData' 
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.hasOrb = 'SavedData'

    def is_alive(self): 
        return self.hp > 0

class Rat(object): 
    def __init__(self):
        self.name = 'Rat'
        self.damage_min = 1 
        self.damage_max = 3
        self.damage = str(self.damage_min)+'-'+str(self.damage_max)
        self.defence = 1
        self.hp = 8 
        self.location = 'a2'

class Rat_King(object): 
    def __init__(self):
        self.name = 'Rat King'
        self.damage_min = 8
        self.damage_max = 12
        self.damage = str(self.damage_min)+'-'+str(self.damage_max)
        self.defence = 5
        self.hp = 25 
        self.location = 'b4'
        self.isImmune = True
    
