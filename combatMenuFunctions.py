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
                
def attack(target, Player):
    playerDamage = random.randint(Player.minDamage,Player.maxDamage)
    targetDamage = random.randint(target.damage_min,target.damage_max)
    targetDefenceLeft = target.defence - playerDamage
    playerDefenceLeft = Player.defence - targetDamage
    
    if target.name == "Rat":

        if targetDefenceLeft > 0:  
            target.defence = targetDefenceLeft
            print("You deal {} damage to the rat".format(playerDamage))
            print("Ouch! The rat hit you for {} damage!".format(targetDamage))
            if playerDefenceLeft > 0:
                print("You have {}HP left.".format(Player.hp))
                print("Encounter! - {}".format(target.name))
                print("Damage: {}".format(target.damage))
                print("Defence: {}".format(target.defence))
                print("HP: {}".format(target.hp))
                print("")
            else:
                Player.hp = Player.hp - targetDamage
                print("You have {}HP left.".format(Player.hp))
                print("Encounter! - {}".format(rat.name))
                print("Damage: {}".format(target.damage))
                print("Defence: {}".format(target.defence))
                print("HP: {}".format(target.hp))
                print("")
                
        else:
            target.hp = target.hp - playerDamage
            if target.hp > 0:
                print("You deal {} damage to the rat".format(playerDamage))
                print("Ouch! The rat hit you for {} damage!".format(targetDamage))
                if playerDefenceLeft > 0:
                    print("You have {}HP left.".format(Player.hp))
                    print("Encounter! - {}".format(target.name))
                    print("Damage: {}".format(target.damage))
                    print("Defence: {}".format(target.defence))
                    print("HP: {}".format(target.hp))
                    print("")
                else:
                    Player.hp = Player.hp - targetDamage
                    print("You have {}HP left.".format(Player.hp))
                    print("Encounter! - {}".format(target.name))
                    print("Damage: {}".format(target.damage))
                    print("Defence: {}".format(target.defence))
                    print("HP: {}".format(target.hp))
                    print("")
                    if Player.hp <= 0:
                        print("You are dead. Game is over.")
            else:
                print("Yay you killed the {}!".format(target.name))
    else:
        if Player.hasOrb == False:
            
            print("Rat King is immune to attacks when you don't have the Orb!")
            print("Ouch! The rat hit you for {} damage!".format(targetDamage))



                


    


   
