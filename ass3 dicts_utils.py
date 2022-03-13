#Assignment 3: Simplified Scrabble
#Laurine Aldairy
#260886886
import doctest
import random

def count_occurrences(my_string):
    """
    (str) --> dict
    
    takes in string and returns dict mapping characters
    to integers, with the int being the number of
    occurrences of the character in the string
    removes spaces from dict if string contains space
    character
    
    >>> d = count_occurrences("banana")
    >>> d == {'b': 1, 'a': 3, 'n': 2}
    True
    >>> count_occurrences("")
    {}
    >>> d = count_occurrences("three trees")
    >>> d == {'t': 2, 'h': 1, 'r': 2, 'e': 4, 's': 1}
    True
    """
    #create dict with characters from string
    my_dict = dict.fromkeys(my_string, 0)
    #iterate through string to update values
    for character in my_string:
        my_dict[character] += 1
    #remove spaces from the dictionary
    if ' ' in my_dict:
        my_dict.pop(' ')
    return my_dict

def flatten_dict(my_dict):
    """
    (dict) --> list
    
    takes in dict mapping strings to non-negative
    integers, returns list containing the string integer
    number of times
    
    >>> flatten_dict({'cat': 2, 'dog': 0, 'bunny': 3})
    ['bunny', 'bunny', 'bunny', 'cat', 'cat']
    >>> d = count_occurrences("three trees")
    >>> flatten_dict(d)
    ['e', 'e', 'e', 'e', 'h', 'r', 'r', 's', 't', 't']
    >>> d = {'l': 2, 'z': 1, 'm': 4}
    >>> flatten_dict(d)
    ['l', 'l', 'm', 'm', 'm', 'm', 'z']
    """
    #create empty list
    flat_list = []
    #iterate through dict
    for key in my_dict:
        #don't append strings with value 0
        if my_dict[key] == 0:
            continue
        for i in range(my_dict[key]):
            flat_list.append(key)
    #sort list so it matches docstring
    flat_list.sort()
    
    return flat_list

def get_word_score(my_string, my_dict):
    """
    (str, dict) --> int
    
    takes in string and dict mapping characters to
    integers, and returns sum of characters in string
    according to dict -- if not in dict, character has
    value 0
    
    >>> v = {}
    >>> get_word_score('banana', v)
    0
    >>> v = count_occurrences("these trees")
    >>> get_word_score('three', v)
    12
    >>> get_word_score('straws', v)
    7
    """
    #create counter
    word_value = 0
    #iterate through string
    for character in my_string:
        #do nothing if not in dict
        if character not in my_dict:
            continue
        #add value of the character
        word_value += my_dict[character]
    return word_value

def is_subset(dict1, dict2):
    """
    (dict, dict) --> bool
    
    takes in two dicts mapping strings to ints and
    returns True if all keys in dict1 are in dict2 and
    all values of the keys in dict2 are greater than
    or equal to the values in dict1
    
    >>> a = {'a': 1, 'c': 5}
    >>> b = {'a': 4, 'b': 4, 'c': 4}
    >>> c = {'a': -2, 'b': 3}
    >>> is_subset(b, a)
    False
    >>> is_subset(a, c)
    False
    >>> is_subset(c, b)
    True
    >>> is_subset(c, c)
    True
    """
    #iterate through dict1
    for key in dict1:
        #check key in both dicts
        if key not in dict2:
            return False
        #check dict2 values >= dict1 values
        if dict1[key] > dict2[key]:
            return False
    return True

def subtract_dicts(d1, d2):
    """
    (dict, dict) --> bool
    
    takes in two dicts of nonneg integers, if d2 c d1,
    d1 updated by subracting values of d2, returns True.
    otherwise, returns False
    
    >>> a = {'a': 1, 'c': 5}
    >>> b = {'a': 4, 'b': 4, 'c': 4}
    >>> c = {'a': 2, 'b': 3}
    >>> subtract_dicts(a, b)
    False
    >>> subtract_dicts(b, c)
    True
    >>> b
    {'a': 2, 'b': 1, 'c': 4}
    >>> subtract_dicts(c, {})
    True
    >>> c == {'a': 2, 'b': 3}
    True
    """
    #check if d2 subset of d1
    if not is_subset(d2, d1):
        return False
    #iterate through d2
    for key in d2:
        d1[key] = d1[key] - d2[key]
        #check if the value is now 0
        if d1[key] == 0:
            del d1[key]
    return True

