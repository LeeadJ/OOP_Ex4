import json

from Agent import Agent
from client import Client
from Pokemon import *
import subprocess

subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {5}'])

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST, PORT)



class Game:
    def __init__(self):
        self.pokemon_list = []  # this list represents the pokemon in the game
        self.agent_list = []  # this list represents the agents in the game
        self.moves = 0  # represents the games moves.

    def initialize(self, pokemon_json_str, agent_json_str):
        pokemons = json.loads(pokemon_json_str)
        for i in pokemons['Pokemons']:
            temp = Pokemon(i['Pokemon'])
            self.pokemon_list.append(temp)
        agents = json.loads(agent_json_str)
        for i in agents['Agents']:
            temp = Agent(i['Agent'])
            self.agent_list.append(temp)



if __name__=='__main__':
    client.add_agent("{\"id\":0}")
    client.add_agent("{\"id\":1}")
    client.add_agent("{\"id\":2}")
    client.add_agent("{\"id\":3}")
    game = Game()
    game.initialize(client.get_pokemons(), client.get_agents())
    print(len(game.agent_list))
    print(len(game.pokemon_list))
    print(game.agent_list)
    print(game.pokemon_list)
