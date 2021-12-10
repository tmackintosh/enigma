from helpers.type_assertion import type_assertion
from helpers.lexigraphical_range_assertion import lexigraphical_range_assertion

def numerical_assertion(string):
    type_assertion(string, str)

    for character in string:
        lexigraphical_range_assertion(character, "0", "9")