import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch, mock_open
import json

"""Our Testing module"""


class TestCaseModels(unittest.TestCase):

    def setUp(self):
        """ Method invoked for each test """
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

    def test_obj_dict_to_json(self):
        """object values are converted to json str"""
        self.assertEqual(Base.to_json_string([{'x': 2,
                        'width': 10,
                        'id': 1,
                        'height': 7,
                        'y': 8}]
                        ),
                        '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
                        )

    def test_obj_list_to_json(self):
        """object values are converted to json str"""
        self.assertEqual(Base.to_json_string([[12,3,4]]),'[[12, 3, 4]]')

    def test_obj_empty_list_to_json(self):
        """Empty object values are converted to json str"""
        self.assertEqual(Base.to_json_string([]),'[]')

    def test_none_to_json(self):
        """Empty object values are converted to json str"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_3(self):
        """ Test JSON file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        res = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]\n'
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_from_json_string (self):
        """ Test from JSON to obj"""

        json_str = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        res = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
                {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]

        self.assertEqual(Rectangle.from_json_string(json_str), res)

    def test_from_json_string2 (self):
        """ Test from JSON to obj"""

        json_str = '[23, 34, 45]'
        res = [23, 34, 45]

        self.assertEqual(Rectangle.from_json_string(json_str), res)

    def test_from_json_string3 (self):
        """ Test from JSON to obj"""

        json_str = None
        res = []

        self.assertEqual(Rectangle.from_json_string(json_str), res)

    def test_from_json_string4 (self):
        """ Test from JSON to obj"""
        json_str = [1,2,3]
        with self.assertRaises(TypeError):
            Rectangle.from_json_string(json_str)

    def test_create (self):
        """Testing the create method"""
        r = Rectangle(3, 5, 1).to_dictionary()
        r1 = Rectangle.create(**r)
        res = "[Rectangle] (1) 1/0 - 3/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_create_2 (self):
        """Testing the create method"""
        r = Rectangle(3, 5, 1).to_dictionary()
        with self.assertRaises(TypeError):
            Rectangle.create(r)

    def test_create_3 (self):
        """Testing the create method"""
        r = Square(3, 5, 1, 4).to_dictionary()
        r1 = Square.create(**r)
        res = "[Square] (4) 5/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)
