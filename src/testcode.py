__author__ = 'Matt Mastin'

import numcass
import numstring

s = numstring.NumStringPile(3)

it = numstring.NSPIterator(s)

print s

t = numstring.NSPGenerator(2)

print t.getnum() == t.getnum()

ins = numcass.NumCass(['10.104.251.45'],"numstring3",3)

#ins.insertpile()

for i in ins.getgen():
    print i