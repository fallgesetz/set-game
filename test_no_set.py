import unittest
from no_set import is_set 

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

if __name__ == '__main__':
    unittest.main()
 
