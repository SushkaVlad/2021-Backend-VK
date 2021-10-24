from itertools import zip_longest


class CustomList(list):
    """Class implements functionality of summarizing lists by elements and comprising by sums"""

    def __add__(self, other):
        return CustomList([x + y for x, y in zip_longest(self, other, fillvalue=0)])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return CustomList([x - y for x, y in zip_longest(self, other, fillvalue=0)])

    def __rsub__(self, other):
        return CustomList(other) - self

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
