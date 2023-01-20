"""Module Documentation"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """Class Hanlding the unittest cases for our rectangle"""
    def set_up(self):
        """Method to setup each test"""
        Base._Base__nb_object = 0

    def test_init(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def test_init_with_no_arg(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_init_with_id(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20, id=1)
        self.assertEqual(r.id, 1)
# ================================================
    def test_init_with_no_id(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        self.assertEqual(r.id, 1)
# ================================================

    def test_width_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_width_setter_with_invalid_value(self):
        """Test case for Rectanlge setter with str"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "30"

    def test_width_setter_with_negative_value(self):
        """Test case for Rectanlge setter with < 0"""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -30

    def test_height_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

    def test_height_setter_with_invalid_value(self):
        """Test case for Rectanlge height setter with str"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = "30"

    def test_height_setter_with_negative_value(self):
        """Test case for Rectanlge height setter with < 0"""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -30

    def test_x_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

    def test_x_setter_with_invalid_value(self):
        """Test case for Rectanlge x setter str"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.x = "30"


    def test_x_setter_with_negative_value(self):
        """Test case for Rectanlge x setter <0"""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -30

    def test_y_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.y = 30
        self.assertEqual(r.y, 30)

    def test_y_setter_with_invalid_value(self):
        """Test case for Rectanlge setter with another type"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.y = "30"

    def test_y_setter_with_negative_value(self):
        """Test case for Rectanlge setter with <0"""
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -30

    def test_area(self):
        """Test case for Area of a Rectangle"""
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)


    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """Testing str Output"""
        r = Rectangle(4, 6, 7, 5, 3)
        str_output = "[Rectangle] (3) 7/5 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as output:
            print(r)
            self.assertEqual(output.getvalue(), str_output)

# ========================================================
    def test_str2(self):
        """Testing str Output 2"""
        r = Rectangle(5, 5, 9, 8)
        str_output = "[Rectangle] (1) 9/8 - 5/5\n"
        with patch('sys.stdout', new=StringIO()) as output:
            print(r)
            self.assertEqual(output.getvalue(), str_output)
    def test_strp(self):
        """Testing str output"""
        r = Rectangle(2, 3, 4)
        str_out = "[Rectangle] (1) 4/0 - 2/3\n"

        with patch('sys.stdout', new=StringIO()) as output:
            print(r)
            self.assertEqual(output.getvalue(), str_out)
# ========================================================

    def test_update(self):
        """Testing for the update method"""
        r = Rectangle(2, 6)
        out = "[Rectangle] (2) 1/3 - 4/2\n"

        with patch('sys.stdout', new=StringIO()) as output:
            r.update(y=3, x=1, height=2, width=4, id=2)
            print(r)
            self.assertEqual(output.getvalue(), out)

    def test_update2(self):
        """Testing for the update method"""
        r = Rectangle(2, 6)
        out = "[Rectangle] (3) 4/2 - 1/2\n"

        with patch('sys.stdout', new=StringIO()) as output:
            r.update(3, 1, 2, 4, 2)
            print(r)
            self.assertEqual(output.getvalue(), out)

    def test_to_dict(self):
        """Testing when dictionary is returned"""
        r = Rectangle(2, 6, 4, 5, 12)
        self.assertEqual(r.to_dictionary(),
        {'id': 12, 'width': 2, 'height': 6, 'x': 4, 'y': 5})

    def test_to_dict_method(self):
        """Testing when dictionary is returned"""
        r = Rectangle(2, 6, 4, 5)
        self.assertEqual(r.to_dictionary(),
        {'id': 1, 'width': 2, 'height': 6, 'x': 4, 'y': 5})

