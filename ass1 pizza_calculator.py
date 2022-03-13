#Assignment 1 - Pizza Calculator
#written by Laurine Aldairy
#ID: 260886886

import math

"""
TO DO
>>> rename and submit
"""

def display_welcome_menu():
    """
    None --> None
    
    displays a welcome menu with modes and returns
    no values
    
    >>> display_welcome_menu()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    """
    
    print("Welcome to the COMP 202 fair pizza calculator!")
    print("Please chose one of the following modes:")
    print("A. \"Quantity mode\"")
    print("B. \"Price mode\"")
    
#display_welcome_menu()

def pizza_area(x):
    """
    (int) --> float
    
    takes diameter and returns area of pizza
    
    >>> pizza_area(8)
    50.2654824574
    >>> pizza_area(3)
    7.0685834706
    >>> pizza_area(-1)
    False
    """
    if (x >= 0):
        radius = x / 2
        area = (radius ** 2) * math.pi
        return round(area, 10)
    else:
        return False
    
#print(pizza_area(-1))
    
def get_fair_quantity(x, y):
    """
    (int, int) --> int
    
    takes two positive integers as input representing the diametersof two pizzas.  The functionreturnsan integer indicating the minimum number of smaller pizzasJohnny must order in order for him to getat leastthe same amount of pizza as one large pizza.
    
    >>> get_fair_quantity(10, 4)
    7
    >>> get_fair_quantity(9, 15)
    3
    >>> get_fair_quantity(15, 9)
    3
    >>> get_fair_quantity(8, 8)
    1
    """
    
    pizza_x = pizza_area(x)
    pizza_y = pizza_area(y)
    
    if (x > 0) and (y > 0):
        #if the two numbers are equal
        if (x == y):
            return 1
        #if the first diameter is bigger
        elif (x > y):
            
            #calculating the number of pizzas needed
            if ((pizza_x % pizza_y) == 0):
                #the dividend if pizzas divide exactly
                return int(pizza_x // pizza_y)
            else:
                #the number if there is some remainder
                return int((pizza_x // pizza_y)) + 1
        #if the second diameter is bigger
        else:
            if ((pizza_y % pizza_x) == 0):
                #the number if pizzas divide exactly
                return int(pizza_y // pizza_x)
            else:
                #the number if pizzas do not divide exactly
                return int((pizza_y // pizza_x)) + 1 
    else:
        return False

#print(get_fair_quantity(10, 4))
        
def get_fair_price(x, y, z, w):
    """
    (int, float, int, int) --> float
    
    takes input of large pizza diameter, its price,
    small pizza diameter, and the number of small pizzas
    
    returns dollar amt for total small pizzas at
    price rate of large pizza
    
    >>> get_fair_price(12, 10.0, 6, 2)
    5.0
    >>> get_fair_price(18, 12, 8, 5)
    11.85
    >>> get_fair_price(9, 8.99, 6, 2)
    7.99
    
    x = diameter large
    y = price large
    z = diameter small
    w = quantity small
    """
    #large pizza inputs
    large_area = pizza_area(x)
    pizza_price = y
    #pizza rate per square inch of pizza
    price_per_sq_inch = pizza_price / large_area
    
    #small pizza inputs
    small_area = pizza_area(z)
    quantity_small = w
    #total sqare inches of pizza
    total_area = small_area * quantity_small
    
    #calculating the price you should pay for that
    #number of small pizzas
    ideal_price = total_area * price_per_sq_inch
    
    return round(ideal_price, 2)
    
# print(get_fair_price(9, 8.99, 6, 2))

def run_pizza_calculator():
    """
    None --> None
    
    takes no input and displays menu, then based on user's
    input, runs through quantity mode with user's two
    pizza sizes of choice and displays result
    or price mode with user's pizza sizes, amounts and
    prices and displays result
    or displays error message
    and returns no value
    
    >>> run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: 2
    This mode is not supported
    
    >>> run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: b
    This mode is not supported
    
    >>> run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: A
    You selected "Quantity mode"
    
    Enter the diameter of the large pizza: 15
    Enter the diameter of the small pizza: 9
    
    To be fully satisfied you should order 3 small pizzas
    
    >>> run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. "Quantity mode"
    B. "Price mode"
    Enter your choice: B
    You selected "Price mode"
    
    Enter the diameter of the large pizza: 18
    Enter the price of the large pizza: 12
    Enter the diameter of the small pizza: 8
    Enter the number of small pizzas you'd like to buy: 5
    
    The fair price to pay for 5 small pizzas is $11.85
    """
    
    #pull up welcome menu
    display_welcome_menu()
    
    #take input from user for mode
    mode = input("Enter your choice: ")
    
    if (mode == "A"):
        #display user's choice
        print("You selected \"Quantity mode\"")
        print("\n")
        
        #retrieving pizza diameters
        large_diameter = int(input("Enter the diameter of the large pizza: "))
        small_diameter = int(input("Enter the diameter of the small pizza: "))
        
        #calculating number of pizzas needed
        num_small_pizzas = get_fair_quantity(large_diameter, small_diameter)
        print("\n")
        
        #displaying result to user
        print("To be fully satisfied you should order", \
              num_small_pizzas, "small pizzas")
    elif (mode == "B"):
        #display user's choice
        print("You selected \"Price mode\"")
        print("\n")
        
        #retrieving pizza diameters/prices/numbers
        large_diameter = int(input("Enter the diameter of the large pizza: "))
        large_price = float(input("Enter the price of the large pizza: "))
        small_diameter = int(input("Enter the diameter of the small pizza: "))
        num_smalls = int(input("Enter the number of small pizzas you'd like to buy: "))
        
        #calculate the fair price
        fair_price = str(get_fair_price(large_diameter, large_price, small_diameter, num_smalls))
        print("\n")
        
        #display result to user
        print("The fair price to pay for", num_smalls, \
              "small pizzas is $" + fair_price)
    else:
        print("This mode is not supported")

if __name__ == "__main__":
    run_pizza_calculator()
