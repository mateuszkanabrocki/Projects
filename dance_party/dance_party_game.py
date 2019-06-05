# dance_party_game.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
A simple text adventure game called dance party game.
This is the engine module, which defines the following:

Classes:

- `Engine`, download game scenerio module and scenes from scenerio module.

How To Use This Module
======================
(See the individual classes, methods, attributes and functions for details.)

Run this module in the default project directory configuration.
"""

__docformat__ = 'restructuredtext'

from sys import exit
from dance_party_scenerio import ZoukScenerio


class Engine(object):

    """
    This class represents a game engine.

    The object can be initialized with no given parameters.

    Attributes
    ----------
    scenerio: class Scenerio
        class containing all game data run by engine

    Methods
    -------
    def download(self, scenerio: ZoukScenerio) -> None
        download game scenerio data from the scenerio module
    play(self) -> None
        run the game
    """

    # download a scenerio and scenes
    def download(self, scenerio: ZoukScenerio) -> None:
        """Download game scenerio data from the scenerio module.

         Parameters:

        - `scenerio`: class Scenerio, class containing all game data run by engine
        """

        self.scenerio = scenerio

    # play a game
    def play(self) -> None:
        """Run the game."""

        next_game_name = None

        while next_game_name not in ('game_over', 'last_scene'):
            next_game_name = self.scenerio.next_scene()

        self.scenerio.next_scene()
        exit()


# create a ZoukScenerio object with default scene object
zouk_scenerio = ZoukScenerio('game_intro')
# create a game engine object
zouk_engine = Engine()
# change so you get a name and the Scenerio class is imported from other file
zouk_engine.download(zouk_scenerio)
# run the game
zouk_engine.play()
