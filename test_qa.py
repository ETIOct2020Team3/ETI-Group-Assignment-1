import pytest
import main
import unittest
import classes
import combatFunctions
import sys
import menus
from unittest import mock
from _pytest.monkeypatch import MonkeyPatch
def test_exit_pass():
    passed = False
    try:
        sys.exit(0)
    except SystemExit as e:
        if e.code == 0:
            passed = True

    assert passed
def test_new1():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: 1

    assert  original_input == 1

""" def test_exit_fail():
    passed = False
    try:
        exitGame()
    except SystemExit as e:
        if e.code != 0:
            passed = True

    assert passed """

""" def test_exitgame_town(monkeypatch) :
    hero = classes.Player()
    monkeypatch.setattr("builtins.input", lambda _: 1 )
    monkeypatch.setattr("builtins.input", lambda _: 6 )
    value = Main()
    assert value == 0 """

""" def test_viewcharacter(monkeypatch) :

    monkeypatch.setattr("builtins.input", lambda _: 1 )
    Main().location == "T"
    monkeypatch.setattr("builtins.input", lambda _: 1 )
    assert Main() == "Name :"
"""     """     passed = True

    assert passed """ """
 """
def test_new():
    input_values = "1"
    output = []
 
    def mock_input(s):
        output.append(s)
        return input_values
    main.input = mock_input
    main.print_Menu = lambda s : output.append(s)
 
 
    assert  main.print_Menu== menus.town_Menu
def test_newgame(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda: '1')
    value = main.main()
    assert value == 1



             