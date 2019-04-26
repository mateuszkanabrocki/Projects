from textwrap import dedent

import random

from os import system

# freeze program execusion for specified time
from time import sleep

# get an OS name
import platform


class GameEngine(object):

    def __init__(self, map_of_locations):
        self.map_of_locations = map_of_locations

    def play(self):

        # begin with a starting location
        current_place = self.map_of_locations.first_place()
        next_place_name = current_place.enter()

        while next_place_name != 'finished':
            current_place = self.map_of_locations.next_place(next_place_name)
            next_place_name = current_place.enter()

        exit(0)


class Place(object):

    # clear IDLE window
    def clear(self):

        # for Windows
        if platform.system() == "Windows":
            system('cls')

        # for Mac and Linux
        else:
            system('clear')


class Rome(Place):

    def enter(self):

        self.clear()
        print(dedent("""
        It's 1963. We're in Roma, the city of ancient gods!
        Today also in the world sport center.
        These are the last days of the Olimpics Games
        and we're about to begin the hide and seek final competition."""))
        sleep(2 * time)
        print(dedent("""
        We have two hide-seekers who made their way to the final.
        As a hiker: Bob McBobber from Englang.
        As a seeker: Jeff Jefftyjeff from USA,
        which is in America."""))
        sleep(2 * time)
        print("(start to count from 10 to 0)")

        number = 10
        while number > -1:
            count = input(">  ")

            if count != str(number):
                print(dedent("""
                Oh no! Jeff didn't practise his counting!
                Now he has to start again!"""))
                sleep(1 * time)
                print("(start to count from 10 to 0)")
                number = 10

            else:
                number -= 1

        self.clear()
        print("\nJeff: Ready or not, here I come!\n")
        sleep(2 * time)
        print("Jeff finished counting!\nWhat a speed!", end=" ")
        print("But Bob is already gone!\n")
        sleep(2 * time)

        answer = input("What will Jeff do?\n('look around' / 'fly to Paris')\n> ")
        decided = False

        while not decided:

            if 'look around' in answer:
                decided = True
                self.clear()
                print(dedent("""
                Jeff spent 2 years 65 days 34 minutes and 21 seconds
                looking for Bob in Rome. Then decided to fly to Paris and look Bob there
                as he knew Bob has a family there."""))
                sleep(2 * time)

            elif 'fly to Paris' in answer:
                self.clear()
                decided = True

            else:
                self.clear()
                answer = input("What will Jeff do?\n('look around' / 'fly to Paris')\n> ")

        return 'Paris'


class Paris(Place):

    def enter(self):

        print(dedent("""
        Paris is a big city.
        Jeff has been looking for Bob for 7 years 54 days 5 hours
        14 minutes and 2 seconds.
        He could't find him anywhere."""))
        sleep(2 * time)
        print(dedent("""
        Jeff started getting tired so he decided to take a break
        and have a drink at the nearest bar."""))
        sleep(2 * time)
        print("But then he saw some shadow moving behind the tree...\n")
        sleep(2 * time)

        answer = input("Was it Bob?!\n(yes/no)\n> ")
        decided = False

        while not decided:

            if 'yes' in answer:
                decided = True
                self.clear()
                print(dedent("""
                Jeff pointed his finger at the tree
                and shouted: Bob behind the tree!
                """))
                sleep(2 * time)
                print("It was just a wind!\nAh, so close...")
                sleep(3 * time)

            elif 'no' in answer:
                decided = True

            else:
                self.clear()
                answer = input("Was it Bob?!\n(yes/no)\n> ")

        return 'Cafe'


class Cafe(Place):

    def enter(self):

        print("\nSomebody run into Cafe.")
        sleep(2 * time)
        print(dedent("""
        Jeff looked and the door. A smile appeared on his face
        He slowly entered the bar."""))
        sleep(2 * time)
        print(dedent("""
        It was a dark and a crowded place. Great to hide.
        Yes! Bob must be somewhere here."""))
        sleep(2 * time)

        places_to_hide = ['kitchen', 'downstairs', 'behind the bar']
        bob_hide = random.choice(places_to_hide)
        answer = input("Where is he hiding?\n(kitchen / downstairs / behind the bar)\n> ")
        found = False

        while not found:

            if 'kitchen' in answer:
                self.clear()
                print("Jeff: Bob in a kitchen!")
                sleep(2 * time)

                if bob_hide == 'kitchen':
                    break

                else:
                    print("There is no Bob in a kitchen!")
                    sleep(2 * time)
                    answer = input("\nWhere is he?\n(kitchen / downstairs / behind the bar)\n> ")

            elif 'downstairs' in answer:
                self.clear()
                print("Jeff: Bob downstairs!")
                sleep(2 * time)

                if bob_hide == 'downstairs':
                    break

                else:
                    print("There is no Bob downstairs!")
                    sleep(2 * time)
                    answer = input("\nWhere is he?\n(kitchen / downstairs / behind the bar)\n> ")

            elif 'behind the bar' in answer:
                self.clear()
                print("Jeff: Bob behind the bar!")
                sleep(2 * time)

                if bob_hide == 'behind the bar':
                    break

                else:
                    print("There is no Bob behind the bar!")
                    sleep(2 * time)
                    answer = input("\nWhere is he?\n(kitchen / downstairs / behind the bar)\n> ")

            else:
                self.clear()
                answer = input("\nWhere is he?\n(kitchen / downstairs / behind the bar)\n> ")

        self.clear()
        print(dedent("""
        You found Bob!
        You broke the world record in hide and seek
        by 3 years 5 days 2 hours 30 minutes and 3 seconds!
        Great job Jeff!
        """))

        return 'finished'


class Map(object):

    locations = {
        'Rome': Rome(),
        'Paris': Paris(),
        'Cafe': Cafe(),
    }

    def __init__(self, starting_point):
        self.starting_point = starting_point

    # run first location
    def first_place(self):
        return self.next_place(self.starting_point)

    # run next location
    def next_place(self, place_name):
        return Map.locations.get(place_name)


# time increment for sleep function
time = 1
# initiate location map for the game
map_of_locations = Map('Rome')
# initiate a game engine
game = GameEngine(map_of_locations)
# play a game
game.play()
