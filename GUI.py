import json

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

"""This is the GUI class"""


class GUI:
    def __init__(self, game: Game, client: Client):
        self.client = client
        self.game = game
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        self.minX = float('inf')
        self.maxX = float('-inf')
        self.minY = float('inf')
        self.maxY = float('-inf')
        for node in self.game.algo.get_graph().get_all_v().values():
            self.minX = min(self.minX, node.location[0])
            self.minY = min(self.minY, node.location[1])
            self.maxX = max(self.maxX, node.location[0])
            self.maxY = max(self.maxY, node.location[1])

        # Adding the buttons for the GUI
        buttonColor = (28, 172, 74)
        buttonWidth = 100
        self.level_button = button(buttonColor, 1, 2, buttonWidth, 20, 'LEVEL')
        self.agent_button = button(buttonColor, 101, 2, buttonWidth, 20, 'AGENTS')
        self.time_button = button(buttonColor, 201, 2, buttonWidth, 20, 'TIME')
        self.move_button = button(buttonColor, 301, 2, buttonWidth, 20, 'MOVES')
        self.grade_button = button(buttonColor, 401, 2, buttonWidth, 20, 'GRADE')
        self.stop_button = button(buttonColor, 930, 640, buttonWidth, 20, 'Click to STOP')

    """The scale and my_scale functions will scale the GUI to fit the screen properly"""

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.minX, self.maxX)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.minY, self.maxY)

    """This function draws the given game graph"""

    def drawGraph(self):
        graph = self.game.algo.get_graph()
        # loop through the nodes in the graph
        for node in self.game.algo.get_graph().get_all_v().values():
            # loop the all the out-nodes in the graph
            for out_node in self.game.algo.get_graph().all_out_edges_of_node(node.key):
                src_node = node
                # scaling the src x and y and the dest x and y
                src_x = self.my_scale(src_node.location[0], x=True) + radius / 2
                src_y = self.my_scale(src_node.location[1], y=True) + radius / 2
                dest_x = self.my_scale(graph.node_map.get(out_node).location[0], x=True) + radius / 2
                dest_y = self.my_scale(graph.node_map.get(out_node).location[1], y=True) + radius / 2

                # drawing the edge to the GUI
                pygame.draw.line(self.screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y), 5)

        # loop through all the nodes in the graph
        for n in graph.get_all_v().values():
            self.screen.blit(node_gui, (self.my_scale(n.location[0], x=True), self.my_scale(n.location[1], y=True)))

    """This function draws the Objects (Pokemon, Agents) to the GUI"""

    def Object_drawer(self):
        # loop through the pokemons in the game
        for pokemon in self.game.pokemon_list:
            # scaling the pokemon position
            x = self.my_scale(pokemon.pos[0], x=True)
            y = self.my_scale(pokemon.pos[1], y=True)
            self.screen.blit(pokemon_gui, (x, y))

        # looping through the agents in the game
        for a in self.game.agent_dict.values():
            # scaling the agents in the game
            x = self.my_scale(a.pos[0], x=True) - radius / 2
            y = self.my_scale(a.pos[1], y=True) - radius / 2
            self.screen.blit(agent_gui, (x, y))

    """This function draws the buttons to the GUI"""
    def draw_button(self) -> None:
        # loading the json file and converting it to a dict:
        info = json.loads(self.client.get_info())["GameServer"]
        self.agent_button.text = 'AGENTS: ' + str(info['agents'])
        self.agent_button.draw(self.screen, (0, 0, 0))
        self.level_button.text = 'LEVEL: ' + str(info['game_level'])
        self.level_button.draw(self.screen, (0, 0, 0))
        self.move_button.text = 'MOVES: ' + str(info['moves'])
        self.move_button.draw(self.screen, (0, 0, 0))
        self.time_button.text = 'TIME: ' + str(int(float(self.client.time_to_end()) / 1000))
        self.time_button.draw(self.screen, (0, 0, 0))
        self.grade_button.text = 'GRADE: ' + str(info["grade"])
        self.grade_button.draw(self.screen, (0, 0, 0))
        self.stop_button.draw(self.screen, (0, 0, 0))

    """This function draws all the functions each iteration to the GUI. Returns true id succesful"""

    def draw(self) -> bool:
        # scaling the background image
        background_image = transform.scale(background_gui, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background_image, [0, 0])
        # checking if the event is not QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False
            # if clicked on the stop button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.stop_button.isOver(mouse.get_pos()):
                    pygame.quit()
                    exit(0)
                    return False
        self.drawGraph()
        self.draw_button()
        self.Object_drawer()
        display.update()
        return True




# Found code from open source (stackoverflow)
# https://stackoverflow.com/questions/63435298/how-to-create-a-button-class-in-pygame
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 10)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False
