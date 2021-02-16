import menus
import combatFunctions as combat
import classes
import sys
import random

try:
    import cPickle as pickle
except ModuleNotFoundError:
    import pickle
    
###################################################################
#General Functions
###################################################################    
def print_Menu(menu):
    for x in range(len(menu)):
        print('{}) {}'.format(x + 1, menu[x]))
    print('')
    option = input('Enter choice:\n')
    return option

def print_Day():
    #Fetching and storing coordinates of hero
    pos_x = hero.positionX
    pos_y = hero.positionY
    location = world.world_Map[pos_x][pos_y]

    description = ""
    
    if location == 'T' or location == 'T/O':
        description = "You are in a town."
        
    elif location == " ":
        description = "You are out in the open."

    elif location == "K":
        description = "You see the Rat King!"

    print('\nDay {}: {}'.format(world.day, description))
    return location

def randomOrb(world):
    townList=[]
    for x in range(len(world.world_Map)):
        for y in range(len(world.world_Map)):
            if world.world_Map[x][y]=="T":
                townList.append((x,y))
    townList.pop(0)
    orbPosition = random.choice(townList)
    world.world_Map[orbPosition[0]][orbPosition[1]] ='T/O'
    return(world)
###################################################################
#Start Menu Functions
###################################################################
def new_Game():
    global world, hero, rat, ratKing
    world = randomOrb(classes.World())
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()

def resume_Game():
    input = open('Save.txt', 'rb')
    global world, hero, rat, ratKing
    world = pickle.load(input)
    hero = pickle.load(input)
    rat = pickle.load(input)
    ratKing = pickle.load(input)
###################################################################
#Main Menu Functions
###################################################################
def view_Character(hero):
    #Printing hero stats
    if hero.hasOrb == True:
        print("\nYou hold the orb of power!")
    print("\nName : {}".format(hero.name))
    print("Damage : {}".format(hero.damage))
    print("Defence : {}".format(hero.defence))
    print("HP : {}".format(hero.hp))
    
def exitGame():
    sys.exit(0)


def print_Map(hero,world):
    #Iterating through world object's worldmap nested list
    print('')
    for x in range(8):
        #Print a header for each nested list that exists
        print("+---+---+---+---+---+---+---+---+")
        for y in range(8):
            #Blank variable to store the Town, Orb or Hero letter icons
            icon= "   "
            #If statements to store the letter icons that is in the current world.worldmap nested list index
            if world.world_Map[x][y] == 'T':
                icon = ' T '
                if x == hero.positionX and y == hero.positionY:
                    icon = 'H/T'

            elif world.world_Map[x][y] == 'K':
                icon = ' K '
                if x == hero.positionX and y == hero.positionY:
                    icon = 'H/K'

            elif world.world_Map[x][y] == "T/O":
                icon = "T/O"

            elif x == hero.positionX and y == hero.positionY:
                icon= ' H '
            #By default python will end each print with a new line
            #end='' replaces the default parameter of '\n' so it does not end with a new line
            print("|{}".format(icon), end='')
        print("|")
    #Print a closing footer
    print("+---+---+---+---+---+---+---+---+")

def rest(hero,world):
    world.day += 1
    hero.hp = 20
    print('\nYou are fully healed.')

def save_Game():
    output = open('Save.txt','wb')
    pickle.dump(world, output, -1)
    pickle.dump(hero, output, -1)
    pickle.dump(rat, output, -1)
    pickle.dump(ratKing, output, -1)
    output.close()
    print('\nGame saved.')
###################################################################
#Combat Functions
###################################################################
def encounter_Rat(hero,rat):
    if rat.hp>0:
        print('\nEncounter! - {}'.format(rat.name))
        print('Damage: {},{}'.format(rat.minDamage, rat.maxDamage))
        print('Defence: {}'.format(rat.defence))
        print("HP: {}".format(rat.hp))
        option = print_Menu(menus.combat_Menu)
    #If player attacks
    if option == '1':
        combat.attack(rat, hero)
    #If player runs
    elif option == '2':
        #Reset enemy hp
        rat.hp = 8
        option = print_Menu(menus.outdoor_Menu)
        if option == '3':
            print_Map(hero,world)
            print('W = up; A = left; S = down; D = right')
            combat.UserMovementOption(hero, world)
        elif option == '4':
            sys.exit(0)
        #If any other action than exiting game or moving
        else:
            encounter_Rat(hero,rat)
    else:
        print('Invalid option.\n')
        
