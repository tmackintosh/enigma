from types import TracebackType
from advanced_helpers.index_of_coincidence import index_of_coincidence
from enigma import EnigmaMachine
from helpers.type_assertion import type_assertion

def fitness_value(a):
    """
    Used as the key function to order the states by how
    fit they are.

    @param a: the state
    @returns the fitness of the state
    """
    return a[2]

def optimise_rotor_setting(machine, rotor_number, code, x):
    """
    Given a premade machine, assess the rotor at the given index
    to optimise it to the optimal ring setting.

    @param machine: the EnigmaMachine with the rotor in
    @param rotor_number: the index of the rotor to optimise
    @param code: the code to compare the fitness function with
    @param x: the top x states to move forward with

    @returns the top x states with the ring setting according to the fitness function
    """
    # Method defense
    type_assertion(machine, EnigmaMachine)
    type_assertion(rotor_number, int)
    type_assertion(code, str)
    type_assertion(x, int)

    rotor = machine.starting_rotor
    starting_position = rotor.position
    rotor_index = rotor_number

    top_fitness_states = []

    # Assess the rotor at index position by traversing the machine
    while rotor_index > 1:
        rotor = rotor.left_connection
        rotor_index -= 1

    for i in range (0, 26):
        # We need to adjust the position setting to make sure we are consistent with the 
        # checks done by other fitness analysis
        rotor.setting = i
        rotor.position = (starting_position + i) % 26
        
        encrypted = machine.encode(code)
        fitness = index_of_coincidence(encrypted)

        # We need to return a state that can be used by other methods in advanced_work
        state = [rotor_number, i, fitness]

        top_fitness_states.append(state)
        top_fitness_states.sort(key = fitness_value, reverse = True)

        # Only assess the top x number of states, so drop the last one
        if len(top_fitness_states) > x:
            top_fitness_states.pop()

    return top_fitness_states