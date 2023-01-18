import unittest
from models.base import Base

"""Our Testing module"""


class TestCaseModels(unittest.TestCase):

    def setUp(self):
        """ Method invoked for each test """
        print("done")
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_empty_id(self):
        """ Test empty id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_increament(self):
        """ Test id increament"""
        one = Base()
        two = Base()
        three = Base()
        four = Base()
        self.assertEqual(one.id, 1)
        self.assertEqual(two.id, 2)
        self.assertEqual(three.id, 3)
        self.assertEqual(four.id, 4)

    def test_big_int(self):
        """ Test Big int"""
        big = Base(2000)
        new = Base()
        self.assertEqual(big.id, 2000)
        self.assertEqual(new.id, 1)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_for_more_args(self):
        """
        Test for case where more than
        the required argument is passed
        """
        with self.assertRaises(TypeError):
            new = Base(1, 2)
