#lexis 3rooms
from planisphere_gothonweb import direction, do, stop, noun
from typing import List, Tuple, Union, Optional

def scan(sentence: str) -> List[Tuple[str, Union[str, int]]]:
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


# take ('noun','princess') and 'noun' pop and return ('noun','princess')
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
    while peek(word_list) == word_type:
        match(word_list, word_type)
    return word_list

# word_list: List[Tuple[str, Union[str, int]]] throw an error - shouldn't
def parse_do(word_list): 
    # skip stop marks, numbers and again stop marks
    # in case there is a stop mark following the number
    skip(word_list, 'stop')
    skip(word_list, 'number')
    skip(word_list, 'stop')
    skip(word_list, 'error')

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
    do = parse_do(word_list)
    obj = parse_object(word_list)

    if obj is None:
        sentence_parsed = f'{do[1]}'
        return sentence_parsed
    else:
        sentence_parsed = f'{do[1]} {obj[1]}'
        return sentence_parsed
