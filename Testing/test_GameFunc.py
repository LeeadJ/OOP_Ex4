from unittest import TestCase

from GameFunc import Game
from client import Client
import subprocess

subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {1}'])

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
# initializing the Client
client = Client()
client.start_connection(HOST, PORT)
client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")
client.add_agent("{\"id\":4}")
client.start()
# initializing the game
game = Game()


class test_GameFunc(TestCase):
    def init_test(self):
        game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())
        self.assertEqual(1, len(game.agent_dict))
        self.assertEqual(2, len(game.pokemon_list))
        self.assertIsNotNone(game.algo.get_graph())

    def refresh_test(self):
        game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())
        game.refresh_game(client.get_pokemons(), client.get_agents())
        # checking that the src and dest of the pokemon has been updated:
        self.assertIsNotNone(game.pokemon_list[0].src)
        self.assertIsNotNone(game.pokemon_list[0].dest)
        self.assertEqual(game.pokemon_list[0].src, 9)
        self.assertEqual(game.pokemon_list[0].dest, 8)

    def pokemon_edge_test(self):
        game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())
        self.assertEqual(game.pokemon_list[0].src, None)
        self.assertEqual(game.pokemon_list[0].dest, None)
        game.refresh_game(client.get_pokemons(), client.get_agents())
        self.assertEqual(game.pokemon_list[0].src, 9)
        self.assertEqual(game.pokemon_list[0].dest, 8)

    def agent2pokemon(self):
        game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())
        game.refresh_game(client.get_pokemons(), client.get_agents())
        self.assertEqual([0, 10, 9, 8], game.agent2pokemon(1))

