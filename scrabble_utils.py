#Assignment 3: Simplified Scrabble
#Laurine Aldairy
#260886886
import board_utils
import dicts_utils 
import random
import doctest

def display_rack(my_dict):
    """
    (dict) --> None
    
    takes in dict mapping each to nonneg int and
    displays each character int number of times
    
    >>> d = dicts_utils.count_occurrences("three trees")
    >>> display_rack(d)
    E E E E H R R S T T 
    >>> b = {'a': 4, 'b': 4, 'c': 4}
    >>> display_rack(b)
    A A A A B B B B C C C C 
    >>> b = {'a': 2, 'e': 1, 'c': 1, 't': 2, 'q': 1, 'u': 0}
    >>> display_rack(b)
    A A C E Q T T 
    """
    #create list of strings
    rack_list = dicts_utils.flatten_dict(my_dict)
    #iterate through list
    for character in rack_list:
        print(character.upper(), end = ' ')

def has_letters(my_dict, my_string):
    """
    (dict, str) --> bool
    
    takes in dict representing player rack and string
    returns True if all characters in string are on
    rack and removes them from rack
    returns False otherwise
    
    >>> b = {'a': 2, 'e': 1, 'c': 1, 't': 2, 'q': 1, 'u': 0}
    >>> has_letters(b, "cake")
    False
    >>> b == {'a': 2, 'e': 1, 'c': 1, 't': 2, 'q': 1, 'u': 0}
    True
    >>> has_letters(b, "ace")
    True
    >>> b == {'a': 1, 't': 2, 'q': 1, 'u': 0}
    True
    >>> b = {'a': 2, 't': 1, 'r': 1, 'c': 1, 'i': 2}
    >>> has_letters(b, "tiara")
    True
    >>> b == {'c': 1, 'i': 1}
    True
    """
    #create dict representing string
    string_dict = dicts_utils.count_occurrences(my_string)
    
    return dicts_utils.subtract_dicts(my_dict, string_dict)

def refill_rack(rack_dict, pool_dict, target):
    """
    (dict, dict, int) --> None
    
    takes in dict of rack, dict of pool, and randomly
    draws from pool until there are target letters in
    rack or pool is empty. returns nothing and can
    modify both input dicts
    
    >>> random.seed(12)
    >>> b = {'a': 2, 'e': 1, 'c': 1, 't': 2, 'q': 1}
    >>> r = {'d': 1, 'v': 1}
    >>> refill_rack(r, b, 4)
    >>> r == {'d': 1, 'v': 1, 'e': 1, 'c': 1}
    True
    >>> b == {'a': 2, 't': 2, 'q': 1}
    True
    >>> refill_rack(r, b, 10)
    >>> r == {'d': 1, 'v': 1, 'e': 1, 'c': 1, 't': 2, 'q': 1, 'a': 2}
    True
    >>> b
    {}
    >>> random.seed(202)
    >>> b = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'z': 1}
    >>> r = {'d': 1, 'v': 1}
    >>> refill_rack(r, b, 7)
    >>> r == {'d': 1, 'v': 1, 't': 1, 'n': 1, 's': 1, 'p': 2}
    True
    >>> b == {'a': 1, 'e': 2, 'h': 1, 'l': 2, 's': 2, 't': 1, 'z': 1}
    True
    """
    #iterate through dicts
    while (dicts_utils.dict_sum(rack_dict) < target) and (len(pool_dict) != 0 and dicts_utils.dict_sum(pool_dict) != 0):
         #create list of available letters
        pool_list = dicts_utils.flatten_dict(pool_dict)
        #randomly select from the list
        next_letter = random.choice(pool_list)
        #if letter is already in the rack
        if next_letter in rack_dict:
            rack_dict[next_letter] += 1
        #add letter to rack
        else:
            rack_dict[next_letter] = 1
        #create dict of next_letter
        temp_dict = {next_letter: 1}
        #remove letter from pool
        dicts_utils.subtract_dicts(pool_dict, temp_dict)

