import pytest
from unittest import mock 
import main as main
import combatMenuFunctions as combat
import classes as classes

def test_exit_pass():
    passed = False
    try:
        main.exitGame()
    except SystemExit as e: 
        if e.code == 0:
            passed = True

    assert passed==False

def test_move_pass():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "D"
    hero = classes.Player()
    world = classes.World()
    combat.UserMovementOption(hero,world)
    assert world.world_map[hero.positionX][hero.positionY]==" " 
    mock.builtins.input = original_input


def test_attack_pass():
    rat= classes.Rat()
    hero=classes.Player()
    ratStartingHP = rat.hp
    combat.attack(rat,hero)
    assert ratStartingHP>rat.hp 

            
