from helpers.type_assertion import type_assertion

def get_string_form(rotors):
    """
    Returns a list of rotors in a format that is compatible with the
    EnigmaMachine constructor.

    @param rotors: list of rotor names
    @returns list of rotors in a constructor compatible format
    """
    
    # Function defense
    type_assertion(rotors, str)

    string = ""

    for rotor in rotors:
        if string == "":
            string = rotor
        else:
            string = string + " " + rotor

    return string