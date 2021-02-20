class World:
    def __init__(self):
        self.name ="world"
        self.world_Map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
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
        self.damage = '2-4'
        self.minDamage = 2
        self.maxDamage = 4
        self.defence = 1
        self.hp = 20
        self.positionX = 0
        self.positionY = 0
        self.location = 'You are in a Town'
        self.hasOrb = False

class Rat(object): 
    def __init__(self):
        self.name = 'Rat'
        self.minDamage = 1 
        self.maxDamage = 3
        self.damage = str(self.minDamage)+'-'+str(self.maxDamage)
        self.defence = 1
        self.hp = 8 

class Rat_King(object): 
    def __init__(self):
        self.name = 'Rat King'
        self.minDamage = 8
        self.maxDamage = 12
        self.damage = str(self.minDamage)+'-'+str(self.maxDamage)
        self.defence = 5
        self.hp = 25 
    
