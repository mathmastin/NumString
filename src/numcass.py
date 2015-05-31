__author__ = 'Matt'

import numstring
from cassandra.cluster import Cluster


class NumCass(numstring.NSPGenerator):
    def __init__(self, hosts=None, keyspace=None, stringsize=0):
        if not hosts:
            hosts = ['localhost']
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
