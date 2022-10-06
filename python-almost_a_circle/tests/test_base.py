#!/usr/bin/python3
""" Unittest for Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        base = Base(89)
        self.assertEqual(base.id, 89)
