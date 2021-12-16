from helpers.length_assertion import length_assertion
from helpers.type_assertion import type_assertion

def lexigraphical_range_assertion(object, minimum_value, maximum_value):
    """
    Asserts whether a character fits within a lexigraphical range.
    Useful for assessing whether or not a character is an alphabetic letter.

    @param object: character to assess
    @param minimum_value: the minimum ascii character in the range (ie, A)
    @param maximum_value: the maximum ascii character in the range (ie, Z)

    @returns nothing, throws on assertion error
    """

    # Function defense
    type_assertion(object, str)
    type_assertion(minimum_value, str)
    type_assertion(maximum_value, str)
    length_assertion(object, 1)
    length_assertion(minimum_value, 1)
    length_assertion(maximum_value, 1)

    if ord(object) < ord(minimum_value) or ord(object) > ord(maximum_value):
        raise TypeError("Should be between", minimum_value, "and", maximum_value, ", got", object)