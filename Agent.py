"""Agent Object"""


class Agent:
    def __init__(self, data: dict):
        self.id = int(data['id'])
        self.value = float(data['value'])
        self.src = int(data['src'])
        self.dest = int(data['dest'])
        self.speed = float(data['speed'])
        location = str(data['pos']).split(',')
        self.pos = (float(location[0]), float(location[1]), float(location[2]))


    def __repr__(self):
        return 'ID: %s Value: %s Src: %s Dest: %s ' \
               'Speed: %s Pos: %s' % (self.id, self.value, self.src, self.dest, self.speed, self.pos)