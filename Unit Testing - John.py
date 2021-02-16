import pytest
from unittest import mock 
from unittest.mock import patch,call
import main
import menus
import combatFunctions as combat
import classes as classes
import os.path

#Passing
def test_random_orb_pass():
    world = classes.World()
    main.randomOrb(world)
    print('')
    print('Testing random orb generation')
    print(world.world_Map)
    output = ''
    
    if any('T/O' in icon for icon in world.world_Map):
        output = 'T/O generated'
    else:
        output = 'T/O not found'
        
    assert output =='T/O generated'


def test_new_game_pass():
    new_game_Objects = main.new_Game()
    print('')
    print('Testing new game')
    print(new_game_Objects)
    has_Null= True

    for object in new_game_Objects:
        if object != None:
            has_Null = False
        else:
            has_Null = True
            break
        
    assert has_Null == False

def test_save_game_pass():
    world = classes.World()
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()

    print('')
    print('Testing game save')
    main.save_Game(world, hero, rat, ratKing)

    is_Saved = False
    

    if os.path.isfile('Save.txt'):
        is_Saved = True

    assert is_Saved == True

def test_resume_game_pass():
    resume_game_Objects = main.new_Game()
    print('')
    print('Testing resume game')
    print(resume_game_Objects)
    has_Null= True

    for object in resume_game_Objects:
        if object != None:
            has_Null = False
            
        else:
            has_Null = True
            break
            
    assert has_Null == False

def test_rat_king_immunity_pass():
    print('')
    print ('Testing rat king immunity')
    world = classes.World()
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()

    hero.hasOrb = False

    combat.attack(ratKing, hero)

    print('Rat king hp: {}'.format(ratKing.hp))
    
    assert ratKing.hp == 25
    
    
def test_rat_king_broken_immunity_pass():
    print('')
    print ('Testing rat king broken immunity after player gets orb of power')
    world = classes.World()
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()

    main.getOrb(hero)
    
    combat.attack(ratKing, hero)

    print('Rat king hp: {}'.format(ratKing.hp))
    
    assert ratKing.hp < 25
    
test_random_orb_pass()
test_new_game_pass()
test_resume_game_pass()
test_save_game_pass()
test_rat_king_immunity_pass()
test_rat_king_broken_immunity_pass()


#Fails
def test_rat_king_immunity_fail():
    print('')
    print ('Failing test of rat king immunity')
    world = classes.World()
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()

    hero.hasOrb = False

    combat.attack(ratKing, hero)

    print('Rat king hp: {}'.format(ratKing.hp))
    
    assert ratKing.hp < 25
    
def test_rat_king_broken_immunity_fail():
    print('')
    print ('Failing test case to see if hero can damage rat king without orb')
    world = classes.World()
    hero = classes.Player()
    rat = classes.Rat()
    ratKing = classes.Rat_King()
    
    combat.attack(ratKing, hero)

    print('Rat king hp: {}'.format(ratKing.hp))
    
    assert ratKing.hp < 25

test_rat_king_immunity_fail()
test_rat_king_broken_immunity_fail()

