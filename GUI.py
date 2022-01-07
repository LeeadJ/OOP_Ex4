import pygame
from pygame import *
from client import Client
from GameFunc import Game

WIDTH, HEIGHT = 1080, 720
radius = 15
background_pic = r"C:\Users\Leead\Downloads\wp4335583.webp"
agent_pic = r"C:\Users\Leead\Downloads\Ashanime.png"
pokemon_pic = r"C:\Users\Leead\Downloads\cara-menggambar-pokemon-api-115632259501lkwncr7ey.png"
node_pic = r"C:\Users\Leead\Downloads\node.png"
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
agent_gui = image.load(agent_pic)
agent_gui = pygame.transform.scale(agent_gui, (50, 50))
pokemon_gui = image.load(pokemon_pic)
pokemon_gui = pygame.transform.scale(pokemon_gui, (50, 50))
background_gui = image.load(background_pic)
node_gui = image.load(node_pic)
node_gui = pygame.transform.scale(node_gui, (50, 50))


class GUI:
    def __init__(self, game: Game, client: Client):
        self.client = client
        self.game = game
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
        for node in self.game.algo.get_graph().get_all_v().values():
            x = node.location[0]
            y = node.location[1]
            self.min_x = min(self.min_x, x)
            self.min_y = min(self.min_y, y)
            self.max_x = max(self.max_x, x)
            self.max_y = max(self.max_y, y)


    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)

    def drawNode(self):
        for n in self.game.algo.get_graph().get_all_v().values():
            x = self.my_scale(n.location[0], x=True)
            y = self.my_scale(n.location[1], y=True)
            self.screen.blit(node_gui, (x, y))

    def drawEdges(self):
        graph = self.game.algo.get_graph()
        for node in self.game.algo.get_graph().get_all_v().values():
            for out_node in self.game.algo.get_graph().all_out_edges_of_node(node.key):
                src_node = node
                src_x = self.my_scale(src_node.location[0], x=True) + radius / 2
                src_y = self.my_scale(src_node.location[1], y=True) + radius / 2
                dest_x = self.my_scale(graph.node_map.get(out_node).location[0], x=True) + radius / 2
                dest_y = self.my_scale(graph.node_map.get(out_node).location[1], y=True) + radius / 2
                pygame.draw.line(self.screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y), 5)

    def drawPokemons(self):
        for pokemon in self.game.pokemon_list:
            x = self.my_scale(pokemon.pos[0], x=True)
            y = self.my_scale(pokemon.pos[1], y=True)
            self.screen.blit(pokemon_gui, (x, y))

    def drawAgents(self):
        for a in self.game.agent_dict.values():
            x = self.my_scale(a.pos[0], x=True) - radius / 2
            y = self.my_scale(a.pos[1], y=True) - radius / 2
            self.screen.blit(agent_gui, (x, y))

    def draw(self) -> bool:
        background_image = transform.scale(background_gui, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background_image, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False
        self.drawEdges()
        self.drawNode()
        self.drawPokemons()
        self.drawAgents()
        display.update()
        return True