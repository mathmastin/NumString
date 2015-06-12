__author__ = 'Matt Mastin'

import numstring
import cass
import cassandra


class NumCass(numstring.NSPGenerator):
    def __init__(self, hosts=None, stringsize=0):
        """Subclass constructor for NumCass

        This class is mainly for insertion of a NumStringPile into Cassandra
        Use NumKeyspace to access an existing Pile.

        hosts will default to localhost, but keyspace must be provided

        :type stringsize: int
        """
        super(NumCass, self).__init__(stringsize)

        self.controller = NumKeyspace(stringsize, hosts)

    def insertpile(self):
        """Inserts the pile into keyspace with a column family for each starting digit"""
        count = 1
        for i in self.getgen():
            self.controller.session.execute_async("INSERT INTO start%s (num_string, comp) VALUES (%s, %s)",
                                                  [i.digits[0], str(i.digits), count])
            count += 1

    def create(self):
        """Create the Keyspace"""
        self.controller.createnumkeyspace()

    def delete(self):
        """Delete the Keyspace"""
        self.controller.deletenumkeyspace()

    #def attachkeyspace(self):
    #    self.controller.usekeyspace(self.controller.keyspace)


class NumKeyspace(cass.CassController):
    """Subcalss of CassController for use by NumCass

    Used for interacting with a NumStringPile that lives in a Cassandra keyspace
    """

    def __init__(self, stringsize=1, hosts=None):
        super(NumKeyspace, self).__init__(hosts)
        self.stringsize = stringsize
        self.keyspace = 'numstring' + str(stringsize)

    def createnumkeyspace(self):
        """Creates a keyspace using the NumString data model"""
        self.session.execute(
            "CREATE KEYSPACE IF NOT EXISTS numstring%s WITH REPLICATION = "
            "{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 }",
            [self.stringsize])

        # Set the keyspace of the session
        self.session.set_keyspace(self.keyspace)

        # This will pass "USE keyspace" to the cluster so we do not need
        # to specify the keyspace in queries
        self.usekeyspace(self.keyspace)

        # Now we create the tables
        for i in range(0, 10):
            self.session.execute(
                "CREATE TABLE IF NOT EXISTS start%s (num_string varchar PRIMARY KEY, comp int)", [i])

    def deletenumkeyspace(self):
        """Deletes the keyspace associated to the NumKeyspace"""
        self.deletekeyspace()

    def numquery(self, cqlstatement):
        """Yields a generator into the results of the query cqlstatement
        Note that we shouldn't need to explicitly include the name of the
        keyspace
        """

        # We assume that if a query is called then the keyspace exists and should be used
        # if the keyspace doesn't exist then Cassandra will throw an InvalidRequest error
        # if the generator is used.
        self.usekeyspace(self.keyspace)

        results = self.query(cqlstatement)
        for i in results:
            # The query yields a unicode version of the digits, so we must format and cast
            # to a list of ints to send to the constructor of NumString
            if self.stringsize > 1:
                yield numstring.NumString(map(int, str(i[0]).lstrip('(').rstrip(')').split(',')))
            else:
                yield numstring.NumString([int(i[0][1])])

    def getnhbs(self, numstring):
        """Returns generator into list of neighbors of numstring in the NumString graph

        Two NumStrings are neighbors if one can be obtained from the other
        by adding 1 to some integer in the string and subtracting 1 from another
        """

        if numstring.stringsize == 0:
            return None

        for i in range(0,numstring.stringsize):
            for j in range(0,numstring.stringsize):
                if i != j:
                    nbr = numstring.digits


    def dumpsubgraph(self, vertlist = None):
        """Dumps neighbor subgraph corresponding to the vertices in vertlist
        to file for processing by Graphx"""
        pass

    def updatecomps(self):
        """Reads connected component data from Graphx generated file
        and update component information in the NumString keyspace"""
        pass