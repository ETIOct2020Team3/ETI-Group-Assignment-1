import pytest
import main
import unittest

def test_exit_pass():
    passed = False
    try:
        main.exitGame()
    except SystemExit as e:
        if e.code == 0:
            passed = True

    assert passed

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
    main.print = lambda s : output.append(s)
 
    main.Main()
 
    assert output == ["View Character",\
             "View Map",\
             "Move",\
             "Rest",\
             "Save Game",\
             "Exit Game"]