from enigma import EnigmaMachine
from advanced_helpers.optimise_ring_setting import optimise_rotor_setting
from advanced_helpers.n_gram_fitness import n_gram_fitness
from helpers.type_assertion import type_assertion

best_settings = []

def fitness_value(a):
    """
    Used as the key function for sorting the states by fitness

    @param a: the state
    @returns b: the fitness of the state
    """
    return a[3]

def find_ring_settings(config, code, x):
    """
    Finds the optimal ring settings for the right and middle ring of a rotor configuration.

    @param config: a list of rotor configuration states
        0: rotors
        1: the index of coincidence for the configuration
        2: the starting positions of the state

    @param code: the code to compare the fitness function against for the new state
    @param x: the top x states to return according to the fitness function

    @returns a new enigma confirguration state with the optimal ring setting
    """
    # Method defense
    type_assertion(config, list)
    type_assertion(code, str)
    type_assertion(x, int)

    for enigma_state in config:
        machine = EnigmaMachine(enigma_state[0], "A", initial_positions = enigma_state[2])

        optimal_rotor_setting_1 = optimise_rotor_setting(machine, 1, code, x)[0]
        machine.starting_rotor.setting = optimal_rotor_setting_1[1]

        optimal_rotor_setting_2 = optimise_rotor_setting(machine, 2, code, x)[0]
        machine.starting_rotor.left_connection.setting = optimal_rotor_setting_2[1]

        encoded = machine.encode(code)

        # Bigram fitness function
        file = "data/bigrams.txt"
        fitness = n_gram_fitness(encoded, file)
        
        # Return a state that other methods in advanced_work can use
        state = [enigma_state[0], enigma_state[2], [optimal_rotor_setting_1[1], optimal_rotor_setting_2[1]], fitness]
        best_settings.append(state)

    # We want the fittest states to be at the top of the list
    best_settings.sort(key = fitness_value)
    return best_settings