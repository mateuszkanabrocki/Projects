# dance_party_scenerio.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
A simple text adventure game called dance party game.
This is the scenerio module, containing all game data run by engine module:

Classes:

- `Scene`, superclass for scenes
- `GameIntro`, Scene subclass, first scene
- `Waiting`, Scene subclass, waiting for a dance scene
- `AskToDance`, Scene subclass, asking to dance scene
- `StartToDance`, Scene subclass, starting to dance scene
- `JustDance`, Scene subclass, dancing scene
- `LastScene`, Scene subclass, last scene scene
- `GameOver`, Scene subclass, the end of the game scene
- `Scenerio`, superclass for scenerios
- `ZoukScenerio`, Scenerio subclass, map names to scene objects
   and run next scenes

How To Use This Module
======================
(See the individual classes, methods, attributes and functions for details.)

This module is intended to be run only by the dance_party_game.py module.
"""

__docformat__ = 'restructuredtext'

from textwrap import dedent
import random
from os import system
from time import sleep  # freeze program execusion for specified time
import platform  # get an OS type name
from typing import Optional


class Scene(object):

    """
    This class is a superclass for all scene objects.

    The object can be initialized with no given parameters.

    Attributes
    ----------
    time: int
        time variable for sleep function

    Methods
    -------
    def clear(self) -> None
        clear standard output
    run(self) -> Optional[str]
        return 'no room'
    """

    def __init__(self) -> None:
        """Initialize a `Scene` object."""

        # set a time variable for a sleep function
        self.time = 1

    # clear terminal output
    def clear(self) -> None:
        """Clear standard output."""

        # for Windows
        if platform.system() == "Windows":
            system('cls')
        # for Mac and Linux
        else:
            system('clear')

    def run(self) -> Optional[str]:
        """Return 'no room'."""

        return 'no room'


class GameIntro(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        self.clear()
        print(dedent("""
            WARNING!!!
            This game is not for the people with weak nerves...
            """))
        sleep(2*self.time)
        self.clear()
        print(dedent("""
                    You are Jeff. Recently you've started attending
                    dancing class. More precisely brazilian zouk classes.
                    (you dance it in couple like salsa or tango)

                    You were always afraid of dancing. That's why you
                    started attending learn how to dance. You're doing
                    pretty well but you're still a little bit shy when
                    it comes dancing at the party.

                    Finally, your friend encouraged you to go to
                    your first one.
                    """), end="")
        sleep(3*self.time)
        print(dedent("""
                    So here you are in the Pick&Roll Club latino party
                    saturday night! Saturday night! It's 11 p.m.
                    There is still only a few people on the dance floor.

                    You can hear the song beat:
                    buuum  cik cik...
                    buuum  cik cik...
                    """))
        return 'waiting'


class Waiting(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        wait_number = 0
        while wait_number < 3:
            wait = input("\nDo you want to wait for the next song?\n(yes/no)\n> ")
            self.clear()
            if 'yes' in wait:
                print("\nLet's wait. Waiting is cool.\n")
                sleep(3*self.time)
                wait_number += 1
                print(random.choice([
                                    "This song is pretty fast.",
                                    "It's Kizomba...",
                                    "It's Bachata...",
                                    "It's Salsa...",
                                    "I don't know this song.",
                                    "I don't like this song.",
                                    "This song is really slow."
                                    ]))
            elif 'no' in wait:
                return 'ask_to_dance'
            else:
                pass
        self.clear()
        print(dedent("""
                    You've been hesitating for a long time now.
                    Finally some girl grabs your hand
                    and drag you on the dance floor.
                    """))
        sleep(5*self.time)
        return 'start_to_dance'


class AskToDance(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        while True:
            self.clear()
            answer = input((dedent("""
                    Ok. Finally you decide to ask for a dance. Good for you!

                    Your eyes catch a girl sitting at the bar.
                    You are slowly walking in her direction.
                    She catches your sight.

                    What do you do next?

                        a) say something to her
                        b) just keep looking at her
                        c) turn back and run for your life!
                        d) smile and show her your hand

                    (type a, b, c or d)
                    > 
                                """)))
            if answer == 'a':
                said = input("Say something to her:\n> ")
                self.clear()
                said_list = said.split()

                for word in said_list:
                    print(random.choice([
                        (f"buuum {word}!"),
                        (f"cik {word}!")
                                        ]), end="")
                print("\n(The music is too loud!)\nIt's hard to hear anything.\n")
                sleep(5*self.time)
            elif answer == 'b':
                sleep(2*self.time)
                self.clear()
                print(dedent("""
                            You've been looking at her for over 5 minutes
                            she got scared and run out of the club.

                            Well...
                            Let's wait for another song.
                            """))
                sleep(1*self.time)
                return 'waiting'
            elif answer == 'c':
                sleep(1*self.time)
                self.clear()
                print("You are safe now!\n")
                sleep(1*self.time)
                return 'waiting'
            elif answer == 'd':
                self.clear()
                return 'start_to_dance'
            else:
                pass


class StartToDance(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        try:
            while True:
                for i in range(4):
                    self.clear()
                    print(dedent(f"""
                                Ok. Here you are on the dance floor.
                                Now, listen to the song and to start on 1.
                                Music is quite fast.

                                {i}
                                (Press 'Ctrl + C' to make a first step.)
                                """))
                    sleep(1*self.time)
        except KeyboardInterrupt:
            self.clear()
            print(f"You moved on {i}!")
            if i != 1:
                print("It wasn't the best way to start a dance...\n", end="")
            else:
                print("In time! Great job!")
        return 'just_dance'


class JustDance(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def just_dancing(self) -> None:
        """Run the dancing part of the game."""

        moves = {
            'a': "Going into laterall!",
            'b': "Now a little bit of crusado...",
            'c': "And a bumerang!\n",
            'd': "Taking some breath while leading boneca.",
            'e': "This song is too fast for roasted chicken!\nI don't wanna die!"
                }

        print(dedent("""
                    Ok, remember the steps.
                    I can't dance basic step all the time.

                    What should I dance now?

                    a) laterall
                    b) cruasado
                    c) bumerang
                    d) boneca
                    e) roasted chicken

                    (type a, b, c, d or e)
                    """))
        i = 0
        while i < 5:
            steps = input()
            if steps in moves.keys():
                print(moves.get(steps))
                i += 1
            else:
                pass

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        print(dedent("""
                Ok. Here we go. Just keep the rhythm, listen to the music,
                and watch the dance floor."""))
        sleep(2*self.time)
        self.just_dancing()
        while True:
            self.clear()
            to_do = input(dedent("""
                                Oh no! While leading a turn girl's hair
                                tungled around your neck!
                                You can't breath!

                                What should You do now?

                                a) turn her again
                                b) turn yourself closkwise
                                c) turn yourself counterclockwise

                                (type a, b, or c)
                                """))
            worse = None
            if to_do == 'a':
                self.clear()
                print("You fainted.\nNice try though!")
                return 'game_over'
            elif to_do == 'b':
                if worse is None:
                    print("\nOh no! Not in this direction!",
                          "It's getting even worse!")
                    sleep(4*self.time)
                    worse = True
                else:
                    self.clear()
                    print("You fainted./n Nice try though!")
                    return 'game_over'
            elif to_do == 'c':
                self.clear()
                print("You are rescued!")
                sleep(2*self.time)
                break
            else:
                pass

        self.just_dancing()

        while True:
            self.clear()
            to_do = input(dedent("""
                                Watch out!
                                One couple is moving very fast towards you
                                and they can't see you!

                                What should you do now?

                                a) step in their way to rescue
                                   rescue the girl you're dancing with!
                                b) jump to the left!

                                (type a or b)
                                """))
            if to_do == 'a':
                print(dedent("""
                            You step in the couple's way.
                            They hit you like a tornado,
                            but the girl you're dancing with is safe!
                            """))
                sleep(3*self.time)
                return 'last_scene'
            elif to_do == 'b':
                print(dedent("""
                            You jump to the left like a monkey!
                            You avoid the dangerous couple
                            but you bump into another one."
                            """))
                sleep(3*self.time)
                return 'last_scene'


class LastScene(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> None:
        print(dedent("""
                    You did it! The song finished and you're alive!
                    Good job!
                    """))


class GameOver(Scene):

    """
    This class is a Scene subclass and has a part fo the game logic
    for one of the game scene.

    No need to initialized an object.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> None:
        """Run the scene logic and return the name of the next scene."""

        print("\nIt could be better. But at least you tried!")


