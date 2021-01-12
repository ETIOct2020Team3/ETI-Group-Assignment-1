import Menus
import combatMenuFunctions as combat
import classes

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
                    icon = 'K/T'

            elif x == hero.positionX and y == hero.positionY:
                icon= ' H '
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

def rest():
    world.day += 1
    hero.hp = 20
    print('You are fully healed.')
    
def new_Game():
    global world, hero
    world = classes.World()
    hero = classes.Player()
    
def save_Game():
    output = open('Save.txt','wb')
    pickle.dump(world, output, -1)
    pickle.dump(hero, output, -1)
    output.close()

def resume_Game():
    input = open('Save.txt', 'rb')
    global world, hero
    world = pickle.load(input)
    hero = pickle.load(input)
    
def Main():
    print('Welcome to Ratventure!')
    print('----------------------')
    start_option = print_Menu(Menus.start_Menu)
    if start_option == 1:
        new_Game()
    elif start_option == 2:
        resume_Game()
    elif start_option == 3:
        sys.exit()
        
    while True:
        location = print_Day()
        if location == "T":
            option = print_Menu(Menus.town_Menu)
            if option == 1:
                print_heroStats()
            elif option == 2:
                print_Map()
            elif option == 3:
                print_Map()
                print('W = up; A = left; S = down; D = right')
                combat.UserMovementOption(hero, world)
                print_Map()
            elif option == 4:
                rest()
            elif option == 5:
                save_Game()
            elif option == 6:
                outdoorMenu.exitGame()
            else:
                print("Other options are still under development. Please select option 2.")

        elif location == ' ':
            option = print_Menu(Menus.outdoor_Menu)
            if option == 1:
                view_Character()
            elif option == 2:
                print_Map()
            elif option == 3:
                print_Map()
                combat.UserMovementOption(hero, world)
                print_Map()
            elif option == 4:
                sys.exit()
        
Main()
