import itertools

from helpers.type_assertion import type_assertion

def likely_value(a):
    """
    Used as the key function in sorting the states by fitness.

    @param a: the state
    @returns b: the fitness of the state
    """
    return a[1]

def get_best_rotors(config):
    """
    Of the top x settings by fitness, count how many rotors were used and
    return a list of the top 3 rotors that performed the best.

    @param config: a list of high performing rotor states
    @returns: a list of the highest performing rotors
    """
    # Method defense
    type_assertion(config, list)
    
    # We need to convert the rotors into a state that can be counted and manipulated,
    # the easiest way to do that is by string
    rotors = ""

    for enigma_state in config:
        rotors = rotors + enigma_state[0]
        rotors = rotors + " "

    rotors = rotors.split(" ")
    all_rotor_names = list(dict.fromkeys(rotors))

    # Performing the list function on a dictionary will make a "" key which is unnecessary
    all_rotor_names.remove("")

    # Count how many times each rotor appeared in the top x best performing states
    
    rotor_count = {}
    for item in all_rotor_names:
        rotor_count[item] = rotors.count(item)

    top_values = []

    for item in rotor_count:
        value = rotor_count.get(item)

        top_values.append([item, value])
        top_values.sort(key = likely_value, reverse = True)

        # Return only the top 3 performing rotors
        if len(top_values) > 3:
            top_values.pop()

    top_rotors = []

    # We only need the rotors, no other redundant information
    for value in top_values:
        top_rotors.append(value[0])

    return top_rotors