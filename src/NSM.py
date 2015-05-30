#Class definitions and methods for the NumString Python class
#

import itertools

class NumString():
    """NumString class

    """
    def __init__(self, Digits=[]):
        """Constructor for NumString()

        
        """
        self.Digits = Digits
        self.Total = sum(self.Digits)
        self.Size = len(self.Digits)

    
    def __str__(self):
        """Return string type for NumString()"""
        if self.Size > 1:
            OutString = ','.join(str(d) for d in self.Digits)
        else:
            OutString = str(self.Digits[0])

        return OutString

    def FixTotal(self):
        """Call to reset sum to correct value"""
        self.Total = sum(self.Digits)

class NumStringPile():
    """NumStringPile class

    """
    def __init__(self, Size=0):
        """Constructor for NumStringPile()


        """
        self.Size = Size
        self.ToNums=itertools.product(range(0,Size),repeat=self.Size)
        self.Pile=[]
        for i in self.ToNums:
            self.Pile.append(NumString(i))

    def __str__(self):
        """Return string type for NumStringPile()"""
        if self.Size==0:
            OutString =  "Empty Pile"
        else:
            OutString = ';'.join(str(x) for x in self.Pile)

        return OutString
