__author__ = 'Matt Mastin'

import numcass
import numstring

# s = numstring.NumStringPile(3)

# print s

# it = numstring.NSPIterator(s)

# for i in it:
#    print i

# t = numstring.NSPGenerator(2)

# print t.getnum() == t.getnum()

# ins = numcass.NumCass(['10.104.251.45'], 'numstring3', 3)

# ins.insertpile()

# for i in ins.getgen():
#    print i

#cass = numcass.NumKeyspace(1, ['10.104.251.45'])

#cass.createnumkeyspace()

cont = numcass.NumCass(['10.104.251.45'], 1)

#cont.create()

#cont.attachkeyspace()

#cont.insertpile()

cont.delete()

#elts = cont.numquery("SELECT * FROM start0 WHERE num_string = '(1, 2)'")

#elts = cont.numquery("SELECT * FROM start0")

#for i in elts:
#    print i
