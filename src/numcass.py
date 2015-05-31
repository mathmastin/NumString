__author__ = 'Matt Mastin'

import numstring
import cass
from cassandra.cluster import Cluster


class NumCass(numstring.NSPGenerator):
    def __init__(self, hosts=None, stringsize=0):
        """Subclass constructor for NumCass

        hosts will default to localhost, but keyspace must be provided
        :type stringsize: int
        """
        super(NumCass, self).__init__(stringsize)

        self.controller = NumKeyspace(stringsize, hosts)

    def insertpile(self):
        """Inserts the pile into keyspace with a column family for each starting digit"""
        count = 1
        for i in self.getgen():
            self.controller.session.execute_async("INSERT INTO start%s (num_string, total, comp) VALUES (%s, %s, %s)",
                                                  [i.digits[0], str(i.digits), i.total, count])
            count += 1

    def pilegen(self):
        """Returns a generator to a NumPile stored in a cassandra keyspace"""
        pass

    def create(self):
        self.controller._createnumkeyspace()

    def delete(self):
        self.controller._deletenumkeyspace()


class NumKeyspace(cass.CassController):
    def __init__(self, stringsize=1, hosts=None):
        super(NumKeyspace, self).__init__(hosts)

        self.keyspace = 'numstring' + str(stringsize)
        self.stringsize = stringsize

    def _createnumkeyspace(self):
        """Creates a keyspace using the NumString data model"""
        self.session.execute(
            "CREATE KEYSPACE IF NOT EXISTS numstring%s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }",
            [self.stringsize])

        self.session.set_keyspace(self.keyspace)

        for i in range(0, 10):
            self.session.execute(
                "CREATE TABLE IF NOT EXISTS start%s (num_string varchar PRIMARY KEY, total int, comp int)", [i])

    def _deletenumkeyspace(self):
        self.deletekeyspace()
