import pytest
import main
import test_base
from unittest.mock import patch
from unittest import TestCase


mock = Mock()
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

# @mock.pa
# def test_rest():
#         value= main.rest()
#         assert value.hero.hp == 20

def test_main():
        main.input = lambda : 1   
        output = main.Main()
        assert output =="hello"


