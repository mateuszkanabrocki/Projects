# planisphere_gothonweb.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
This is the gothonweb game data module for a simple web browser
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

__docformat__ = "restructuredtext"

import os
from typing import Any, Dict, Optional, Union

this_module = os.path.dirname(os.path.realpath(__file__))
planisphere_gothonweb_path = os.path.join(this_module, __file__)


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

    def go(
        self, direction: str
    ) -> Any:  # Union[Room, None] throw error "Room not defined"
        """Change scene by given direction (user action).

         Parameters:

        - `direction`: a string, a user's action
        """

        return self.paths.get(direction, None)

    def add_paths(
        self, paths: Any
    ) -> None:  # paths: Dict[str, Room] throw error Room not defined
        """Change paths attribute by appending a new 'path' - user's actions
        and it's results.

         Parameters:

        - `paths`: Dict[str, Room], connects user actions with scenes they result in
        """

        self.paths.update(paths)


start_place = Room(
    "Central Corridor",
    """
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory, put
it in the bridge, and blow the ship up after getting into an escape pod.

You're running down the central corridor to the Weapons Armory when a
Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown
costume flowing around his hate filled body.  He's blocking the door to
the Armory and about to pull a weapon to blast you.
""",
)


laser_weapon_armory = Room(
    "Laser Weapon Armory",
    """
Lucky for you they made you learn Gothon insults in the academy.  You
tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf
nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
not to laugh, then busts out laughing and can't move.  While he's
laughing you run up and shoot him square in the head putting him down,
then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room for
more Gothons that might be hiding.  It's dead quiet, too quiet.  You
stand up and run to the far side of the room and find the neutron bomb
in its container.  There's a keypad lock on the box and you need the
code to get the bomb out.  If you get the code wrong then the
lock closes forever and you can't get the bomb. 
The code is a 1 digit number from 1 to 3 (so you have any chance ;) ).
""",
)


the_bridge = Room(
    "The Bridge",
    """
The container clicks open and the seal breaks, letting gas out.  You
grab the neutron bomb and run as fast as you can to the bridge where you
must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb under your arm
and surprise 5 Gothons who are trying to take control of the ship.  Each
of them has an even uglier clown costume than the last.  They haven't
pulled their weapons out yet, as they see the active bomb under your arm
and don't want to set it off.
""",
)


escape_pod = Room(
    "Escape Pod",
    """
You point your blaster at the bomb under your arm and the Gothons put
their hands up and start to sweat.  You inch backward to the door, open
it, and then carefully place the bomb on the floor, pointing your
blaster at it.  You then jump back through the door, punch the close
button and blast the lock so the Gothons can't get out.  Now that the
bomb is placed you run to the escape pod to get off this tin can.

You rush through the ship desperately trying to make it to the escape
pod before the whole ship explodes.  It seems like hardly any Gothons
are on the ship, so your run is clear of interference.  You get to the
chamber with the escape pods, and now need to pick one to take.  Some of
them could be damaged but you don't have time to look.  There are 2 pods,
which one do you take?
""",
)


the_end_winner = Room(
    "Happy Ending",
    """
You jump into pod and hit the eject button.  The pod easily slides out
into space heading to the planet below.  As it flies to the planet, you
look back and see your ship implode then explode like a bright star,
taking out the Gothon ship at the same time.  You won!
""",
)


shoot = Room(
    "Death",
    """
Quick on the draw you yank out your blaster and fire
it at the Gothon.  His clown costume is flowing and
moving around his body, which throws off your aim.
Your laser hits his costume but misses him entirely.
This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage
and blast you repeatedly in the face until you are
dead.  Then he eats you.
""",
)


dodge = Room(
    "Death",
    """
Like a world class boxer you dodge, weave, slip and
slide right as the Gothon's blaster cranks a laser
past your head.  In the middle of your artful dodge
your foot slips and you bang your head on the metal
wall and pass out.  You wake up shortly after only to
die as the Gothon stomps on your head and eats you.
""",
)


wrong_code = Room(
    "Death",
    """
The lock buzzes one last time and then you hear a
sickening melting sound as the mechanism is fused
together.  You decide to sit there, and finally the
Gothons blow up the ship from their ship and you die.
""",
)


throw_the_bomb = Room(
    "Death",
    """
In a panic you throw the bomb at the group of Gothons
and make a leap for the door.  Right as you drop it a
Gothon shoots you right in the back killing you.  As
you die you see another Gothon frantically try to
disarm the bomb. You die knowing they will probably
blow up when it goes off.
""",
)


wrong_pod = Room(
    "Death",
    """
You jump into a random pod and hit the eject button.  The pod escapes
out into the void of space, then implodes as the hull ruptures, crushing
your body into jam jelly.
""",
)


class Map(object):

    """
    This class maps user actions with scenes this actions result in.

    The object is initialized with no parameters.

    Attributes
    ----------
    name : dictionary
        maps str actions with room objects
    """

    dict = {
        "shoot": shoot,
        "dodge": dodge,
        "tell a joke": laser_weapon_armory,
        "say joke": laser_weapon_armory,
        "right_code": the_bridge,
        "wrong_code": wrong_code,
        "throw the bomb": throw_the_bomb,
        "slowly place the bomb": escape_pod,
        "right_pod": the_end_winner,
        "wrong_pod": wrong_pod,
    }


start_place.add_paths(
    {
        "shoot": Map.dict["shoot"],
        "kill": Map.dict["shoot"],
        "dodge": Map.dict["dodge"],
        "hit": Map.dict["dodge"],
        "kick": Map.dict["dodge"],
        "tell joke": Map.dict["tell a joke"],
    }
)

laser_weapon_armory.add_paths(
    {
        "right_code": Map.dict["right_code"],  # a testing cheat word
        "wrong_code": Map.dict["wrong_code"],  # a testing cheat word
    }
)

the_bridge.add_paths(
    {
        "throw bomb": Map.dict["throw the bomb"],
        "place bomb": Map.dict["slowly place the bomb"],
        "leave bomb": Map.dict["slowly place the bomb"],
    }
)

escape_pod.add_paths(
    {
        "right_pod": Map.dict["right_pod"],  # a testing cheat word
        "wrong_pod": Map.dict["wrong_pod"],  # a testing cheat word
    }
)


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

    white_list = (
        "start_place",
        "laser_weapon_armory",
        "the_bridge",
        "escape_pod",
        "the_end_winner",
        "wrong_pod",
        "generic_death",
        "throw_the_bomb",
        "shoot",
        "dodge",
        "wrong_code",
    )

    if name in white_list:
        return globals().get(name)
    else:
        raise Exception(f"You can't run load_room with {name} as a parameter.")


def name_room(room: Room) -> Union[str, Exception]:
    """Return name of the given Room class object.

    The name of the given Room class object is returned if the name
    belongs to white_list list.

    If given object name do not belong to the white_list - > return Exception

    :param room: game scene
    :type room: class Room

    :returns: game scene name
    :rtype: str
    """

    white_list = (
        "start_place",
        "laser_weapon_armory",
        "the_bridge",
        "escape_pod",
        "the_end_winner",
        "wrong_pod",
        "generic_death",
        "throw_the_bomb",
        "shoot",
        "dodge",
        "wrong_code",
    )

    # give room object, get room name
    for key, value in globals().items():
        if value == room and key in white_list:
            return key
    raise Exception(f"You can't run name_room with {room} as a parameter.")
