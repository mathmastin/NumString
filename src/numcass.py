__author__ = 'Matt Mastin'

import numstring
import cass
from cassandra.cluster import Cluster

class NumCass(numstring.NSPGenerator):
    def __init__(self, hosts=None, keyspace=None, stringsize=0):
        """Subclass constructor NumCass

        hosts will default to localhost, but keyspace must be provided
        """
        if not hosts:
            hosts = ['localhost']
        if not keyspace:
            raise ValueError("Name of keyspace must be provided.")
        super(NumCass, self).__init__(stringsize)
        self.cluster = Cluster(hosts)
        self.keyspace = keyspace
        self.session = self.cluster.connect(self.keyspace)

    def insertpile(self):
        """Inserts the pile into keyspace with a column family for each starting digit"""
        for i in self.getgen():
            self.session.execute("INSERT INTO start%s (num_string, total) VALUES (%s, %s)",
                                 [i.digits[0], str(i.digits), i.total])

    def pilegen(self):
        """Returns a generator to a NumPile stored in a cassandra keyspace"""
        pass


class NumKeyspace(cass.CassController):
    def __init__(self, stringsize=1, hosts=None):
        super(NumKeyspace, self).__init__(hosts)
        self.keyspace = 'numstring'+str(stringsize)

        self.stringsize = stringsize


    def createnumkeyspace(self):
        self.session.execute(
            "CREATE KEYSPACE numstring%s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }",
            [self.stringsize])

        self.session.set_keyspace(self.keyspace)

        for i in range(0,10):
            self.session.execute("CREATE TABLE start%s (num_string varchar PRIMARY KEY, total int)",[i])

    def deletenumkeyspace(self):
        self.deletekeyspace()