from unittest import TestCase
from Agent import*
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
game.initialize(client.get_pokemons(), client.get_agents(), client.get_graph())
game.refresh_game(client.get_pokemons(), client.get_agents())


class TestObjects(TestCase):
    def test_Agent(self):
        self.assertEqual(0, game.agent_dict.get(0).id)
        self.assertEqual(0.0, game.agent_dict.get(0).value)
        self.assertEqual(0, game.agent_dict.get(0).src)
        self.assertEqual(-1, game.agent_dict.get(0).dest)
        self.assertEqual(1.0, game.agent_dict.get(0).speed)
        self.assertEqual(35.18753053591606, game.agent_dict.get(0).pos[0])
        self.assertEqual(32.10378225882353, game.agent_dict.get(0).pos[1])
        self.assertEqual(0.0, game.agent_dict.get(0).pos[2])

    def test_Pokemon(self):
        self.assertEqual(5.0, game.pokemon_list[0].value)
        self.assertEqual(-1, game.pokemon_list[0].type)
        self.assertEqual(35.197656770719604, game.pokemon_list[0].pos[0])
        self.assertEqual(32.10191878639921, game.pokemon_list[0].pos[1])
        self.assertEqual(0.0, game.pokemon_list[0].pos[2])
        self.assertEqual(False, game.pokemon_list[0].marked)
        self.assertEqual(9, game.pokemon_list[0].src)
        self.assertEqual(8, game.pokemon_list[0].dest)


