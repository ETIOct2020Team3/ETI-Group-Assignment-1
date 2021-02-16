import pytest
from unittest import mock 
from unittest.mock import patch,call
import main 
import combatFunctions as combat
import classes as classes




def test_exit_pass():
    passed = False
    try:
        main.exitGame()
    except SystemExit as e: 
        if e.code == 0:
            passed = True
    assert passed==True

def test_exit_fail():
    passed = 1
    try:
        main.exitGame()
    except SystemExit as e: 
        if e.code == 0:
            passed = e.code
    assert passed != 0

def test_move_right_pass():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "D"
    hero = classes.Player()
    world = classes.World()
    world.world_Map[0][1]="right"
    combat.UserMovementOption(hero,world)
    assert world.world_Map[hero.positionX][hero.positionY]=="right" 
    mock.builtins.input = original_input

def test_move_right_fail():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "D"
    hero = classes.Player()
    world = classes.World()
    world.world_Map[0][1]="right"
    world.world_Map[1][0]="down"
    combat.UserMovementOption(hero,world)
    assert world.world_Map[hero.positionX][hero.positionY]=="down" 
    mock.builtins.input = original_input

def test_move_down_pass():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "S"
    hero = classes.Player()
    world = classes.World()
    world.world_Map[0][1]="right"
    world.world_Map[1][0]="down"    
    combat.UserMovementOption(hero,world)
    assert world.world_Map[hero.positionX][hero.positionY]=="down" 
    mock.builtins.input = original_input

def test_move_down_fail():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "S"
    hero = classes.Player()
    world = classes.World()
    world.world_Map[1][0]="down"
    combat.UserMovementOption(hero,world)
    assert world.world_Map[hero.positionX][hero.positionY]=="right" 
    mock.builtins.input = original_input



def test_attack_pass():
    rat= classes.Rat()
    hero=classes.Player()
    ratStartingHP = rat.hp
    combat.attack(rat,hero)
    assert ratStartingHP>rat.hp 

def test_attack_fail():
    rat= classes.Rat()
    hero=classes.Player()
    ratStartingHP = rat.hp
    combat.attack(rat,hero)
    assert ratStartingHP==rat.hp 

@patch('builtins.print')
def test_view_char_with_orb_pass(mock_stdout):
    hero = classes.Player()
    hero.hasOrb = True
    main.view_Character(hero)
    assert mock_stdout.mock_calls == [call('\nYou hold the orb of power!'), call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

@patch('builtins.print')
def test_view_char_with_orb_fail(mock_stdout):
    hero = classes.Player()
    hero.hasOrb = False
    main.view_Character(hero)
    assert mock_stdout.mock_calls == [call('\nYou hold the orb of power!'), call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

@patch('builtins.print')
def test_view_char_without_orb_pass(mock_stdout):
    hero = classes.Player()
    hero.hasOrb = False
    main.view_Character(hero)
    assert mock_stdout.mock_calls == [call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

@patch('builtins.print')
def test_view_char_without_orb_fail(mock_stdout):
    hero = classes.Player()
    hero.hasOrb = True
    main.view_Character(hero)
    assert mock_stdout.mock_calls == [call('\nName : {}'.format(hero.name)),call("Damage : {}".format(hero.damage)),call("Defence : {}".format(hero.defence)),call("HP : {}".format(hero.hp))]

@patch('builtins.print')
def test_print_map_town_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    main.print_Map(hero,world)
    assert mock_stdout.mock_calls ==[
            call(''),call('+---+---+---+---+---+---+---+---+'),
            call('|H/T', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('| T ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('| T ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('| T ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('| T ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''), call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('| K ', end=''), 
            call('|'), call('+---+---+---+---+---+---+---+---+')]

@patch('builtins.print')
def test_print_map_town_fail(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    main.print_Map(hero,world)
    assert mock_stdout.mock_calls !=[
            call(''),call('+---+---+---+---+---+---+---+---+'),
            call('|H/T', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('| T ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('| T ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('| T ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('| T ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('|   ', end=''),
            call('|'),
            call('+---+---+---+---+---+---+---+---+'),
            call('|   ', end=''),call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''), call('|   ', end=''),call('|   ', end=''),
            call('|   ', end=''),call('| K ', end=''), 
            call('|'), call('+---+---+---+---+---+---+---+---+')]

@patch('builtins.print')
def test_rest_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    newWorldDay = world.day
    newWorldDay+=1
    main.rest(hero,world)
    assert hero.hp == 20    
    assert world.day == newWorldDay
    assert mock_stdout.mock_calls == [call("\nYou are fully healed.")]

@patch('builtins.print')
def test_rest_fail(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    newWorldDay = world.day
    newWorldDay+=1
    main.rest(hero,world)
    assert hero.hp != 20    
    assert world.day != newWorldDay
    assert mock_stdout.mock_calls != [call("\nYou are fully healed.")]

@patch('builtins.print')
def test_encounter_rat_pass(mock_stdout):
    rat = classes.Rat()
    hero = classes.Player()
    ratOriginalHP = rat.hp
    heroOriginalHP = hero.hp
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    main.encounter_Rat(hero,rat)
    assert rat.hp<=ratOriginalHP
    assert hero.hp<=heroOriginalHP

@patch('builtins.print')
def test_encounter_rat_fail(mock_stdout):
    rat = classes.Rat()
    hero = classes.Player()
    ratOriginalHP = rat.hp
    heroOriginalHP = hero.hp
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    main.encounter_Rat(hero,rat)
    assert rat.hp>=ratOriginalHP
    assert hero.hp>=heroOriginalHP


@patch('builtins.print')
def test_encounter_ratKing_without_orb_pass(mock_stdout):
    ratKing = classes.Rat_King()
    hero = classes.Player()
    ratKingOriginalHP = ratKing.hp
    heroOriginalHP = hero.hp
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    main.encounter_ratKing(hero,ratKing)
    assert ratKing.hp==ratKingOriginalHP
    assert hero.hp<heroOriginalHP

@patch('builtins.print')
def test_encounter_ratKing_without_orb_fail(mock_stdout):
    ratKing = classes.Rat_King()
    hero = classes.Player()
    ratKingOriginalHP = ratKing.hp
    heroOriginalHP = hero.hp
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "1"
    main.encounter_ratKing(hero,ratKing)
    assert ratKing.hp!=ratKingOriginalHP
    assert hero.hp==heroOriginalHP