def dict_sum(my_dict):
    """
    (dict) --> int
    
    takes in dict mapping strings to ints and returns
    sum of ints
    
    >>> b = {'a': 2, 'e': 1, 'c': 1, 't': 2, 'q': 1, 'u': 0}
    >>> dict_sum(b)
    7
    >>> dict_sum({'r': 1, 'd': 4, 'c': 3, 't': 2})
    10
    >>> dict_sum({'z': 2, 'o': 0, 'e': 3, 't': -1})
    4
    """
    #create counter variable
    counter = 0
    #iterate through dictionary
    for key in my_dict:
        counter += my_dict[key]
    return counter

def word_list(character, length, string_list):
    """
    (str, int, list) --> list
    
    takes in character representing first letter,
    length representing length of string, and list of
    avaiable words, returns list of string of length
    length starting with character
    
    >>> b = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> word_list('u', 5, b)
    ['umami', 'uncle']
    >>> word_list('c', 3, b)
    ['cat', 'can', 'cow']
    >>> word_list('q', 4, b)
    []
    """
    #create empty list
    new_list = []
    #iterate through elements of list
    for word in string_list:
        if (word[0] == character) and (len(word) == length):
            new_list.append(word)
    return new_list

def create_scrabble_dict(string_list):
    """
    (list) --> 2D dict
    
    takes in list of strings and returns dict mapping
    ints to dicts of words of that length
    
    >>> b = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(b)
    >>> d == {2: {'a': ['aa'], 'q': ['qi'], 'z': ['za']}, 3: {'c': ['cat', 'can', 'cow'], 'd': ['dog', 'dad']}, 5: {'h': ['hippo'], 'u': ['umami', 'uncle']}}
    True
    >>> b = ['aftosas', 'haws', 'hear', 'jots', 'ki', 'kicked', 'nuncle', 'pearl', 'pi', 'sister', 'toph']
    >>> d = create_scrabble_dict(b)
    >>> d == {7: {'a': ['aftosas']}, 4: {'h': ['haws', 'hear'], 'j': ['jots'], 't': ['toph']}, 2: {'k': ['ki'], 'p': ['pi']}, 6: {'k': ['kicked'], 'n': ['nuncle'], 's': ['sister']}, 5: {'p': ['pearl']}}
    True
    >>> b = ['haws', 'hear', 'jots', 'ki', 'pi', 'toph']
    >>> d = create_scrabble_dict(b)
    >>> d == {4: {'h': ['haws', 'hear'], 'j': ['jots'], 't': ['toph']}, 2: {'k': ['ki'], 'p': ['pi']}}
    True
    """
    #create empty dict
    scrabble_dict = {}
    #iterate through elements of list to create dict
    for word in string_list:
        #create empty dicts
        scrabble_dict[len(word)] = {}
    #now we have {2: {}, 3: {}} etc.
    #iterate through dict
    for key in scrabble_dict:
        #iterate through list
        for word in string_list:
            w = word[0]
            #store list of key length words starting w/ w
            w_list = word_list(w, key, string_list)
            #check list is not empty
            if len(w_list) != 0:
                scrabble_dict[key][w] = w_list
    return scrabble_dict

def is_valid_word(my_string, my_dict):
    """
    (str, 2D dict) --> bool
    
    takes in a string representing a word and 2D dict
    and returns True if word in dict and False otherwise
    
    >>> b = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = create_scrabble_dict(b)
    >>> is_valid_word('cat', d)
    True
    >>> is_valid_word('yellow', d)
    False
    >>> b = ['haws', 'hear', 'jots', 'ki', 'pi', 'toph']
    >>> d = create_scrabble_dict(b)
    >>> is_valid_word('orange', d)
    False
    >>> is_valid_word('toph', d)
    True
    """
    #iterate through outer dictionary
    for key in my_dict:
        #iterate through inner dictionary
        for character in my_dict[key]:
            #check for string
            if my_string in my_dict[key][character]:
                return True
    return False

if __name__ == "__main__":
    doctest.testmod()
