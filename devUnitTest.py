import unittest
from unittest import mock 
import main as main
import combatMenuFunctions as combat
import classes as classes

class test_harith(unittest.TestCase):
    def test_exit_pass(self):
        passed = False
        try:
            main.exitGame()
        except SystemExit as e: 
            if e.code == 0:
                passed = True

        self.assertEqual(passed,True) 

    def test_move_pass(self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _: "D"
        hero = classes.Player()
        world = classes.World()
        combat.UserMovementOption(hero,world)
        self.assertEqual(world.world_map[hero.positionX][hero.positionY]," ")
        mock.builtins.input = original_input


    def test_attack_pass(self):
        rat= classes.Rat()
        hero=classes.Player()
        ratStartingHP = rat.hp
        combat.attack(rat,hero)
        self.assertGreater(ratStartingHP,rat.hp)

            
if __name__ == '__main__':
    unittest.main()