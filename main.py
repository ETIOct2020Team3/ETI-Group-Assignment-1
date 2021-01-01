import Menus
from classes import *


# Prints the input menu based on the user's choice

def print_Menu(menu):
    for x in range(len(menu)):
        print('{}) {}'.format(x + 1, menu[x]))
    option = int(input('Enter choice: '))
    return option    
    
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
        
    print('Day {}: {}'.format(day, description))
    return location
    
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
                if x == hero.positionX & y == hero.positionY:
                    icon = 'H/T'
            if world.world_map[x][y] == 'K':
                icon = ' K '
            if world.world_map[x][y] == 'H':
                icon = ' H'
            #By default python will end each print with a new line
            #end='' replaces the default parameter of '\n' so it does not end with a new line
            print("|{}".format(icon), end='')
        print("|")
    #Print a closing footer
    print("+---+---+---+---+---+---+---+---+")
    
def print_heroStats():
    #Printing hero stats
    print("Name : {}".format(hero.name))
    print("Damage : {}".format(hero.damage))
    print("Defence : {}".format(hero.defence))
    print("HP : {}".format(hero.hp))

def new_Game():
    global world, hero, day
    day = 1
    world = World()
    hero = Player()

def Main():
    print('Welcome to Ratventure!')
    print('----------------------')
    start_option = print_Menu(Menus.start_Menu)
    if start_option == 1:
        new_Game()
    else:
        print("Other options are still under development. Option 1 will be selected automatically.")
        new_Game()
    while True:
        location = print_Day()
        if location == "T":
            option = print_Menu(Menus.town_Menu)
            if option == 1:
                print_heroStats()
            if option == 2:
                print_Map()
            else:
                print("Other options are still under development. Please select option 2.")
        
Main()
