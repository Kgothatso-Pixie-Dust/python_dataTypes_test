import unittest
from unittest.mock import patch


def function():

    user_input = input('Enter a number')
    
    return int(user_input)



class TextFunction(unittest.TestCase):

    def test_function(self):
        with patch('builtins.input', return_value = '123'):
            self.assertEqual(function(), 123)