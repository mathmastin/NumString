__author__ = 'Matt'

from cassandra.cluster import Cluster


class CassController(object):
    """Controller for interacting with a cassandra database."""

    def __init__(self, hosts=None, keyspace=None):
        if not hosts:
            hosts = ['localhost']
        self.cluster = Cluster(hosts)
        self.keyspace = keyspace

        self.session = self.cluster.connect(self.keyspace)

    def deletekeyspace(self):
        if self.keyspace is not None:
            self.session.execute("DROP KEYSPACE " + self.keyspace)