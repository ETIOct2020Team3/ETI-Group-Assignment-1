import classes
import errorMessages
import random
import sys
gridList = [1,2,3,4,5,6,7]

def UserMovementOption(hero, world):
    inputOption = input("Your Move:")
    if inputOption.isalpha:
        inputOption = inputOption.upper()
        
        if inputOption == 'W':
            hero.positionX -= 1
            if hero.positionX < 0:
                hero.positionX += 1                
                errorMessages.exitGridError()
                UserMovementOption(hero, world)
            else:
                world.day += 1
                
        elif inputOption == 'A':
            hero.positionY -= 1
            if hero.positionY < 0:
                hero.positionY += 1
                errorMessages.exitGridError()
                UserMovementOption(hero, world)
            else:
                world.day += 1                
            
        elif inputOption == 'S':
            hero.positionX += 1
            if hero.positionX > 7: 
                hero.positionX -= 1
                errorMessages.exitGridError()
                UserMovementOption(hero, world)
            else:
                world.day += 1
            
        elif inputOption == 'D':
            hero.positionY += 1
            if hero.positionY > 7:
                hero.positionY -= 1
                errorMessages.exitGridError()
                UserMovementOption(hero, world)
            else:
                world.day += 1
        else:
            print('\nInvalid input.')
                
def attack(enemy, player):
    #Random damage enemy will do based on a random int from their min to max damage, mitigated by player's defence
    enemyDamage = (random.randint(enemy.minDamage,enemy.maxDamage)) - player.defence
    #If negative, set it to 0 to prevent bugs. EG: -1 damage might heal instead
    if enemyDamage <= 0:
        enemyDamage = 0
                   
    #Random damage player will do based on a random int from their min to max damage, mitigated by enemy's defence    
    playerDamage = (random.randint(player.minDamage, player.maxDamage)) - enemy.defence
    #If negative, set it to 0 to prevent bugs. EG: -1 damage might heal instead
    if playerDamage <= 0:
        playerDamage = 0

    #If enemy is rat king and player has no orb, change damage to 0
    if enemy.name == 'Rat King' and player.hasOrb == False:
        print('You do not have the orb of power! The Rat King is immune to your attacks.')
        playerDamage = 0

    enemy.hp = enemy.hp - playerDamage
    print("\nYou deal {} damage to the {}".format(playerDamage, enemy.name))
    
    if enemy.hp > 0: 
        print("Ouch! The {} hit you for {} damage!".format(enemy.name, enemyDamage))
        if player.hp > 0:
            player.hp = player.hp - enemyDamage
            print("You have {}HP left.".format(player.hp))
                
    if player.hp <= 0:
            print("\nOh dear, you are dead!")
            print("Game over.")
            sys.exit(0)
            
    if enemy.hp <=0:
        print("\nYay you killed the {}!".format(enemy.name))




   
