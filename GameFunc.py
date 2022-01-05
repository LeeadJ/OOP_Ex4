import json
import math
from Agent import Agent
from Gnode import Gnode
from GraphAlgo import GraphAlgo
from client import Client
from Pokemon import *
import subprocess
epsilon = 0.00000000001

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
        self.agent_dict = {} # this list represents the agents in the game
        self.moves = 0  # represents the games moves.
        self.algo = GraphAlgo()


    def initialize(self, pokemon_json_str, agent_json_str, graph_str):
        pokemons = json.loads(pokemon_json_str)
        for i in pokemons['Pokemons']:
            temp = Pokemon(i['Pokemon'])
            self.pokemon_list.append(temp)
        agents = json.loads(agent_json_str)
        for i in agents['Agents']:
            agent_id = int(i['Agent']['id'])
            self.agent_dict[agent_id] = Agent(i['Agent'])
        self.algo.load_from_json(graph_str)

    """This function refreshes the game (updates the current information)."""
    def refresh_game(self, pokemon_json_str=None, agent_json_str=None ):
        if agent_json_str is not None:
            agents = json.loads(agent_json_str)
            for i in agents['Agents']:
                agent_id = int(i['Agent']['id'])
                self.agent_dict[agent_id] = Agent(i['Agent'])
        if pokemon_json_str is not None:
            self.pokemon_list = []
            pokemons = json.loads(pokemon_json_str)
            for i in pokemons['Pokemons']:
                temp = Pokemon(i['Pokemon'])
                self.pokemon_edge(temp) # updating the pokemon src/dest
                self.pokemon_list.append(temp)



    """Find the edge of the given pokemon."""
    def pokemon_edge(self, pokemon: Pokemon) ->None:
        p_node = Gnode(1, pokemon.pos)

        # loop through the graph nodes and find fitting ones:
        for n1 in self.algo.get_graph().get_all_v().values():
            for n2 in self.algo.get_graph().get_all_v().values():
                node_dist = Game.distance(n1, n2)
                pokemon_dist = Game.distance(n1, p_node) + Game.distance(p_node, n2)

                if(abs(node_dist-pokemon_dist) < epsilon):
                    if(pokemon.type < 0):
                        s = max(n1.key, n2.key)
                        d = min(n1.key, n2.key)
                        if(s in self.algo.get_graph().edge_map.keys()):

                            if(d in self.algo.get_graph().edge_map[s].keys()):
                                pokemon.src = s
                                pokemon.dest = d
                    else:
                        s = min(n1.key, n2.key)
                        d = max(n1.key, n2.key)
                        if (s in self.algo.get_graph().edge_map.keys()):
                            if (d in self.algo.get_graph().edge_map[s].keys()):
                                pokemon.src = s
                                pokemon.dest = d


        return
    @staticmethod
    def distance(n1: Gnode, n2: Gnode):
        x = (n1.location[0] - n2.location[0])
        y = (n1.location[1] - n2.location[1])
        return math.sqrt(pow(x, 2) + pow(y, 2))



if __name__=='__main__':
    client.add_agent("{\"id\":0}")
    client.add_agent("{\"id\":1}")
    client.add_agent("{\"id\":2}")
    client.add_agent("{\"id\":3}")
    game = Game()
    game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())



    print()
    print("\nInitialize")
    print("Agents: ",game.agent_dict)
    print("Pokemon: ", game.pokemon_list)
    print('\n')
    game.refresh_game(client.get_pokemons(), client.get_agents())
    print("Refresh")
    print("Agents: ", game.agent_dict)
    print("Pokemon: ", game.pokemon_list)
    print("Graph: ", game.algo.get_graph().edge_map)





