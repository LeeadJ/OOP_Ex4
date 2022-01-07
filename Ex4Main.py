import json


from client import Client
from time import sleep
from GUI import GUI
from GameFunc import *
import subprocess
subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {11}'])
# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

clock = pygame.time.Clock()

client = Client()
game = Game()
client.start_connection(HOST,PORT)
client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")
client.add_agent("{\"id\":4}")
client.start()
game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())
print(game.algo.get_graph())
# game.pokemon_src_dest(game.pokemons_list[0])
gui = GUI(game, client)


# game.pokemon_src_dest(game.pokemons_list[0])

while client.is_running() == 'true':
    game.play(client)
    gui.draw()
    print(client.move())
    print(client.get_info())