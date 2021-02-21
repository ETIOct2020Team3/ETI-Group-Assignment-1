import pytest
from unittest import mock 
from unittest.mock import patch,call
import main
import menus
import combatFunctions as combat
import classes as classes
import os.path

###Did integration testing because test cases provided were wrong
#TC07
@patch ('builtins.print')
def test_viewCharacter_town_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    with patch('builtins.print') as mock_print:
        with patch('builtins.input', return_value='1') as mock_input:
            if world.world_Map[hero.positionX][hero.positionY] == 'T':
                choice = main.print_Menu(menus.town_Menu)
                   
    if choice == '1':
        main.view_Character(hero)
        assert mock_stdout.mock_calls == [call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]
        
#TC08
@patch ('builtins.print')
def test_viewCharacter_town_validation_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    with patch('builtins.print') as mock_print:
        with patch('builtins.input', return_value='7') as mock_input:
            if world.world_Map[hero.positionX][hero.positionY] == 'T':
                choice = main.print_Menu(menus.town_Menu)
                
    if choice == '7':
        print('Invalid option.\n')
    assert mock_stdout.mock_calls == [call('Invalid option.\n')]
        
#TC23
@patch('builtins.print')
def test_viewCharacter_outdoors_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    #Setting hero position to outdoors
    hero.positionX = 1
    
    with patch('builtins.print') as mock_print:
        with patch('builtins.input', return_value='1') as mock_input:
            if world.world_Map[hero.positionX][hero.positionY] == ' ':
                choice = main.print_Menu(menus.outdoor_Menu)
                
    if choice == '1':
        main.view_Character(hero)
        assert mock_stdout.mock_calls == [call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]
        

#TC24
@patch('builtins.print')
def test_view_Character_outdoors_validation_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    #Setting hero position to outdoors
    hero.positionX = 1
    with patch('builtins.print') as mock_print:
        with patch('builtins.input', return_value='7') as mock_input:
            if world.world_Map[hero.positionX][hero.positionY] == ' ':
                choice = main.print_Menu(menus.outdoor_Menu)

    if choice == '7':
        print('Invalid option.\n')
    assert mock_stdout.mock_calls == [call('Invalid option.\n')]



#TC07
test_viewCharacter_town_pass()
#TC08
test_viewCharacter_town_validation_pass()


#TC23
test_viewCharacter_outdoors_pass()
#TC24
test_view_Character_outdoors_validation_pass()



###Unit tests for attack rat king
def test_attackratKing_passing_pass():
    world = classes.World()
    hero = classes.Player()
    ratKing = classes.Rat_King()
    #Giving the hero the orb and attack boost
    hero.hasOrb = True
    hero.damage = '7-9'
    hero.minDamage = hero.minDamage + 5
    hero.maxDamage = hero.maxDamage + 5
    hero.defence = hero.defence + 5
    
    combat.attack(ratKing, hero)

    assert ratKing.hp < 25

def test_attackratKing_passing_fail():
    world = classes.World()
    hero = classes.Player()
    ratKing = classes.Rat_King()
    #Fails because setting the hasOrb property to true doesn't give the hero enough
    #attack points to bypass the rat king's defence
    #and assert is checking if ratking's hp drops
    hero.hasOrb = True
    
    combat.attack(ratKing, hero)

    assert ratKing.hp < 25

def test_attackratKing_failing_fail():
    world = classes.World()
    hero = classes.Player()
    ratKing = classes.Rat_King()

    #Fails because hero does not have the orb and has no stat boost
    combat.attack(ratKing, hero)

    assert ratKing.hp < 25

def test_attackratKing_failing_pass():
    world = classes.World()
    hero = classes.Player()
    ratKing = classes.Rat_King()

    combat.attack(ratKing, hero)

    assert ratKing.hp == 25
    
test_attackratKing_passing_pass()
test_attackratKing_passing_fail()
test_attackratKing_failing_fail()
test_attackratKing_failing_pass()

###Unit tests for encounter rat king
@patch ('builtins.print')
def test_view_Character_passing_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    main.view_Character(hero)
        
    assert mock_stdout.mock_calls == [call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

@patch ('builtins.print')
def test_view_Character_passing_fail(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    hero.hasOrb = True
    main.view_Character(hero)

    #Fails because its asserting that function will not print a statement
    #That the hero has the orb, while it does
    assert mock_stdout.mock_calls == [call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

  
@patch ('builtins.print')
def test_view_Character_failing_fail(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    hero.hasOrb = False
    main.view_Character(hero)

    #Fails because its asserting that function will print a statement
    #That the hero has the orb, while it doesnt
    assert mock_stdout.mock_calls == [call('\nYou hold the orb of power!'),call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

@patch ('builtins.print')
def test_view_Character_failing_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    hero.hasOrb = True
    main.view_Character(hero)
    assert mock_stdout.mock_calls == [call('\nYou hold the orb of power!'),call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

test_view_Character_passing_pass()
test_view_Character_passing_fail()
test_view_Character_failing_fail()
test_view_Character_failing_pass()
