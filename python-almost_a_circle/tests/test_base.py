#!/usr/bin/python3
""" Unittest for Base class """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        base = Base()
        self.assertEqual(base.id, 1)
