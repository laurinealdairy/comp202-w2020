#Assignment 2: Ciphers
#Laurine Aldairy
#260886886
import doctest
from crypto_helpers import *

def caesar(s, k, m):
    """
    (str, int, int) --> str
    
    takes string, key, and mode as input and returns
    encrypted string if mode = 1 and decrypted string
    if m = -1
    
    >>> caesar("lip balm", 9, 1)
    'ury kjuv'
    >>> caesar("wtaad", 15, -1)
    'hello'
    >>> caesar("laptop", -4, 1)
    'hwlpkl'
    >>> caesar("i miss the sun", 22, 1)
    'e ieoo pda oqj'
    >>> caesar("compsci", 14, 7)
    Traceback (most recent call last):
    ValueError: mode not supported
    """
    #create empty string
    new_string = ""
    #raise appropriate errors
    if m not in [1, -1]:
        raise ValueError("mode not supported")
    #iterate through string to encrypt
    if m == 1:
        for character in s:
            if character == " ":
                new_string = new_string + " "
                continue
            new_character = shift_char(character, k)
            new_string = new_string + new_character
        return new_string
    #iterate through string to decrypt
    if m == -1:
        for character in s:
            if character == " ":
                new_string = new_string + " "
                continue
            new_character = shift_char(character, -k)
            new_string = new_string + new_character
        return new_string
    
def vigenere(message, key, m):
    """
    (str, str, int) --> str
    
    takes string, key, and mode as input and returns
    encrypted string if mode = 1 and decrypted string
    if m = -1
    
    >>> vigenere("nOtebook", "lilyzoe", 1)
    'ywecacsv'
    >>> vigenere("ywecacsv", "lilyzoe", -1)
    'notebook'
    >>> vigenere("too many midterms", "math", 1)
    'foh yagf mbkfekte'
    >>> vigenere("foh yagf mbkfekte", "math", -1)
    'too many midterms'
    >>> vigenere("hello", "cat", 5)
    Traceback (most recent call last):
    ValueError: mode not supported
    """
    #create empty string
    new_string = ""
    #raise appropriate errors
    if m not in [1, -1]:
        raise ValueError("mode not supported")
    #create keyword and list
    keyword = pad_keyword(key, len(message))
    keyword_list = get_keys(keyword)
    #iterate through characters in message to encrypt
    if m == 1:
        for i in range(len(message)):
            #create new character
            new_character = shift_char(message[i], keyword_list[i])
            #concatenate new character
            new_string = new_string + new_character
        return new_string
    #iterate through characters in message to decrypt
    if m == -1:
        for i in range(len(message)):
            #create new character
            new_character = shift_char(message[i], -keyword_list[i])
            #concatenate new character
            new_string = new_string + new_character
        return new_string

if __name__ == "__main__":
    doctest.testmod()