import random
"""This class represents a Node.
    - Edges In.
    - Edges Out.
    - Key (ID).
    - location."""


class Gnode:

    """Constructor"""
    def __init__(self, key, location: tuple = None,):
        self.edges_in = 0
        self.edges_out = 0
        self.key = key
        if location is None:
            x = random.uniform(35, 36)
            y = random.uniform(32, 33)
            location = (x, y, 0)
            self.location = location
        else:
            self.location = location
        self.tag = 0

    def __repr__(self):
        return '%s: |edges out| %s |edges in| %s' % (self.key, self.edges_out, self.edges_in)
