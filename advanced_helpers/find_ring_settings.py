from enigma import EnigmaMachine
from advanced_helpers.optimise_ring_setting import optimise_rotor_setting
from advanced_helpers.n_gram_fitness import n_gram_fitness

best_settings = []

def fitness_value(a):
    return a[3]

def find_ring_settings(config, code):
    for enigma_state in config:
        machine = EnigmaMachine(enigma_state[0], "A", initial_positions = enigma_state[2])

        optimal_rotor_setting_1 = optimise_rotor_setting(machine, 1, code)[0]
        machine.starting_rotor.setting = optimal_rotor_setting_1[1]

        optimal_rotor_setting_2 = optimise_rotor_setting(machine, 2, code)[0]
        machine.starting_rotor.left_connection.setting = optimal_rotor_setting_2[1]

        encoded = machine.encode(code)

        file = "data/bigrams.txt"
        fitness = n_gram_fitness(encoded, file)
        
        state = [enigma_state[0], enigma_state[2], [optimal_rotor_setting_1[1], optimal_rotor_setting_2[1]], fitness]
        best_settings.append(state)

    best_settings.sort(key = fitness_value)
    return best_settings