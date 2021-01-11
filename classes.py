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

class Player:  
    def __init__(self):   
        self.name = 'The Hero'
        self.damage = '2-4'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 1
        self.hp = 20
        self.day = 1
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.locationTag = 'H'

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
        self.locationTag = 'H'

    def is_alive(self): 
        return self.hp > 0

class Rat(object): 
    def __init__(self):
        self.name = 'Rat'
        self.damage = '1-3'
        self.damage_min = 1 
        self.damage_max = 3
        self.defence = 1
        self.hp = 8 
        self.location = 'a2'
    
