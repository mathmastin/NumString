__author__ = 'Matt Mastin'

import itertools
import cartgen


class NumString(object):
    """NumString class

    """
    def __init__(self, digits=None):
        """Constructor for NumString()

        Generates a NumString from the given list.
        A NumString is empty by default.

        :type digits: list
        """
        self.digits = digits
        self.total = sum(self.digits)
        self.stringsize = len(self.digits)

    def __str__(self):
        """Return string type for NumString()

        :rtype : string
        """
        if self.stringsize > 1:
            outstring = ','.join(str(d) for d in self.digits)
        else:
            outstring = str(self.digits[0])

        return outstring

    def __eq__(self, other):
        """Overload equality"""
        return self.digits == other.digits

    def fixtotal(self):
        """Call to reset sum to correct value"""
        self.total = sum(self.digits)


class NumStringPile(object):
    """NumStringPile class

    The NumStringPile is a list of all possible NumStrings
    of a given Size
    """

    def __init__(self, stringsize=0):
        """Constructor for NumStringPile()

        Generates a list of all NumStrings of length Size
        Size will default to 0 creating an empty Pile
        This will build the pile in memory, so be warned
        """
        self.stringsize = stringsize
        self.nums = itertools.product(range(0, 10), repeat=self.stringsize)
        self.pile = []
        for i in self.nums:
            self.pile.append(NumString(i))

    def __str__(self):
        """Return string type for NumStringPile()

        :rtype : string
        """
        if self.stringsize == 0:
            outstring = 'Empty Pile'
        else:
            outstring = ';'.join(str(x) for x in self.pile)
        return outstring


class NSPIterator(object):
    """Iterator for NumStringPile"""

    def __init__(self, itpile=None):
        self.itpile = itpile
        if self.itpile is not None:
            self.pilelength = len(self.itpile.pile)
            self.step = self.pilelength
        else:
            self.step = 0

    def __iter__(self):
        """Returns the iterator"""
        return self

    def next(self):
        """Returns the next element in the pile"""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.itpile.pile[(self.pilelength - 1) - self.step]


class NSPGenerator(object):
    """Generator to create NumStringPiles

    This should be used for piles of large NumStrings
    """
    def __init__(self, stringsize=0):
        self.stringsize = stringsize
        self.sets = []
        self.count = 0

        for i in range(0, self.stringsize):
            self.sets.append(range(0, 10))

        self.gen = cartgen.cart_prod(self.sets)

    def getnum(self):
        """Returns the NumString corresponding to the next element yielded by self.gen"""
        return NumString(self.gen.next())

    def getgen(self):
        """Returns a generator for the NumStringPile"""
        for x in self.gen:
            yield NumString(x)