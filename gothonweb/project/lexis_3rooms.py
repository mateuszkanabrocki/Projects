# lexis_3rooms.py 2019-06-01
# Author: Mateusz Kanabrocki <mateusz.kanabrocki@gmail.com>
# Copyright: This module has been placed in the public domain
# https://github.com/mateuszkanabrocki/projects

"""
This is the lexis module of 3rooms game for a simple web browser
text adventure game called gothonweb.
This module defines the following:

Functions:

- `scan(sentence: str) -> Union[str, List[Tuple[str, Union[str, int]]]]`
   take sentence and return list of tuples (type of word, word or number)
- `peek(word_list: List[Tuple[str, Union[str, int]]]) -> Optional[str]`
   take list of tuples (type of word, word or number) and return the type
   of the word in the first tuple from the list
- `match(word_list: List[Tuple[str, Union[str, int]]], expecting: str)
   -> Optional[Tuple[str, Union[str, int]]]`
   pop next tuple (type of word, word or number) and return it if type
   of the word is same as given
- `skip(word_list: List[Tuple[str, Union[str, int]]], word_type: str)
   -> List[Tuple[str, Union[str, int]]]`
   strip list of tuples (type of word, word or number) of tuples of
   deleting tuples with given type of word
- `parse_do(word_list)` return the name of the room
   object if the object exists
- `parse_do(word_list)`
   strip list of tuples and return first tuple
   with word of 'do' type
- `parse_object(word_list) -> Optional[Tuple[str, Union[str, int]]]`
   strip list of tuples and return first tuple with word of 'object' type
- `parse_sentence(word_list: Union[str, List[Tuple[str, Union[str, int]]]])`
   return verb or verb and object from given sentence

Variables:

- `do`, list of recognised verbs
- `stop`, list of recognised verbs marks to be skept by skip function


How To Use This Module
======================
(See the individual classes, methods, attributes and functions for details.)

This module is intended to by used only by the game engine module app.py.
"""

__docformat__ = "restructuredtext"

from typing import List, Optional, Tuple, Union

do = [
    "yes",
    "yeah",
    "sure",
    "ready",
    "go",
    "1",
    "one",
    "2",
    "two",
    "3",
    "three",
    "quit",
    "exit",
    "leave",
    "room",
]
stop = ["the", "in", "of", "from", "at", "it", "a", "him"]


def scan(sentence: str) -> List[Tuple[str, Union[str, int]]]:
    """Take sentence and return list of tuples (type of word, word or number).

    Available types of words:
    - do (verbs)
    - stop (words to be skept)
    - noun
    - number
    - error (not recognized)

    :param sentence: sentence given by the user as an action to be done
    :type sentence: str

    :returns: single words mapped to their types
    :rtype: List[Tuple[str, Union[str, int]]]

    :returns: specified words (see first lines of code)
     if session.get('room_name')== 'laser_weapon_armory' or 'escape_pod'
    :rtype: str
    """

    sentence_cleaned = sentence.strip()
    for i in ".,;:?!":
        sentence_cleaned = sentence_cleaned.replace(i, "")
    words_lowercase = sentence_cleaned.lower().split()
    words = sentence_cleaned.split()

    union_str_int = Union[str, int]  # can't do List[Tuple[str, Union[str, int]]
    lexicon = []  # type: List[Tuple[str, union_str_int]]

    adress = -1
    for i in words_lowercase:
        adress += 1
        if i in do:
            lexicon.append(("do", i))
        elif i in stop:
            lexicon.append(("stop", i))
        else:
            try:
                lexicon.append(("number", int(i)))
            except ValueError:
                lexicon.append(("error", words[adress]))
    return lexicon


# take ('noun','princess') return 'noun'
def peek(word_list: List[Tuple[str, Union[str, int]]]) -> Optional[str]:
    """Take list of tuples (type of word, word or number) and return
    the type of the word in the first tuple from the list.

    :param word_list: list of words mapped to their types
    :type word_list: List[Tuple[str, Union[str, int]]]

    :returns: type of the word from the first tuple from the list
    :rtype: str
    """

    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


# take ('noun','princess') and 'noun' pop and return ('noun','princess')
def match(
    word_list: List[Tuple[str, Union[str, int]]], expecting: str
) -> Optional[Tuple[str, Union[str, int]]]:
    """Pop next tuple (type of word, word or number) and return it
    if type of the word is same as given.

    :param word_list: list of words mapped to their types
    :type word_list: List[Tuple[str, Union[str, int]]]
    :param expecting: type of word to be matched
    :type expecting: str

    :returns: word mapped to it's type is the type is the same as given
    :rtype: Tuple[str, Union[str, int]]
    """

    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(
    word_list: List[Tuple[str, Union[str, int]]], word_type: str
) -> List[Tuple[str, Union[str, int]]]:
    """Strip list of tuples (type of word, word or number)
    of tuples deleting tuples with given type od word

    :param word_list: list of words mapped to their types
    :type word_list: List[Tuple[str, Union[str, int]]]
    :param word_type: type of word to be stripped from the lisr of words
    :type word_type: str

    :returns: list of words mapped to their types stripped of given word types
    :rtype: List[Tuple[str, Union[str, int]]]
    """

    while peek(word_list) == word_type:
        match(word_list, word_type)
    return word_list


# word_list: List[Tuple[str, Union[str, int]]] throw an error - shouldn't
def parse_do(word_list) -> Optional[Tuple[str, Union[str, int]]]:
    """Strip list of tuples deleting stop, number, error and noun types of words
    and return first tuple with word of 'do' type.

    :param word_list: list of words mapped to their types
    :type word_list: List[Tuple[str, Union[str, int]]]

    :returns: mapped word of 'do' type
    :rtype: Tuple[str, Union[str, int]]
    """

    # skip stop marks, numbers and again stop marks
    # in case there is a stop mark following the number
    skip(word_list, "stop")
    skip(word_list, "number")
    skip(word_list, "stop")
    skip(word_list, "error")

    if peek(word_list) == "do":
        return match(word_list, "do")
    else:
        return None


# word_list: List[Tuple[str, Union[str, int]]] throw an error - shouldn't
def parse_object(word_list) -> Optional[Tuple[str, Union[str, int]]]:
    """Strip list of tuples deleting stop, number, error and noun types of words
    and return first tuple with word of 'object' type.

    :param word_list: list of words mapped to their types
    :type word_list: List[Tuple[str, Union[str, int]]]

    :returns: mapped word of 'object' type
    :rtype: Tuple[str, Union[str, int]]
    """

    skip(word_list, "stop")
    skip(word_list, "number")
    skip(word_list, "error")
    next_word = peek(word_list)

    if next_word == "noun":
        return match(word_list, "noun")
    elif next_word == "direction":
        return match(word_list, "direction")
    else:
        return None


def parse_sentence(
    word_list: Union[str, List[Tuple[str, Union[str, int]]]]
):  # -> str: gives an error
    """Return verb or verb and object from given sentence.

    :param word_list: list of words mapped to their types (scanned sentence)
    :type word_list: List[Tuple[str, Union[str, int]]]

    :returns: verb or verb and object
    :rtype: str
    """

    do = parse_do(word_list)
    obj = parse_object(word_list)
    if do is not None:
        if obj is None:
            sentence_parsed = f"{do[1]}"
            return sentence_parsed
        else:
            sentence_parsed = f"{do[1]} {obj[1]}"
            return sentence_parsed
    else:
        return None
