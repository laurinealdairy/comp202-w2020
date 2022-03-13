#Laurine Aldairy - COMP202 Final
#260886886
#import doctest
import random

def tower_list(large, small):
    """
    (int, int) --> list
    
    takes in #s of 7in and 2in blocks and creates a list
    of all possible tower heights
    
    >>> tower_list(0, 0)
    [0]
    >>> tower_list(1, 2)
    [0, 2, 4, 7, 9, 11]
    >>> tower_list(2, 1)
    [0, 2, 7, 9, 14, 16]
    """
    #create empty list
    new_list = []
    #iterate through each number of larges
    for large_block in range(large + 1):
        #iterate through number of smalls
        for small_block in range(small + 1):
            height = 7*large_block + 2*small_block
            new_list.append(height)
    return new_list

def brick_tower(large, small, height):
    """
    (int, int, int) --> bool
    
    takes in inputs for # of 7in bricks, # of 2in bricks,
    and height of tower to build. returns True if tower
    of exact height can be built, False othwerwise.
    
    >>> brick_tower(3, 4, 0)
    True
    >>> brick_tower(1, 3, 8)
    False
    >>> brick_tower(2, 5, 8)
    True
    """
    #create list of possible heights
    possible_heights = tower_list(large, small)
    #check for target height
    if height in possible_heights:
        return True
    else:
        return False
    
def get_triangle(height, my_string):
    """
    (int, str) --> string
    
    takes in int representing height of triangle and
    string used to draw triangle and returns string
    representing the triangle
    raises ValueError if int is negative or string is
    empty
    
    >>> a = get_triangle(2, "$")
    >>> print(a)
    $ 
    $ $ 
    $ 
    """
    #create empty string
    tri_string = ""
    #check for valid integer
    if height < 0:
        raise ValueError("Integer must be non-negative.")
    #check for valid string
    if len(my_string) < 1:
        raise ValueError("String must contain at least one character")
    #check if height is 0
    if height == 0:
        return tri_string
    #now check if height is 1
    if height == 1:
        tri_string += my_string
        return tri_string
    #iterate through first half of triangle (not including peak)
    for num in range(1, height):
        tri_string += ((my_string + " ") * num) + "\n"
    #from peak to end of triangle
    for num2 in range(height, 0, -1):
        if num2 == 1:
            tri_string += ((my_string + " ") * num2)
        else:
            tri_string += ((my_string + " ") * num2) + "\n"
    return tri_string

def sort_numbers(my_list):
    """
    (list of int) --> None
    
    sorts list in place by putting evens first then odds
    returns nothing
    
    >>> a = [1, 2, 3, -4, 5]
    >>> sort_numbers(a)
    >>> a
    [-4, 2, 3, 1, 5]
    >>> b = [6, 2, 22, 4, 0]
    >>> sort_numbers(b)
    >>> b
    [6, 2, 22, 4, 0]
    >>> c = []
    >>> sort_numbers(c)
    >>> c
    []
    >>> d = [1]
    >>> sort_numbers(d)
    >>> d
    [1]
    >>> e = [2]
    >>> sort_numbers(e)
    >>> e
    [2]
    """
    #check if list is empty
    if len(my_list) < 1:
        return
    #create counter to look for even numbers
    counter = len(my_list) - 1
    #iterate through list from start to find odds
    for i in range(len(my_list)):
        #check if odd
        if (my_list[i] % 2) != 0:
            #store odd value
            temp = my_list[i]
            #check if we have looked at all elements
            if i >= counter:
                break
            #iterate from the end to look for an even number
            for j in range(counter, i, -1):
                #if you find an even
                if (my_list[j] % 2) == 0:
                    #replace the odd
                    my_list[i] = my_list[j]
                    #move the odd
                    my_list[j] = temp
                    break
                #if no even do nothing
            counter = j
        #do nothing if number is even

def select_vector(big_list, index_list):
    """
    (2D list, list) --> list
    
    takes in 2d list of ints and 1d list of int, returns
    list of elements of sublists of big_list in position
    from index_list or raises appropriate value errors
    
    >>> select_vector([[1, 2, 3, 4, 5], [6, 7], [8, 9]], [3, 0, 1])
    [4, 6, 9]
    >>> select_vector([[1, 2, 3, 4, 5], [6, 7], [8, 9]], [3, 0, 1, 0])
    Traceback (most recent call last):
    ValueError: Second list contains too many or too few elements.
    >>> select_vector([[1, 2, 3, 4, 5], [6, 7], [8, 9]], [3, 2, 1])
    Traceback (most recent call last):
    ValueError: Indices in second list are out of bounds.
    """
    #check both lists are same size
    if len(big_list) != len(index_list):
        raise ValueError("Second list contains too many or too few elements.")
    #create empty list
    value_list = []
    #iterate through index list
    for i in range(len(index_list)):
        #check the value is in range
        if index_list[i] >= len(big_list[i]):
            raise ValueError("Indices in second list are out of bounds.")
        value_list.append(big_list[i][index_list[i]])
    return value_list

