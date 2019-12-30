def break_words(stuff):
    # this string with the """ is called a documentation string
    """This function will break up words for us."""
    # separate words at the spaces
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    # sorted() is an existing python function; returns values in ascending or descending; must be strings OR numberic
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    # pop() removes and returns one word; parameter is optional but defaults to -1 (last item)
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# run inside of python in the terminal
# import ex25 OR from ex25 import * --> this way I don't have to preface each fx with 'ex25.'
