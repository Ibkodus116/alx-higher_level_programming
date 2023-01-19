"""Module Documentation"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_width_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_width_setter_with_invalid_value(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "30"
        with self.assertRaises(ValueError):
            r.width = -30

    def test_height_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.height = 30
        self.assertEqual(r.height, 30)

    def test_height_setter_with_invalid_value(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = "30"
        with self.assertRaises(ValueError):
            r.height = -30

    def test_x_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.x = 30
        self.assertEqual(r.x, 30)

    def test_x_setter_with_invalid_value(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.x = "30"
        with self.assertRaises(ValueError):
            r.x = -30

    def test_y_setter(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        r.y = 30
        self.assertEqual(r.y, 30)

    def test_y_setter_with_invalid_value(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.y = "30"
        with self.assertRaises(ValueError):
            r.y = -30

    def test_area(self):
        """Test case for Rectanlge"""
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)
