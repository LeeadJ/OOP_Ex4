"""Pokemon Object"""


class Pokemon:
    def __init__(self, data: dict):
        self.value = float(data['value'])
        self.type = int(data['type'])
        location = str(data['pos']).split(',')
        self.pos = []
        for point in location:
            self.pos.append(float(point))
        self.marked = False
