import unittest
from metaclass import CustomClass


class TestCustomClass(unittest.TestCase):
    """TestClass for CustomClass"""

    def setUp(self):
        """method to execute before each test"""
        self.inst = CustomClass(20)

    def test_invalid_method(self):
        """checks inaccessibility of methods by names 'default_name'"""
        self.assertRaises(AttributeError, lambda: self.inst.line())

    def test_valid_method(self):
        """checks availability of methods by names 'prefix+default_name'"""
        self.assertEqual(self.inst.custom_line(), 100)

    def test_invalid_class_attribute(self):
        """checks inaccessibility of class attributes by names 'default_name'"""
        self.assertRaises(AttributeError, lambda: self.inst.x)

    def test_valid_class_attribute(self):
        """checks availability of class attributes by names 'prefix+default_name'"""
        self.assertEqual(self.inst.custom_x, 50)

    def test_invalid_initialized_attribute(self):
        """checks inaccessibility of class attributes by names 'default_name'"""
        self.assertRaises(AttributeError, lambda: self.inst.val)

    def test_valid_initialized_attribute(self):
        """checks availability of class attributes by names 'prefix+default_name'"""
        self.assertEqual(self.inst.custom_val, 20)


if __name__ == '__main__':
    unittest.main()
