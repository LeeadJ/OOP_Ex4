"""This class represents an Edge."""


class Edge:

    """Constructor"""
    def __init__(self, Src, Weight, Dest):
        self.Src = Src
        self.Weight = Weight
        self.Dest = Dest

    def __repr__(self):
        return 'Src: %s, Dest: %d, Weight: %s' % (self.Src, self.Dest, self.Weight)
