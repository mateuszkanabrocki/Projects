# import sleep to show output for some time period 
from time import sleep 

# import system to run any shell cmdlet
from os import system

# import platform to get an OS name
import platform

# import webbrowser to open URL
import webbrowser

# import exit to quit the function
from sys import exit

# True if user hasn't visited any room yet
# first_choice = True



# clear IDLE window
def clear():
    
    # for Windows
    if system_name == "Windows":
        system('cls')

    # for Mac and Linux
    else: 
        system('clear') 

# open URL
def open_URL():

    # open URLs in default browser
    webbrowser.open(strURL_bu, new=1)
    sleep(3*time)
    webbrowser.open(strURL_sense_fear, new=1)
    sleep(3*time)

# begin the conversation
def game_instroduction():

    # start a conversion
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
    sleep(time)

    # open URLs in default browser
    open_URL()
    
    clear()
    print("Didn't mean to scare you.")
    sleep(3*time)
    print("It's a peaceful game. Hope you'll enjoy it.\n")
    sleep(3*time)
    print("Imagine you're in a dark room with 3 doors.\n")
    sleep(2*time)

# main game function
def main_game():

    # ask for a door number
    door_picked = pick_the_door()
    # ask whether to knock the door or not
    knock = ask_to_knock()

    # user wants to knock the door
    if knock == True:
        # knock the door
        knock_the_door(door_picked)

    # user want don't want to knock the door
    elif knock == False:
        # open the door
        open_the_door(door_picked)

    else:
        print("main_game knock value error")
        exit()

# ask a user for a door number
def pick_the_door():

    print("Which door do you choose?")
    
    # OUT OF USE
    # if it's a first room to visit
    #if first_choice == True:
        #sleep(time)
        #print("WAIT!")
        #sleep(time)
        #print("Pick wisely...\n> ")
        #sleep(time)

    try:
        # if user gave a number
        door_picked = int(input())
        
        # if user picked no. 1, 2 or 3
        if door_picked in range(1, 4):
            clear()
            print("Ok.")
            sleep(time)
            clear()

            # return picked door number
            return door_picked

        else:
            # if user picked another number
            clear()
            print("Give me a number: 1, 2 or 3.")

            # run a function again and take the return value
            door_picked = pick_the_door()

            # return pick door number
            return door_picked

    except:
            # if user didn't give a number
            clear()
            print("Give me a number: 1, 2 or 3.")

            # run a function again and take the return value
            door_picked = pick_the_door()

            # return picked door number
            return door_picked

# ask whether to knock the door or not
def ask_to_knock():

    # get user answer
    knock_decision = input("Do you want to knock the door or open it right away?\n> ")

    # convert user answer into words list - tulip    
    knock_decision_list = knock_decision.split(" ")

    # user want to knock
    if 'knock' in knock_decision_list or 'Knock' in knock_decision_list:
        # save user decision
        knock = True

    # user want to open
    elif 'open' in knock_decision_list or 'Open' in knock_decision_list:
        # save user decision
        knock = False

        print("So rude...")
        sleep(2*time)
        clear()

    # other answer
    else:
        # run the function again
        knock = ask_to_knock()

    # return user decision
    return knock

# knock the door
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

    # open the door
    open_the_door(door_picked)

# open the picked door
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
        print("KotLecik!")
        sleep(3*time)
        print("\nThe cat is too busy.")
        
    elif door_picked == 2:
        clear()
        print("Wchodzisz do drugiego pokoju.")
        sleep(time)
        print("Jesteś na VI Miedzyregionalnych Zawodach Jeździeckich.")
        sleep(2*time)
        print("W Cieszynie.\n")
        sleep(2*time)
        print("Następna konkurencja to wyścig z przekodami.")
        sleep(1*time)
        print("W konkurencji bierze udział ślepy koń, który udziela wywiadu tuż przed rozpoczęciem wyścigiem.")
        sleep(4*time)

        input("\nCo mówi ślepy koń na wyścigach z przeszkodami?\n> ")

        sleep(1*time)
        clear()
        sleep(2*time)
        print("Nie widzę przeszkód.")
        sleep(3*time)

    elif door_picked == 3:
        clear()
        print("Wchodzisz do trzeciego pokoju.")
        sleep(2*time)
        print("Nie wiem gdzie jesteś.")
        sleep(2*time)
        print("Przed sobą widzisz złomiarza ciągnącego za sobą worek z puszkami.")
        sleep(2*time)
        print("Za złomiarzem podąża jego pies.")
        sleep(4*time)

        input("\nJak nazywa się pies złomiarza?\n> ")

        sleep(1*time)
        clear()
        sleep(1*time)
        print("Puszek.")
        sleep(3*time)

    else:
        print("open_the_door error")
        exit()

    print("\n(If you don't know Polish. Just so you know, this part was realy funny.)")
    sleep(4*time)
    clear()

    print("\nYou have to leave the room now.")
    sleep(4*time)
    clear()

    # OUT OF USE
    # ask whether to to visit another room or leave
    #enter_or_leave()

    # take user answer
    decision = input("Do you want to visit another room? You can quit the game - just type 'leave'\n> ")

    # if user wants to leave the game
    if 'leave' in decision or 'Leave' in decision:
        clear()
        print("Hope you enjoyed the game\n")
        print("Have a nice day! :)\n")
        # leave the game
        exit()

    else:
        # play again 
        main_game()

# OUT OF USE
# # ask whether to to visit another room or leave 
def enter_or_leave():

    # take user answer
    decision = input("\nDo you want to visit another room? You can quit the game - just type 'leave'\n> ")

    # if user wants to leave the game
    if 'leave' in decision or 'Leave' in decision:
        clear()
        print("Have a nice day :)\n")
        # leave the game
        exit()

    else:
        # play again 
        main_game()



# get an OS name
system_name = platform.system()

# assign URLs to be opened
strURL_bu = "https://drive.google.com/file/d/1dae-FJTJnbZ_xQmmsFFRUh5kZUalkFqc/view?usp=sharing"
strURL_sense_fear = "https://drive.google.com/file/d/1xkDTRZA3Fsm1gGJVFFlNfFq_851aKQlh/view?usp=sharing"

# define a time increment [seconds]
# set to 0 for the faster debugging
time = 1

# start the conversation with a user
game_instroduction()

# start the main game
main_game()

