"""Pokemon Object"""
import math

from Gnode import Gnode
from client import Client

class Pokemon:
    def __init__(self, data: dict):
        self.value = float(data['value'])
        self.type = int(data['type'])
        location = str(data['pos']).split(',')
        self.pos = [float(location[0]), float(location[1]), float(location[2])]
        self.marked = False
        self.src = None
        self.dest = None



    def __repr__(self):
        return 'Value: %s Type: %s Pos: %s Marked: %s Src: %s Dest: %s ' % (self.value, self.type, self.pos, self.marked, self.src, self.dest)