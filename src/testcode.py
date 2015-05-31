__author__ = 'Matt Mastin'

import cassandra
import numstring

s = numstring.NumStringPile(3)

it = numstring.NSPIterator(s)

# for i in it:
#    print(i)

t = numstring.NSPGenerator(2)

print t.getnum() == t.getnum()