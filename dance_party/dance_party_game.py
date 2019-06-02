from sys import exit
from dance_party_scenerio import ZoukScenerio


class Engine(object):

    # download a scenerio and scenes
    def download(self, scenerio: ZoukScenerio) -> None:
        self.scenerio = scenerio

    # play a game
    def play(self) -> None:
        next_game_name = None

        while next_game_name not in ('game_over', 'last_scene'):
            next_game_name = self.scenerio.next_scene()

        self.scenerio.next_scene()
        exit()

    # run next scene
    def next_scene(self) -> None:
        pass


# create a ZoukScenerio object with default scene object
zouk_scenerio = ZoukScenerio('game_intro')
# create a game engine object
zouk_engine = Engine()
# change so you get a name and the Scenerio class is imported from other file
zouk_engine.download(zouk_scenerio)
# run the game
zouk_engine.play()
