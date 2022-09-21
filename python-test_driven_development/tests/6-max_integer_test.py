#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_only_one_item(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_at_the_beggining(self):
        self.assertEqual(max_integer([5, 2, 3, 4]), 5)
    
    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
    
    def test_max_with_a_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_max_of_negative_values(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
if __name__ == '__main__':
    unittest.main()
