# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from character_reverse import Character

class TestCharacterClass(unittest.TestCase):
    def setUp(self):
        self.character = Character('Hello World')
        
    def test_initialization(self):
        self.assertEqual(self.character.str, 'Hello World', 'incorrect str')
        
    def test_reverse_character(self):
        self.assertEqual(self.character.reverse_character(),\
                         'dlroW olleH', 'wrong reversed characters')
        
if __name__ == '__main__':
    unittest.main()