def compute_score(word_list, point_dict, valid_words):
    """
    (list, dict, 2D dict) --> int
    
    takes in list of words, dict mapping letters to their
    point values, and 2D dict of valid words. returns
    sum of individual words scores and returns 0 if any
    of the words are invalid
    
    >>> b = ['aa', 'qi', 'za', 'cat', 'can', 'cow', 'dog', 'dad', 'hippo', 'umami', 'uncle']
    >>> d = dicts_utils.create_scrabble_dict(b)
    >>> p = {'a': 1, 'e': 2, 'h': 1, 'l': 2, 'n': 1, 'p': 2, 's': 3, 't': 2, 'h': 1}
    >>> words = ['hippo', 'cat']
    >>> compute_score(words, p, d)
    8
    >>> compute_score(['za'], p, d)
    1
    >>> compute_score(['pizza'], p, d)
    0
    >>> compute_score(['cat', 'can', 'dog', 'pizza'], p, d)
    0
    """
    #create counter
    counter = 0
    #iterate through list
    for word in word_list:
        #check both words are valid
        if not dicts_utils.is_valid_word(word, valid_words):
            return 0
        #add score of individual word
        temp_score = dicts_utils.get_word_score(word, point_dict)
        counter += temp_score
    return counter

def place_tiles(board_list, my_letters, row, column, direction):
    """
    (2D list, str, int, int, str) --> list
    
    takes as input a 2D list representing the board,
    a string representing the letters to add,
    two integers representing the row and the column of
    starting square, and a string indicating direction
    adds letters to the board from position in direction
    returns list of new words created by adding letters
    if invalid direction, returns empty list
    
    >>> b = board_utils.create_board(4, 4)
    >>> place_tiles(b, "egg", 1, 1, 'down')
    ['egg']
    >>> place_tiles(b, "ben", 1, 0, 'right')
    ['been']
    >>> b
    [[' ', ' ', ' ', ' '], ['b', 'e', 'e', 'n'], [' ', 'g', ' ', ' '], [' ', 'g', ' ', ' ']]
    >>> place_tiles(b, "oe", 0, 3, 'down')
    ['one']
    >>> b
    [[' ', ' ', ' ', 'o'], ['b', 'e', 'e', 'n'], [' ', 'g', ' ', 'e'], [' ', 'g', ' ', ' ']]
    >>> place_tiles(b, "aes", 3, 0, 'right')
    ['ages', 'ones']
    """
    #create empty list
    new_words = []
    #down case
    if direction == 'down':
        #create list of rows with words to skip
        skip_rows = []
        #add new tiles
        #initialise variables for the row and word position
        i = row
        j = 0
        #iterate through the board columns
        while i < len(board_list):
            #if empty place tile
            if board_list[i][column] == ' ':
                board_list[i][column] = my_letters[j]
                #move on to next letter
                j += 1
                #if you've placed the last letter then stop
                if j == len(my_letters):
                    break
            #if not empty make note
            else:
                skip_rows.append(i)
            #move down a row
            i += 1
        #create list of vertical axis
        down_list = board_utils.get_vertical_axis(board_list, column)
        #find the word and append it
        down_word = board_utils.find_word(down_list, row)
        new_words.append(down_word)
        #initialise the variable
        i = row
        #iterate through rows to find new words
        while i in range(len(board_list)):
            #store potential word
            temp_word = board_utils.find_word(board_list[i], column)
            #if word is new and long enough, append it
            if (len(temp_word) > 1) and (i not in skip_rows):
                new_words.append(temp_word)
            i += 1
    elif direction == 'right':
        #create empty list of column to skip
        skip_columns = []
        #initialise variables for the column and word position
        i = column
        j = 0
        #iterate through the board row
        while i < len(board_list[0]):
            #if empty place tile
            if board_list[row][i] == ' ':
                board_list[row][i] = my_letters[j]
                #move on to next letter
                j += 1
                #if you've placed the last letter then stop
                if j == len(my_letters):
                    break
            else:
                skip_columns.append(i)
            #move across a column
            i += 1
        #find the word and append it
        across_word = board_utils.find_word(board_list[row], column)
        new_words.append(across_word)
        #initialise the variable
        i = column
        #iterate through rows to find new words
        while i in range(len(board_list[0])):
            #create vertical list
            temp_list = board_utils.get_vertical_axis(board_list, i)
            #store potential word
            temp_word = board_utils.find_word(temp_list, row)
            #if it is new and long enough, append it
            if (len(temp_word) > 1) and (i not in skip_columns):
                new_words.append(temp_word)
            i += 1
    #if neither, will return empty list
    #if down/right will return list of words
    return new_words

