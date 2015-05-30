## Class definitions and methods for the NumString Python class
## Matt Mastin

import itertools


class NumString:
    """NumString class

    """

    def __init__(self, digits=None):
        """Constructor for NumString()

        Generates a NumString from the given list
        A NumString is empty by default

        :type digits: list
        """
        self.digits = digits
        self.total = sum(self.digits)
        self.size = len(self.digits)

    def __str__(self):
        """Return string type for NumString()

        :rtype : string
        """
        if self.size > 1:
            outstring = ','.join(str(d) for d in self.digits)
        else:
            outstring = str(self.digits[0])

        return outstring

    def fixtotal(self):
        """Call to reset sum to correct value"""
        self.total = sum(self.digits)


class NumStringPile:
    """NumStringPile class

    The NumStringPile is a list of all possible NumStrings
    of a given Size
    """

    def __init__(self, size=0):
        """Constructor for NumStringPile()

        Generates a list of all NumStrings of length Size
        Size will default to 0 creating an empty Pile
        """
        self.size = size
        self.nums = itertools.product(range(0, size), repeat=self.size)
        self.pile = []
        for i in self.nums:
            self.pile.append(NumString(i))

    def __str__(self):
        """Return string type for NumStringPile()

        :rtype : string
        """
        if self.size == 0:
            outstring = 'Empty Pile'
        else:
            outstring = ';'.join(str(x) for x in self.pile)
        return outstring

    def __iter__(self):
        """Defines the iteration of a NumStringPile

        :type self: NumStringPile
        """
