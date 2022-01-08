"""This is the Main Class"""
from client import Client
from GUI import GUI
from GameFunc import Game
import subprocess
subprocess.Popen(['powershell.exe', f'java -jar Ex4_Server_v0.0.jar {1}'])


def main():
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

    # initializing the Gui
    gui = GUI(game, client)

    # the main while loop: The game will run while the 'is_running' function remains true:
    while client.is_running() == 'true':
        game.play(client)
        print(game.pokemon_list)
        gui.draw()
        print(client.move())
        print(client.get_info())


if __name__ == '__main__':
    main()
