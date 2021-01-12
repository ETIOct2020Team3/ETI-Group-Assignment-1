import classes
import errorMessages
import random
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
                
def attack(rat, Player):
    ratDamage = random.randint(Player.minDamage,Player.maxDamage)
    playerDamage = random.randint(rat.damage_min,rat.damage_max)
    ratDefenceLeft = rat.defence - playerDamage
    playerDefenceLeft = Player.defence - ratDamage
    
    if ratDefenceLeft > 0:  
        rat.defence = ratDefenceLeft
        print("You deal {} damage to the rat".format(playerDamage))
        print("Ouch! The rat hit you for {} damage!".format(ratDamage))
        if playerDefenceLeft > 0:
            print("You have {}HP left.".format(Player.hp))
            print("Encounter! - {}".format(rat.name))
            print("Damage: {}".format(rat.damage))
            print("Defence: {}".format(rat.defence))
            print("HP: {}".format(rat.hp))
        else:
            Player.hp = Player.hp - ratDamage
            print("You have {}HP left.".format(Player.hp))
            print("Encounter! - {}".format(rat.name))
            print("Damage: {}".format(rat.damage))
            print("Defence: {}".format(rat.defence))
            print("HP: {}".format(rat.hp))
            
    else:
        rat.hp = rat.hp - playerDamage
        if rat.hp > 0:
            print("You deal {} damage to the rat".format(playerDamage))
            print("Ouch! The rat hit you for {} damage!".format(ratDamage))
            if playerDefenceLeft > 0:
                print("You have {}HP left.".format(Player.hp))
                print("Encounter! - {}".format(rat.name))
                print("Damage: {}".format(rat.damage))
                print("Defence: {}".format(rat.defence))
                print("HP: {}".format(rat.hp))
            else:
                Player.hp = Player.hp - ratDamage
                print("You have {}HP left.".format(Player.hp))
                print("Encounter! - {}".format(rat.name))
                print("Damage: {}".format(rat.damage))
                print("Defence: {}".format(rat.defence))
                print("HP: {}".format(rat.hp))
                if Player.hp <= 0:
                    print("You are dead. Game is over.")
        else:
            print("Yay you killed the {}!".format(rat.name))


    


   
