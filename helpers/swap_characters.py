from helpers.length_assertion import length_assertion
from helpers.type_assertion import type_assertion

def swap_characters(string, a, b):
    """
    Takes an original string and returns a modification by swapping the first instances
    of a and b.

    Useful for adjusting the wiring inside a rotor.

    @param: string, the original string to modify
    @param: a, a character to swap
    @param: b, the character to swap a with

    @returns a new string of the modified original string
    """
    # Function defense
    type_assertion(string, str)
    type_assertion(a, str)
    type_assertion(b, str)
    length_assertion(a, 1)
    length_assertion(b, 1)

    new_string = string

    a_index = string.index(a)
    new_string = new_string[:a_index] + b + new_string[a_index + 1:]

    b_index = string.index(b)
    new_string = new_string[:b_index] + a + new_string[b_index + 1:]

    return new_string