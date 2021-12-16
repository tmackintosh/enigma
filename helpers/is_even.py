from helpers.type_assertion import type_assertion

def is_even(number):
    """
    Assess whether each digit of a number is even or not.
    Useful when assessing ring settings in enigma machines.

    @param number: int of the number to assess
    @returns boolean of whether each digit is even or not
    """

    # Function defense
    type_assertion(number, int)

    string = str(number)
    
    for character in string:
        if int(character) % 2 != 0:
            return False

    return True