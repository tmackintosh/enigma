from helpers.type_assertion import type_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion

def numerical_assertion(string):
    """
    Asserts whether or not a string is a number

    @param string: the string to assess
    @returns nothing, throws on assertion error
    """
    # Function defense
    type_assertion(string, str)

    for character in string:
        lexigraphical_range_assertion(character, "0", "9")