def get_coordinates(list_of_strings, target):
    """
    (list of str, str) --> list of tuples
    
    takes in 2d list of strings and target string
    returns list of tuples of positions of target string
    returns empty list if target does not appear
    
    >>> get_coordinates([['q', '', '4'], ['j', 'k', ''], []], "")
    [(0, 1), (1, 2)]
    >>> get_coordinates([['llama', '', 'Llama'], ['llama', 'LLAMA', ''], []], "llama")
    [(0, 0), (1, 0)]
    >>> get_coordinates([[], [''], []], "hello")
    []
    """
    #create empty list
    tuple_list = []
    #iterate through list
    for i in range(len(list_of_strings)):
        #check if sublist is empty
        if len(list_of_strings[i]) == 0:
            continue
        #iterate through sublist
        for j in range(len(list_of_strings[i])): 
            #check if string matches target
            if list_of_strings[i][j] == target:
                tuple_list.append((i, j))
    return tuple_list

def evaluate_polynomial(poly_dict, value):
    """
    (dict of nonneg ints to numbers, number) --> number
    
    takes in dict mapping powers of x to its coefficient
    and a number value for x and returns the result of
    the expression
    
    # 2x^4 - 3x^2 + 9
    # x^2 - 3x + 4
    # x^4 + 2x - 12
    >>> evaluate_polynomial({4:2, 2: -3, 0: 9, 1: 0}, 1)
    8
    >>> evaluate_polynomial({2: 1, 0: 4, 1: -3}, 0.5)
    2.75
    >>> evaluate_polynomial({4: 1, 0: -12, 1: 2}, -2)
    0
    """
    #initialise result
    result = 0
    #iterate through dict
    for key in poly_dict:
        result += poly_dict[key] * (value ** key)
    return round(result, 4)

def str_to_list(my_string):
    """
    (str) --> list
    
    takes in string and returns list where each element
    is one of the characters in string
    
    >>> str_to_list('hello')
    ['h', 'e', 'l', 'l', 'o']
    """
    #create empty list
    my_list = []
    #iterate through string
    for character in my_string:
        my_list.append(character.lower())
    return my_list

def anagrams(ana_list, target):
    """
    (list of str, str) --> bool
    
    takes in list of strings and a word and returns
    True if each element in list is an anagram of the
    input word and False otherwise, ignores cases
    
    >>> anagrams(['ICEMAN', 'Cinema'], 'cinema')
    True
    >>> anagrams(['teas', 'seat', 'sea'], 'east')
    False
    >>> anagrams(['nit', 'int', 'tin', 'not'], 'tin')
    False
    >>> anagrams(['nit', 'int', 'tin', 'not'], '')
    False
    """
    #iterate through list
    for word in ana_list:
        #create list of target letters
        temp = str_to_list(target)
        #iterate through letters in word
        for character in word:
            #false if letter not in target
            if character.lower() not in temp:
                return False
            else:
                temp.remove(character.lower())
        #check temp is now empty
        if temp != []:
            return False
    return True

def flatten_dict(my_dict):
    """
    (dict) --> list
    
    takes in dict mapping strings to non-negative
    integers, returns list containing the string integer
    number of times
    
    >>> flatten_dict({'cat': 2, 'dog': 0, 'bunny': 3})
    ['cat', 'cat', 'bunny', 'bunny', 'bunny']
    >>> d = {'l': 2, 'z': 1, 'm': 4}
    >>> flatten_dict(d)
    ['l', 'l', 'z', 'm', 'm', 'm', 'm']
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
    return flat_list

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

def refill_rack(rack_dict, pool_dict, target):
    """
    (dict, dict, int) --> None
    
    takes in dict of rack, dict of pool, and randomly
    draws from pool until there are target letters in
    rack or pool is empty. returns nothing and modifies
    both input dicts
    
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
    #until either rack is full or pool is empty
    while (dict_sum(rack_dict) < target) and (len(pool_dict) != 0):
        #create list of letters available
        pool_list = flatten_dict(pool_dict)
        #choose one randomly
        next_letter = random.choice(pool_list)
        #if letter is in rack, increase its value
        if next_letter in rack_dict:
            rack_dict[next_letter] += 1
        else:
            rack_dict[next_letter] = 1
        #remove letter from pool
        pool_dict[next_letter] -= 1
        #check if there are none left now
        if pool_dict[next_letter] == 0:
            del pool_dict[next_letter]

