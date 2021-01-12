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
            else:
                world.day += 1
                
        elif inputOption == 'A':
            hero.positionY -= 1
            if hero.positionY < 0:
                hero.positionY += 1
                errorMessages.exitGridError()
            else:
                world.day += 1                
            
        elif inputOption == 'S':
            hero.positionX += 1
            if hero.positionX > 7: 
                hero.positionX -= 1
            else:
                world.day += 1
            
        elif inputOption == 'D':
            hero.positionY += 1
            if hero.positionY > 7:
                hero.positionY -= 1
            else:
                world.day += 1
                
def attack():
    Rat = classes.Rat()
    Player = classes.Player()
    ratDamage = random.randint(Player.minDamage,Player.maxDamage)
    playerDamage = random.randint(Rat.damage_min,Rat.damage_max)
    ratDefenceLeft = Rat.defence - playerDamage
    playerDefenceLeft = Player.defence - ratDamage
    if ratDefenceLeft > 0:  
        Rat.defence = ratDefenceLeft
        print("You deal {} damage to the Rat".format(playerDamage))
        print("Ouch! The Rat hit you for {} damage!".format(ratDamage))
        if playerDefenceLeft > 0:
            print("You have {}HP left.".format(Player.hp))
            print("Encounter! - {}".format(Rat.name))
            print("Damage: {}".format(Rat.damage))
            print("Defence: {}".format(Rat.defence))
            print("HP: {}".format(Rat.hp))
        else:
            Player.hp = Player.hp - ratDamage
            print("You have {}HP left.".format(Player.hp))
            print("Encounter! - {}".format(Rat.name))
            print("Damage: {}".format(Rat.damage))
            print("Defence: {}".format(Rat.defence))
            print("HP: {}".format(Rat.hp))
    else:
        Rat.hp = Rat.hp - playerDamage
        if Rat.hp > 0:
            print("You deal {} damage to the Rat".format(playerDamage))
            print("Ouch! The Rat hit you for {} damage!".format(ratDamage))
            if playerDefenceLeft > 0:
                print("You have {}HP left.".format(Player.hp))
                print("Encounter! - {}".format(Rat.name))
                print("Damage: {}".format(Rat.damage))
                print("Defence: {}".format(Rat.defence))
                print("HP: {}".format(Rat.hp))
            else:
                Player.hp = Player.hp - ratDamage
                print("You have {}HP left.".format(Player.hp))
                print("Encounter! - {}".format(Rat.name))
                print("Damage: {}".format(Rat.damage))
                print("Defence: {}".format(Rat.defence))
                print("HP: {}".format(Rat.hp))
                if Player.hp <= 0:
                    print("You are dead. Game is over.")
        else:
            print("Yay you killed the {}!".format(Rat.name))


    


   
