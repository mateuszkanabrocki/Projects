# -*- coding: utf-8 -*-

# in case o 'unicode error':
# export PYTHONIOENCODING=UTF-8


# freeze program for specified time
from time import sleep
# run shell cmdlet
from os import system
# get an OS name
import platform
# open URL in browser
import webbrowser
# quit the function
from sys import exit


# clear IDLE window
def clear():
    # for Windows
    if system_name == "Windows":
        system('cls')

    # for Mac and Linux
    else:
        system('clear')

def open_URL():
    # open URL in default browser
    #webbrowser.open(strURL_bu, new=1)
    #sleep(3*time)
    webbrowser.open(strURL_sense_fear, new=1)
    sleep(3*time)

def begin_a_game():
    clear()
    input(f"Hi there {system_name} user.\n> ")
    sleep(time)
    clear()

    print("Nice to see you.")
    print("Welcome to this simple text adventure game.\n")
    sleep(2*time)

    ready = input("Are you ready?\n> ")
    sleep(time)

    # user is ready to play
    if 'yes' in ready or 'Yes' in ready:
        clear()
        sleep(time)
    # user is not ready to play
    elif 'no' in ready or 'No' in ready:
        print("Take your time.")
        sleep(5*time)
        print("Ok. The time is over.")
        sleep(time)
        clear()
    else:
        print("Hm, I take it for yes.")
        sleep(2*time)
        clear()

    print("Let's play a game...")
    sleep(2*time)
    clear()

    for i in range(3, 0, -1):
        print(f"Let's play a game.\n{i}...")
        sleep(time)
        clear()

    print("Bu.")
    sleep(2*time)
    open_URL()

    clear()
    print("Didn't mean to scare you.")
    sleep(3*time)
    print("It's a peaceful game. Hope you'll enjoy it.\n")
    sleep(3*time)
    print("Imagine you're in a dark room with 3 doors.\n")
    sleep(2*time)

def main_game():
    # ask for a door number
    door_picked = pick_the_door()

    # ask whether to knock or not
    knock = ask_to_knock()

    # user wants to knock
    if knock:
        knock_the_door(door_picked)

    # user want don't want to knock
    else:
        open_the_door(door_picked)

# ask a user for a door number
def pick_the_door():
    global first_choice
    clear()
    print("Which door do you choose?\n> ")

    if first_choice:
        sleep(time/2)
        print("WAIT!")
        sleep(time)
        print("Pick wisely...\n> ", end="")
        sleep(time)
        first_choice = False

    bad_pick = True
    while(bad_pick):
        try:
            door_picked = int(input())
            if door_picked in range(1, 4):
                bad_pick = False
        except ValueError:
            print("Give me number 1, 2 or 3:\n> ")

    return door_picked

# ask whether to knock the door or not
def ask_to_knock():
    knock = None
    while knock is None:
        # get user answer
        knock_decision = input(
            ' Do you want to knock or open it right away?\n> '
        )
        knock_decision_list = knock_decision.split(" ")

        knock_list = ('knock', 'Knock', 'yes')
        open_list = ('open', 'Open')
        
        for i in knock_list:
            # user want to knock
            if i in knock_decision_list:
                knock = True
                break
        for i in open_list:
            # user wants to open
            if i in knock_decision_list:
                knock = False
                print("So rude...")
                sleep(2*time)
                clear()
                break

        return knock

def knock_the_door(door_picked):
    # knock-knock joke
    clear()
    print("> Knock, knock\n> ", end="")
    sleep(2*time)
    answer_first = input("Who's there?\n> ")
    sleep(2*time)
    input(f"> {answer_first} who?\n> ")
    sleep(1*time)
    print("\nHaha\nGood one!\nYou can enter the door.")
    sleep(4*time)

    open_the_door(door_picked)

def open_the_door(door_picked):
    clear()
    print("(Unfortunately. This part will be covered in Polish.)")
    sleep(4*time)
    clear()

    if door_picked == 1:
        clear()
        print("Wchodzisz do pierwszego pokoju.")
        sleep(time)
        print("W pokoju widzisz kota,  który leci w Twoim kierunku.")
        sleep(2*time)

        input("Jak nazywa się ten kot?\n> ")
        sleep(1*time)
        clear()
        sleep(2*time)
        print("Kotlecik!")
        sleep(3*time)
        print("\nThe cat is too busy.")

    elif door_picked == 2:
        clear()
        print("Wchodzisz do drugiego pokoju.")
        sleep(time)
        print(u"Jesteś na VI Miedzyregionalnych Zawodach Jeździeckich.")
        sleep(2*time)
        print("W Cieszynie.\n")
        sleep(2*time)
        print(u"Następna konkurencja to wyścig z przekodami.")
        sleep(1*time)
        print(
            u"W konkurencji bierze udział ślepy koń, ",
            u"który udziela wywiadu tuż przed rozpoczęciem wyścigiem."
        )
        sleep(4*time)

        input(u"\nCo mówi ślepy koń na wyścigach z przeszkodami?\n> ")
        sleep(1*time)
        clear()
        sleep(2*time)
        print(u"Nie widzę przeszkód!")
        sleep(3*time)

    elif door_picked == 3:
        clear()
        print("Wchodzisz do trzeciego pokoju.")
        sleep(2*time)
        print(u"Nie wiem gdzie jesteś.")
        sleep(2*time)
        print(
            u"Przed sobą widzisz złomiarza ",
            u"ciągnącego za sobą worek z puszkami."
        )
        sleep(2*time)
        print(u"Za złomiarzem podąża jego pies.")
        sleep(4*time)

        input(u"\nJak nazywa się pies złomiarza?\n> ")
        sleep(1*time)
        clear()
        sleep(1*time)
        print("Puszek.")
        sleep(3*time)

    print(
        "\n(If you don't know Polish. Just so you know, "
        "this part was realy funny.)"
    )
    sleep(4*time)
    clear()

    print("\nYou have to leave the room now.")
    sleep(4*time)
    clear()

    decision = input(
        "Do you want to visit another room?\n"
        "You can quit the game - just type 'leave'\n> "
    )

    if 'leave' in decision or 'Leave' in decision:
        clear()
        print("Hope you enjoyed the game\n")
        print("Have a nice day! :)\n")
        exit()
    else:
        # play again
        main_game()

# get an OS name
system_name = platform.system()

try:
    print('załółć gęślą jaźń')
    clear()
except UnicodeEncodeError:
    clear()
    print("To run the game set default encoding to UTF-8"
          "by typing the following in the command line:\n"
          "export PYTHONIOENCODING=UTF-8")
    exit()


# assign URLs to be opened
#strURL_bu = "https://drive.google.com/file/d/1dae-FJTJnbZ_xQmmsFFRUh5kZUalkFqc/view?usp=sharing"
strURL_sense_fear = "https://drive.google.com/file/d/1xkDTRZA3Fsm1gGJVFFlNfFq_851aKQlh/view?usp=sharing"

# define a time increment [seconds]
# set to 0 for the faster debugging
time = 1

first_choice = True

begin_a_game()

main_game()
