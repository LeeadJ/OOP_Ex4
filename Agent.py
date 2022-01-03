"""Agent Object"""


class Agent:
    def __init__(self, data: dict):
        self.id = int(data['id'])
        self.value = float(data['value'])
        self.src = int(data['src'])
        self.dest = int(data['dest'])
        self.speed = float(data['speed'])
        location = str(data['pos']).split(',')
        self.pos = []
        for n in location:
            self.pos.append(float(n))
        self.pokemon_list = []
