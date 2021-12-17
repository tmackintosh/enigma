
import itertools

from advanced_helpers.index_of_coincidence import index_of_coincidence
from enigma import EnigmaMachine
from helpers.type_assertion import type_assertion

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def fitness_value(a):
    """
    Used to sort the list by the fittest state.

    @param a: the state
    @returns the fitness of the state
    """
    return a[1]

def find_rotor_configuration(code, rotors, x):
    """
    From a list of possible rotors, return a list of the x fittest rotor configurations
    and their starting positions determined by the index of coincidence fitness
    function.

    @param code: the code to compare the fitness function against
    @param rotors: the list of all possible rotors in the encryption configuration
    @param x: the top x number of states to return

    @returns a list of the top x states according to the fitness function
    """
    # Method defense
    type_assertion(code, str)
    type_assertion(rotors, list)
    type_assertion(x, int)

    # We need to assess every permutation of rotors as it could be any of them
    permutations = list(itertools.permutations(rotors, 3))
    top_fitness_states = []

    for permutation in permutations:
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    starting_positions = a + " " + b + " " + c
                    rotors = permutation[0] + " " + permutation[1] + " " + permutation[2]

                    ring_positions = "01 01 01"
                    plugboard = []

                    machine = EnigmaMachine(rotors, "B", ring_positions, starting_positions, plugboard)
                    decrypted = machine.encode(code)
                    fitness = index_of_coincidence(decrypted)

                    # Return a state that can be used by other methods in advanced_work
                    state = [rotors, fitness, starting_positions]

                    top_fitness_states.append(state)
                    top_fitness_states.sort(key = fitness_value, reverse = True)

                    # We only want to assess the top x number of states after everything has been assessed, so we need to drop the 6th state
                    if len(top_fitness_states) > x:
                        top_fitness_states.pop()
        
    return top_fitness_states