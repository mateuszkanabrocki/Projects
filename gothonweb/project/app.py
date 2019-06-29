# app.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
A simple web browser text adventure game called gothonweb.
This is the engine module, which defines the following:

Functions:

- `load_session(username: str) -> None:` load user data from a text file
- `save_session(username: str, game: str, death_count: str, win_count: str, room_name: str) -> None:`
   save user's data to a text file
- `game():` main game engine function - game login
- `index():` return 'logged in' or 'ot logged in' html template
- `login():` return html template for login
- `logout():` return logout html template
- `nextgame():` save user session and start the same game again
- `score():` check the user's score
- `choose_a_game():` return html template for choosing a game
- `change_a_game():` change game into the chosen one

How To Use This Module
======================
(See the individual classes, methods, attributes and functions for details.)

Run this module in the default directory configuration then open http://127.0.0.1:5000/
in you web browser to start the game.
"""

__docformat__ = "restructuredtext"

import os
import sys
from os.path import exists
from shutil import copyfile
from typing import List

import lexis
import planisphere
from flask import Flask, redirect, render_template, request, session, url_for

this_module = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_module, "../gothonweb/"))

app = Flask(__name__)


def load_session(username: str) -> None:
    """Load user data from a text file.

    If it's a new user - set default game name, score data and make
    a next file in sessions/ to store them.
    If the user already exists - read the information the stored.
    Then set the collected data to session directory.

    :param username: name of the user
    :type username: str

    :returns: None
    """

    # if it's not a new user - a game name is set
    if session.get("game"):
        pass
    else:
        # set a game name
        session["game"] = "gothonweb"
    file_path = os.path.dirname(__file__)
    game_name = session.get("game")
    path_end = f"sessions/{username}_{game_name}.txt"
    session_path = os.path.join(file_path, path_end)

    # create a user's session file
    if not exists(session_path):
        with open(session_path, "w") as file:
            file.write("death_count = 0\nwin_count = 0\nroom_name = start_place")
    # load data from a user's session file to the session
    with open(session_path, "r") as file:
        session["death_count"] = int(file.readline().strip().strip("death_count = "))
        session["win_count"] = int(file.readline().strip().strip("win_count = "))
        session["room_name"] = file.readline().strip().replace("room_name = ", "")


def save_session(
    username: str, game: str, death_count: str, win_count: str, room_name: str
) -> None:
    """Save user's data to a text file.

    Save user session data into user .txt file (overwrite).
    If you change a game and there is no user .txt file for this game
    save_session run load_session(session['username']) to create a new user file.

    :param username: name of the user
    :type username: str
    :param game: name of the game
    :type game: str   
    :param death_count: user death score in the game
    :type death_count: str   
    :param win_count: user win score in the game
    :type win_count: str   
    :param room_name: current user scene name of the game
    :type room_name: str

    :returns: None
    """

    # read the session file data
    try:
        with open(
            os.path.join(os.path.dirname(__file__), f"sessions/{username}_{game}.txt"),
            "r",
        ) as file:
            line_list = []  # type: List[str]
            line_list.append(f"death_count = {death_count}\n")
            line_list.append(f"win_count = {win_count}\n")
            line_list.append(f"room_name = {room_name}")
            new_lines = "".join(line_list)
        # overwrite a session file
        with open(
            os.path.join(os.path.dirname(__file__), f"sessions/{username}_{game}.txt"),
            "w",
        ) as file:
            file.write(new_lines)
    # if the game was changed and there is no user file for the new game
    except:
        load_session(session["username"])


@app.route("/")
def index():
    """Return 'logged in' or 'ot logged in' html template.

    Return 'logged in' html template if user is logged in displaying username.
    Return 'not logged in' html template for not logged in users.
    Logged in user can log out or continue the game.
    Not logged in user can log in.
    """

    # if it's not a new user
    if "username" in session:
        username = session["username"]
        load_session(username)
        return render_template("logged_in.html", username=username)
    else:
        return render_template("not_logged_in.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Return html template for login."""

    if request.method == "POST":
        session["username"] = request.form["username"]
        return redirect(url_for("index"))
    return render_template("log_in.html")


