__author__ = 'Matt Mastin'

import numstring

s = numstring.NumStringPile(3)

it = numstring.NSPIterator(s)

# for i in it:
#    print(i)

t = numstring.NSPGenerator(2)

g = t.gen()


