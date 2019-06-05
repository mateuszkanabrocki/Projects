# dance_party_scenerio.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
A simple text adventure game called dance party game.
This is the scenerio module, containing all game data run by engine module:

Classes:

- `Scene`, scene superclass
- `GameIntro`, scene subclass, first scene
- `Waiting`, scene subclass, waiting for a dance
- `AskToDance`, scene subclass, asking to dance
- `StartToDance`, scene subclass, starting to dance
- `JustDance`, scene subclass, dancing
- `LastScene`, scene subclass, last scene
- `GameOver`, scene subclass, the end of the game
- `Scenerio`, scenerio superclass
- `ZoukScenerio`, scenerio subclass, map names to scene subclasses, run next scenes

How To Use This Module
======================
(See the individual classes, methods, attributes and functions for details.)

This module is intended to be run only by dance_party_game.py module.
"""

__docformat__ = 'restructuredtext'

from textwrap import dedent
import random
from os import system
# freeze program execusion for specified time
from time import sleep
# get an OS name
import platform
from typing import Optional


class Scene(object):

    """
    This class is a superclass for all scene classes discribing game scenes.

    The object can be initialized with no given parameters.

    Attributes
    ----------
    time: int
        a time variable for sleep function

    Methods
    -------
    def clear(self) -> None
        clear standard output
    run(self) -> Optional[str]
        retun default string 'no room'
    """

    def __init__(self) -> None:
        """Initialize a `Scene` object."""

        # set a time variable for sleep function
        self.time = 1

    # clear IDLE window
    def clear(self) -> None:
        """Clear standard output."""

        # for Windows
        if platform.system() == "Windows":
            system('cls')
        # for Mac and Linux
        else:
            system('clear')

    def run(self) -> Optional[str]:
        """Retun default string 'no room'"""

        return 'no room'


class GameIntro(Scene):

    """
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

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
                    Today you are Jeff. Recently you've started attending
                    dancing class, brazilian zouk classes more precisely .
                    (it's a dance in couples like salsa or tango)

                    You were always scared of dancing. That's why you
                    started attending these classes. You're doing pretty
                    fine but you're still a little a bit shy when
                    it's a bout dancing in the party.

                    Finally, your friend encouraged you to go to one.

                    Damn, you're scared like a little mouse!
                    """), end="")

        sleep(3*self.time)
        print(dedent("""
                    But here you are in Pick&Roll Club latino party
                    saturday night! It's 11 p.m.. There is stil only
                    a few people around.
                    That's good. The less the better, right?

                    You hear the song rhytm going like:
                    buuum  cik cik...
                    buuum  cik cik...
                    """))

        return 'waiting'


class Waiting(Scene):

    """
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        wait_number = 0

        while wait_number < 3:
            wait = input("\nWanna wait for the next song?\n(yes/no)\n> ")
            self.clear()

            if 'yes' in wait:
                print("\nLet's wait. Waiting is cool.\n")
                sleep(3*self.time)
                wait_number += 1
                print(random.choice([
                                    "This song is pretty fast.",
                                    "Ahh, it's Kizomba...",
                                    "Ahh, it's Bachata...",
                                    "Ahh, it's Salsa...",
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
                    You've been waiting so long for the better song
                    that finally some girl asked you to dance.

                    """))

        sleep(5*self.time)
        return 'start_to_dance'


class AskToDance(Scene):

    """
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

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
                    Ok. Finally you've found enough courage to get yourself
                    on the dance floor. Good for you!

                    Your eyes found a girl at the bar waiting for the dance.
                    You are slowly walking in her direction. She starts to look
                    at you too.

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

                for i in range(len(said_list)):
                    print(random.choice([
                        (f"buuum {said_list[i]}!"),
                        (f"cik {said_list[i]}!")
                                        ]), end="")
                print("\n(The music is too loud!)\n")
                sleep(5*self.time)

            elif answer == 'b':
                sleep(2*self.time)
                self.clear()
                print(dedent("""
                            You've been looking at her so long
                            she got scared and run.

                            Happens...
                            Let's wait for another song then.
                            """))
                sleep(1*self.time)

                return 'waiting'

            elif answer == 'c':
                sleep(1*self.time)
                self.clear()
                print("You are safe now.\n")
                sleep(1*self.time)
                return 'waiting'
            elif answer == 'd':
                self.clear()
                return 'start_to_dance'
            else:
                pass


class StartToDance(Scene):

    """
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

    Methods
    -------
    def run(self) -> str
        run the scene logic and return the name of the next scene
    """

    def run(self) -> str:
        """Run the scene logic and return the name of the next scene."""

        try:
            while True:
                for i in range(1, 5):
                    self.clear()
                    print(dedent(f"""
                                Ok. Here we are on the dance floor.
                                Now, just to start in rhythm.

                                Music is quite fast.

                                Try to move on 1.

                                {i}
                                (press 'Ctrl + C' to move)
                                """))

                    sleep(1*self.time)

        except KeyboardInterrupt:
            self.clear()
            print(f"You moved on {i}!")

            if i != 1:
                print("Not the best start...\n", end="")
            else:
                print("Great job!")

        return 'just_dance'


class JustDance(Scene):

    """
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

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
                    Ok, the steps.
                    I need to dance some other steps now.

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
                watch the dance floor and lead the steps."""))
        sleep(2*self.time)
        self.just_dancing()

        while True:
            self.clear()
            to_do = input(dedent("""
                                Oh no! While doing a turn girl's hair
                                tungled around my neck!
                                I can't breath!

                                What should I do now?

                                a) turn her again
                                b) turn myself closkwise
                                c) turn myself counterclockwise

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
                          "It's getting worse!")
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
                                One couple is moving very fast towards us.
                                They can't see us!

                                What should I do now?

                                a) step in the their way to block them and
                                    rescue the girl you're dancing with
                                b) jump to the left!

                                (type a or b)
                                """))
            if to_do == 'a':
                print(dedent("""
                            You step in the couple's way.
                            They hit you like a tornado,
                            but you're girl is safe!

                            That hurt."""))
                sleep(3*self.time)
                return 'last_scene'

            elif to_do == 'b':
                print(dedent("""
                            You jump to the left like lion!
                            You avoided the dangerous couple
                            but youbumped into another one.")

                            That hurt."""))
                sleep(3*self.time)
                return 'last_scene'


class LastScene(Scene):

    """
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

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
    This class is a subclass of scene class and was the main
    logic for one of the game scene.

    The object can be initialized with no given parameters.

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
    game scene classes.

    Method next_scene is used to get a new scene name.

    The object can be initialized with no given parameters.

    Methods
    -------
    def next_scene(self) -> Optional[str]
        return next scene name
    """

    # assign scenes to strings
    scenerio = {
        'game_intro': GameIntro(),
        'waiting': Waiting(),
        'ask_to_dance': AskToDance(),
        'start_to_dance': StartToDance(),
        'just_dance': JustDance(),
        'last_scene': LastScene(),
        'game_over': GameOver()
    }

    # run next scene, return following scene name
    def next_scene(self) -> Optional[str]:
        """Return next scene name."""

        try:
            self.current_scene_name = ZoukScenerio.scenerio.get(self.current_scene_name).run()
            return self.current_scene_name
        except:
            raise Exception("There is no next scene.")