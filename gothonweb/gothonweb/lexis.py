#lexis gothonweb
from planisphere_gothonweb import direction, do, stop, noun
from random import randint
from app import session
from typing import List, Tuple, Union, Optional

def scan(sentence: str) -> Union[str, List[Tuple[str, Union[str, int]]]]:
    if session.get('room_name') == 'laser_weapon_armory':
        try:
            type_code = int(sentence)
            right_code = randint(1, 3)
            if type_code == right_code:
                return 'right_code'
            else:
                return 'wrong_code'
        except:
            pass
    elif session.get('room_name') == 'escape_pod':
        try:
            type_pod = int(sentence)
            right_pod = randint(1, 2)
            if type_pod == right_pod:
                return 'right_pod'
            else:
                return 'wrong_pod'
        except:
            pass
    else:
        pass

    sentence_cleaned = sentence.strip()
    for i in '.,;:?!':
        sentence_cleaned = sentence_cleaned.replace(i, '')
    words_lowercase = sentence_cleaned.lower().split()
    words = sentence_cleaned.split()

    union_str_int = Union[str, int] # can't do List[Tuple[str, Union[str, int]]
    lexicon = [] # type: List[Tuple[str, union_str_int]]

    adress = -1
    for i in words_lowercase:
        adress += 1
        if i in direction:
            lexicon.append(('direction', i))
        elif i in do:
            lexicon.append(('do', i))
        elif i in stop:
            lexicon.append(('stop', i))
        elif i in noun:
            lexicon.append(('noun', i))
        else:
            try:
                lexicon.append(('number', int(i)))
            except ValueError:
                lexicon.append(('error', words[adress]))
    return lexicon


# take ('noun','princess') return 'noun'
def peek(word_list: List[Tuple[str, Union[str, int]]]) -> Optional[str]:
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


# take ('noun','princess') and 'noun' return and pop ('noun','princess')
def match(word_list: List[Tuple[str, Union[str, int]]], expecting: str) -> Optional[Tuple[str, Union[str, int]]]:
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list: List[Tuple[str, Union[str, int]]], word_type: str) -> List[Tuple[str, Union[str, int]]]:
    # if next word is of the given word type
    while peek(word_list) == word_type:
        match(word_list, word_type)
    return word_list

# word_list: List[Tuple[str, Union[str, int]]] throw an error - shouldn't
def parse_do(word_list):
    # Skip stop marks, numbers and again stop marks
    # in case there is a stop mark following the number.
    skip(word_list, 'stop')
    skip(word_list, 'number')
    skip(word_list, 'stop')
    skip(word_list, 'error')
    skip(word_list, 'noun')
    if peek(word_list) == 'do':
        return match(word_list, 'do')

# word_list: List[Tuple[str, Union[str, int]]] throw an error - shouldn't
def parse_object(word_list):
    skip(word_list, 'stop')
    skip(word_list, 'number')
    skip(word_list, 'error')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')


def parse_sentence(word_list: Union[str, List[Tuple[str, Union[str, int]]]]): # -> str: gives an error
    # see scan function (session.get('room_name') == 'laser_weapon_armory')
    if type(word_list) is str:
        return word_list
    else:
        do = parse_do(word_list)
        obj = parse_object(word_list)

        if obj is None:
            sentence_parsed = f'{do[1]}'
        else:
            sentence_parsed = f'{do[1]} {obj[1]}'
        return sentence_parsed
