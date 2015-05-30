__author__ = 'Matt Mastin'

import numstring
import cartgen

s = numstring.NumStringPile(3)

it = numstring.NSPIterator(s)

# for i in it:
#    print(i)

t = numstring.NSPGenerator(9)

for i in range(0,50):
    print t.gen.next()