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

cont = numcass.NumCass(['10.104.251.45'], 2)

cont.create()

cont.insertpile()

#cont.insertpile()

#cass.deletenumkeyspace()
