import unittest
from parameterized import parameterized

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """TestClass for CustomList"""

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [[1, 2, 3, 4], CustomList([1, 2, 3])]
    ])
    def test_inst_add(self, lst1, lst2):
        """Checks that the result of addition is object of CustomList"""
        self.assertIsInstance(lst1 + lst2, CustomList)

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [[1, 2, 3, 4], CustomList([1, 2, 3])]
    ])
    def test_add(self, lst1, lst2):
        """Checks the correctness of addition operation"""
        self.assertTrue(list.__eq__((lst1 + lst2), CustomList([2, 4, 6, 4])))

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [[1, 2, 3, 4], CustomList([1, 2, 3])]
    ])
    def test_inst_sub(self, lst1, lst2):
        """Checks that the result of substitution is object of CustomList"""
        self.assertIsInstance(lst1 - lst2, CustomList)

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [[1, 2, 3], CustomList([1, 2, 3, 4])]
    ])
    def test_sub(self, lst1, lst2):
        """Checks the correctness of substitution operation"""
        self.assertTrue(list.__eq__((lst1 - lst2), CustomList([0, 0, 0, -4])))

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [[1, 2, 3], CustomList([1, 2, 3, 4])]
    ])
    def test_lt(self, lst1, lst2):
        """Checks the correctness of comparison (<)"""
        self.assertTrue(lst1 < lst2)

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3])],
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [CustomList([1, 2, 3]), [1, 2, 3]],
        [[1, 2, 3], CustomList([1, 2, 3, 4])],
        [[1, 2, 3], CustomList([1, 2, 3])]
    ])
    def test_le(self, lst1, lst2):
        """Checks the correctness of comparison (<=)"""
        self.assertTrue(lst1 <= lst2)

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3]), [1, 2, 3, 4]],
        [[1, 2, 3], CustomList([1, 2, 3, 4])]
    ])
    def test_ne(self, lst1, lst2):
        """Checks the correctness of comparison (!=)"""
        self.assertTrue(lst1 != lst2)

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3])],
        [CustomList([1, 2, 3]), [1, 2, 3]],
        [[1, 2, 3], CustomList([1, 2, 3])]
    ])
    def test_eq(self, lst1, lst2):
        """Checks the correctness of comparison (==)"""
        self.assertTrue(lst1 == lst2)

    @parameterized.expand([
        [CustomList([1, 2, 3]), CustomList([1, 2, 3])],
        [CustomList([1, 2, 3, 4]), CustomList([1, 2, 3, 3])],
        [CustomList([1, 2, 3, 5]), [1, 2, 3, 4]],
        [CustomList([1, 2, 3]), [1, 2, 3]],
        [[1, 2, 3, 5], CustomList([1, 2, 3, 4])],
        [[1, 2, 3], CustomList([1, 2, 3])]
    ])
    def test_ge(self, lst1, lst2):
        """Checks the correctness of comparison (>=)"""
        self.assertTrue(lst1 >= lst2)

    @parameterized.expand([
        [CustomList([1, 2, 3, 5]), CustomList([1, 2, 3, 4])],
        [CustomList([1, 2, 3, 5]), [1, 2, 3, 4]],
        [[1, 2, 3, 5], CustomList([1, 2, 3, 4])]
    ])
    def test_gt(self, lst1, lst2):
        """Checks the correctness of comparison (>)"""
        self.assertTrue(lst1 > lst2)


if __name__ == '__main__':
    unittest.main()
