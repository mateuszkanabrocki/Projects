from sys import exit

from textwrap import dedent

import random

from os import system

# freeze program execusion for specified time
from time import sleep

# get an OS name
import platform



class Engine(object):

    #def __init__(self, scenerio):

        #self.scenerio = scenerio

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


class Scene(object):

    def __init__(self):
        self.time = 1

    # clear IDLE window
    def clear(self):

        # for Windows
        if platform.system() == "Windows":
            system('cls')

        # for Mac and Linux
        else:
            system('clear')


class Game_intro(Scene):

    def run(self):
        
        self.clear()
        print(dedent("""
            WARNING!!!
            This game is not for people with weak nerves...
            """))

        sleep(3*self.time)
        self.clear()
        print(dedent("""
                    Today you are Jeff. Recently you've started attending
                    dancing class, more precisely brazilian zouk classes.
                    (it's a dance in a couple like salsa or tango)

                    You've always had a fear of dancing. That's why you
                    started to take these classes. You're doing pretty 
                    well but you're still a little afraid of dancing at
                    the regular latino dance party.

                    Finally, your friend encouraged you to visit one.
                    Damn, you're scared like a scared mouse!
                    """), end="")

        sleep(4*self.time)
        print(dedent("""
                    But here you are in Pick&Roll Club latino party saturday night!
                    It's 11 p.m.. There is stil only a few people around.
                    That's good. The less the better, right.

                    You here the song rhytm going like:
                    buuum  cik cik...
                    buuum  cik cik...
                    """))

        return 'waiting'


class Waiting(Scene):

    def run(self):

        for wait_number in range(4):
            # self.clear()
            print(random.choice([
                "This song is pretty fast.",
                "Ahh, it's Kizomba...",
                "Ahh, it's Bachata...",
                "Ahh, it's Salsa...",
                "I don't know this song.",
                "I don't like this song.",
                "This song is really slow."
            ]))
            wait = input("\nWanna wait for the next song?\n(yes/no)\n> ")
            self.clear()

            if 'yes' in wait:    
                print("\nLet's wait than, waiting is cool.\n")
                sleep(5*self.time)
                wait_number += 1

            elif 'no' in wait:
                return 'ask_to_dance'

            else: # use it like this or not?
                pass

        self.clear()
        print(dedent("""You've been waiting so long for the better song
                    that finally some girl asked you to dance.\n
                    """))

        return 'start_to_dance'
        

class Ask_to_dance(Scene):
    
    def run(self):

        while True:
            self.clear()
            answer = input((dedent("""
                    Ok. Finally you've found enough courage to get yourself
                    on the dance floor. Good for you!

                    Your eyes found a girl at the bar waiting for the dance.
                    You are slowly going in her direction. She start to look
                    at you too.

                    What do you do next?

                        a) say something to her
                        b) just keep looking at her
                        c) turn back and run for your life!
                        d) smile and show her your hand
                    
                    (type a,b,c or d)
                    > 
                    """)))

            if answer is 'a':
                said = input("Say something to her:\n> ")
                self.clear()
                said_list = said.split()

                for i in range(len(said_list)):
                    print(random.choice([(f"buuum {said_list[i]}!"), (f"cik {said_list[i]}!")]), end="")

                print("\n(The music is too loud!)\n")
                sleep(5*self.time)

            elif answer is 'b':
                sleep(2*self.time)
                self.clear()
                print(dedent("""
                            You've been looking at her so long she got scared and run.

                            Happens...
                            Let's wait for another song then.
                            """))
                sleep(1*self.time)

                return 'waiting'

            elif answer is 'c':
                sleep(1*self.time)
                self.clear()
                print("You are safe now.")
                sleep(1*self.time)

                return 'waiting'

            elif answer is 'd':
                self.clear()
                return 'start_to_dance'

            else:
                pass


class Start_to_dance(Scene):

     def run(self):

        print(dedent(f"""
                        Ok. Here we are on the dance floor.
                        Now, just to start in rhythm.

                        Music is quite fast.
                        """))
        sleep(2*self.time)
        self.clear()

        try:
            while True:
                for i in range(1, 5):
                    print(dedent(f"""
                                Ok. Here we are on the dance floor.
                                Now, just to start in rhythm.

                                Music is quite fast.

                                Try to move on 1.

                                {i}
                                (press 'Ctrl + C' to move)
                                """))

                    sleep(1*self.time)
                    self.clear()

        except KeyboardInterrupt:
            print(f"You moved on {i}!")

            if i != 1:
                print("No the best start...\n")

            else:
                print("Great job!\n")

        return 'just_dance'


class Just_dance(Scene):

    def run(self):
        print("So you enter the just_dance scene.")
        print("You do something.")
        print("And finaly the object returns the name of the next room.")

        return 'last_scene'
        #return 'game_over'


class Last_scene(Scene):

    def run(self):
        print("So you enter the last_scene.")
        print("You do something.")
        print("And finaly the object returns the name of the next room.")

        exit()


class Game_over(Scene):

    def run(self):
        print("So you enter the game_over scene.")
        print("You do something.")
        print("And finaly the object returns the name of the next room.")

        exit()


class Scenerio(object):

    def __init__(self, first_scene_name):
        self.current_scene_name = first_scene_name


class Zouk_scenerio(Scenerio):

    # assign strings to scenes
    scenerio = {
        'game_intro': Game_intro(),
        'waiting': Waiting(),
        'ask_to_dance': Ask_to_dance(),
        'start_to_dance': Start_to_dance(),
        'just_dance': Just_dance(),
        'last_scene': Last_scene(),
        'game_over': Game_over()
    }

    # run next scene, return following scene name
    def next_scene(self):
        self.current_scene_name = Zouk_scenerio.scenerio.get(self.current_scene_name).run()
        return self.current_scene_name

# create a zouk_scenerio object
zouk_scenerio = Zouk_scenerio('game_intro')
# create this game engine object
#zouk_engine = Engine(zouk_scenerio)
zouk_engine = Engine()
# change so you get a name and the Scenerio class is imported from other file
zouk_engine.download(zouk_scenerio)
# run the game
zouk_engine.play()