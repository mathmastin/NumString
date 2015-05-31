__author__ = 'Matt'

import numstring
from cassandra.cluster import Cluster


class NumCass(numstring.NSPGenerator):
    def __init__(self, hosts=['localhost'], keyspace=None):
        self.cluster = Cluster(hosts)
        self.keyspace = keyspace
        self.session = self.cluster.connect(self.keyspace)

    def insertpile(self):
        pass