def make_a_move(board_list, rack_dict, my_letters, row, column, direction):
    """
    (list, dict, str, int, int, str) --> list
    
    takes as input list representing board, dict
    representing player rack, str representing letters
    to place, two ints representing row and column of
    starting square, and string representing direction.
    if invalid direction, returns empty list. otherwise
    checks for available space, and if letters in rack
    if yes for both, runs place tiles and returns list
    of new words and removes letters from rack
    if no space, raises IndexError, if letters not in
    rack, raises ValueError
    
    >>> b = board_utils.create_board(4, 4)
    >>> r = {'e': 4, 'g': 3, 'b': 2, 'n': 1, 'o': 1}
    >>> make_a_move(b, r, "egg", 1, 1, 'down')
    ['egg']
    >>> b
    [[' ', ' ', ' ', ' '], [' ', 'e', ' ', ' '], [' ', 'g', ' ', ' '], [' ', 'g', ' ', ' ']]
    >>> r
    {'e': 3, 'g': 1, 'b': 2, 'n': 1, 'o': 1}
    >>> make_a_move(b, r, "ben", 1, 0, 'right')
    ['been']
    >>> b
    [[' ', ' ', ' ', ' '], ['b', 'e', 'e', 'n'], [' ', 'g', ' ', ' '], [' ', 'g', ' ', ' ']]
    >>> r
    {'e': 2, 'g': 1, 'b': 1, 'o': 1}
    >>> make_a_move(b, r, "oset", 0, 3, 'down')
    Traceback (most recent call last):
    IndexError: Not enough space on the board.
    >>> make_a_move(b, r, "aes", 3, 0, 'right')
    Traceback (most recent call last):
    ValueError: Not all letters on player rack.
    """
    #create dict of letters
    letters_dict = dicts_utils.count_occurrences(my_letters)
    #if invalid direction return empty list
    if direction not in ['down', 'right']:
        return place_tiles(board_list, my_letters, row, column, direction)
    #down case
    elif direction == 'down':
        #create vertical list
        down_list = board_utils.get_vertical_axis(board_list, column)
        #check the letters fit
        if not board_utils.fit_on_board(down_list, my_letters, row):
            raise IndexError("Not enough space on the board.")
        #check the letters are in rack
        elif not dicts_utils.subtract_dicts(rack_dict, letters_dict):
            raise ValueError("Not all letters on player rack.")
        #make the move
        else:
            return place_tiles(board_list, my_letters, row, column, direction)
    #right case
    else:
        #create row list
        right_list = board_list[row]
        #check letters will fit
        if not board_utils.fit_on_board(right_list, my_letters, column):
            raise IndexError("Not enough space on the board.")
        #check player has these letters
        elif not dicts_utils.subtract_dicts(rack_dict, letters_dict):
            raise ValueError("Not all letters on player rack.")
        #make the move
        else:
            return place_tiles(board_list, my_letters, row, column, direction)

if __name__ == "__main__":
    doctest.testmod()
    random.seed(42)
    rack={'d': 1, 'b': 1}
    bag={'z': 2, 'v': 3, 'h': 3, 'g': 1, 'a': 3, 'w': 4, 'o': 4, 'j': 3, 'x': 3, 's': 4, 'e': 6, 'd': 4, 'p': 1, 'l': 4, 'b': 1, 'm': 2, 'r': 1, 'y': 3, 'k': 1, 'i': 4, 'u': 1, 'n': 1, 'f': 1}
    number=5
    refill_rack(rack,bag,number)