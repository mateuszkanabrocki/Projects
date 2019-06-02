# statemachine.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
A simple web browser text adventure game called gothonweb.
This is the engine module, which defines the following:

Functions:

- `load_session(username: str) -> None:` load user data from a text file
- `save_session(username: str, game: str, death_count: str, win_count: str, room_name: str) -> None:`
   save user data to a text file
- `game():` main game engine function
- `index():` return 'logged in' or 'not logged in' html template
- `login():` log in
- `logout():` log out
- `nextgame():` save user session and start the game again
- `score():` check the user score
- `choose_a_game():` choose a game
- `change_a_game():` change current game


How To Use This Module
======================
(See the individual classes, methods, and attributes for details.)

1. Import it: ``import statemachine`` or ``from statemachine import ...``.
   You will also need to ``import re``.

2. Derive a subclass of `State` (or `StateWS`) for each state in your state
   machine::

       class MyState(statemachine.State):

   Within the state's class definition:

   a) Include a pattern for each transition, in `State.patterns`::

          patterns = {'atransition': r'pattern', ...}

   b) Include a list of initial transitions to be set up automatically, in
      `State.initial_transitions`::

          initial_transitions = ['atransition', ...]

   c) Define a method for each transition, with the same name as the
      transition pattern::

          def atransition(self, match, context, next_state):
              # do something
              result = [...]  # a list
              return context, next_state, result
              # context, next_state may be altered

      Transition methods may raise an `EOFError` to cut processing short.

   d) You may wish to override the `State.bof()` and/or `State.eof()` implicit
      transition methods, which handle the beginning- and end-of-file.

   e) In order to handle nested processing, you may wish to override the
      attributes `State.nested_sm` and/or `State.nested_sm_kwargs`.

      If you are using `StateWS` as a base class, in order to handle nested
      indented blocks, you may wish to:

      - override the attributes `StateWS.indent_sm`,
        `StateWS.indent_sm_kwargs`, `StateWS.known_indent_sm`, and/or
        `StateWS.known_indent_sm_kwargs`;
      - override the `StateWS.blank()` method; and/or
      - override or extend the `StateWS.indent()`, `StateWS.known_indent()`,
        and/or `StateWS.firstknown_indent()` methods.

3. Create a state machine object::

       sm = StateMachine(state_classes=[MyState, ...],
                         initial_state='MyState')

4. Obtain the input text, which needs to be converted into a tab-free list of
   one-line strings. For example, to read text from a file called
   'inputfile'::

       input_string = open('inputfile').read()
       input_lines = statemachine.string2lines(input_string)

5. Run the state machine on the input text and collect the results, a list::

       results = sm.run(input_lines)

6. Remove any lingering circular references::

       sm.unlink()
"""















import sys
import os
from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from flask import make_response
from os.path import exists
from shutil import copyfile

this_module = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_module, '../gothonweb/'))

import planisphere
import lexis


app = Flask(__name__)


def load_session(username: str) -> None:
    # if it's not a new user - a game name is set
    if session.get('game'):
        pass
    else:
        # set a game name
        session['game'] = 'gothonweb'
    file_path = os.path.dirname(__file__)
    game_name = session.get('game')
    path_end = f"sessions/{username}_{game_name}.txt"
    session_path = os.path.join(file_path, path_end)
    
    # create a user's session file
    if not exists(session_path):
        with open(session_path, "w") as file:
            file.write('death_count = 0\nwin_count = 0\nroom_name = start_place')
    # load data from a user's session file to the session
    with open(session_path, "r") as file:
        session['death_count'] = int(file.readline().strip().strip('death_count = '))
        session['win_count'] = int(file.readline().strip().strip('win_count = '))
        session['room_name'] = file.readline().strip().replace('room_name = ', '')

def save_session(username: str, game: str, death_count: str, win_count: str, room_name: str) -> None:
    # read the session file data
    try:
        with open(os.path.join(os.path.dirname(__file__), f"sessions/{username}_{game}.txt"), "r") as file:
            line_list = [file.readline(), file.readline(), file.readline()]
            line_list[0] = f"death_count = {death_count}\n"
            line_list[1] = f"win_count = {win_count}\n"
            line_list[2] = f"room_name = {room_name}"
            new_lines = ''.join(line_list)
        # overwrite a session file
        with open(os.path.join(os.path.dirname(__file__), f"sessions/{username}_{game}.txt"), "w") as file:
            file.write(new_lines)
    # if it's a new user
    except:
        load_session(session['username'])

@app.route("/")
def index():
    # if it's not a new user
    if 'username' in session:
        username = session['username']
        load_session(username)
        return render_template("logged_in.html", username=username)
    return render_template("not_logged_in.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("log_in.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/nextgame')
def nextgame():
    # assign the session[room_name] start value
    save_session(session['username'], session['game'], session['death_count'],
                 session['win_count'], 'start_place')
    return redirect(url_for('index'))


@app.route('/score')
def score():
    death_count = session['death_count']
    win_count = session['win_count']
    game = session['game']
    room = room = planisphere.load_room(session['room_name'])
    return render_template("score.html", death_count=death_count,
                           win_count=win_count, room=room, game=game)


@app.route('/choose_a_game')
def choose_a_game():
    return render_template("choose_a_game.html")


@app.route('/change_a_game', methods=['GET', 'POST'])
def change_a_game():
    # load a map(planisphere)
    game_name = request.form.get('game_name')
    session['game'] = game_name

    game_file_name = f"planisphere_{game_name}.py"
    game_file_name = game_file_name.replace(" ", "")

    lexis_file_name = f"lexis_{game_name}.py"
    lexis_file_name = lexis_file_name.replace(" ", "")
    
    # files paths
    new_planisphere_path = os.path.join(os.path.dirname(__file__), game_file_name)
    planisphere_path = os.path.join(os.path.dirname(__file__), 'planisphere.py')
    new_lexis_path = os.path.join(os.path.dirname(__file__), lexis_file_name)
    lexis_path = os.path.join(os.path.dirname(__file__), 'lexis.py')

    try:
        copyfile(new_planisphere_path, planisphere_path)
        copyfile(new_lexis_path, lexis_path)
    except:
        return render_template("choose_a_game.html")

    session['room_name'] = 'start_place'
    room = planisphere.load_room(session['room_name'])
    return render_template("changed_a_game.html", room=room)


@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    # by default, the Flask route responds to the GET requests
    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(session['room_name'])
            # if user failed
            if room.name in 'Death':
                session['death_count'] += 1
            # if user won
            elif room.name in 'Happy Ending':
                session['win_count'] += 1
            return render_template("show_room.html", room=room)
        # if user starts from '/game' instead of from '/'and has no account
        else:
            return render_template("you_died.html")
    else:
        action = request.form.get('action')
        if session['room_name'] and action:
            room = planisphere.load_room(session['room_name'])
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
                session['room_name'] = planisphere.name_room(room)
            else:
                # save next room name
                session['room_name'] = planisphere.name_room(next_room)

        save_session(session['username'], session['game'],
                     session['death_count'], session['win_count'],
                     session['room_name'])

        return redirect(url_for("game"))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# module is run directly (not imported)
if __name__ == "__main__":
    # only for development server - for changing a game functionality
    app.run(debug=True)