def encounter_ratKing(hero,ratKing):
    if ratKing.hp>0:
        print('Encounter! - {}'.format(ratKing.name))
        print('Damage: {},{}'.format(ratKing.minDamage, ratKing.maxDamage))
        print('Defence: {}'.format(ratKing.defence))
        print("HP: {}".format(ratKing.hp))
        option = print_Menu(menus.combat_Menu)
    #If player attacks
    if option == '1':
        combat.attack(ratKing, hero)
    #If player runs       
    elif option == '2':
        #Reset enemy hp
        ratKing.hp = 25
        option = print_Menu(menus.outdoor_Menu)
        if option == '3':
            print_Map(hero,world)
            print('W = up; A = left; S = down; D = right')
            combat.UserMovementOption(hero, world)
        elif option == '4':
            sys.exit(0)
        #If any other action than exiting game or moving
        else:
            encounter_ratKing(hero,ratKing)        
###################################################################
#Main Function
###################################################################
def main():
    print('Welcome to Ratventure!')
    print('----------------------')
    
    start_option = print_Menu(menus.start_Menu)
    
    if start_option == '1':
        new_Game()
    elif start_option == '2':
        resume_Game()
    elif start_option == '3':
        exitGame()
    else:
        print('Invalid option.\n')
        main()

    condition = True

    while condition:
        location = print_Day()
        #Available options when the player is in a town
        if location == "T":
            option = print_Menu(menus.town_Menu)
            if option == '1':
                view_Character(hero)
            elif option == '2':
                print_Map(hero,world)
            elif option == '3':
                print_Map(hero,world)
                print('W = up; A = left; S = down; D = right')
                combat.UserMovementOption(hero, world)
            elif option == '4':
                rest(hero,world)
            elif option == '5':
                save_Game()
            elif option == '6':
                condition = False
                exitGame()
            else:
                print('Invalid option.\n')

        #Available options when the player is in the open
        elif location == ' ':
            if rat.hp <= 0:
                option = print_Menu(menus.outdoor_Menu)
                if option == '1':
                    view_Character(hero)
                elif option == '2':
                    print_Map(hero,world)
                elif option == '3':
                    print_Map(hero,world)
                    combat.UserMovementOption(hero, world)
                    rat.hp = 8
                elif option == '4':
                    sys.exit(0)
            else:
                encounter_Rat(hero,rat)
                
        #Available options when the player finds the town with the orb
        elif location == "T/O":
            #Player discovering the orb of power
            print("You found the Orb of Power!")
            print("Your attack increases by 5!")
            print("Your defence increases by 5!")
            #Player getting the boosted stats
            hero.damage = '7-9'
            hero.minDamage = hero.minDamage + 5
            hero.maxDamage = hero.maxDamage + 5
            hero.defence = hero.defence + 5
            
            #Setting the town back to location tag 'T'
            world.world_Map[hero.positionX][hero.positionY] = 'T'
            #Setting hasOrb attribute to true to denote that the hero has the orb
            hero.hasOrb = True
            
            option = print_Menu(menus.town_Menu)
            if option == '1':
                view_Character(hero)
            elif option == '2':
                print_Map(hero,world)
            elif option == '3':
                print_Map(hero,world)
                print('W = up; A = left; S = down; D = right')
                combat.UserMovementOption(hero, world)
            elif option == '4':
                rest(hero,world)
            elif option == '5':
                save_Game()
            elif option == '6':
                condition = False
                sys.exit(0)
            else:
                print('Invalid option.\n')

        #Available options when the player encounters the rat king
        elif location == "K":
            if ratKing.hp <= 0:
                print("You have already slain the Rat King!")
                option = print_Menu(menus.outdoor_Menu)
                if option == '1':
                    view_Character(hero)
                elif option == '2':
                    print_Map(hero,world)
                elif option == '3':
                    print_Map(hero,world)
                    combat.UserMovementOption(hero, world)
                    rat.hp = 8
                elif option == '4':
                    sys.exit(0)
            else:
                encounter_ratKing(hero,ratKing)
        else:
            print("\n Error. This you have somehow moved to an invalid location.")
            sys.exit(0)
        
if __name__ == "__main__":
   main()