class Scenerio(object):

    """
    This class is a scenerio superclass.

    The object can be initialized with no given parameters.
    """

    def __init__(self, first_scene_name: str) -> None:
        """Initialize the Scenerio object with given first scene name.

         Parameters:

        - `first_scene_nameo`: str, the name of the first game
           scene - mapped to the first Scene subclass
        """

        self.current_scene_name = first_scene_name


class ZoukScenerio(Scenerio):

    """
    This class is a scenerio subclass mapping game names with
    the game scene classes.

    Method next_scene is used to get a new scene name.

    The object can be initialized with no given parameters.

    Methods
    -------
    def next_scene(self) -> Optional[str]
        return next scene name
    """

    scenerio = {
        'game_intro': GameIntro(),
        'waiting': Waiting(),
        'ask_to_dance': AskToDance(),
        'start_to_dance': StartToDance(),
        'just_dance': JustDance(),
        'last_scene': LastScene(),
        'game_over': GameOver()
    }

    def next_scene(self) -> Optional[str]:
        """Return next scene name."""

        if self.current_scene_name is not None:
            try:
                # ignore mypy error as it's a 'try' block
                self.current_scene_name = ZoukScenerio.scenerio.get(self.current_scene_name).run() 
                return self.current_scene_name
            except AttributeError:
                raise Exception("There is no next scene.")
            return None
        else:
            raise Exception('No current scene.')
