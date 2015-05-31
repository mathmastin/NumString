__author__ = 'Matt Mastin'

import numstring


def cart_prod(sets):
    """Gives a generator for the cartesian product
    of the lists in sets

    :param sets: list of lists

    :rtype : list
    """
    if not sets:
        yield ()
    else:
        for i in sets[0]:
            for x in cart_prod(sets[1:]):
                yield (i,) + x