@app.route("/logout")
def logout():
    """Return logout html template.
  
    There is a login key displayed.
    """

    session.clear()
    return redirect(url_for("index"))


@app.route("/nextgame")
def nextgame():
    """Save user session and start the same game again.

    Save user win and death counts, set current scene to start scene and run index().
    """

    # assign the session[room_name] start value
    save_session(
        session["username"],
        session["game"],
        session["death_count"],
        session["win_count"],
        "start_place",
    )
    return redirect(url_for("index"))


@app.route("/score")
def score():
    """Check the user's score.

    Read user's win count, death counts, current room name
    and current game from ther session data and display
    the data on the score html template.
    """

    death_count = session["death_count"]
    win_count = session["win_count"]
    game = session["game"]
    room = room = planisphere.load_room(session["room_name"])
    return render_template(
        "score.html", death_count=death_count, win_count=win_count, room=room, game=game
    )


@app.route("/choose_a_game")
def choose_a_game():
    """Return html template for choosing a game.

    Display log out key and back to the game key.
    Display available game names.
    """

    return render_template("choose_a_game.html")


@app.route("/change_a_game", methods=["GET", "POST"])
def change_a_game():
    """Change game into the chosen one.

    Copy new game modules to the current game modules.
    Set session data.
    If the game name is not recognized (there is no game
    modules found) redirect to choose_a_game().
    """

    # load a map(planisphere)
    game_name = request.form.get("game_name")
    session["game"] = game_name

    game_file_name = f"planisphere_{game_name}.py"
    game_file_name = game_file_name.replace(" ", "")

    lexis_file_name = f"lexis_{game_name}.py"
    lexis_file_name = lexis_file_name.replace(" ", "")

    # files paths
    new_planisphere_path = os.path.join(os.path.dirname(__file__), game_file_name)
    planisphere_path = os.path.join(os.path.dirname(__file__), "planisphere.py")
    new_lexis_path = os.path.join(os.path.dirname(__file__), lexis_file_name)
    lexis_path = os.path.join(os.path.dirname(__file__), "lexis.py")

    try:
        copyfile(new_planisphere_path, planisphere_path)
        copyfile(new_lexis_path, lexis_path)
    except:
        return render_template("choose_a_game.html")

    session["room_name"] = "start_place"
    room = planisphere.load_room(session["room_name"])
    return render_template("changed_a_game.html", room=room)


@app.route("/game", methods=["GET", "POST"])
def game():
    """Main game engine function - game login.

    Display scenes' descriptions and collect user's actions.
    """

    room_name = session.get("room_name")
    # by default, the Flask route responds to the GET requests
    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(session["room_name"])
            # if user failed
            if room.name in "Death":
                session["death_count"] += 1
            # if user won
            elif room.name in "Happy Ending":
                session["win_count"] += 1
            return render_template("show_room.html", room=room)
        # if user starts from '/game' instead of from '/'and has no account
        else:
            return render_template("you_died.html")
    else:
        action = request.form.get("action")
        if session["room_name"] and action:
            room = planisphere.load_room(session["room_name"])
            # get next room
            next_room = room.go(action)
            if not next_room:
                try:
                    action = lexis.parse_sentence(lexis.scan(action))
                    next_room = room.go(action)
                except:
                    pass
            if not next_room:
                # save current room name
                session["room_name"] = planisphere.name_room(room)
            else:
                # save next room name
                session["room_name"] = planisphere.name_room(next_room)

        save_session(
            session["username"],
            session["game"],
            session["death_count"],
            session["win_count"],
            session["room_name"],
        )

        return redirect(url_for("game"))


app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

# module is run directly (not imported)
if __name__ == "__main__":
    # only for development server - for changing a game functionality
    app.run(debug=True)
