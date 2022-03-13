#Assignment 2: Ciphers - Helper Functions
#Laurine Aldairy
#260886886
import doctest

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def in_engl_alpha(s):
    """
    (str) --> bool
    
    takes in a string and returns True if string
    consists of only letters in the english alphabet
    and False otherwise
    
    >>> in_engl_alpha("")
    False
    >>> in_engl_alpha("candle")
    True
    >>> in_engl_alpha("#")
    False
    >>> in_engl_alpha("7 wheels")
    False
    >>> in_engl_alpha("ë")
    False
    """
    #convert string to lower case
    lower_string = s.lower()
    #return false if empty
    if len(s) == 0:
        return False
    #iterate through characters in s
    for character in lower_string:
        if character not in ALPHABET:
            return False
    return True

def shift_char(character, n):
    """
    (str, int) --> str
    
    takes single character and integer and returns
    a character
    
    >>> shift_char("D", 4)
    'h'
    >>> shift_char("y", 8)
    'g'
    >>> shift_char("&", 1)
    '&'
    >>> shift_char("u", -3)
    'r'
    >>> shift_char("seven", 7)
    Traceback (most recent call last):
    ValueError: input string should contain a single character

    """
    #check if only one-character string
    if len(character) != 1:
        raise ValueError("input string should contain a single character")
    #convert character to lower case
    lower_character = character.lower()
    #convert to new character if in alphabet
    if in_engl_alpha(lower_character):
        old_index = ALPHABET.find(lower_character)
        new_index = old_index + n
        if new_index >= len(ALPHABET):
            new_index = new_index - len(ALPHABET)
        if new_index < 0:
            new_index = new_index + len(ALPHABET)
        return ALPHABET[new_index]
    else:
        return character

def get_keys(s):
    """
    (str) --> list of int
    
    takes string as input and returns list of indices
    of each character in alphabet
    if character not in alphabet, raises error
    if string empty, returns empty list
    
    >>> get_keys("many")
    [12, 0, 13, 24]
    >>> get_keys("dEF")
    [3, 4, 5]
    >>> get_keys("")
    []
    >>> get_keys("educ@tion")
    Traceback (most recent call last):
    ValueError: input string must contain only characters from the English alphabet
    """
    #convert to lower case
    new_string = s.lower()
    #create empty list
    key_list = []
    #check if string empty
    if len(s) == 0:
        return key_list
    #create list if characters in alphabet
    if in_engl_alpha(new_string):
        #iterate through characters to make list
        for character in new_string:
            char_index = ALPHABET.find(character)
            key_list.append(char_index)
        return key_list
    #raise error is characters not in alphabet
    else:
        raise ValueError("input string must contain only characters from the English alphabet")

def pad_keyword(s, n):
    """
    (str, int) --> str
    
    takes in string and integer and concatenates string
    with itself until it has length n
    
    >>> pad_keyword("nope", 12)
    'nopenopenope'
    >>> pad_keyword("manyfish", 6)
    'manyfi'
    >>> pad_keyword("", 9)
    Traceback (most recent call last):
    ValueError: string must not be empty
    
    """
    #create empty string
    new_string = ""
    #find length of s
    len_s = len(s)
    #raise errors if necessary
    if len_s == 0:
        raise ValueError("string must not be empty")
    if in_engl_alpha(s) == False:
        raise ValueError("string must contain only characters in the English alphabet")
    if n <= 0:
        raise ValueError("n must be positive integer")
    #iterate through until len = n
    i = 0
    while i < n:
        new_string = new_string + s[i % len_s]
        i += 1
    return new_string

if __name__ == "__main__":
    doctest.testmod()
