import pytest
import main
from test_base import *
from unittest.mock import patch
from unittest import TestCase



 # exit game test


# def test_exit():
#     with pytest.raises(SystemExit) as pytest_wrapped_e:
#             set_keyboard_input(['1','6'])
#             main.exitGame()
            
#     assert pytest_wrapped_e.type == SystemExit
#     assert pytest_wrapped_e.value.code == 0

# def test_exit_2():
#     with pytest.raises(SystemExit) as pytest_wrapped_e:
#             main.exitGame()
#     assert pytest_wrapped_e.type != SystemExit
#     assert pytest_wrapped_e.value.code !=0      


def test_rest():
    value = main.rest()
    assert hero.hp == 20





