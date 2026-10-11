"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(number_of_minutes):
    """Calculate the bake time remaining.

    Parameters:
        number_of_minutes (int): The actual minutes the lasagna has been in the oven.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - number_of_minutes

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: The total preparation time (in minutes) based on the number of layers.
    """
    
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The baking time already elapsed.   

    Returns:
        int: The total elapsed time (in minutes) based on the number of layers and the elapsed bake time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time