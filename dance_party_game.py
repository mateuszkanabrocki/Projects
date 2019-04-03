from sys import exit

import dance_party_scenerio


class Engine(object):

    # download a scenerio and scenes
    def download(self, scenerio):

        self.scenerio = scenerio

    # play a game
    def play(self):

        next_game_name = None

        while next_game_name not in ('game_over', 'last_scene'):
            next_game_name = self.scenerio.next_scene()

        self.scenerio.next_scene()
        exit()

    # run next scene
    def next_scene(self):
        pass


# create a zouk_scenerio object
zouk_scenerio = dance_party_scenerio.Zouk_scenerio('game_intro')
# create this game engine object
zouk_engine = Engine()
# change so you get a name and the Scenerio class is imported from other file
zouk_engine.download(zouk_scenerio)
# run the game
zouk_engine.play()
