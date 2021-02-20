import pytest
from unittest import mock 
from unittest.mock import patch,call
import main 
import combatFunctions as combat
import classes as classes

#passing test case pass
@patch('builtins.print')
def test_rest_passing_pass(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    tempWorldDay = world
    hero.hp -= 10
    temphero = hero
    main.rest(temphero,tempWorldDay)
    assert hero.hp == temphero.hp    
    assert tempWorldDay.day == 2
    assert mock_stdout.mock_calls == [call("\nYou are fully healed.")]

#passing test case fail 
@patch('builtins.print')
def test_rest_passing_fail(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    tempWorldDay = world
    hero.hp -= 20
    temphero = hero
    main.rest(temphero,tempWorldDay)
    assert hero.hp == temphero.hp    
    assert tempWorldDay.day == 1
    assert mock_stdout.mock_calls == [call("\nYou are fully healed.")]

#failing test case pass
@patch('builtins.print')
def test_rest_failing_pass(mock_stdout):
    world = classes.Rat()
    hero = classes.Player()
    tempWorldDay = world
    hero.hp -= 20
    temphero = hero
    main.rest(temphero,tempWorldDay)
    assert mock_stdout.mock_calls == [call("Error occured: Wrong object entered")]

#failing test case fail 
@patch('builtins.print')
def test_rest_failing_fail(mock_stdout):
    world = classes.World()
    hero = classes.Player()
    tempWorldDay = world
    tempWorldDay.day =0
    temphero = hero
    main.rest(temphero,tempWorldDay)
    assert mock_stdout.mock_calls == [call("Cant Rest when dead")]

    #passing test case pass
@patch('builtins.print')
def test_print_map_passing_pass(mock_stdout):
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

#passing test case fail
@patch('builtins.print')
def test_print_map_passing_fail(mock_stdout):
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "S"
    world = classes.World()
    hero = classes.Player()
    combat.UserMovementOption(hero,world)
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

#failing test case pass
@patch('builtins.print')
def test_print_map_failing_pass(mock_stdout):
    world = classes.Rat()
    hero = classes.Player()
    main.print_Map(hero,world)
    assert mock_stdout.mock_calls ==[call('Error occured: Wrong object entered')]

#failing test case fail
@patch('builtins.print')
def test_print_map_failing_fail(mock_stdout):
    mock.builtins.input = lambda _: "D"
    world = classes.World()
    hero = classes.Player()
    world.world_Map = None
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


