import Menus
import combatMenuFunctions as combat
import classes
import sys
import random

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle

# Prints the input menu based on the user's choice
def print_Menu(menu):
    for x in range(len(menu)):
        print('{}) {}'.format(x + 1, menu[x]))
    option = int(input('Enter choice: '))
    return option    

def randomOrb(world):
    townList=[]
    for x in range(len(world.world_map)):
        for y in range(len(world.world_map)):
            if world.world_map[x][y]=="T":
                townList.append((x,y))
    townList.pop(0)
    orbPosition = random.choice(townList)
    world.world_map[orbPosition[0]][orbPosition[1]] ='T/O'
    return(world)

def print_Day():
    #Fetching and storing coordinates of hero
    pos_x = hero.positionX
    pos_y = hero.positionY
    location = world.world_map[pos_x][pos_y]
    
    description = ""
    if location == 'T':
        description = "You are in a town."
    if location == " ":
        description = "You are out in the open."
        
    print('Day {}: {}'.format(world.day, description))
    return location
def exitGame():
    sys.exit(0)

def print_Map():   
    #Iterating through world object's worldmap nested list
    for x in range(8):
        #Print a header for each nested list that exists
        print("+---+---+---+---+---+---+---+---+")
        for y in range(8):
            #Blank variable to store the Town, Orb or Hero letter icons
            icon= "   "
            #If statements to store the letter icons that is in the current world.worldmap nested list index
            if world.world_map[x][y] == 'T':
                icon = ' T '
                if x == hero.positionX and y == hero.positionY:
                    icon = 'H/T'
                    
            elif world.world_map[x][y] == 'K':
                icon = ' K '
                if x == hero.positionX and y == hero.positionY:
                    icon = 'H/K'

            elif world.world_map[x][y] == "T/O":
                icon = "T/O"

            elif x == hero.positionX and y == hero.positionY:
                icon= ' H '
            #By default python will end each print with a new line
            #end='' replaces the default parameter of '\n' so it does not end with a new line
            print("|{}".format(icon), end='')
        print("|")
    #Print a closing footer
    print("+---+---+---+---+---+---+---+---+")
    
def view_Character():
    #Printing hero stats
    print("Name : {}".format(hero.name))
    print("Damage : {}".format(hero.damage))
    print("Defence : {}".format(hero.defence))
    print("HP : {}".format(hero.hp))

def rest():
    world.day += 1
    hero.hp = 20
    print('You are fully healed.')
    
def new_Game():
    global world, hero, rat,ratKing
    world = randomOrb(classes.World())
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()
    
def save_Game():
    output = open('Save.txt','wb')
    pickle.dump(world, output, -1)
    pickle.dump(hero, output, -1)
    pickle.dump(rat, output, -1)
    output.close()
    print('Game saved.')
    
def resume_Game():
    input = open('Save.txt', 'rb')
    global world, hero, rat, ratKing
    world = pickle.load(input)
    hero = pickle.load(input)
    rat = pickle.load(input)
    ratKing = pickle.load(input)
    
def encounter_Rat():
    if rat.hp>0:
        print('Encounter! - {}'.format(rat.name))
        print('Damage: {},{}'.format(rat.damage_min, rat.damage_max))
        print('Defence: {}'.format(rat.defence))
        print("HP: {}".format(rat.hp))
        option = print_Menu(Menus.combat_Menu)
    
    if option == 1:
        combat.attack(rat, hero)
        
    elif option == 2:
        rat.hp = 8
        option = print_Menu(Menus.outdoor_Menu)
        if option == 3:
            print_Map()
            print('W = up; A = left; S = down; D = right')
            combat.UserMovementOption(hero, world)
        elif option == 4:
            exitGame()
        else:
            encounter_Rat()
            
def encounter_RatKing():
    if rat.hp>0:
        print('Encounter! - {}'.format(ratKing.name))
        print('Damage: {},{}'.format(ratKing.damage_min, ratKing.damage_max))
        print('Defence: {}'.format(ratKing.defence))
        print("HP: {}".format(ratKing.hp))
        option = print_Menu(Menus.combat_Menu)
    
    if option == 1:
        combat.attack(ratKing, hero)
        
    elif option == 2:
        option = print_Menu(Menus.outdoor_Menu)
        if option == 3:
            print_Map()
            print('W = up; A = left; S = down; D = right')
            combat.UserMovementOption(hero, world)
        else:
            encounter_RatKing()
def Main():
    print('Welcome to Ratventure!')
    print('----------------------')
    start_option = print_Menu(Menus.start_Menu)
    if start_option == 1:
        new_Game()
    elif start_option == 2:
        resume_Game()
    elif start_option == 3:
        exitGame()
        
    while True:
        location = print_Day()
        if location == "T":
            option = print_Menu(Menus.town_Menu)
            if option == 1:
                view_Character()
            elif option == 2:
                print_Map()
            elif option == 3:
                print_Map()
                print('W = up; A = left; S = down; D = right')
                combat.UserMovementOption(hero, world)
            elif option == 4:
                rest()
            elif option == 5:
                save_Game()
            elif option == 6:
                exitGame()
                
        elif location == ' ':
            if rat.hp <= 0:
                option = print_Menu(Menus.outdoor_Menu)
                if option == 1:
                    view_Character()
                elif option == 2:
                    print_Map()
                elif option == 3:
                    print_Map()
                    combat.UserMovementOption(hero, world)
                    rat.hp = 8
                elif option == 4:
                    exitGame()
            else:
                encounter_Rat()
        elif location == "K":
            if ratKing.hp <= 0:
                option = print_Menu(Menus.outdoor_Menu)
                if option == 1:
                    view_Character()
                elif option == 2:
                    print_Map()
                elif option == 3:
                    print_Map()
                    combat.UserMovementOption(hero, world)
                    rat.hp = 8
                elif option == 4:
                    exitGame()
            else:
                encounter_RatKing()
if __name__ == "__main__":
   Main()