class Cake:
    """
    represents cakes
    
    Attributes: name (str), ingreds (list of str), price (float)
    Methods: __init__ (creates Cake object), __str__
    (creates string to display), is_better (compares
    price/ingredient ratio)
    """
    def __init__(self, name, ingreds):
        self.name = name
        if len(ingreds) < 3:
            raise ValueError("Cake has too few ingredients.")
        self.ingreds = ingreds
        self.price = random.uniform(10.00, 15.00)
    
    def __str__(self):
        """
        (Cake) --> str
        
        takes in class object and returns string representing
        object which shows cake name and price
        
        >>> c = Cake("Carrot Cake", ['carrot', 'eggs', 'sugar', 'flour'])
        >>> c.price = 13.75
        >>> print(c)
        Carrot Cake $13.75
        """
        #create string of name
        cake_string = self.name
        #add price
        cake_string += " $" + str(round(self.price, 2))
        return cake_string
        
    def get_ratio(self):
        """
        (Cake) --> float
        
        takes in self and returns float ratio of cost to
        ingredients
        
        >>> c = Cake("Carrot Cake", ['carrot', 'eggs', 'sugar', 'flour'])
        >>> c.price = 12.00
        >>> c.get_ratio()
        3.0
        >>> g = Cake("Chocolate Cake", ['cocoa', 'sugar', 'flour'])
        >>> g.price = 12.0
        >>> g.get_ratio()
        4.0
        """
        return self.price / len(self.ingreds)
    
    def is_better(self, other):
        """
        (Cake, Cake) --> bool
        
        returns True if current cake has lower price/ingred
        ratio than other cake, False otherwise
        returns False if equal
        
        >>> c = Cake("Carrot Cake", ['carrot', 'eggs', 'sugar', 'flour'])
        >>> c.price = 12.00
        >>> g = Cake("Chocolate Cake", ['cocoa', 'eggs', 'sugar', 'flour'])
        >>> g.price = 12.0
        >>> c.is_better(g)
        False
        >>> c = Cake("Carrot Cake", ['carrot', 'eggs', 'sugar', 'flour'])
        >>> c.price = 12.00
        >>> g = Cake("Chocolate Cake", ['cocoa', 'eggs', 'sugar', 'flour', 'milk'])
        >>> g.price = 12.0
        >>> c.is_better(g)
        False
        """ 
        #return value
        return self.get_ratio() < other.get_ratio()

def create_menu(cake_dict):
    """
    (dict of str to lists) --> list of Cakes
    
    takes in dict mapping cake names to lists of
    ingredients and returns list of Cake objects
    
    >>> random.seed(12)
    >>> create_menu({'Chocolate Cake': ['butter', 'flour', 'sugar', 'cocoa'], 'Carrot Cake': ['flour', 'sugar', 'carrot'], 'Victoria Sponge Cake': ['butter', 'flour', 'sugar', 'eggs', 'vanilla', 'milk'], 'Pound Cake': ['butter', 'flour', 'sugar', 'eggs']})
    Chocolate Cake $12.37
    Carrot Cake $13.29
    Victoria Sponge Cake $13.33
    Pound Cake $10.71
    [<__main__.Cake object at 0x10b428990>, <__main__.Cake object at 0x10b428850>, <__main__.Cake object at 0x10b428890>, <__main__.Cake object at 0x10b428910>]
    """
    #create empty list
    cake_list = []
    #iterate through dict
    for key in cake_dict:
        new_cake = Cake(key, cake_dict[key])
        cake_list.append(new_cake)
    #display menu
    for element in cake_list:
        print(element)
    return cake_list

def find_best(cake_list):
    """
    (list of Cakes) --> Cake
    
    takes in nonempty list of cakes and returns best cake
    in list or if multiple the first best cake
    
    >>>random.seed(12)
    >>> g = Cake('Chocolate Cake', ['butter', 'flour', 'sugar', 'cocoa'])
    >>> c = Cake('Carrot Cake', ['flour', 'sugar', 'carrot'])
    >>> v = Cake('Victoria Sponge Cake', ['butter', 'flour', 'sugar', 'eggs', 'vanilla', 'milk'])
    >>> p = Cake('Pound Cake', ['butter', 'flour', 'sugar', 'eggs'])
    >>> find_best([g, c, v, p])
    <__main__.Cake object at 0x103cde2d0>
    """
    #iterate from beginning
    for this_cake in cake_list:
        #compare this cake to all other cakes
        for other_cake in cake_list:
            #check there is no better cake
            #if this cake is not best
            if not this_cake.is_better(other_cake):
                #check if other cake is better
                if other_cake.is_better(this_cake):
                    #break out of inner loop
                    break
        #if this cake is not the best, continue searching
        if other_cake.is_better(this_cake):
            continue
        #if we get here, we have the best cake
        #so return cake and end loop
        return this_cake
