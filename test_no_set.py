#!/usr/bin/env python
import unittest
from no_set import is_set, SetGame 

class SetGameTest(unittest.TestCase):
    def test_is_set(self):
        self.assertTrue(is_set(("squiggle", "purple", "empty", "one"),
                               ("squiggle", "purple", "empty", "two"),
                               ("squiggle", "purple", "empty", "three")))
    
        self.assertTrue(is_set(("squiggle", "purple", "empty", "one"),
                               ("squiggle", "purple", "solid", "one"),
                               ("squiggle", "purple", "lined", "one")))

        self.assertTrue(is_set(("squiggle", "purple", "empty", "one"),
                               ("squiggle", "green", "empty", "one"),
                               ("squiggle", "red", "empty", "one")))
        
        self.assertTrue(is_set(("squiggle", "purple", "empty", "one"),
                               ("pill", "green", "solid", "two"),
                               ("diamond", "red", "lined", "three")))

        self.assertFalse(is_set(("squiggle", "purple", "empty", "one"),
                               ("squiggle", "green", "solid", "two"),
                               ("diamond", "red", "lined", "three")))

        self.assertFalse(is_set(("squiggle", "purple", "empty", "one"),
                               ("squiggle", "purple", "empty", "two"),
                               ("squiggle", "purple", "empty", "one")))

 
class WithoutReplacementTest(unittest.TestCase):
    def setUp(self):
        """docstring for setUp"""
        self.game = SetGame(with_replacement=False)

    def test_exhaust_cards(self):
        """docstring for test_exhaust_cards"""
        all_cards = set()
        for i in xrange(81):
            all_cards.add(self.game.get_random_card())

        self.assertRaises(Exception, self.game.get_random_card)
        self.assertEqual(81, len(all_cards))

if __name__ == '__main__':
    unittest.main()
 
