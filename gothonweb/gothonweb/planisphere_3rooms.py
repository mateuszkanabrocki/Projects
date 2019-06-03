# planisphere_3rooms.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
This is the 3rooms game data module for a simple web browser
text adventure game called gothonweb.
This module defines the following:

Functions:

- `load_room(name: str) -> Optional[Any]:` return room object of given name
- `name_room(room: Room) -> Union[str, Exception]:` return the name of the room
   object if the object exists

Classes:

- `Room`, a single scene class
- `Map`, maps Room class objects with strings


How To Use This Module
======================
(See the individual classes, methods, attributes and functions for details.)

This module is intended to by used only by the game engine module app.py.
"""

__docformat__ = 'restructuredtext'

from typing import Dict, Union, Optional, Any


class Room(object):

    """
    This class represents a single scene of the text adventure game.

    The object is initialized by giving the name and the description.
    It may contain paths connecting user actions with other room objects
    as the results of user actions.

    Attributes
    ----------
    name : str
        the name of the scene
    description : str
        the description of the scene
    paths : Dict[str, Room]
        connects user actions with resulting scenes

    Methods
    -------
    go(self, direction: str) -> Any
        return scene by given direction/action
    add_paths(self, paths: Any) -> None
        change paths attribute by appending a new 'path'
    """
    def __init__(self, name: str, description: str) -> None:
        """
        Initialize a `Room` object

        Parameters:

        - `name`: a string, a name of the game scene
        - `description`: a string, the scene description
        """

        self.name = name
        """Name of the scene."""

        self.description = description
        """Description of the scene."""

        self.paths = {}  # type: Dict[str, Room]
        """Map user actions with room objects (scenes)."""

    def go(self, direction: str) -> Any:  # Union[Room, None] throw error "Room not defined"
        """Change scene by given direction (user action).

         Parameters:

        - `direction`: a string, a user's action
        """

        return self.paths.get(direction, None)

    def add_paths(self, paths: Any) -> None:  # paths: Dict[str, Room] throw error Room not defined
        """Change paths attribute by appending a new 'path' - user's actions
        and it's results.

         Parameters:

        - `paths`: Dict[str, Room], connects user actions with scenes they result in
        """

        self.paths.update(paths)


start_place = Room('Welcome!',
"""
Hi there. Welcome to this simple text adventure game.
Are you ready to play?
""")


door_pick = Room('Pick the door', 
"""
Imagine you're in a dark room with 3 doors.
Which door do you choose?

Pick wisely...
""")


door_1 = Room('Room no. 1', 
"""
(Unfortunately this part will be covered in Polish)

Wchodzisz do pierwszego pokoju.
W pokoju widzisz kota, który leci w Twoim kierunku.
Jak nazywa się ten kot?




...KotLecik!


Do you want to stay with a cat or exit the room?
""")


door_2 = Room('Room no. 2', 
"""
(Unfortunately this part will be covered in Polish)

Wchodzisz do drugiego pokoju.
Jesteś na VI Miedzyregionalnych Zawodach Jeździeckich
w Cieszynie.
Następna konkurencja to wyścig z przekodami.
W konkurencji bierze udział ślepy koń, który udziela
właśnie wywiadu tuż przed rozpoczęciem wyścigiem.

Co mówi ślepy koń na wyścigach z przeszkodami?





...Nie widzę przeszkód.


Do you want to stay here or exit the room?
""")


door_3 = Room('Room no. 3', 
"""
(Unfortunately this part will be covered in Polish)

Wchodzisz do trzeciego pokoju.
Przed sobą widzisz złomiarza ciągnącego
za sobą worek z puszkami.
Za złomiarzem podąża jego pies.

Jak nazywa się pies złomiarza?






...Puszek


Do you want to stay here or exit the room?
""")


next_pick = Room('Another pick?', 
"""
Do you want to visit another room
or leave the game?
""")


the_end = Room('Happy Ending', 
"""
Hope you enjoyed the game
Have a nice day!
""")


class Map(object):

    """
    This class maps user actions with scenes this actions result in.

    The object is initialized with no parameters.

    Attributes
    ----------
    name : dictionary
        maps str actions with room objects
    """

    dict = {'door_pick': door_pick,
            'door_1': door_1,
            'door_2': door_2,
            'door_3': door_3,
            'next_pick': next_pick,
            'the_end': the_end
           }

door_1.add_paths({
    'quit': Map.dict['next_pick'],
    'leave': Map.dict['next_pick'],
    'exit': Map.dict['next_pick']
})

door_2.add_paths({
    'quit': Map.dict['next_pick'],
    'leave': Map.dict['next_pick'],
    'exit': Map.dict['next_pick']
})

door_3.add_paths({
    'quit': Map.dict['next_pick'],
    'leave': Map.dict['next_pick'],
    'exit': Map.dict['next_pick']
})

next_pick.add_paths({
    'leave': Map.dict['the_end'],
    'yes': Map.dict['the_end'],
    'visit': Map.dict['door_pick'],
    'room': Map.dict['door_pick']
})

door_pick.add_paths({
    '1': Map.dict['door_1'],
    'one': Map.dict['door_1'],
    '2': Map.dict['door_2'],
    'two': Map.dict['door_2'],
    '3': Map.dict['door_3'],
    'three': Map.dict['door_3']
})

start_place.add_paths({
    'yes': Map.dict['door_pick'],
    'ready': Map.dict['door_pick'],
    'go': Map.dict['door_pick']
})


def load_room(name: str) -> Optional[Any]:
    """Return room object of given name.

    Object of given name is returned if the name is a part of
    a white_list list containing all room object possible to be used.

    If the object of given name doesn't exist or do not belong to
    the white_list - > return Exception

    :param name: name of the scene (room)
    :type name: str

    :returns: scene
    :rtype: class Room
    """

    white_list = ('start_place', 'door_pick', 'next_pick', 'door_3', 'door_2', 'door_1', 'the_end')
    if name not in white_list:
        raise Exception(f'You can\'t run load_room with {name} as a parameter.')
    return globals().get(name)


def name_room(room: Room) -> Union[str, Exception]:
    """Return name of the given Room class object.

    The name of the given Room class object is returned if the name
    belongs to white_list list.

    If given object name do not belong to the white_list - > return Exception

    :param room: game scene
    :type name: class Room

    :returns: game scene name
    :rtype: str
    """

    white_list = ('start_place', 'door_pick', 'next_pick', 'door_3', 'door_2', 'door_1', 'the_end')
    # give room object get room name
    for key, value in globals().items():
        if value == room and key in white_list:
            return key
    raise Exception(f'You can\'t run name_room with {room} as a parameter.')
